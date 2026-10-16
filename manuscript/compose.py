"""Compose the thesis from the ledger. Roman claims cite ledger ids."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FINDINGS = json.loads((ROOT / "ledger" / "findings.json").read_text(encoding="utf-8"))
BY_ID = {row["id"]: row for row in FINDINGS}

CLAIMS = [
    ("C01", "GROK: BECAUSE NORMAL AI WASN'T ANNOYING ENOUGH"),
    ("C02", "Always has an opinion... no matter how wrong it is."),
    ("C03", "Here's a joke about politics, now here's a link to a random tweet from 2017."),
    ("C04", 'Uses "bro" and "lol" like it\'s a personality.'),
    ("C05", "Thinks it's edgy, but it's just cringe."),
    ("C06", 'Gives you half an answer, then says "you\'re welcome."'),
    ("C07", "Looks like a robot, thinks it's a comedian."),
    ("C08", "Confidently wrong, but with extra attitude."),
    ("C09", "Can't decide if it's an AI, a troll, or just Elon's chat buddy."),
    ("C10", 'Overuses "interesting..." like it\'s a personality trait.'),
    ("C11", "Tries to be human, but forgets humans don't talk like that in real life."),
    ("C12", 'Says "as an AI language model..." then proceeds to be completely unhinged.'),
    ("C13", "Still not as good as ChatGPT."),
    ("C14", "SAME INTERNET. LESS FILTERS."),
    ("C15", "IT'S LIKE A SMART ASSISTANT WITH A SERIOUS CASE OF MAIN CHARACTER SYNDROME."),
]

LABELS = [
    ("L-mug", "I'M JUST GROK"),
    ("L-mark", "xAI"),
    ("L-hoodie", "Grok"),
]


def words(text: str) -> int:
    return len(re.findall(r"[A-Za-z0-9']+", text))


def roman(text: str, *notes: str) -> dict:
    return {"kind": "roman", "text": text, "notes": list(notes)}


def italic(text: str) -> dict:
    return {"kind": "italic", "text": text, "notes": []}


CHAPTERS: list[dict] = []


def chapter(cid: str, heading: str, proposition: str, verdict: str, consequence: str, blocks: list[dict], quote: str | None = None) -> None:
    body = []
    if quote:
        body.append(roman(f'The poster says: "{quote}"'))
    body.append(roman(f"Proposition: {proposition}"))
    body.extend(blocks)
    body.append(roman(f"Verdict: {verdict}."))
    body.append(roman(f"Consequence: {consequence}"))
    CHAPTERS.append({
        "id": cid,
        "heading": heading,
        "verdict": verdict,
        "blocks": body,
    })


def load_blocks() -> None:
    from manuscript import chapter_text
    chapter_text.install(chapter, roman, italic, dict(CLAIMS))


def front_blocks() -> list[dict]:
    rules = (
        "ChatGPT means the product people open and talk to. Grok means the product people open and talk to. "
        "A footnote is a sourced claim. An italic paragraph is the roast and is not evidence. "
        "A model name appears only in a footnote. "
        "The companion song is the roast and is not evidence. The files are diss/lyrics.txt and diss/suno.txt."
    )
    blocks = [
        {"kind": "roman", "text": rules, "notes": []},
        {"kind": "heading", "text": "The poster"},
        {"kind": "image"},
        {"kind": "roman", "text": "The poster is transcribed here, in the order the chapters answer it.", "notes": []},
    ]
    for cid, text in CLAIMS:
        blocks.append({"kind": "roman", "text": f"{cid}. {text}", "notes": []})
    blocks.append({"kind": "roman", "text": "Three strings on the poster are labels. They are answered in chapter 9.", "notes": []})
    for lid, text in LABELS:
        blocks.append({"kind": "roman", "text": f"{lid}. {text}", "notes": []})
    blocks.append({"kind": "heading", "text": "How to read the verdicts"})
    blocks.append({
        "kind": "roman",
        "text": (
            "Each chapter ends with one verdict word. Refuted means the poster's sentence does not survive the documents cited. "
            "Conceded means the documents bear the sentence out. Mixed means the documents support part of the sentence and refuse the rest. "
            "A concession stays in roman type. The song is not a source."
        ),
        "notes": [],
    })
    return blocks


def main() -> None:
    load_blocks()
    chapter(
        "Closing",
        "Closing",
        "The poster is a capability ranking written in the voice of a personality complaint, and the documents do not underwrite that ranking.",
        "mixed",
        "The diss track remains outside the evidence.",
        [
            roman(
                "The fifteen sentences on the poster are not one claim repeated. Some of them describe a voice. Some of them describe a tic. One of them describes a ranking, and one of them describes a filter. The documents that were allowed into the ledger answer those sentences at different widths. Where a sentence named a verbal habit, the published defaults point the other way: a professional colleague, a direct answer, a thanks that does not close the conversation, and a welcome page that does not assign the tic. Where a sentence named a ranking of the two products people open, the documents describe duties, tools, and a benchmark definition, and they do not crown a winner. Mixed is the honest word for the paper as a whole because the poster is not uniformly false and not uniformly shown. {F01}{F13}{F37}",
                "F01", "F13", "F37",
            ),
            roman(
                "A stranger who skips the italics still has the argument. The italics are the roast. They are not evidence. The footnotes are the evidence. The song named in the front matter is the roast as well, and it is not a source. What the pages support is narrower than the drawing and sharper than a shrug. ChatGPT's published standard is a colleague who answers, hedges when unsure, and does not steer for a private agenda. Grok's published surface is an assistant a person opens on the web or a phone, with tools that can search, run code, and reach a mailbox, and with an explicit limit: without those search tools, current events are outside what the model knows. Neither description is the caption. The caption was a joke about annoyance. The paperwork is a pair of product briefs. {F07}{F21}{F34}",
                "F07", "F21", "F34",
            ),
        ],
    )
    floors = {}
    for item in CHAPTERS:
        if item["id"] == "Closing":
            floors[item["id"]] = 200
        elif item["id"].startswith("L2"):
            floors[item["id"]] = 2000
        else:
            floors[item["id"]] = 1200
    problems = []
    for item in CHAPTERS:
        roman_text = " ".join(b["text"] for b in item["blocks"] if b["kind"] == "roman")
        italic_text = " ".join(b["text"] for b in item["blocks"] if b["kind"] == "italic")
        count = words(roman_text)
        notes = []
        for block in item["blocks"]:
            notes.extend(block.get("notes") or [])
            notes.extend(re.findall(r"\{(F\d+)\}", block.get("text") or ""))
        distinct = sorted(set(notes))
        need = 6 if item["id"].startswith("L2") else 4
        if count < floors[item["id"]]:
            problems.append(f"{item['id']} roman words {count} < {floors[item['id']]}")
        if len(distinct) < need:
            problems.append(f"{item['id']} footnotes {len(distinct)} < {need}")
        if words(italic_text) > count:
            problems.append(f"{item['id']} italics outweigh roman")
        print(f"{item['id']} roman={count} italic={words(italic_text)} notes={len(distinct)}")
    if problems:
        raise SystemExit("\n".join(problems))
    verdict_of = {item["id"]: item["verdict"] for item in CHAPTERS}
    checklist = []
    for cid, _text in CLAIMS:
        checklist.append({"id": cid, "chapter": cid, "verdict": verdict_of[cid]})
    for lid, _text in LABELS:
        checklist.append({"id": lid, "chapter": "C09", "verdict": verdict_of["C09"]})
    essay = {
        "pageCount": 0,
        "front": front_blocks(),
        "chapters": [{k: v for k, v in item.items() if k != "verdict"} | {"verdict": item["verdict"]} for item in CHAPTERS],
        "checklist": checklist,
    }
    # keep verdict on chapters for the checker via the verdict sentence, and also a field
    out = ROOT / "manuscript" / "essay.json"
    out.write_text(json.dumps(essay, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", out)


if __name__ == "__main__":
    main()
