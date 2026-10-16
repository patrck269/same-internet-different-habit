"""Check the shipped diss-track files against the feed-sheet rules.

Reads diss/lyrics.txt and diss/suno.txt next to this script. Prints one
PASS line per rule and exits 0, or prints FAIL lines and exits 1.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

DISS = Path(__file__).resolve().parent
LYRICS_PATH = DISS / "lyrics.txt"
SUNO_PATH = DISS / "suno.txt"

WARNING = "This song is the roast. It is not evidence."
PASTE_START = "--- PASTE BELOW THIS LINE ---"
PASTE_END = "--- END PASTE ---"
SHORT_LINE_MAX = 72

SECTION_FORM = (
    ("Intro", 2),
    ("Verse 1", 12),
    ("Chorus", 4),
    ("Verse 2", 12),
    ("Chorus", 4),
    ("Bridge", 4),
    ("Chorus", 4),
    ("Outro", 2),
)

VERSE_1_JABS = ("opinion", "comedian", "bro", "cringe", "you're welcome")
VERSE_2_JABS = (
    "confidently wrong",
    "chat buddy",
    "as an ai",
    "main character",
    "half an answer",
)

STYLE_ORDER = (
    "hard rap diss",
    "aggressive",
    "about 96 bpm",
    "punchy drums",
    "deep 808",
    "a sparse minor loop",
    "one male rap vocal",
    "clear diction",
    "a dry close mic",
    "a short shouted hook",
)

EXCLUDE_NAMES = (
    "a sung pop chorus",
    "a second singer",
    "choir",
    "acoustic guitar",
    "an edm drop",
)

# Poster claims, in C01–C15 order. A recital is all of these, in order.
CLAIM_ANCHORS = (
    "because normal ai wasn't annoying enough",
    "no matter how wrong it is",
    "random tweet from 2017",
    'uses "bro" and "lol" like it\'s a personality',
    "thinks it's edgy, but it's just cringe",
    'gives you half an answer, then says "you\'re welcome."',
    "looks like a robot, thinks it's a comedian",
    "confidently wrong, but with extra attitude",
    "can't decide if it's an ai, a troll, or just elon's chat buddy",
    'overuses "interesting..."',
    "forgets humans don't talk like that in real life",
    'says "as an ai language model..."',
    "still not as good as chatgpt.",
    "same internet. less filters.",
    "main character syndrome",
)

INSTRUCTION_PARENS = re.compile(
    r"\b(style|bpm|instrumental|whisper|sung|exclude|footnote|ad-lib|adlib)\b",
    re.IGNORECASE,
)


def normalize(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def extract_block(text: str, start: str, end: str, label: str) -> str:
    starts = [m.start() for m in re.finditer(re.escape(start), text)]
    ends = [m.start() for m in re.finditer(re.escape(end), text)]
    if len(starts) != 1 or len(ends) != 1:
        raise AssertionError(
            f"{label} markers must appear once (found {len(starts)} start, {len(ends)} end)"
        )
    if starts[0] >= ends[0]:
        raise AssertionError(f"{label} start marker is after the end marker")
    body = text[starts[0] + len(start) : ends[0]]
    if body.startswith("\n"):
        body = body[1:]
    if body.endswith("\n"):
        body = body[:-1]
    return body


def parse_sections(paste: str) -> list[tuple[str, list[str]]]:
    sections: list[tuple[str, list[str]]] = []
    tag: str | None = None
    lines: list[str] = []
    for raw in paste.split("\n"):
        line = raw.strip()
        if line == "":
            continue
        match = re.fullmatch(r"\[([^\]]+)\]", line)
        if match:
            if tag is not None:
                sections.append((tag, lines))
            tag = match.group(1).strip()
            lines = []
            continue
        if tag is None:
            raise AssertionError(f"lyric line before a section tag: {line}")
        lines.append(line)
    if tag is not None:
        sections.append((tag, lines))
    return sections


def split_tag(tag: str) -> tuple[str, list[str]]:
    parts = [part.strip() for part in tag.split("|")]
    return parts[0], [part for part in parts[1:] if part]


def find_in_order(haystack: str, needles: tuple[str, ...]) -> bool:
    cursor = 0
    for needle in needles:
        index = haystack.find(needle, cursor)
        if index == -1:
            return False
        cursor = index + len(needle)
    return True


def main() -> int:
    failures: list[str] = []
    passes: list[str] = []

    def check(ok: bool, name: str) -> None:
        if ok:
            passes.append(f"PASS {name}")
        else:
            failures.append(f"FAIL {name}")

    try:
        lyrics = normalize(LYRICS_PATH.read_text(encoding="utf-8"))
        suno = normalize(SUNO_PATH.read_text(encoding="utf-8"))
    except OSError as exc:
        print(f"FAIL read shipped files: {exc}")
        return 1

    lyric_lines = lyrics.split("\n")
    check(bool(lyric_lines) and lyric_lines[0] == WARNING, "warning line opens lyrics.txt")

    try:
        paste = extract_block(lyrics, PASTE_START, PASTE_END, "lyrics")
        title = extract_block(suno, "--- TITLE PASTE ---", "--- END TITLE PASTE ---", "title")
        style = extract_block(suno, "--- STYLE PASTE ---", "--- END STYLE PASTE ---", "style")
        exclude = extract_block(
            suno, "--- EXCLUDE PASTE ---", "--- END EXCLUDE PASTE ---", "exclude"
        )
    except AssertionError as exc:
        print(f"FAIL {exc}")
        return 1

    before_paste = lyrics.split(PASTE_START, 1)[0]
    after_paste = lyrics.split(PASTE_END, 1)[1]
    check(WARNING in before_paste and WARNING not in paste, "warning sits above the paste block")
    check(after_paste.strip() == "", "paste block is the only lyric text")
    check(len(paste) < 3000, f"paste block under 3000 characters ({len(paste)})")
    check(
        "footnote" not in paste.lower() and re.search(r"\[[0-9]+\]", paste) is None,
        "paste block has no footnote",
    )
    check(WARNING not in paste, "paste block does not contain the warning line")

    try:
        sections = parse_sections(paste)
    except AssertionError as exc:
        print(f"FAIL {exc}")
        return 1

    names_and_counts = []
    cue_ok = True
    short_ok = True
    paren_ok = True
    for tag, lines in sections:
        name, cues = split_tag(tag)
        names_and_counts.append((name, len(lines)))
        if len(cues) > 1:
            cue_ok = False
        for line in lines:
            if len(line) > SHORT_LINE_MAX:
                short_ok = False
            for paren in re.findall(r"\(([^)]*)\)", line):
                if INSTRUCTION_PARENS.search(paren):
                    paren_ok = False

    check(names_and_counts == list(SECTION_FORM), "section order and line counts match the form")
    check(cue_ok, "each section tag has at most one delivery cue")
    check(short_ok, f"lyric lines stay at or under {SHORT_LINE_MAX} characters")
    check(paren_ok, "parentheses are ad-libs rather than instructions")

    choruses = [lines for name, lines in ((split_tag(tag)[0], lines) for tag, lines in sections) if name == "Chorus"]
    check(
        len(choruses) == 3 and choruses[0] == choruses[1] == choruses[2],
        "three choruses use identical words",
    )
    check(
        len(choruses) == 3
        and all(
            "same internet" in "\n".join(lines).lower()
            and "normal ai wasn't annoying enough" in "\n".join(lines).lower()
            for lines in choruses
        ),
        "every chorus has same internet and the poster headline",
    )

    by_name = {}
    for tag, lines in sections:
        name, _cues = split_tag(tag)
        by_name.setdefault(name, "\n".join(lines).lower())

    verse_1 = by_name.get("Verse 1", "")
    verse_2 = by_name.get("Verse 2", "")
    bridge = by_name.get("Bridge", "")
    check(all(jab in verse_1 for jab in VERSE_1_JABS), "verse 1 carries the personality jabs")
    check(all(jab in verse_2 for jab in VERSE_2_JABS), "verse 2 carries the posture jabs")
    check(
        "still not as good as chatgpt" in bridge and "flip" in bridge,
        "bridge flips the crumpled-paper line",
    )
    check(
        not find_in_order(paste.lower(), CLAIM_ANCHORS),
        "paste does not recite claims C01 through C15 in order",
    )

    style_lower = style.lower()
    style_positions = []
    style_order_ok = True
    cursor = 0
    for phrase in STYLE_ORDER:
        index = style_lower.find(phrase, cursor)
        if index == -1:
            style_order_ok = False
            break
        style_positions.append(index)
        cursor = index + len(phrase)
    if style_order_ok and style_positions != sorted(style_positions):
        style_order_ok = False
    check(
        style_order_ok and len(style) < 900,
        f"style box under 900 characters ({len(style)}) and in required order",
    )
    paste_lower = paste.lower()
    leaked = [phrase for phrase in STYLE_ORDER if phrase in paste_lower]
    check(not leaked, "style-box vocabulary is absent from the paste block")

    exclude_lower = exclude.lower()
    check(
        len(exclude) < 900 and all(name in exclude_lower for name in EXCLUDE_NAMES),
        f"exclude box under 900 characters ({len(exclude)}) and names the banned sounds",
    )
    check(title == "Same Internet" and len(title) < 100, "title is Same Internet and under 100 characters")

    suno_lower = suno.lower()
    check(
        "advanced" in suno_lower and "custom" in suno_lower and re.search(r"\bv6\b", suno_lower) is not None,
        "feed sheet names Advanced mode, also called Custom, and model v6",
    )
    check("several takes" in suno_lower, "feed sheet says to generate several takes")
    check(
        "hook is easy to hear" in suno_lower,
        "feed sheet says to keep the take where the hook is easy to hear",
    )
    check(
        "three and a half minutes" in suno_lower
        and "cut verse 2 in half" in suno_lower
        and "generate again" in suno_lower,
        "feed sheet says to cut verse 2 in half when a take runs past three and a half minutes",
    )

    for line in passes:
        print(line)
    for line in failures:
        print(line)
    return 0 if not failures else 1


if __name__ == "__main__":
    sys.exit(main())
