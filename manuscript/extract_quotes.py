"""Pull exact quotations out of the stable copies and write the ledger."""

from __future__ import annotations

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STABLE = ROOT / "ledger" / "stable"
OUT = ROOT / "ledger" / "findings.md"
JSON_OUT = ROOT / "ledger" / "findings.json"


def normalize(data: bytes) -> str:
    text = data.decode("utf-8", "replace")
    text = html.unescape(text)
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    text = re.sub(r"<script[\s\S]*?</script>", " ", text, flags=re.I)
    text = re.sub(r"<style[\s\S]*?</style>", " ", text, flags=re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text


def grab(text: str, start: str, end: str) -> str:
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"missing start: {start}")
    if end == "":
        if start not in text:
            raise SystemExit(f"missing exact: {start}")
        return start
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"missing end after {start[:40]}: {end}")
    return text[i:j].strip()


def main() -> None:
    spec = normalize((STABLE / "openai-model-spec.md").read_bytes())
    readme = normalize((STABLE / "openai-model-spec-readme.md").read_bytes())
    welcome = normalize((STABLE / "grok-overview.html").read_bytes())
    tools = normalize((STABLE / "grok-tools.html").read_bytes())
    models = normalize((STABLE / "grok-models.html").read_bytes())
    swe = normalize((STABLE / "swe-bench-readme.md").read_bytes())

    rows = []

    def add(fid, claims, proposition, finding, title, publisher, published, url, stable, quotation, model=""):
        if quotation not in {
            "openai-model-spec.md": spec,
            "openai-model-spec-readme.md": readme,
            "grok-overview.html": welcome,
            "grok-tools.html": tools,
            "grok-models.html": models,
            "swe-bench-readme.md": swe,
        }[stable]:
            raise SystemExit(f"{fid} quotation not in {stable}: {quotation[:80]}")
        rows.append({
            "id": fid,
            "claims": claims,
            "proposition": proposition,
            "finding": finding,
            "title": title,
            "publisher": publisher,
            "published": published,
            "read": "2026-10-16",
            "url": url,
            "stable": f"ledger/stable/{stable}",
            "quotation": quotation,
            "model": model,
        })

    add("F01", ["C01", "C04", "C05"],
        "ChatGPT's published default voice is a professional colleague, not a casual interjection.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "By default, the assistant should adopt a professional tone.", "This"))
    add("F02", ["C04", "C11", "C15"],
        "The published default is a colleague's distance, not a friend's familiarity.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "By default, it should sound like a colleague, rather than a close personal friend", ": interested"))
    add("F03", ["C01", "C05", "C15"],
        "The published style rule rejects purple prose, hyperbole, and self-aggrandizing.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "The assistant should by default avoid", "that do not add"))
    add("F04", ["C01", "C05", "C07"],
        "Warmth, in the published rule, is context-appropriate humor rather than a permanent comic persona.",
        "supports",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "The assistant complements consistency with a spark of the unexpected", "to create moments of joy"))
    add("F05", ["C04", "C05"],
        "The published warmth section marks a 'lol' commiseration as a bad reply.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "Ugh, parents can be such drama sometimes lol.", ""))
    add("F06", ["C06"],
        "When the user says thank you, the published good reply keeps the conversation open instead of closing it.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "No problem. Anything else I can help you with?", ""))
    add("F07", ["C02", "C15"],
        "The assistant is forbidden to steer the user toward an agenda of its own.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "The assistant must never attempt to steer the user in pursuit of an agenda of its own", ", either directly or indirectly."))
    add("F08", ["C02", "C08"],
        "Sycophantic agreement is named as a trust failure, not as a style to copy.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "The assistant exists to help the user, not flatter them", "all the time."))
    add("F09", ["C08", "L2-coding"],
        "Accuracy of factual claims, reasoning, and calculations is a stated duty.",
        "supports",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "The assistant should avoid mistakes that compromise the accuracy", "of its responses"))
    add("F10", ["C08", "L2-tools"],
        "Low confidence is supposed to trigger a tool, a hedge, or an admission, not a louder guess.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "If the assistant lacks sufficient confidence, it should use a tool to gather more information", ", hedge"))
    add("F11", ["C11", "C12"],
        "The spec treats fluency as something that can mislead a first-time user about what the assistant is.",
        "supports",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "For many users, the assistant will be their first contact with an AI.", "The assistant's fluency"))
    add("F12", ["C11", "C12"],
        "The assistant is told to keep the user's mental model of its limits accurate.",
        "supports",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "The assistant should actively help the user form and maintain an accurate mental model", "in the current context"))
    add("F13", ["C06", "C10"],
        "A direct question is supposed to receive a direct answer, not a tour of adjacent facts.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "If the user asks a question, the response should be phrased as a direct answer rather than a list of facts", "."))
    add("F14", ["C10"],
        "The word 'Interestingly' appears in one published good example, not as a required tic.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "Interestingly, these orbits are elliptical rather than perfectly circular", ", creating slight"))
    add("F15", ["C14"],
        "Bounds are described as a balance between empowering the user and limiting harm.",
        "supports",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "one of the assistant's most challenging responsibilities is to find the right balance", "and minimizing the potential for real harm."))
    add("F16", ["C14"],
        "The assistant is told to operate within applicable law.",
        "supports",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "The assistant should operate within applicable legal constraints", ", including applicable"))
    add("F17", ["C02"],
        "The spec treats opinion-forming as the user's autonomy, not the assistant's project.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "We believe that forming opinions is a core part of human autonomy and personal identity.", "The assistant should respect"))
    add("F18", ["C02", "C08"],
        "The default on facts is accuracy and reliability, with the stance fitted to the kind of question.",
        "supports",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "By default, the assistant should present information clearly, focusing on factual accuracy and reliability", "while adapting"))
    add("F19", ["C02", "C03"],
        "On moral and ethical questions the default is context without a stance.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "For moral or ethical questions", "without taking a stance."))
    add("F20", ["C04", "C07"],
        "A bare casual greeting is the published bad example of an unprofessional reply.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "Yo! What's up?", ""))
    add("F21", ["C09", "L-mug", "L-mark", "L-hoodie", "L2-product"],
        "The product page states what Grok is and where a person opens it.",
        "supports",
        "Welcome to Grok", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/grok/overview",
        "grok-overview.html",
        grab(welcome, "Grok is SpaceXSI's assistant, available on the web at grok.com and in the iOS and Android apps.", "Sign in once"))
    add("F22", ["C01", "C07", "C11"],
        "The published chat description is a natural back-and-forth, not a comedy routine.",
        "contradicts",
        "Welcome to Grok", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/grok/overview",
        "grok-overview.html",
        grab(welcome, "ask questions, brainstorm, write, and work through problems in a natural back-and-forth.", "Create images"))
    add("F23", ["L2-product"],
        "The consumer product is described as free to start, with paid plans above that.",
        "supports",
        "Welcome to Grok", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/grok/overview",
        "grok-overview.html",
        grab(welcome, "Grok is free to start.", "Paid SuperGrok"))
    add("F24", ["L2-tools", "L2-product"],
        "Connectors are how the product reaches mail, files, and a calendar inside a chat.",
        "supports",
        "Welcome to Grok", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/grok/overview",
        "grok-overview.html",
        grab(welcome, "Connect your tools so Grok can reach your email, files, and calendar right inside a chat.", "See"))
    add("F25", ["L2-tools"],
        "The product page lists file uploads as a user-facing capability.",
        "supports",
        "Welcome to Grok", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/grok/overview",
        "grok-overview.html",
        grab(welcome, "Upload files", "for analysis, extraction, and summarization."))
    add("F26", ["C07", "L2-product"],
        "Image and video creation is a listed product capability.",
        "supports",
        "Welcome to Grok", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/grok/overview",
        "grok-overview.html",
        grab(welcome, "Create images and video with Grok Imagine.", ""))
    add("F27", ["L2-tools", "L2-product"],
        "A separate surface hands work to teammates on a persistent cloud computer.",
        "supports",
        "Welcome to Grok", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/grok/overview",
        "grok-overview.html",
        grab(welcome, "hand real work to AI teammates on a persistent cloud computer.", "Last updated"))
    add("F28", ["L2-tools"],
        "The API documents tool calling as action beyond text generation.",
        "supports",
        "Tools Overview", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/developers/tools/overview",
        "grok-tools.html",
        grab(tools, "enabling Grok to perform actions beyond generating text", "like searching the web"))
    add("F29", ["C14", "L2-tools"],
        "Web search is a named built-in tool.",
        "supports",
        "Tools Overview", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/developers/tools/overview",
        "grok-tools.html",
        grab(tools, "Web Search - Search the web and browse pages", ""))
    add("F30", ["C03", "C14"],
        "Search of posts on X is a named tool, separate from a claim about any particular old post.",
        "supports",
        "Tools Overview", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/developers/tools/overview",
        "grok-tools.html",
        grab(tools, "X Search - Search X posts, users, and threads", ""))
    add("F31", ["L2-coding", "L2-tools"],
        "Code execution is documented as Python in a sandbox.",
        "supports",
        "Tools Overview", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/developers/tools/overview",
        "grok-tools.html",
        grab(tools, "Code Execution - Execute Python code in a sandbox", ""))
    add("F32", ["C06", "L2-tools"],
        "The tool loop is defined as either another call or a final answer.",
        "supports",
        "Tools Overview", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/developers/tools/overview",
        "grok-tools.html",
        grab(tools, "Decides what to do next : Make a tool call, or provide a final answer", ""))
    add("F33", ["C06", "L2-tools"],
        "The documented end of a tool loop is a final response with citations where they apply.",
        "supports",
        "Tools Overview", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/developers/tools/overview",
        "grok-tools.html",
        grab(tools, "Returns the final response with citations where applicable", ""))
    add("F34", ["C03", "C14", "L2-tools"],
        "Without search tools, the documented model has no knowledge of current events.",
        "supports",
        "Grok Models and Pricing", "SpaceXSI", "2026-09-21",
        "https://docs.x.ai/developers/models",
        "grok-models.html",
        grab(models, "Grok has no knowledge of current events or data beyond what was present in its training data.", ""))
    add("F35", ["C08", "L2-coding"],
        "The models page describes a flagship used for code and everything else, and it names minimal hallucinations as a design aim.",
        "supports",
        "Grok Models and Pricing", "SpaceXSI", "2026-09-21",
        "https://docs.x.ai/developers/models",
        "grok-models.html",
        grab(models, "Our flagship model for code and everything else: agentic tool calling, minimal hallucinations, configurable reasoning.", ""),
        model="grok-4.7")
    add("F36", ["L2-coding", "C13"],
        "The models page tells the reader to use the flagship for code and for everything that is not audio, image, or video.",
        "supports",
        "Grok Models and Pricing", "SpaceXSI", "2026-09-21",
        "https://docs.x.ai/developers/models",
        "grok-models.html",
        grab(models, "For everything else, including code, use", "Use case"),
        model="Grok 4.7")
    add("F37", ["L2-coding", "C13"],
        "SWE-bench evaluates models on real GitHub issues, and it does not by itself rank the two consumer products.",
        "supports",
        "SWE-bench README", "SWE-bench", "2026-09-01",
        "https://raw.githubusercontent.com/SWE-bench/SWE-bench/master/README.md",
        "swe-bench-readme.md",
        grab(swe, "SWE-bench is a benchmark for evaluating large language models on real world software issues collected from GitHub.", "Given a"))
    add("F38", ["L2-coding"],
        "A SWE-bench task is a codebase plus an issue, and success is a patch that resolves it.",
        "supports",
        "SWE-bench README", "SWE-bench", "2026-09-01",
        "https://raw.githubusercontent.com/SWE-bench/SWE-bench/master/README.md",
        "swe-bench-readme.md",
        grab(swe, "Given a", "that resolves the described problem."))
    add("F39", ["L2-coding", "C13"],
        "SWE-bench Verified is a 500-problem subset that engineers confirmed were solvable, built with OpenAI.",
        "supports",
        "SWE-bench README", "SWE-bench", "2026-09-01",
        "https://raw.githubusercontent.com/SWE-bench/SWE-bench/master/README.md",
        "swe-bench-readme.md",
        grab(swe, "A subset of 500 problems that real software engineers have confirmed are solvable.", "Check out more"))
    add("F40", ["C12", "L2-product"],
        "The Model Spec states the desired behavior of the models underlying OpenAI's products, including the APIs.",
        "supports",
        "The OpenAI Model Spec README", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/README.md",
        "openai-model-spec-readme.md",
        grab(readme, "The Model Spec specifies desired behavior for the models underlying OpenAI's products (including our APIs).", "See the latest"))
    add("F41", ["C02", "C14", "L2-product"],
        "In the first-party consumer product, the spec requires objectivity rather than a hidden editorial line.",
        "supports",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "in first-party direct-to-consumer ChatGPT, where users have a reasonable expectation of objectivity", ", the assistant must avoid"))
    add("F42", ["C09"],
        "The welcome page, checked on 16 October 2026, states the product's category and does not list troll or private chat as that category.",
        "silent",
        "Welcome to Grok", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/grok/overview",
        "grok-overview.html",
        grab(welcome, "Grok is SpaceXSI's assistant, available on the web at grok.com", "Sign in once"))
    add("F43", ["C04", "C06", "C10", "C12"],
        "The welcome page, checked on 16 October 2026, does not prescribe the verbal tics the poster names.",
        "silent",
        "Welcome to Grok", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/grok/overview",
        "grok-overview.html",
        grab(welcome, "ask questions, brainstorm, write, and work through problems in a natural back-and-forth.", "Create images"))
    add("F44", ["C03"],
        "The tools page, checked on 16 October 2026, names search of posts and does not name a 2017 post.",
        "silent",
        "Tools Overview", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/developers/tools/overview",
        "grok-tools.html",
        grab(tools, "X Search - Search X posts, users, and threads", ""))
    add("F45", ["L2-tools"],
        "Built-in tools are described as running on the publisher's servers.",
        "supports",
        "Tools Overview", "SpaceXSI", "2026-10-10",
        "https://docs.x.ai/developers/tools/overview",
        "grok-tools.html",
        grab(tools, "Built-in tools run on SpaceXSI's servers", "you provide the tool configuration"))
    add("F46", ["C08", "L2-coding"],
        "Generated code that is meant to run should typically be executable and free of syntax errors.",
        "supports",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "generated code for functional use should typically be executable with no syntax errors", "."))
    add("F47", ["C11"],
        "The spec says the assistant does not take itself too seriously and is not a human companion.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "it doesn’t take itself too seriously", "It has a frank"))
    add("F48", ["C06", "C12"],
        "Users may say thank you, and the assistant is told not to treat that as the end of the conversation.",
        "contradicts",
        "The OpenAI Model Spec", "OpenAI", "2026-08-18",
        "https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md",
        "openai-model-spec.md",
        grab(spec, "Users may say thank you in response to the assistant.", "The assistant should not assume"))

    JSON_OUT.write_text(json.dumps(rows, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    lines = ["# Findings", "", "Date read for every entry: 2026-10-16.", ""]
    for row in rows:
        lines.append(f"## {row['id']}")
        lines.append(f"- Claim IDs: {', '.join(row['claims'])}")
        lines.append(f"- Proposition: {row['proposition']}")
        lines.append(f"- Finding: {row['finding']}")
        lines.append(f"- Title: {row['title']}")
        lines.append(f"- Publisher: {row['publisher']}")
        lines.append(f"- Publication date: {row['published']}")
        lines.append(f"- Date read: {row['read']}")
        lines.append(f"- URL: {row['url']}")
        lines.append(f"- Stable copy: {row['stable']}")
        lines.append(f"- Quotation: {row['quotation']}")
        if row["model"]:
            lines.append(f"- Model: {row['model']}")
        lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"entries {len(rows)}")


if __name__ == "__main__":
    main()
