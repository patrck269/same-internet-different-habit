const { Document, Packer, Paragraph, TextRun, Footer, Header, PageNumber,
        FootnoteReferenceRun, ImageRun, AlignmentType, HeadingLevel,
        Table, TableRow, TableCell, WidthType, BorderStyle, ShadingType } = require("docx");
const fs = require("fs");
const path = require("path");

const root = path.resolve(__dirname, "..");
const essay = JSON.parse(fs.readFileSync(path.join(root, "manuscript", "essay.json"), "utf8"));
const findings = JSON.parse(fs.readFileSync(path.join(root, "ledger", "findings.json"), "utf8"));
const png = fs.readFileSync(path.join(root, "assets", "poster.png"));
const byId = Object.fromEntries(findings.map((row) => [row.id, row]));
const noteIds = [];
for (const chapter of essay.chapters) {
  for (const block of chapter.blocks) {
    const inline = (block.text || "").match(/\{(F\d+)\}/g) || [];
    for (const id of [...(block.notes || []), ...inline.map((token) => token.slice(1, -1))]) {
      if (!noteIds.includes(id)) noteIds.push(id);
    }
  }
}
const noteNumber = Object.fromEntries(noteIds.map((id, i) => [id, i + 1]));

function footnoteParagraph(id) {
  const row = byId[id];
  const model = row.model ? ` Model name: ${row.model}.` : "";
  const text = `${id}. ${row.title}. ${row.publisher}, ${row.published}. Read ${row.read}. ${row.url}. Quotation: ${row.quotation}.${model}`;
  return new Paragraph({ children: [new TextRun({ font: "Times New Roman", size: 20, text })] });
}

const footnotes = {};
for (const id of noteIds) footnotes[noteNumber[id]] = { children: [footnoteParagraph(id)] };

const thin = { style: BorderStyle.SINGLE, size: 4, color: "CCCCCC" };
const borders = { top: thin, bottom: thin, left: thin, right: thin };

function cell(text, width) {
  return new TableCell({
    borders,
    width: { size: width, type: WidthType.DXA },
    margins: { top: 60, bottom: 60, left: 80, right: 80 },
    children: [new Paragraph({ children: [new TextRun({ font: "Times New Roman", size: 20, text })] })],
  });
}

function runsFrom(text, italics, notes) {
  const parts = text.split(/(\{F\d+\})/g);
  const runs = [];
  for (const part of parts) {
    const match = part.match(/^\{(F\d+)\}$/);
    if (match) {
      runs.push(new FootnoteReferenceRun(noteNumber[match[1]]));
    } else if (part) {
      runs.push(new TextRun({ font: "Times New Roman", size: 24, italics, text: part }));
    }
  }
  return runs;
}

function bodyParagraph(block) {
  return new Paragraph({
    spacing: { line: 480, lineRule: "auto", after: 200 },
    children: runsFrom(block.text, block.kind === "italic", block.notes),
  });
}

const children = [];
children.push(new Paragraph({
  heading: HeadingLevel.TITLE,
  spacing: { after: 200 },
  children: [new TextRun({ font: "Times New Roman", size: 48, text: "Same Internet, Different Habit" })],
}));
children.push(new Paragraph({
  spacing: { after: 200 },
  children: [new TextRun({ font: "Times New Roman", size: 24, text: "October 2026" })],
}));
children.push(new Paragraph({
  spacing: { after: 400 },
  children: [new TextRun({ font: "Times New Roman", size: 24, text: `Physical page count: ${essay.pageCount}` })],
}));
for (const block of essay.front) {
  if (block.kind === "image") {
    children.push(new Paragraph({
      alignment: AlignmentType.CENTER,
      spacing: { before: 200, after: 200 },
      children: [new ImageRun({
        type: "png",
        data: png,
        transformation: { width: 540, height: 540 },
        altText: { name: "Poster", description: "The poster this paper answers", title: "Poster" },
      })],
    }));
  } else if (block.kind === "heading") {
    children.push(new Paragraph({
      heading: HeadingLevel.HEADING_1,
      children: [new TextRun(block.text)],
    }));
  } else {
    children.push(bodyParagraph(block));
  }
}

for (const chapter of essay.chapters) {
  children.push(new Paragraph({
    heading: HeadingLevel.HEADING_1,
    pageBreakBefore: true,
    children: [new TextRun(chapter.heading)],
  }));
  for (const block of chapter.blocks) children.push(bodyParagraph(block));
}

children.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  pageBreakBefore: true,
  children: [new TextRun("Bibliography")],
}));
for (const row of findings) {
  const text = `${row.id}. ${row.title}. ${row.publisher}, ${row.published}. Read ${row.read}. ${row.url}. Stable copy: ${row.stable}. Claim IDs: ${row.claims.join(", ")}.`;
  children.push(new Paragraph({
    spacing: { after: 160 },
    children: [new TextRun({ font: "Times New Roman", size: 20, text })],
  }));
}

children.push(new Paragraph({
  heading: HeadingLevel.HEADING_1,
  pageBreakBefore: true,
  children: [new TextRun("Checklist")],
}));
const widths = [1400, 5200, 1400, 1360];
const header = ["ID", "Chapter", "Verdict", ""];
children.push(new Table({
  width: { size: 9360, type: WidthType.DXA },
  columnWidths: widths,
  rows: [
    new TableRow({ children: header.map((text, i) => cell(text, widths[i])), tableHeader: true }),
    ...essay.checklist.map((row) => new TableRow({
      children: [row.id, row.chapter, row.verdict, ""].map((text, i) => cell(text, widths[i])),
    })),
  ],
}));

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Times New Roman", size: 24 } } },
    paragraphStyles: [
      { id: "Title", name: "Title", basedOn: "Normal", quickFormat: true,
        run: { font: "Times New Roman", size: 48 },
        paragraph: { spacing: { after: 200 } } },
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { font: "Times New Roman", size: 32, bold: true },
        paragraph: { spacing: { before: 240, after: 200 }, outlineLevel: 0 } },
    ],
  },
  footnotes,
  sections: [{
    properties: {
      page: {
        size: { width: 12240, height: 15840 },
        margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 },
      },
    },
    headers: {
      default: new Header({
        children: [new Paragraph({
          children: [new TextRun({ font: "Times New Roman", size: 18, italics: true, text: "Same Internet, Different Habit" })],
        })],
      }),
    },
    footers: {
      default: new Footer({
        children: [new Paragraph({
          alignment: AlignmentType.CENTER,
          children: [
            new TextRun({ font: "Times New Roman", size: 20, text: "Page " }),
            new TextRun({ font: "Times New Roman", size: 20, children: [PageNumber.CURRENT] }),
          ],
        })],
      }),
    },
    children,
  }],
});

Packer.toBuffer(doc).then((buf) => {
  const out = path.join(root, "manuscript", "paper.docx");
  fs.mkdirSync(path.dirname(out), { recursive: true });
  fs.writeFileSync(out, buf);
  console.log(`wrote ${buf.length} bytes, footnotes ${noteIds.length}`);
});
