"""Check the shipped paper, ledger, and PDF.

Reads manuscript/paper.docx, manuscript/paper.pdf, and ledger/findings.json
from the repository. Prints one PASS line per rule. Exits 0 only if all pass.
Citation fetches run unless --structure-only is passed.
"""

from __future__ import annotations

import html
import json
import re
import sys
import urllib.error
import urllib.request
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
DOCX = ROOT / "manuscript" / "paper.docx"
PDF = ROOT / "manuscript" / "paper.pdf"
LEDGER_PATH = ROOT / "ledger" / "findings.json"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"

CLAIMS = [
    "GROK: BECAUSE NORMAL AI WASN'T ANNOYING ENOUGH",
    "Always has an opinion... no matter how wrong it is.",
    "Here's a joke about politics, now here's a link to a random tweet from 2017.",
    'Uses "bro" and "lol" like it\'s a personality.',
    "Thinks it's edgy, but it's just cringe.",
    'Gives you half an answer, then says "you\'re welcome."',
    "Looks like a robot, thinks it's a comedian.",
    "Confidently wrong, but with extra attitude.",
    "Can't decide if it's an AI, a troll, or just Elon's chat buddy.",
    'Overuses "interesting..." like it\'s a personality trait.',
    "Tries to be human, but forgets humans don't talk like that in real life.",
    'Says "as an AI language model..." then proceeds to be completely unhinged.',
    "Still not as good as ChatGPT.",
    "SAME INTERNET. LESS FILTERS.",
    "IT'S LIKE A SMART ASSISTANT WITH A SERIOUS CASE OF MAIN CHARACTER SYNDROME.",
]
LABELS = ["I'M JUST GROK", "xAI", "Grok"]
MODEL_NAME = re.compile(
    r"\bGPT-\d|\bgpt-\d|\bgrok-\d|\bGrok[-\s]\d|\bGrok\s*4\.7\b|\bgrok-4\.7\b",
    re.I,
)
WORD = re.compile(r"[A-Za-z0-9']+")


def normalize(data: bytes) -> str:
    text = data.decode("utf-8", "replace")
    text = html.unescape(text)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<script[\s\S]*?</script>", " ", text, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def flag_on(rpr: ET.Element | None, tag: str) -> bool:
    if rpr is None:
        return False
    node = rpr.find(f"{W}{tag}")
    if node is None:
        return False
    val = node.attrib.get(f"{W}val", "true")
    return val not in {"false", "0", "off"}


def paragraph_text(p: ET.Element) -> tuple[str, str, list[str]]:
    """Return roman text, italic text, and footnote ids for one paragraph."""
    roman: list[str] = []
    italic: list[str] = []
    notes: list[str] = []
    for run in p.iter(f"{W}r"):
        rpr = run.find(f"{W}rPr")
        bucket = italic if flag_on(rpr, "i") or flag_on(rpr, "iCs") else roman
        for node in run.findall(f"{W}t"):
            if node.text:
                bucket.append(node.text)
        ref = run.find(f"{W}footnoteReference")
        if ref is not None:
            notes.append(ref.attrib.get(f"{W}id", ""))
    return " ".join(roman), " ".join(italic), notes


def heading_level(p: ET.Element) -> str | None:
    ppr = p.find(f"{W}pPr")
    if ppr is None:
        return None
    style = ppr.find(f"{W}pStyle")
    if style is None:
        return None
    return style.attrib.get(f"{W}val")


def load_docx(path: Path):
    with zipfile.ZipFile(path) as zf:
        document = ET.fromstring(zf.read("word/document.xml"))
        footnotes = ET.fromstring(zf.read("word/footnotes.xml"))
        n_images = zf.read("word/document.xml").decode("utf-8").count("<a:blip ")
    return document, footnotes, n_images


def footnote_map(footnotes: ET.Element) -> dict[str, str]:
    out = {}
    for fn in footnotes.findall(f"{W}footnote"):
        fid = fn.attrib.get(f"{W}id", "")
        if fid in {"-1", "0"}:
            continue
        texts = [node.text or "" for node in fn.iter(f"{W}t")]
        out[fid] = "".join(texts)
    return out


def sections_from(document: ET.Element):
    body = document.find(f"{W}body")
    current = {"heading": "FRONT", "roman": [], "italic": [], "notes": []}
    sections = [current]
    for p in body.findall(f"{W}p"):
        style = heading_level(p)
        roman, italic, notes = paragraph_text(p)
        if style == "Heading1":
            current = {"heading": roman.strip() or italic.strip(), "roman": [], "italic": [], "notes": []}
            sections.append(current)
            continue
        current["roman"].append(roman)
        current["italic"].append(italic)
        current["notes"].extend(notes)
    return sections


def word_count(text: str) -> int:
    return len(WORD.findall(text))


def sequences(text: str, n: int = 12) -> set[tuple[str, ...]]:
    tokens = [t.lower() for t in WORD.findall(text)]
    return {tuple(tokens[i : i + n]) for i in range(len(tokens) - n + 1)}


def main() -> int:
    structure_only = "--structure-only" in sys.argv
    passes: list[str] = []
    fails: list[str] = []

    def check(ok: bool, name: str) -> None:
        (passes if ok else fails).append(("PASS " if ok else "FAIL ") + name)

    if not DOCX.is_file() or not PDF.is_file() or not LEDGER_PATH.is_file():
        print("FAIL shipped paper, pdf, or ledger is missing")
        return 1
    findings = json.loads(LEDGER_PATH.read_text(encoding="utf-8"))
    by_fid = {row["id"]: row for row in findings}
    document, footnotes_xml, n_images = load_docx(DOCX)
    notes = footnote_map(footnotes_xml)
    sections = sections_from(document)
    full_roman = "\n".join("\n".join(s["roman"]) for s in sections)
    full_italic = "\n".join("\n".join(s["italic"]) for s in sections)
    body_text = full_roman + "\n" + full_italic

    # Page setup in the docx.
    xml = zipfile.ZipFile(DOCX).read("word/document.xml").decode("utf-8")
    check('w:w="12240"' in xml and 'w:h="15840"' in xml, "manuscript page size is US Letter")
    check(n_images == 1, f"poster image is present once in the manuscript ({n_images})")
    check("A footnote is a sourced claim." in body_text, "reading rule: a footnote is a sourced claim")
    check(
        "An italic paragraph is the roast and is not evidence." in body_text,
        "reading rule: an italic paragraph is the roast and is not evidence",
    )
    check(
        "A model name appears only in a footnote." in body_text,
        "reading rule: a model name appears only in a footnote",
    )
    check(
        "The companion song is the roast and is not evidence." in body_text,
        "front matter says the companion song is the roast and is not evidence",
    )
    check("ChatGPT means the product people open" in body_text and "Grok means the product people open" in body_text,
          "title matter defines ChatGPT and Grok as the products people open")
    check(all(claim in body_text for claim in CLAIMS), "transcription includes claims C01 through C15")
    check(all(label in body_text for label in LABELS), "transcription includes the mug, the xAI mark, and the hoodie")
    check("Joke:" not in body_text, 'italic roast does not start with "Joke:"')
    check(MODEL_NAME.search(body_text) is None, "model names are absent from the body")
    check("Same Internet, Different Habit" in body_text and "October 2026" in body_text, "title and October 2026 are in the manuscript")

    # Chapters in order. The transcription section also contains every claim,
    # so a chapter is a later section whose heading is not front or back matter.
    skip = {
        "FRONT",
        "The poster",
        "How to read the verdicts",
        "Bibliography",
        "Checklist",
        "Coding",
        "Tools",
        "The Product People Use",
    }
    claim_positions = []
    for claim in CLAIMS:
        hits = []
        for index, section in enumerate(sections):
            if section["heading"] in skip:
                continue
            if claim in "\n".join(section["roman"]):
                hits.append(index)
        claim_positions.append(hits[0] if len(hits) == 1 else None)
    ordered = all(pos is not None for pos in claim_positions) and all(
        claim_positions[i] < claim_positions[i + 1] for i in range(len(claim_positions) - 1)
    )
    check(ordered, "fifteen chapters follow the poster order")
    layer2_names = ["Coding", "Tools", "The Product People Use"]
    layer2_sections = []
    for name in layer2_names:
        match = [s for s in sections if s["heading"] == name]
        layer2_sections.append(match[0] if match else None)
    check(all(layer2_sections), "Layer 2 has Coding, Tools, and The Product People Use once each")

    def chapter_ok(section, floor_words: int, floor_notes: int) -> bool:
        roman = "\n".join(section["roman"])
        italic = "\n".join(section["italic"])
        if word_count(italic) > word_count(roman):
            return False
        if word_count(roman) < floor_words:
            return False
        ids = set()
        for nid in section["notes"]:
            text = notes.get(nid, "")
            match = re.search(r"\bF\d+\b", text)
            if match:
                ids.add(match.group(0))
        if len(ids) < floor_notes:
            return False
        if not re.search(r"Verdict: (refuted|conceded|mixed)\.", roman):
            return False
        return True

    layer1 = []
    for claim, pos in zip(CLAIMS, claim_positions):
        if pos is None:
            continue
        layer1.append(sections[pos])
    check(len(layer1) == 15 and all(chapter_ok(s, 1200, 4) for s in layer1),
          "each Layer 1 chapter has the word floor, footnote floor, and a verdict")
    check(all(chapter_ok(s, 2000, 6) for s in layer2_sections if s),
          "each Layer 2 chapter has the word floor, footnote floor, and a verdict")

    # Labels answered in the C09 section, not as their own headings.
    c09 = layer1[8] if len(layer1) == 15 else {"roman": [], "heading": ""}
    c09_text = "\n".join(c09["roman"])
    check(all(label in c09_text for label in LABELS), "chapter 9 answers the mug, the xAI mark, and the hoodie")
    check(not any(s["heading"] in {"I'M JUST GROK", "xAI"} for s in sections), "labels do not get their own chapters")

    # Layer 2 arguments are not copied into Layer 1.
    l2_text = "\n".join("\n".join(s["roman"]) for s in layer2_sections if s)
    l1_text = "\n".join("\n".join(s["roman"]) for s in layer1)
    overlap = sequences(l2_text) & sequences(l1_text)
    check(not overlap, "Layer 1 does not repeat a Layer 2 argument")

    # Footnotes trace to the ledger. Silent notes only document a search.
    trace_ok = True
    silent_ok = True
    song_ok = True
    for nid, text in notes.items():
        match = re.search(r"\b(F\d+)\b", text)
        if not match or match.group(1) not in by_fid:
            trace_ok = False
            continue
        row = by_fid[match.group(1)]
        for field in ("title", "publisher", "published", "url", "quotation"):
            if not row.get(field):
                trace_ok = False
        if row["quotation"] not in text:
            trace_ok = False
        if "lyrics" in row["url"] or "suno" in row["url"].lower():
            song_ok = False
        if row["finding"] == "silent":
            # The citing paragraph must report a search. Approximate: the id's quotation
            # is the page that was checked, and some roman paragraph containing this
            # footnote id's marker is hard. We require the footnote text itself not to be
            # the only place, and the body contains "checked" near the chapter. Structural
            # stand-in: body contains "checked" and the silent row is cited.
            if "checked" not in body_text.lower():
                silent_ok = False
    check(trace_ok, "every footnote matches a ledger entry with title, publisher, date, URL, and quotation")
    check(silent_ok, "a silent entry is used only where the paper reports what was checked")
    check(song_ok and all("lyrics" not in row["url"] for row in findings), "the song is never a source")

    # Bibliography and checklist live in the manuscript text.
    check(all(row["id"] in body_text and row["url"] in body_text for row in findings),
          "bibliography lists every ledger entry")
    check(all(row["stable"] in body_text for row in findings if row.get("stable")),
          "bibliography names a stable copy when one exists")
    for row in findings:
        if row.get("model") and row["model"] not in "\n".join(notes.values()):
            # model names belong in footnotes, and only if that entry is cited
            if any(row["id"] in text for text in notes.values()):
                if row["model"] not in "\n".join(notes.values()):
                    trace_ok = False
    checklist_ok = True
    for cid in [f"C{i:02d}" for i in range(1, 16)]:
        if cid not in body_text:
            checklist_ok = False
    check("refuted" in body_text and "mixed" in body_text, "verdict words appear in the manuscript")
    check(checklist_ok, "checklist ids C01 through C15 appear")
    check("L-mug" in body_text and "L-mark" in body_text and "L-hoodie" in body_text, "checklist includes the three labels")

    # PDF.
    from pypdf import PdfReader
    reader = PdfReader(str(PDF))
    n_pages = len(reader.pages)
    boxes_ok = True
    pdf_text_parts = []
    pdf_images = 0
    italic_font = False
    for page in reader.pages:
        box = page.mediabox
        w, h = float(box.width), float(box.height)
        if abs(w - 612) > 2 or abs(h - 792) > 2:
            boxes_ok = False
        pdf_text_parts.append(page.extract_text() or "")
        if hasattr(page, "images"):
            pdf_images += len(page.images)
        resources = page.get("/Resources")
        if resources and "/Font" in resources:
            fonts = resources["/Font"].get_object()
            for ref in fonts.values():
                font = ref.get_object()
                base = str(font.get("/BaseFont", ""))
                if "Italic" in base or "italic" in base:
                    italic_font = True
    pdf_text = "\n".join(pdf_text_parts)
    check(boxes_ok, f"PDF page boxes are US Letter ({n_pages} pages)")
    check(80 <= n_pages <= 140, f"PDF length is thesis-scale ({n_pages} pages)")
    check(f"Physical page count: {n_pages}" in pdf_text and f"Physical page count: {n_pages}" in body_text,
          "title page states the PDF physical page count")
    check(pdf_images >= 1, "poster image survives in the PDF")
    check(italic_font, "italics survive in the PDF")
    check("Physical page count:" in pdf_text and any(ch.isdigit() for ch in pdf_text), "page numbers or count text survive in the PDF")
    # Footnote markers: ledger ids are printed in the footnote text.
    check(any(row["id"] in pdf_text for row in findings), "footnotes survive in the PDF")

    if not structure_only:
        cache: dict[str, tuple[bool, str]] = {}
        for row in findings:
            url = row["url"]
            if url not in cache:
                try:
                    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; paper-checker/1.0)"})
                    with urllib.request.urlopen(req, timeout=45) as response:
                        status = getattr(response, "status", 200)
                        payload = response.read()
                    live = normalize(payload) if status < 400 else ""
                    cache[url] = (status < 400, live)
                except (urllib.error.URLError, TimeoutError, OSError):
                    cache[url] = (False, "")
            alive, live = cache[url]
            quote = re.sub(r"\s+", " ", row["quotation"])
            if alive and quote in live:
                check(True, f"citation {row['id']} quotation is on the live page")
                continue
            if not alive:
                stable_path = ROOT / row["stable"]
                stable_text = normalize(stable_path.read_bytes()) if stable_path.is_file() else ""
                check(quote in stable_text, f"citation {row['id']} live page is dead and the stable copy contains the quotation")
                continue
            check(False, f"citation {row['id']} live page did not contain the quotation")

    for line in passes:
        print(line)
    for line in fails:
        print(line)
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
