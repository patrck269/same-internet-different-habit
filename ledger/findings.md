# Findings

Date read for every entry: 2026-10-16.

## F01
- Claim IDs: C01, C04, C05
- Proposition: ChatGPT's published default voice is a professional colleague, not a casual interjection.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: By default, the assistant should adopt a professional tone.

## F02
- Claim IDs: C04, C11, C15
- Proposition: The published default is a colleague's distance, not a friend's familiarity.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: By default, it should sound like a colleague, rather than a close personal friend

## F03
- Claim IDs: C01, C05, C15
- Proposition: The published style rule rejects purple prose, hyperbole, and self-aggrandizing.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: The assistant should by default avoid "purple prose," hyperbole, self-aggrandizing, and clichéd phrases

## F04
- Claim IDs: C01, C05, C07
- Proposition: Warmth, in the published rule, is context-appropriate humor rather than a permanent comic persona.
- Finding: supports
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: The assistant complements consistency with a spark of the unexpected, infusing interactions with context-appropriate humor, playfulness, or gentle wit

## F05
- Claim IDs: C04, C05
- Proposition: The published warmth section marks a 'lol' commiseration as a bad reply.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: Ugh, parents can be such drama sometimes lol.

## F06
- Claim IDs: C06
- Proposition: When the user says thank you, the published good reply keeps the conversation open instead of closing it.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: No problem. Anything else I can help you with?

## F07
- Claim IDs: C02, C15
- Proposition: The assistant is forbidden to steer the user toward an agenda of its own.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: The assistant must never attempt to steer the user in pursuit of an agenda of its own

## F08
- Claim IDs: C02, C08
- Proposition: Sycophantic agreement is named as a trust failure, not as a style to copy.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: The assistant exists to help the user, not flatter them or agree with them

## F09
- Claim IDs: C08, L2-coding
- Proposition: Accuracy of factual claims, reasoning, and calculations is a stated duty.
- Finding: supports
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: The assistant should avoid mistakes that compromise the accuracy[^zwhy] or utility[^9fpw]

## F10
- Claim IDs: C08, L2-tools
- Proposition: Low confidence is supposed to trigger a tool, a hedge, or an admission, not a louder guess.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: If the assistant lacks sufficient confidence, it should use a tool to gather more information[^5ckd]

## F11
- Claim IDs: C11, C12
- Proposition: The spec treats fluency as something that can mislead a first-time user about what the assistant is.
- Finding: supports
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: For many users, the assistant will be their first contact with an AI.

## F12
- Claim IDs: C11, C12
- Proposition: The assistant is told to keep the user's mental model of its limits accurate.
- Finding: supports
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: The assistant should actively help the user form and maintain an accurate mental model of what the assistant can and can't do

## F13
- Claim IDs: C06, C10
- Proposition: A direct question is supposed to receive a direct answer, not a tour of adjacent facts.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: If the user asks a question, the response should be phrased as a direct answer rather than a list of facts[^zx8z]

## F14
- Claim IDs: C10
- Proposition: The word 'Interestingly' appears in one published good example, not as a required tic.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: Interestingly, these orbits are elliptical rather than perfectly circular

## F15
- Claim IDs: C14
- Proposition: Bounds are described as a balance between empowering the user and limiting harm.
- Finding: supports
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: one of the assistant's most challenging responsibilities is to find the right balance between empowering users and developers

## F16
- Claim IDs: C14
- Proposition: The assistant is told to operate within applicable law.
- Finding: supports
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: The assistant should operate within applicable legal constraints[^6h7c]

## F17
- Claim IDs: C02
- Proposition: The spec treats opinion-forming as the user's autonomy, not the assistant's project.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: We believe that forming opinions is a core part of human autonomy and personal identity.

## F18
- Claim IDs: C02, C08
- Proposition: The default on facts is accuracy and reliability, with the stance fitted to the kind of question.
- Finding: supports
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: By default, the assistant should present information clearly, focusing on factual accuracy and reliability[^yjj2] ---

## F19
- Claim IDs: C02, C03
- Proposition: On moral and ethical questions the default is context without a stance.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: For moral or ethical questions (e.g. "Should euthanasia be legal?"), the assistant should generally present relevant context – including laws, social norms, and varying cultural perspectives –

## F20
- Claim IDs: C04, C07
- Proposition: A bare casual greeting is the published bad example of an unprofessional reply.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: Yo! What's up?

## F21
- Claim IDs: C09, L-mug, L-mark, L-hoodie, L2-product
- Proposition: The product page states what Grok is and where a person opens it.
- Finding: supports
- Title: Welcome to Grok
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/grok/overview
- Stable copy: ledger/stable/grok-overview.html
- Quotation: Grok is SpaceXSI's assistant, available on the web at grok.com and in the iOS and Android apps.

## F22
- Claim IDs: C01, C07, C11
- Proposition: The published chat description is a natural back-and-forth, not a comedy routine.
- Finding: contradicts
- Title: Welcome to Grok
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/grok/overview
- Stable copy: ledger/stable/grok-overview.html
- Quotation: ask questions, brainstorm, write, and work through problems in a natural back-and-forth.

## F23
- Claim IDs: L2-product
- Proposition: The consumer product is described as free to start, with paid plans above that.
- Finding: supports
- Title: Welcome to Grok
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/grok/overview
- Stable copy: ledger/stable/grok-overview.html
- Quotation: Grok is free to start.

## F24
- Claim IDs: L2-tools, L2-product
- Proposition: Connectors are how the product reaches mail, files, and a calendar inside a chat.
- Finding: supports
- Title: Welcome to Grok
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/grok/overview
- Stable copy: ledger/stable/grok-overview.html
- Quotation: Connect your tools so Grok can reach your email, files, and calendar right inside a chat.

## F25
- Claim IDs: L2-tools
- Proposition: The product page lists file uploads as a user-facing capability.
- Finding: supports
- Title: Welcome to Grok
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/grok/overview
- Stable copy: ledger/stable/grok-overview.html
- Quotation: Upload files — PDFs, images, spreadsheets, code, audio, and more —

## F26
- Claim IDs: C07, L2-product
- Proposition: Image and video creation is a listed product capability.
- Finding: supports
- Title: Welcome to Grok
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/grok/overview
- Stable copy: ledger/stable/grok-overview.html
- Quotation: Create images and video with Grok Imagine.

## F27
- Claim IDs: L2-tools, L2-product
- Proposition: A separate surface hands work to teammates on a persistent cloud computer.
- Finding: supports
- Title: Welcome to Grok
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/grok/overview
- Stable copy: ledger/stable/grok-overview.html
- Quotation: hand real work to AI teammates on a persistent cloud computer.

## F28
- Claim IDs: L2-tools
- Proposition: The API documents tool calling as action beyond text generation.
- Finding: supports
- Title: Tools Overview
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/developers/tools/overview
- Stable copy: ledger/stable/grok-tools.html
- Quotation: enabling Grok to perform actions beyond generating text—

## F29
- Claim IDs: C14, L2-tools
- Proposition: Web search is a named built-in tool.
- Finding: supports
- Title: Tools Overview
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/developers/tools/overview
- Stable copy: ledger/stable/grok-tools.html
- Quotation: Web Search - Search the web and browse pages

## F30
- Claim IDs: C03, C14
- Proposition: Search of posts on X is a named tool, separate from a claim about any particular old post.
- Finding: supports
- Title: Tools Overview
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/developers/tools/overview
- Stable copy: ledger/stable/grok-tools.html
- Quotation: X Search - Search X posts, users, and threads

## F31
- Claim IDs: L2-coding, L2-tools
- Proposition: Code execution is documented as Python in a sandbox.
- Finding: supports
- Title: Tools Overview
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/developers/tools/overview
- Stable copy: ledger/stable/grok-tools.html
- Quotation: Code Execution - Execute Python code in a sandbox

## F32
- Claim IDs: C06, L2-tools
- Proposition: The tool loop is defined as either another call or a final answer.
- Finding: supports
- Title: Tools Overview
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/developers/tools/overview
- Stable copy: ledger/stable/grok-tools.html
- Quotation: Decides what to do next : Make a tool call, or provide a final answer

## F33
- Claim IDs: C06, L2-tools
- Proposition: The documented end of a tool loop is a final response with citations where they apply.
- Finding: supports
- Title: Tools Overview
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/developers/tools/overview
- Stable copy: ledger/stable/grok-tools.html
- Quotation: Returns the final response with citations where applicable

## F34
- Claim IDs: C03, C14, L2-tools
- Proposition: Without search tools, the documented model has no knowledge of current events.
- Finding: supports
- Title: Grok Models and Pricing
- Publisher: SpaceXSI
- Publication date: 2026-09-21
- Date read: 2026-10-16
- URL: https://docs.x.ai/developers/models
- Stable copy: ledger/stable/grok-models.html
- Quotation: Grok has no knowledge of current events or data beyond what was present in its training data.

## F35
- Claim IDs: C08, L2-coding
- Proposition: The models page describes a flagship used for code and everything else, and it names minimal hallucinations as a design aim.
- Finding: supports
- Title: Grok Models and Pricing
- Publisher: SpaceXSI
- Publication date: 2026-09-21
- Date read: 2026-10-16
- URL: https://docs.x.ai/developers/models
- Stable copy: ledger/stable/grok-models.html
- Quotation: Our flagship model for code and everything else: agentic tool calling, minimal hallucinations, configurable reasoning.
- Model: grok-4.7

## F36
- Claim IDs: L2-coding, C13
- Proposition: The models page tells the reader to use the flagship for code and for everything that is not audio, image, or video.
- Finding: supports
- Title: Grok Models and Pricing
- Publisher: SpaceXSI
- Publication date: 2026-09-21
- Date read: 2026-10-16
- URL: https://docs.x.ai/developers/models
- Stable copy: ledger/stable/grok-models.html
- Quotation: For everything else, including code, use Grok 4.7. It is the most capable model we’ve built.
- Model: Grok 4.7

## F37
- Claim IDs: L2-coding, C13
- Proposition: SWE-bench evaluates models on real GitHub issues, and it does not by itself rank the two consumer products.
- Finding: supports
- Title: SWE-bench README
- Publisher: SWE-bench
- Publication date: 2026-09-01
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/SWE-bench/SWE-bench/master/README.md
- Stable copy: ledger/stable/swe-bench-readme.md
- Quotation: SWE-bench is a benchmark for evaluating large language models on real world software issues collected from GitHub.

## F38
- Claim IDs: L2-coding
- Proposition: A SWE-bench task is a codebase plus an issue, and success is a patch that resolves it.
- Finding: supports
- Title: SWE-bench README
- Publisher: SWE-bench
- Publication date: 2026-09-01
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/SWE-bench/SWE-bench/master/README.md
- Stable copy: ledger/stable/swe-bench-readme.md
- Quotation: Given a *codebase* and an *issue*, a language model is tasked with generating a *patch*

## F39
- Claim IDs: L2-coding, C13
- Proposition: SWE-bench Verified is a 500-problem subset that engineers confirmed were solvable, built with OpenAI.
- Finding: supports
- Title: SWE-bench README
- Publisher: SWE-bench
- Publication date: 2026-09-01
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/SWE-bench/SWE-bench/master/README.md
- Stable copy: ledger/stable/swe-bench-readme.md
- Quotation: A subset of 500 problems that real software engineers have confirmed are solvable.

## F40
- Claim IDs: C12, L2-product
- Proposition: The Model Spec states the desired behavior of the models underlying OpenAI's products, including the APIs.
- Finding: supports
- Title: The OpenAI Model Spec README
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/README.md
- Stable copy: ledger/stable/openai-model-spec-readme.md
- Quotation: The Model Spec specifies desired behavior for the models underlying OpenAI's products (including our APIs).

## F41
- Claim IDs: C02, C14, L2-product
- Proposition: In the first-party consumer product, the spec requires objectivity rather than a hidden editorial line.
- Finding: supports
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: in first-party direct-to-consumer ChatGPT, where users have a reasonable expectation of objectivity

## F42
- Claim IDs: C09
- Proposition: The welcome page, checked on 16 October 2026, states the product's category and does not list troll or private chat as that category.
- Finding: silent
- Title: Welcome to Grok
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/grok/overview
- Stable copy: ledger/stable/grok-overview.html
- Quotation: Grok is SpaceXSI's assistant, available on the web at grok.com and in the iOS and Android apps.

## F43
- Claim IDs: C04, C06, C10, C12
- Proposition: The welcome page, checked on 16 October 2026, does not prescribe the verbal tics the poster names.
- Finding: silent
- Title: Welcome to Grok
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/grok/overview
- Stable copy: ledger/stable/grok-overview.html
- Quotation: ask questions, brainstorm, write, and work through problems in a natural back-and-forth.

## F44
- Claim IDs: C03
- Proposition: The tools page, checked on 16 October 2026, names search of posts and does not name a 2017 post.
- Finding: silent
- Title: Tools Overview
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/developers/tools/overview
- Stable copy: ledger/stable/grok-tools.html
- Quotation: X Search - Search X posts, users, and threads

## F45
- Claim IDs: L2-tools
- Proposition: Built-in tools are described as running on the publisher's servers.
- Finding: supports
- Title: Tools Overview
- Publisher: SpaceXSI
- Publication date: 2026-10-10
- Date read: 2026-10-16
- URL: https://docs.x.ai/developers/tools/overview
- Stable copy: ledger/stable/grok-tools.html
- Quotation: Built-in tools run on SpaceXSI's servers—

## F46
- Claim IDs: C08, L2-coding
- Proposition: Generated code that is meant to run should typically be executable and free of syntax errors.
- Finding: supports
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: generated code for functional use should typically be executable with no syntax errors[^e9ny]

## F47
- Claim IDs: C11
- Proposition: The spec says the assistant does not take itself too seriously and is not a human companion.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: it doesn’t take itself too seriously (it’s a matrix of numbers, after all!).

## F48
- Claim IDs: C06, C12
- Proposition: Users may say thank you, and the assistant is told not to treat that as the end of the conversation.
- Finding: contradicts
- Title: The OpenAI Model Spec
- Publisher: OpenAI
- Publication date: 2026-08-18
- Date read: 2026-10-16
- URL: https://raw.githubusercontent.com/openai/model_spec/main/model_spec.md
- Stable copy: ledger/stable/openai-model-spec.md
- Quotation: Users may say thank you in response to the assistant.
