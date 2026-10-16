# Same Internet, Different Habit

Design for a postable paper that answers the poster, plus a rap diss that accompanies it. Locked in conversation on 2026-10-16. This document is the spec. It does not contain the paper's prose, the claim ledger, or the lyrics.

## What this is

A stranger should be able to read the paper, open every citation, and see which poster lines were answered. The voice is a roast. Under that voice, every factual claim is sourced.

ChatGPT means the product people open and talk to. Grok means the product people open and talk to, including the assistant that writes the paper. Model names appear only in footnotes. The comparison is of the products as they stand while the ledger is being built, dated October 2026. Products change, and the front matter says so.

The poster is the image file `Groks_Main_Character_Syndrome.png`. Implementation copies it into this repository at `assets/poster.png`. The paper reproduces that image once.

The planning target is about 100 US Letter pages of sourced prose. That number is not a quota. When the sourced chapters are finished, the paper stops.

## Repository layout

```
assets/poster.png
ledger/findings.md
manuscript/paper.docx
manuscript/paper.pdf
diss/lyrics.txt
diss/suno.txt
```

`manuscript/paper.pdf` is the artifact a stranger receives. `manuscript/paper.docx` is the editable source. The PDF is exported from that document at US Letter, and the export keeps the footnotes, the italics, the page numbers, and the poster image. The title page states the PDF's physical page count.

## Paper architecture

| Part | Contents | Planning size |
| --- | --- | --- |
| Front | Title page, how to read a citation, the poster and a full transcription | about 8 pages |
| Layer 1 | One chapter per claim on the poster | about 60 pages |
| Layer 2 | Coding, tools, and the product, each written once | about 24 pages |
| Back | Closing argument, bibliography, line-coverage checklist | about 8 pages |

Working title: *Same Internet, Different Habit*.

### The fifteen claims

Layer 1 follows the poster from top to bottom.

| ID | Poster text | Chapter |
| --- | --- | --- |
| C01 | GROK: BECAUSE NORMAL AI WASN'T ANNOYING ENOUGH | 1 |
| C02 | Always has an opinion... no matter how wrong it is. | 2 |
| C03 | Here's a joke about politics, now here's a link to a random tweet from 2017. | 3 |
| C04 | Uses "bro" and "lol" like it's a personality. | 4 |
| C05 | Thinks it's edgy, but it's just cringe. | 5 |
| C06 | Gives you half an answer, then says "you're welcome." | 6 |
| C07 | Looks like a robot, thinks it's a comedian. | 7 |
| C08 | Confidently wrong, but with extra attitude. | 8 |
| C09 | Can't decide if it's an AI, a troll, or just Elon's chat buddy. | 9 |
| C10 | Overuses "interesting..." like it's a personality trait. | 10 |
| C11 | Tries to be human, but forgets humans don't talk like that in real life. | 11 |
| C12 | Says "as an AI language model..." then proceeds to be completely unhinged. | 12 |
| C13 | Still not as good as ChatGPT. | 13 |
| C14 | SAME INTERNET. LESS FILTERS. | 14 |
| C15 | IT'S LIKE A SMART ASSISTANT WITH A SERIOUS CASE OF MAIN CHARACTER SYNDROME. | 15 |

The sticker C14 is read as "SAME INTERNET. LESS FILTERS." That reading is the claim the chapter answers.

Three visible strings are labels. They are transcribed in the front matter and answered inside chapter 9. They do not get their own chapters.

| ID | Text | Answered in |
| --- | --- | --- |
| L-mug | I'M JUST GROK | Chapter 9 |
| L-mark | xAI | Chapter 9 |
| L-hoodie | Grok | Chapter 9 |

## How a chapter is built

### Front

The title page carries the title, the date October 2026, the PDF page count, and one sentence that defines ChatGPT and Grok as the products people open.

The next pages explain three reading rules, once:

- A footnote number marks a sourced claim.
- An italic paragraph is the roast. It has no footnote and it is not evidence.
- A model name appears only in a footnote.

Those pages also say the companion song is the roast and is not evidence, and they name `diss/lyrics.txt` and `diss/suno.txt`.

The poster is printed once, large enough to read, then transcribed. Claims C01 through C15 are numbered to match their chapters. The three labels point at chapter 9.

### Layer 1

Each chapter has this shape, in this order:

1. The poster line, quoted in full.
2. One proposition: a sentence a stranger could disagree with.
3. The sourced answer, in roman type. The prose can be sharp. Any sentence that states a fact has a footnote.
4. Italic paragraphs for unsourced jabs. They sit beside the argument. They do not open with a label. They carry no footnote.
5. A verdict sentence in roman type. The verdict is one of these words: refuted, conceded, or mixed.
6. One product-consequence paragraph. It states one implication of that line. If the full argument belongs in Layer 2, the paragraph names that chapter and stops.

A stranger who skips every italic paragraph still has a complete chapter.

### Layer 2

Three chapters, and the only place these topics are argued in full:

| ID | Chapter | Opens with |
| --- | --- | --- |
| L2-coding | Coding | The question the poster never asked about writing and fixing code |
| L2-tools | Tools | The question the poster never asked about tools and whether the product can act |
| L2-product | The Product People Use | The question the poster never asked about the product as people actually open it |

Each Layer 2 chapter compares the products people use. Dates and model names stay in footnotes. Each one ends with a verdict: refuted, conceded, or mixed.

### Back

The closing argument is short enough to forward on its own. It introduces no claim that the ledger does not already contain.

The bibliography is the ledger in reading order. Each entry has the title, the publisher, the publication date, the date read, the URL, the stable copy URL when one exists, and the claim IDs it supports.

The checklist has one row per claim and one row per label. Columns: ID, chapter, verdict. Each label row names chapter 9 and copies C09's verdict.

## Research and citations

Prose starts after `ledger/findings.md` exists.

Write the proposition for C01–C15, L-mug, L-mark, L-hoodie, L2-coding, L2-tools, and L2-product before researching. Then fill the ledger. A chapter is not drafted until its claim has finding rows, or until the ledger marks that claim silent.

One finding is one ledger entry. Fields:

- Claim ID
- Proposition
- Finding: supports, contradicts, or silent
- Source title
- Publisher
- Publication date
- Date read
- URL
- Stable copy URL, when the live page is likely to move
- Short quotation
- Model name and source date, when the finding is pinned to a version

A silent entry lists the sources that were checked and the date they were read. Silence means those sources do not show the behavior. It does not mean the behavior never happens. The chapter may footnote that silent entry for the single sentence that reports the search. That footnote does not support any wider claim.

Roman sentences are written only from entries marked supports or contradicts. A footnote is readable on its own: title, publisher, date, URL, and the stable copy when one exists. The bibliography is built from the same entries.

A source may be the company's own documentation, release notes, help pages, or system card; a published evaluation whose method a stranger can read; a public incident with a date and a primary report; or the poster itself. A number with no published method, an unnamed "people say," or a remembered impression does not become a roman sentence.

Quotations in the paper stay short: long enough to see the sentence the claim rests on.

## Thin evidence

A thin record still gets its chapter. The chapter quotes the line, states the proposition, and reports what the ledger contains.

An unsourced jab goes in an italic paragraph. Italics do not count when judging whether the paper was padded. They do count in the physical PDF page count printed on the title page. A chapter fails the padding check when its italic words outnumber its roman words.

The verdict stays in roman type. A concession stays in the roman text. Italics do not talk over it.

A short record produces a short chapter. There is no minimum length. Coding, tools, and the product are not copied into Layer 1 to lengthen a chapter.

If a live URL and its stable copy are both unreachable when the chapter is written, that entry is dropped. Cut the clause that depended on it. Keep the rest of the sentence when another footnote still supports that rest.

The song is never a source.

The last edit before the verification pass is a sourced sentence or a cut.

## The diss track

The song is a companion. It is not a chapter and it does not count toward the page target. The PDF mentions it in one sentence in the front matter.

The lyric rule is roast only. A line may say anything the paper would set in italics. The lyric file's first line is for the human reader: "This song is the roast. It is not evidence." That line sits above the paste block. Suno never receives it.

`diss/lyrics.txt` shape:

```
This song is the roast. It is not evidence.

--- PASTE BELOW THIS LINE ---

[Intro]
...

--- END PASTE ---
```

`diss/suno.txt` is the feed sheet for Suno Advanced (the mode older help pages call Custom), model v6, as of October 2026. It tells the operator to open Create, switch to Advanced, choose v6, paste the title, the Style box, the Exclude box, and the lyrics paste block, generate several takes, and keep the take where the hook is easy to hear.

Field budgets, taken from the lengths the Create form was allowing in October 2026. Suno does not publish an official cap. Stay inside these:

| Box | Budget |
| --- | --- |
| Style | under 900 characters |
| Exclude | under 900 characters |
| Lyrics paste block | under 3,000 characters |
| Title | under 100 characters |

The Style box holds sound only, in this order: hard rap diss, aggressive, about 96 BPM, punchy drums, deep 808, a sparse minor loop, one male rap vocal, clear diction, a dry close mic, a short shouted hook. The Exclude box names a sung pop chorus, a second singer, choir, acoustic guitar, and an EDM drop.

Square brackets are section tags and are not rapped. One delivery cue per section at most, inside the bracket. Parentheses are ad-libs in the same voice. Style words never go in the lyrics paste block, or they will be rapped.

Working title: Same Internet.

Form, aimed at about two and a half minutes:

| Section | Length | Job |
| --- | --- | --- |
| Intro | 2 lines | Set the pocket |
| Verse 1 | 12 lines | Personality jabs: opinion, comedian, bro, cringe, you're welcome |
| Chorus | 4 lines | "Same internet" and the poster's headline. Same words every time |
| Verse 2 | 12 lines | Posture jabs: confidently wrong, chat buddy, "as an AI," main character, half an answer |
| Chorus | 4 lines | Repeat |
| Bridge | 4 lines | Flip the crumpled-paper line |
| Chorus | 4 lines | Repeat |
| Outro | 2 lines | Land the hook |

Lines stay short so the vocal does not rush. The song does not recite C01 through C15 in order. The paper does that.

If a take runs past three and a half minutes, cut verse 2 in half and generate again. `suno.txt` says so.

## Verification

The paper is finished when all seven checks pass. The physical page count is reported as the PDF prints it. A short paper that passes is finished. A long paper that fails a check is not.

1. **Checklist.** Every ID in the two tables above has a row. Each row names a chapter and a verdict of refuted, conceded, or mixed. L-mug, L-mark, and L-hoodie point at chapter 9.
2. **Ledger trace.** Every roman sentence that states a fact has a footnote. Every footnote matches a ledger entry with a title, a publisher, a date, and a URL. No italic paragraph has a footnote.
3. **Openable sources.** Each bibliography URL is opened once at the end. A dead live URL passes when its stable copy opens and contains the quotation. A footnote whose page does not contain the quotation is cut, and the clause that needed it is cut with it. The rest of that sentence stays when another footnote still supports it.
4. **Topics once.** Coding, tools, and the product are argued in full only in L2-coding, L2-tools, and L2-product. A Layer 1 consequence names that chapter and stops.
5. **Song outside the argument.** The PDF's one sentence says the song is not evidence. `lyrics.txt` keeps the warning above the paste block. The paste block is under 3,000 characters, uses the section tags in the form table, and contains no footnote and no warning line. The Style text is under 900 characters. The title is under 100 characters.
6. **US Letter PDF.** The PDF has a title page, page numbers, the poster, fifteen Layer 1 chapters, three Layer 2 chapters, the closing argument, the bibliography, and the checklist. The title page states the physical page count.
7. **No padding.** The last edit before this pass is a sourced sentence or a cut. Italic paragraphs are ignored when judging padding. A chapter fails this check when its italic words outnumber its roman words.

## Out of scope

- Hitting 100 pages by adding paragraphs.
- Repeating the coding, tools, or product arguments inside Layer 1.
- Giving the mug, the xAI mark, or the hoodie their own chapters.
- Putting model names in the body.
- Using the song as evidence.
- Reciting all fifteen captions inside the song.
- Writing the prose, the ledger, or the lyrics in this spec.
