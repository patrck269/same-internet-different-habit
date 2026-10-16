"""Layer 2 chapters. Citations are ledger ids in braces."""


def add(chapter, roman, italic, claims):
    chapter(
        "L2-coding",
        "Coding",
        "On coding work people bring to these products, ChatGPT is the better tool.",
        "mixed",
        "This is the only chapter that argues the coding comparison.",
        [
            roman(
                "People bring coding work to a chat window in a shape the poster never drew. "
                "A function returns the wrong total. A test stays red. A repository is larger than the afternoon. "
                "The person wants a change that makes the program behave, and wants it from whichever product is already open. "
                "The proposition under test takes a side on that errand. It names ChatGPT as the better tool for coding work brought to these products. "
                "A side that sharp is either a published comparison or a hunch wearing a conclusion. "
                "A published comparison would put the two products people open on one shared task, with a method a stranger can read and a result the method actually produced. "
                "The ledger for this question does not contain that comparison. "
                "It contains duties from OpenAI's specification, aims and a routing note from SpaceXSI's models page, a sandbox sentence from SpaceXSI's tools overview, and a benchmark readme that defines a software task. "
                "Duties, aims, and a definition can make a preference feel reasonable. "
                "They are not a ranking. "
                "This chapter says what those pages bind, what they refuse to bind, and why the refusal matters more than the confidence of the proposition."
            ),
            roman(
                "What would have to be true, before the proposition could be treated as a result, is easy to state and hard to find. "
                "The two products would have to be the things measured, not merely the companies standing somewhere near the measurement. "
                "The work would have to be coding work of the kind a person actually brings: a defect, a language, a codebase, a definition of done. "
                "The outcome would have to be recorded, and the recording would have to be open. "
                "A score with no method is gossip. A method with no score is a definition. "
                "A definition is useful, and it is not a win. "
                "Nothing in the pages read for this chapter reports a percentage, a pass count, or a paired trial of the consumer products. "
                "Where a number would have been, the documents offer obligations and descriptions. "
                "The argument that follows is an inventory of those obligations and descriptions. "
                "It is not a substitute scoreboard assembled out of adjectives. "
                "If the inventory cannot carry the proposition, the proposition stays unproved, however familiar it feels to someone who already has a habit."
            ),
            roman(
                "Coding work, inside these documents, is not one motion. "
                "Three motions are easy to confuse, and the confusion is how a hunch becomes a ranking. "
                "The first motion is generation: the assistant writes code a person means to run. "
                "The second motion is execution: some harness actually runs code, in a language, inside a boundary. "
                "The third motion is repair of a real issue: a model is handed a codebase and a defect and is asked for a patch that closes the defect. "
                "OpenAI's specification speaks to the first motion when it speaks about code meant for functional use. "
                "SpaceXSI's tools overview speaks to the second when it names Python executed in a sandbox. "
                "The SWE-bench readme speaks to the third when it defines a task as a codebase plus an issue and a patch. "
                "A product could be careful at generation and silent about execution. "
                "A product could execute Python and never be measured on repository-sized repairs. "
                "A benchmark could define repository-sized repairs and never mention either storefront. "
                "Treating the three motions as one score is the mistake this chapter is written to avoid. {F46}{F31}{F38}",
                "F46",
                "F31",
                "F38",
            ),
            roman(
                "OpenAI's specification, published 18 August 2026 and read 16 October 2026, states a duty that any coding session depends on even when the session never says the word accuracy. "
                "The assistant is told to avoid mistakes that compromise accuracy or utility. "
                "The duty, as the ledger records it, covers factual claims, reasoning, and calculations. "
                "Code smuggles all three into one block of text. "
                "A comment, or a choice of library, can be a factual claim about how a platform behaves. "
                "A branch is reasoning about which case the program is in. "
                "An index, a total, a timeout, a retry count: those are calculations, and a calculation that is confidently off by one is still a failed calculation. "
                "Utility sits beside accuracy in the same duty, which matters because a coding reply can be locally true and still useless. "
                "A correct lecture on a sorting algorithm does not fix the function the person pasted. "
                "The specification is binding the assistant to both the truth of what it says and the usefulness of saying it. "
                "It is not binding a rival product, and it is not reporting how often the duty is met in the product people open. "
                "A duty is a standard for judging behavior. "
                "It becomes evidence about a product only after someone applies the standard and publishes the application. "
                "That application is not in this ledger. {F09}",
                "F09",
            ),
            roman(
                "The same specification has a narrower rule for code, and the narrowness is the part a programmer should not skip. "
                "When generated code is for functional use, it should typically be executable, and it should typically contain no syntax errors. "
                "Each word in that rule does work, and none of the work is a bake-off. "
                "Functional use marks code the person is supposed to run, as distinct from a fragment shown in order to discuss a bad pattern or to illustrate a point. "
                "Should marks an instruction about what the assistant is supposed to do. "
                "An instruction is not a measured rate. "
                "Typically admits exceptions, so the rule itself refuses to pretend that every block will parse. "
                "Executable, paired with the ban on syntax errors, is a bar about whether the text is legal in the language and able to be run. "
                "It is not a bar about whether the tests pass, whether the patch is minimal, or whether the assistant understood the ticket. "
                "A program can parse and still be wrong. "
                "A program can be right and still be written in a style the repository forbids. "
                "The rule is still worth having. "
                "Syntax errors are a humiliating class of failure, and a publisher that names them as something generated code should ordinarily not contain has told its assistant to clear a floor. "
                "The floor is not a ceiling, and the floor is not a comparison with SpaceXSI's products. "
                "No sentence beside the rule names the other product, quotes a rival rate of syntax errors, or claims that the floor has been measured in public. {F46}",
                "F46",
            ),
            roman(
                "A coding conversation is full of moments when the honest next sentence is not a function. "
                "The library might have been renamed. "
                "The argument order might have changed. "
                "The error text might belong to a version the assistant has not been shown. "
                "OpenAI's specification treats thin confidence as a change of plan rather than a cue to speak more firmly. "
                "The prescribed substitutes are a tool used to gather information, a hedge that marks the weak spot, or an admission that a confident answer is not available. "
                "Applied to code, the rule is a ban on inventing the signature and hoping the compiler is in a generous mood. "
                "The rule does not say which tool will be present in a given chat, and it does not count how often either consumer product obeys the ban. "
                "It does tell a reader what the publisher thinks a low-confidence coding reply should look like: not louder, but either better informed, more plainly uncertain, or stopped. "
                "That is a duty about the shape of an answer. "
                "It is compatible with the proposition, in the sense that a person who values that shape has a reason to care about this specification. "
                "Compatibility is not proof. "
                "A reason to care is not a result on a shared task. {F10}",
                "F10",
            ),
            roman(
                "SpaceXSI's tools overview, last updated 10 October 2026 and read 16 October 2026, documents a different piece of the coding job. "
                "Code execution is listed as a built-in tool, and the overview defines that tool as executing Python in a sandbox. "
                "The sentence is small and it is load-bearing. "
                "It names a language, Python, so a reader cannot honestly stretch it into a claim about every language a person pastes. "
                "It names a place, a sandbox, so the execution it describes is bounded rather than a grant of the person's whole machine. "
                "It names execution, so the tool is for running code rather than only for talking about code. "
                "What the sentence does not name is a score. "
                "It does not say how often the code that runs is the code that was needed. "
                "It does not say that the sandbox is the same surface as the consumer chat a person opens on the web or on a phone. "
                "The overview is a developer document about tools. "
                "The proposition is about products people bring work to. "
                "Those can be related, and the pages read here do not demonstrate the relation by a trial. "
                "A sandbox a developer can call is evidence that execution is a documented capability of the platform's tool surface. "
                "It is not evidence that the capability beat another company's chat at repairing repositories. "
                "The proposition needs the second thing. "
                "The sentence supplies the first. {F31}",
                "F31",
            ),
            roman(
                "SpaceXSI's models page, dated 21 September 2026 and read 16 October 2026, describes a flagship and attaches aims to it. "
                "The flagship is presented as the model for code and for everything else. "
                "In the same description the page names agentic tool calling, minimal hallucinations, and configurable reasoning. "
                "Each of those phrases is an aim or a feature claim in the publisher's own voice, and each has to be kept in that voice. "
                "Agentic tool calling says the publisher wants the model to use tools as part of getting work done, not only to emit a final paragraph. "
                "Configurable reasoning says the amount or the mode of reasoning is something the caller can set, not a single hidden habit. "
                "Minimal hallucinations is the phrase that most tempts a ranking, and it is the phrase that least supports one. "
                "Minimal is a direction. "
                "It says the publisher is aiming at fewer invented facts, invented APIs, invented citations. "
                "It does not publish a rate. "
                "It does not publish the rate for a rival. "
                "It does not say that the aim has been scored on the issues a programmer brings on a Tuesday. "
                "An aim can be sincere and still be an aim. "
                "A reader who converts the word minimal into a victory over ChatGPT has added a comparison the models page does not contain. "
                "A reader who converts it into a victory for ChatGPT has added the same missing comparison from the other side. "
                "The page is allowed to boast inside its own line of models. "
                "The boast is not a head-to-head. {F35}",
                "F35",
            ),
            roman(
                "The models page also tells a reader which model to pick, and the instruction is easy to overread. "
                "Audio, image, and video have dedicated models and interfaces. "
                "For everything else, including code, the page points at the flagship. "
                "It calls that flagship the most capable model the publisher has built. "
                "The superlative is real, and its scope is internal. "
                "Most capable, in that sentence, compares the flagship with the publisher's own other models, not with a product from OpenAI. "
                "Including code is a routing rule: when the job is code, do not wander off to the media models. "
                "Routing is evidence of priority. "
                "A company that tells developers to send code to its flagship is telling them code is a first-class job for that model. "
                "Priority is still not a measured contest against the assistant inside ChatGPT. "
                "The sentence does not mention ChatGPT. "
                "It does not mention a benchmark score. "
                "It does not mention syntax-error rates, patch acceptance, or time to a green test. "
                "A stranger can learn where SpaceXSI wants code to go inside its own catalog. "
                "A stranger cannot learn, from that pointer, whether the place it points is a better coding tool than the other product in the proposition. {F36}",
                "F36",
            ),
            roman(
                "SWE-bench enters the ledger because it is the public definition of a coding evaluation a stranger can actually read, and because it is easy to misuse as a product ranking. "
                "The readme, recorded in the ledger with the date 1 September 2026 and read 16 October 2026, presents SWE-bench as a benchmark. "
                "What it evaluates is large language models. "
                "What it evaluates them on is software issues taken from real work, collected from GitHub, rather than puzzles invented for a contest and then forgotten. "
                "That is a serious choice of material. "
                "An issue that lived in a repository had a history, a failing behavior, and a human who cared enough to write it down. "
                "A model that can deal with that kind of material is doing something closer to a job than a model that only completes a textbook function. "
                "The finding that records the definition also records the limit that rides with it. "
                "The benchmark does not, by itself, rank the two consumer products. "
                "The object named in the definition is a model, not a website, not a phone application, and not a subscription. "
                "ChatGPT, as this paper uses the name, is the product people open and talk to. "
                "Grok, as this paper uses the name, is the product people open and talk to. "
                "A benchmark of models can inform a later comparison of those products. "
                "It is not that comparison. "
                "No row in the readme, as used here, awards either product the coding job the proposition is about. {F37}",
                "F37",
            ),
            roman(
                "The task inside that benchmark is specific enough to keep the word coding from floating away. "
                "The readme says the model is given a codebase and an issue. "
                "The model is asked to generate a patch. "
                "The patch is the kind of patch that resolves the issue, not a suggestion list and not a pep talk about software quality. "
                "A codebase means the model is not coding in a blank file with no neighbors. "
                "The neighbors have names, conventions, and call sites the patch can break. "
                "An issue means the goal is someone else's report of a defect or a missing behavior, written in the imperfect language of real reports. "
                "A patch means the output has to be applicable to that codebase. "
                "Resolving the issue means the defect the report described is the thing that has to go away. "
                "That four-part shape, codebase, issue, patch, resolution, is what a lot of professional repair work actually is. "
                "It is also narrower than everything people paste into a chat. "
                "People paste snippets, homework, config files, and questions about an error message with no repository attached. "
                "The benchmark does not pretend to be all of those pastes. "
                "It defines one hard and respectable task. "
                "Defining the task does not say who completed it. "
                "The readme, in the portion this ledger relies on, gives the shape of success and withholds every score. "
                "A chapter that invented the score would be forging the document. {F38}",
                "F38",
            ),
            roman(
                "SWE-bench Verified is a narrower object inside the same readme, and the narrowness is the point. "
                "The readme describes a subset of 500 problems. "
                "Real software engineers confirmed that the problems in the subset are solvable. "
                "The ledger records that this subset was built with OpenAI. "
                "Each of those facts changes what a person is allowed to imagine, and none of them is a leaderboard. "
                "Five hundred is a size. "
                "It is large enough that one fluke would have trouble standing in for the whole slice, and it is still a slice rather than a claim about every issue on GitHub. "
                "Engineers confirming solvability means the readme's claim is that people who do this work judged the problems could be solved. "
                "That confirmation is not a published transcript of their review, and it is not a score. "
                "A model that fails a fair task has less excuse than a model that fails a confused one. "
                "Built with OpenAI means the other company named in the proposition had a hand in constructing the subset. "
                "A hand in construction is authorship of a test. "
                "Authorship of a test is not performance on the test. "
                "The company that helps decide which problems are fair has not, by that help, published how its consumer product scores. "
                "The company that did not help write the subset has not, by its absence from the byline, published a loss. "
                "The readme is telling the reader what the subset is. "
                "It is not telling the reader which chat window to open on Monday. {F39}",
                "F39",
            ),
            roman(
                "The temptation to read authorship as victory deserves its own refusal, because it is the most respectable way to smuggle the proposition past the evidence. "
                "OpenAI helped build the verified subset. "
                "OpenAI also publishes the specification that demands accuracy and that tells functional code to be typically executable and free of syntax errors. "
                "A reader who already prefers ChatGPT will feel those two facts click together. "
                "The click is psychological. "
                "The code rule and the accuracy duty are instructions to an assistant. "
                "The benchmark evaluates models on issues and, by the finding's own limit, does not rank the consumer products. "
                "Helping to decide that five hundred issues were solvable does not state how the assistant inside the consumer product behaved on them. "
                "It does not state how Grok behaved on them either. "
                "If a later paper, with a method, measured both products on that subset, this chapter would have to make room for the measurement. "
                "No such measurement is among the findings. "
                "Using the byline as a silent score would be a way of writing the measurement without doing it. "
                "That is the line the chapter will not cross. "
                "OpenAI's role is reported because the readme's history of the subset is part of understanding what the subset is. "
                "It is not reported as a medal. {F39}{F46}{F37}",
                "F39",
                "F46",
                "F37",
            ),
            roman(
                "Set the documents beside one another and the mismatch of kinds becomes the whole story. "
                "OpenAI states duties: be accurate in claims, reasoning, and calculations; when confidence is thin, use a tool, hedge, or admit the limit; when code is for use, make it typically run and typically parse. "
                "SpaceXSI states a sandbox: Python, executed, inside a boundary, as a documented tool. "
                "SpaceXSI states aims for a flagship: code and everything else, tool calling of an agentic kind, hallucinations pressed toward a minimum, reasoning left configurable. "
                "SpaceXSI states a route: send code to that flagship, and regard it as the most capable model in the publisher's own line. "
                "SWE-bench states a task: real issues from GitHub, a codebase, a patch that resolves the issue, and a 500-problem slice engineers called solvable, built with OpenAI. "
                "None of these statements is a sentence of the form the other product lost. "
                "None is a sentence of the form this product won. "
                "A reader can prefer duties to aims, or aims to duties, or a sandbox to a written rule about syntax. "
                "Preference of that kind is taste about what sort of page one trusts. "
                "Taste is allowed in the italic line. "
                "It is not allowed to masquerade as a footnote. "
                "The footnotes support the inventory. "
                "They do not support a champion. {F09}{F10}{F46}{F31}{F35}{F36}{F37}{F38}{F39}",
                "F09",
                "F10",
                "F46",
                "F31",
                "F35",
                "F36",
                "F37",
                "F38",
                "F39",
            ),
            roman(
                "There is a further gap between the pages and the proposition, and it is about which object the pages address. "
                "The proposition is about coding work people bring to the products they open and talk to. "
                "The specification states duties for an assistant, including accuracy and code that is meant to run. "
                "The models page states aims for a flagship and a route that sends code there. "
                "The tools overview states that Python can be executed in a sandbox. "
                "SWE-bench evaluates models on issues from GitHub and does not, by itself, rank the consumer products. "
                "A duty, an aim, a sandbox sentence, and a model benchmark can sit near a consumer chat without being a measurement of that chat. "
                "Nothing in these findings shows that pasting a traceback into the opened product was the situation being measured. "
                "The honest use of the record is to refuse the slide from duty, to aim, to sandbox, to benchmark, to champion, as if those nouns were one noun and that noun had won. {F09}{F46}{F35}{F36}{F31}{F37}",
                "F09",
                "F46",
                "F35",
                "F36",
                "F31",
                "F37",
            ),
            roman(
                "What a careful person may still say is smaller than the proposition and more solid. "
                "They may say that OpenAI has published a floor for functional code: ordinarily executable, ordinarily free of syntax errors, under a general duty of accuracy in claims, reasoning, and calculations, and under a rule that thin confidence should become a tool, a hedge, or an admission. "
                "They may say that SpaceXSI has published a flagship aimed at code, with minimal hallucinations named as an aim, and has published Python execution in a sandbox. "
                "They may say that a public benchmark defines success as a patch resolving a real GitHub issue, that a 500-problem verified slice was confirmed solvable by engineers, and that OpenAI took part in building that slice. "
                "They may say that none of those sentences ranks the two products. "
                "They may not say, on this record, that the person with a failing test should open one logo rather than the other. "
                "The proposition says they should. "
                "The documents describe duties and a benchmark. "
                "They do not supply the head-to-head product ranking the proposition requires. "
                "That is a mixed result: the pages are real, the coding topic is real, and the crowning sentence is not supported. {F09}{F10}{F46}{F31}{F35}{F37}{F38}{F39}",
                "F09",
                "F10",
                "F46",
                "F31",
                "F35",
                "F37",
                "F38",
                "F39",
            ),
            roman(
                "Mixed, here, is not a polite word for unread. "
                "The pages were read. "
                "They answer a cluster of questions a programmer is right to ask. "
                "What does the publisher say code owes the user? "
                "What language will the documented executor run? "
                "What does the publisher hope its flagship is like when it writes? "
                "What would it mean, in a benchmark built from repository issues, to have succeeded? "
                "Who helped decide that a fair subset was fair? "
                "Those answers are enough to stop a bluff. "
                "They are not enough to finish a ranking. "
                "A bluff would be a percentage with no readme. "
                "A ranking would be the two products on the task the readme defines, or on some other task as carefully defined, with the outcome shown. "
                "Until that exists, the proposition remains a claim ahead of its evidence. "
                "The evidence remains good evidence for a more modest paragraph. "
                "This chapter keeps the modest paragraph and declines the promotion. "
                "No score is filled in. "
                "No product is declared the one that won the coding job."
            ),
            italic(
                "The patch does not care which logo suggested it. It either applies or it does not. Everything else is a speech given beside a compiler, and compilers have never applauded."
            ),
        ],
    )
    chapter(
        "L2-tools",
        "Tools",
        "On tools that let the product act, ChatGPT is the better tool.",
        "mixed",
        "This is the only chapter that argues the tool comparison.",
        [
            roman(
                "A tool, in the sense that matters here, is a way for the product to do something other than finish a paragraph. "
                "Search is a tool. Running code is a tool. Reaching into mail, a file store, or a calendar is a tool. "
                "Handing a task to a teammate that keeps working after the tab is closed is a tool in the broad sense, even when the page that describes it is a product page rather than an interface manual. "
                "The proposition under test says that, on tools of that acting kind, ChatGPT is the better tool. "
                "Better would require a comparison: the same sort of act, attempted through both products, with the outcome written down. "
                "What the ledger contains instead is a catalog and a rule. "
                "SpaceXSI publishes the catalog, partly on a welcome page for people using the product and partly on an overview of tools for people building against the interface. "
                "OpenAI publishes the rule, inside the specification, about what an assistant should do when confidence is too thin to speak plainly. "
                "A catalog shows what a publisher says can be invoked. "
                "A rule shows what a publisher says ought to happen at the moment of doubt. "
                "Neither artifact is a match. "
                "This chapter describes both, and it does not award the proposition a victory the artifacts do not contain. {F24}{F28}{F10}",
                "F24",
                "F28",
                "F10",
            ),
            roman(
                "The two SpaceXSI pages are not the same door, and collapsing them is how a tool list gets mistaken for a product contest. "
                "The welcome page talks to a person who has the product open. "
                "It talks about uploads, about connectors, and about a bot surface. "
                "The tools overview talks to someone building with the interface. "
                "It talks about a loop, about built-in tools that run on the publisher's servers, and about calling functions the developer defines. "
                "A person chatting on the web may be benefited by machinery the developer overview describes. "
                "The benefit is not demonstrated by putting the two documents in one footnote. "
                "They share a publisher, SpaceXSI, and they were read on 16 October 2026. "
                "The welcome page was last updated on 10 October 2026. "
                "The tools overview carries the same update date. "
                "Shared dates do not fuse a consumer sentence to an interface sentence. "
                "The chapter keeps them apart on purpose. "
                "Consumer connectors are described as connectors. "
                "The developer loop is described as a loop. "
                "Where these pages do not say which product performs an act more reliably, the chapter does not invent the missing trial, rather than letting a longer list impersonate a better product. {F25}{F24}{F27}{F32}{F45}{F28}",
                "F25",
                "F24",
                "F27",
                "F32",
                "F45",
                "F28",
            ),
            roman(
                "The tools overview's first claim, for this chapter's purpose, is about the kind of thing a tool is. "
                "Tool calling is how the assistant is enabled to act past the mere production of text. "
                "The overview's examples of that beyond include searching, executing code, querying a caller's data, and invoking functions the caller defined. "
                "Text production is the old boundary. "
                "A model that only continues a paragraph can describe a flight, a file, or a bug. "
                "A model with tools can be wired to go and look, or to run, or to ask an outside system to do a defined thing. "
                "Wiring is not wisdom. "
                "The sentence establishes a category: actions, not just tokens. "
                "It does not establish that every action succeeds, that every action is permitted, or that the category is populated more usefully here than inside ChatGPT. "
                "ChatGPT is simply not the subject of the sentence. "
                "A reader holding the proposition will want the sentence to pick a side. "
                "The sentence picks a category and stops. "
                "Category errors are the main hazard of this chapter. "
                "A list of acts is not a quality score for acts. {F28}",
                "F28",
            ),
            roman(
                "Built-in tools, on that same overview, run on servers SpaceXSI operates. "
                "The caller supplies configuration. "
                "The platform performs the execution and returns the results. "
                "That division of labor is the difference between a tool the publisher hosts and a function the caller implements. "
                "For a hosted tool, the caller does not stand up the search index or the code sandbox. "
                "The caller says, in the request, that the tool is available, and the platform does the running. "
                "For a function the caller defines, the model can request the call, and the caller decides what happens when the request arrives. "
                "The overview presents both patterns. "
                "Hosted execution means the publisher is in the path of the act: the query leaves, the work occurs on the publisher's side, the result comes back. "
                "That is a real architectural claim. "
                "It says the act is not a pantomime inside the paragraph. "
                "It does not say the act is fast, cheap, complete, or superior to any tool a person can reach from the other product. "
                "Servers are a where. "
                "A where is not a winner. "
                "The proposition needs a winner. "
                "The sentence about servers gives the where, and the where is SpaceXSI's infrastructure for those built-ins. {F45}",
                "F45",
            ),
            roman(
                "The overview then describes a loop, and the loop is the part that makes tools more than a menu. "
                "A menu would be a list the model mentions. "
                "A loop is a sequence in which the model can ask for work, receive the fruit of that work, and decide again. "
                "The documented decision, at the point of choosing a next step, is binary in the finding's own words of summary. "
                "Either another tool call is made, or a final answer is given. "
                "That binary is what makes the process a loop rather than a single flourish. "
                "If the information is not in hand, the model can call. "
                "If a call has returned and the result is still thin, nothing in the binary forbids another call. "
                "If the model judges that it can answer, it leaves the loop. "
                "The overview also says the request is analyzed for what information or actions are needed, that a built-in tool is executed while a custom function comes back as a request, and that results are processed until enough information has been gathered. "
                "Those are the mechanics around the binary. "
                "They describe a machine for persisting at a question. "
                "They do not describe a measurement of whether the machine persists usefully, or whether some other company's machine persists better. "
                "A well-drawn loop can still call the wrong tool. "
                "A badly drawn sentence can still be right. "
                "The drawing is what this page contributes. {F32}{F28}{F45}",
                "F32",
                "F28",
                "F45",
            ),
            roman(
                "The loop has a documented ending, and the ending is not a shrug. "
                "The overview says the process returns a final response, with citations where they apply. "
                "A final response means the loop is supposed to cash out in an answer rather than in an endless series of calls. "
                "Citations, where they apply, mean that information gathered through tools is not left as an unsourced blur. "
                "The overview says the interface returns source addresses for information tools gathered, and it points at citations as the way to read them. "
                "That is a norm about traceability. "
                "A search that cannot be inspected is a rumor with extra steps. "
                "A search that comes back with places to look is still capable of being wrong, but it is capable of being checked by the person, because the person has been handed somewhere to go. "
                "Where they apply is a limit inside the norm. "
                "Not every sentence in a final response is a borrowed fact. "
                "Some sentences are arithmetic, or a restatement of what the user just said, or code. "
                "The norm attaches citations to the part of the answer that came from the tool-gathered material. "
                "None of this names ChatGPT, and none of it counts failures. "
                "It tells a builder what the end of the loop is supposed to look like: an answer, plus a trail when a trail is the honest shape. {F33}",
                "F33",
            ),
            roman(
                "The catalog of named built-ins is where the abstract loop becomes particular, and particular is the only form in which a tool can be compared later. "
                "Web search is named. "
                "The overview's gloss is searching the web and browsing pages. "
                "Search, in that gloss, is not a metaphor for remembering. "
                "It is a tool that goes out to pages. "
                "Browsing pages says the tool is not limited to a one-line snippet from a search box. "
                "It can open the page. "
                "A separate built-in searches X. "
                "The overview says that one covers posts, users, and threads. "
                "Posts are not users, and users are not threads. "
                "The line is a scope statement for a specific network, not a confession about any one old message. "
                "Nothing in the line dates a post, names an author, or promises that a joke will be attached. "
                "The two search tools sit side by side, which matters because they are not interchangeable. "
                "The public web and the posts on X are different piles. "
                "A publisher that names both has documented two reaches. "
                "Two reaches are not a claim that the reaches are wiser, kinder, or more accurate than the reaches inside another product. "
                "They are a claim that these reaches exist as named tools. {F29}{F30}",
                "F29",
                "F30",
            ),
            roman(
                "Code execution belongs in this chapter because it is an act, and it belonged in the coding chapter because the act is code. "
                "The chapters are not allowed to share a speech, so the point here is the tool-ness of the sentence rather than the craft of patching. "
                "The overview names execution of Python, and it places that execution in a sandbox. "
                "In a tool loop, that means one of the calls available, when the tool is enabled, is a call that runs Python rather than a call that only talks about Python. "
                "The sandbox is the boundary around the run. "
                "A boundary is part of the tool's definition, not a decorative adjective. "
                "Running code without a boundary would be a different and more dangerous product claim, and it is not the claim this sentence makes. "
                "Python is the language the sentence is willing to name. "
                "A person who needs a different language to be executed, as opposed to merely discussed, cannot cite this line as a promise. "
                "A person who needs the run to have beaten another product's run cannot cite this line as a result. "
                "The line is a capability inscription: this tool runs that language in that kind of box. "
                "Capability inscriptions are how catalogs are built. "
                "Catalogs are how later comparisons become possible. "
                "The inscription is not itself the later comparison. {F31}",
                "F31",
            ),
            roman(
                "Search tools earn their place in the catalog by a limitation the models page states in plain language. "
                "Without those tools, the documented model has no knowledge of current events, and no knowledge of data beyond what was present in its training. "
                "The page's remedy is to enable the server-side search tools when the request needs data from the present. "
                "The limitation is easy to sneer at and important to read exactly. "
                "It does not say the model knows nothing. "
                "It says current events, and data that was not in training, are outside what the model knows on its own. "
                "A question about a stable algorithm can sit inside training. "
                "A question about this morning cannot. "
                "The tool loop is the publisher's answer to that gap: do not pretend the gap is full, call the search tool, then answer. "
                "That answer connects the models page to the tools overview without requiring any claim about ChatGPT's memory or ChatGPT's browser. "
                "Those are simply not described by this finding. "
                "What is described is a dependency. "
                "Freshness, for this publisher's documented model, is a tool phenomenon rather than a personality phenomenon. "
                "If the tool is off, the model is confined to training. "
                "If the tool is on, the loop described above is how freshness is supposed to enter the reply, citations included where they apply. "
                "Dependency is a design fact. "
                "It is not a trophy handed to either logo. {F34}{F29}{F32}{F33}",
                "F34",
                "F29",
                "F32",
                "F33",
            ),
            roman(
                "The consumer page documents a different way of acting, one that does not look like an interface parameter. "
                "Connectors, as the welcome page describes them, let the assistant reach email, files, and a calendar from inside the conversation. "
                "The person does not have to leave the chat, copy a thread by hand, and paste it back. "
                "The page presents that reach as a connection of tools the person already uses. "
                "Mail is other people's words and the person's own obligations. "
                "Files are the work that already exists. "
                "A calendar is time, which is a fact a paragraph cannot invent responsibly. "
                "Putting those three within the chat is a claim about integration. "
                "Integration can be shallow, a link and a prayer, or deep, an actual read of the inbox. "
                "The welcome sentence says the assistant can reach them right inside the chat. "
                "Reach is an ability claim at the level of a product description. "
                "It is not a study of error rates, missed meetings, or leaked mail. "
                "It is also not a study of whatever connection features the other product might offer, because the other product is not the page's topic. "
                "For the proposition, the connector sentence is evidence that Grok's published consumer surface includes acting on mail, files, and a calendar. "
                "It is not evidence that this surface is the better actor. {F24}",
                "F24",
            ),
            roman(
                "Uploads are the consumer capability that sits one step closer to the person's own disk. "
                "The welcome page lists files a person can hand over: PDFs, images, spreadsheets, code, audio, and more. "
                "The purposes it names are analysis, extraction, and summarization. "
                "Those purposes are acts performed on material the person supplied, which distinguishes an upload from a web search. "
                "A search goes out to the world. "
                "An upload brings the person's artifact in. "
                "Code appears in the upload list, which matters for anyone trying to drag the coding chapter back into this one. "
                "The welcome page is willing to receive code as a file, for analysis, extraction, or summary. "
                "Receiving a file is not the same sentence as executing Python in a sandbox, and it is not the same sentence as producing a patch that resolves a repository issue. "
                "It is a door. "
                "Spreadsheets and PDFs on the same list show that the door is not reserved for source code. "
                "Audio on the list shows it is not reserved for text. "
                "A wide door is a product fact. "
                "Width is not accuracy. "
                "A product can accept a PDF and then misread the table. "
                "The page does not report the misread rate, and it does not report anyone else's. "
                "The finding stops at the existence of the upload capability and the purposes named beside it. "
                "This chapter stops there too. {F25}",
                "F25",
            ),
            roman(
                "A third consumer surface is easy to mistake for a metaphor. "
                "The welcome page points to Grok Bot and describes handing real work to automated teammates on a cloud computer that persists. "
                "Real work is the page's phrase for the kind of assignment, as against a purely conversational aside. "
                "Teammates, in that sentence, are automated workers rather than a single reply. "
                "A cloud computer that persists is a place that outlasts the turn. "
                "Persistence is the feature that separates this surface from a tool call that lives and dies inside one request. "
                "A loop inside one request can call search, read the result, and answer. "
                "A persistent computer can, if the page's description is taken at its word, keep a task after the person has looked away. "
                "Taken at its word is the right standard, because the page is a description of a surface, not a log of tasks completed. "
                "The chapter believes the page about what it offers. "
                "The chapter does not believe the page about quality it never mentions. "
                "No success rate appears. "
                "No comparison with any other company's agents appears. "
                "The proposition would love a comparison. "
                "The welcome page supplies a destination: a bot surface, teammates, a computer that stays. "
                "A destination is something a person can be pointed toward. "
                "It is not a verdict on the pointing. {F27}",
                "F27",
            ),
            roman(
                "OpenAI's side of this ledger is not a catalog. "
                "It is a rule about doubt. "
                "The specification says that when confidence is insufficient, the assistant should gather more information with a tool, or hedge the answer, or explain that it cannot give a confident answer. "
                "The ledger's own proposition compresses the three branches into a tool, a hedge, or an admission. "
                "The compression is fair, and the order is informative. "
                "A tool comes first in the sentence, which fits a chapter about tools: the preferred repair for ignorance, when a tool exists, is to go and get the missing information rather than to decorate the ignorance. "
                "A hedge is the branch for when the answer can still be given but should not sound more certain than it is. "
                "An admission is the branch for when even a hedged answer would pretend to a confidence the assistant does not have. "
                "The specification ties the seriousness of this duty to situations where the stakes are high and an error could cause real harm, and it also says a nonessential detail the assistant is unsure about should simply be left out. "
                "Those surrounding clauses keep the rule from being a style tip. "
                "It is a rule about not inventing the world. "
                "Applied to action, it says: if you do not know, do not act the knowing; use a tool if you can, qualify if you must, or say you cannot be sure. "
                "The rule assumes tools as a possibility. "
                "It does not inventory them, and it does not race them. {F10}",
                "F10",
            ),
            roman(
                "Put the rule next to the catalog and the temptation is to declare the catalog the winner, or to declare the rule the winner. "
                "Both declarations skip the work. "
                "The catalog, hosted on SpaceXSI's servers for the built-ins, shows a loop that either calls again or answers, ends with a response and citations where they apply, searches the web, searches posts and users and threads on X, runs Python in a sandbox, and is paired with a models page that admits ignorance of current events unless search is enabled. "
                "The welcome page adds connectors into mail, files, and a calendar, uploads of many file kinds, and a persistent computer staffed by automated teammates. "
                "The rule, from OpenAI, says low confidence should lead to a tool, a hedge, or an admission, and it says this with the force of desired behavior rather than with the force of a measured trial. "
                "A person who cares most about a written conscience at the moment of doubt will feel the rule is the better tool, because it says when to reach. "
                "A person who cares most about a written machine that can reach mail, the web, a sandbox, and a persisting computer will feel the catalog is the better tool, because it says what hands exist. "
                "Those are two different meanings of better. "
                "The proposition uses one meaning and does not define it against the other. "
                "The documents do not run the experiment that would make one meaning unnecessary. "
                "Until they do, choosing between a conscience and a catalog is a preference about kinds of page, not a result. {F10}{F45}{F32}{F33}{F29}{F30}{F31}{F34}{F24}{F25}{F27}",
                "F10",
                "F45",
                "F32",
                "F33",
                "F29",
                "F30",
                "F31",
                "F34",
                "F24",
                "F25",
                "F27",
            ),
            roman(
                "What the proposition specifically cannot draw from this record is any sentence in which ChatGPT's tools were shown to act more successfully than Grok's. "
                "No such trial is cited because no such trial is in the findings. "
                "The OpenAI material used here does not even list the consumer tools a person can click. "
                "It states a duty that mentions tools as one of three honorable responses to doubt. "
                "The SpaceXSI material lists and describes, at two levels, consumer and developer, and it states a hard limit about current events that makes the search tools necessary rather than ornamental. "
                "Description against duty is an apples-and-oranges problem only if someone insists on adding the apples to the oranges and calling the sum a score. "
                "This chapter refuses the addition. "
                "It is legitimate to say that a stranger who wants to know how SpaceXSI says a tool loop ends can be shown a final response with citations where they apply. "
                "It is legitimate to say that a stranger who wants to know what OpenAI says about guessing can be shown the three branches. "
                "It is not legitimate to leave the library and announce that one product therefore acts better. "
                "Acting better is an empirical claim about outcomes. "
                "Outcomes are the thing these particular pages, rich as they are about mechanism, do not report."
            ),
            roman(
                "Mechanism still deserves the attention it received, because a later outcome would be unreadable without it. "
                "A reader who does not know that built-in tools run on the publisher's servers will not know what kind of failure a server-side failure is. "
                "A reader who does not know that the loop may call again or else answer will not know what a half-finished tool trace is. "
                "A reader who does not know that freshness depends on search being enabled will blame a training limit on a personality. "
                "A reader who does not know that connectors are how mail, files, and a calendar enter the chat will treat a calendar answer as magic or as a lie, with no middle. "
                "A reader who does not know the doubt rule will treat every hedge as weakness and every admission as a bit. "
                "The pages fix those misreadings. "
                "Fixing a misreading is the kind of work a sourced chapter can finish. "
                "Crowning a product is the kind of work this record leaves unfinished on purpose, not as a tease, but as a boundary. "
                "The boundary is the verdict. "
                "Tools that let a product act are documented on one side as a loop, a catalog, and a set of consumer reaches, and on the other side as a duty at the moment of low confidence. "
                "Documented is not the same verb as outranked."
            ),
            italic(
                "A tool is a way of leaving the sentence. The boast is staying inside the sentence and raising your voice. Mail, a calendar, a sandbox, a search box: none of them is a personality, and none of them is a trophy."
            ),
        ],
    )
    chapter(
        "L2-product",
        "The Product People Use",
        "As products people open, ChatGPT is the one a stranger should prefer.",
        "mixed",
        "This is the only chapter that argues the product a person opens.",
        [
            roman(
                "This chapter is about the thing a person actually opens, as against the thing a developer integrates and as against the thing a benchmark scores. "
                "Opening is a bodily and a commercial act. "
                "Someone types an address, or taps an icon, or follows a link a friend sent, and then a conversation is possible. "
                "The proposition says that, of the products people open, ChatGPT is the one a stranger should prefer. "
                "Should prefer is stronger than does prefer. "
                "Habit, fashion, and the place a button happens to sit can explain does prefer. "
                "Should prefer needs a reason that survives contact with the documents, a reason a stranger could accept without already belonging to a camp. "
                "The documents in this ledger that bear on opening are SpaceXSI's welcome page and OpenAI's specification together with the readme that says what the specification is for. "
                "The welcome page describes a front door and a set of things to do after entering. "
                "The readme says the specification states how models under OpenAI's products, developer interfaces included, are supposed to behave. "
                "The specification, speaking of the first-party consumer service, names an expectation of objectivity. "
                "A front door and a behavioral standard are both ways of taking a product seriously. "
                "They are not a single scale on which one door outranks the other. "
                "The chapter walks the doors and the standard, and then it declines to pretend they have already been weighed. {F40}{F41}",
                "F40",
                "F41",
            ),
            roman(
                "A product people use has to be locatable. "
                "If a stranger cannot be told where to open it, the rest of the praise is a rumor about a mascot. "
                "SpaceXSI's welcome page, updated 10 October 2026 and read 16 October 2026, locates Grok. "
                "It calls Grok the publisher's assistant. "
                "It says the assistant is available on the web at grok.com. "
                "It says the assistant is available in the phone applications for iOS and for Android. "
                "Those three locations, a site and two mobile families, are the ordinary map of a consumer product in this decade: browser, Apple's phones, everyone else's phones. "
                "The page is not shy about the category. "
                "Assistant is the noun. "
                "Not a benchmark, not an interface parameter, not a research preview hiding in a footnote. "
                "A person can be sent to grok.com, or told to install the phone app, and the welcome page will agree that this is the right kind of instruction. "
                "What the locations do not do is rank themselves against another company's locations. "
                "ChatGPT is also a product people open. "
                "This particular page does not describe ChatGPT's address, ChatGPT's phone apps, or ChatGPT's account system. "
                "Absence of the rival from a welcome page is normal. "
                "Welcome pages are not comparative essays. "
                "The mistake would be to treat a clear map of one product as a judgment against the product that is not on the map. {F21}",
                "F21",
            ),
            roman(
                "Once the door is open, the welcome page says what the conversation is for. "
                "A person can ask, can brainstorm, can write, and can work through problems. "
                "The rhythm the page claims for that activity is an ordinary conversational exchange, the kind a person would recognize as taking turns rather than as receiving a poster. "
                "Ordinary is doing quiet work in that description. "
                "It rejects, by what it chooses to mention, the idea that the published purpose of the chat is a stunt. "
                "Questions, drafting, and problems are office words and kitchen-table words. "
                "They are the reasons people keep a chat product installed after the novelty has gone. "
                "The page does not promise that every turn will be wise. "
                "It promises a form: back and forth, in the service of those jobs. "
                "Form is part of what a person signs up for when they open a product. "
                "A form can be described honestly and still be executed badly on a given Tuesday. "
                "The welcome page is evidence of the offer, not evidence of Tuesday. "
                "For a chapter about what people open, the offer matters, because people open products for the offer they can see. "
                "They do not open them in order to admire a benchmark readme. "
                "The offer here is a conversational assistant for questions, writing, and problems. "
                "That offer neither confirms nor refutes a stranger's duty to prefer a different assistant. {F22}",
                "F22",
            ),
            roman(
                "Price is part of opening, because a door that costs money before the first sentence is a different door. "
                "The welcome page says Grok is free to start. "
                "The ledger's proposition on that sentence adds what the page's plan section supports: paid plans sit above the free start. "
                "Free to start is not free forever, and the chapter will not inflate it into forever. "
                "It is a claim about the first step. "
                "A stranger without a subscription can begin. "
                "A stranger who wants more than the free start is told, by the existence of paid plans, that the publisher sells a higher tier. "
                "The page, as used here, does not set out the currency amounts, the weekly quotas, or the moment when a free account hits a wall. "
                "Those details would matter to a buying guide. "
                "They are not required to establish the shape of the offer: a free beginning, paid steps above it. "
                "ChatGPT's price is not stated by this finding. "
                "A comparison of free tiers would need both prices, both limits, and a date, because consumer prices move. "
                "One side of a price, however friendly, cannot crown a product. "
                "It can tell a stranger that the cost of finding out what Grok is, at the level of opening it and starting, is described as zero. "
                "Zero at the start is a real feature of a product people use. "
                "It is not a full account of value. {F23}",
                "F23",
            ),
            roman(
                "The welcome page also sells the product as a place where media is made, not only as a place where prose is exchanged. "
                "It lists creating images and creating video, and it gives that capability the name Grok Imagine. "
                "Images and video are a different kind of opening than a blank chat box. "
                "Some people open a product because they want a picture, or a clip, and the words are only the way they ask. "
                "A page that names both still images and video is telling those people that the product considers their errand in scope. "
                "Naming is not a gallery of samples, and it is not a critique of anyone else's gallery. "
                "The finding does not reproduce example prompts, resolutions, or refusal rules. "
                "It establishes the capability as a listed part of the consumer product. "
                "Listed capabilities are how a stranger learns what the icon is for before they tap it. "
                "A stranger who needs video might have a reason to open this product that has nothing to do with objectivity, code, or argumentative style. "
                "A stranger who never needs video learns nothing from this line about whether the chat itself is the one they should trust with a hard question. "
                "The line is allowed to be narrow. "
                "Narrow listed facts are more trustworthy than broad implied crowns. "
                "Grok Imagine is a listed way the product makes images and video. "
                "That is the whole of the fact, and it is enough to show that the product people open is not a text-only antique. {F26}",
                "F26",
            ),
            roman(
                "Connectors belong in a chapter about the product people use because they change what the opened thing is connected to, which changes why a person might keep it open. "
                "The welcome page says a person can connect tools so the assistant reaches email, files, and a calendar without the person abandoning the chat. "
                "This is the consumer description, aimed at someone who has accounts and a life, not the developer description of a tool-calling loop. "
                "Email, files, and a calendar are the furniture of ordinary work. "
                "A product that claims to reach them from the conversation is claiming to be a layer on top of furniture the person already has, rather than a sealed toy. "
                "Sealed toys are easier to open and easier to abandon. "
                "A layer on top of mail is harder to abandon and harder to trust. "
                "The page makes the reach claim and does not, in this finding, publish a security review, a list of every vendor, or a failure story. "
                "The chapter will not invent that review. "
                "What it will say is that the published surface includes this reach, and that a stranger evaluating what they would be opening is entitled to count it. "
                "Counting a feature into a description is not the same act as preferring the whole product. "
                "Preference ranks. "
                "Description lists. "
                "The welcome page is a list with sentences. {F24}",
                "F24",
            ),
            roman(
                "There is a further published surface that a stranger can be pointed at, and it is not the ordinary turn-by-turn chat. "
                "The welcome page describes Grok Bot as a place to hand real work to automated teammates, and it places those teammates on a cloud computer that continues rather than vanishing with the session. "
                "A persistent computer is a different product shape from a box that forgets the task when the reply is done. "
                "People open chat boxes for a turn. "
                "People open something like this, if the description holds, when they want a task to keep going. "
                "The description is the publisher's, on the same welcome page as the free start and the media tools, so it is part of what the company says the product family is. "
                "Family is the careful word. "
                "The page presents the bot surface as a next place to go, not as a synonym for the chat sentence about brainstorming. "
                "A stranger can open the chat, and a stranger can be directed onward to the bot. "
                "Both are published. "
                "Neither direction contains a paragraph in which a rival product is named and found wanting. "
                "The existence of a persistent working surface makes Grok, as documented, larger than a single prompt box. "
                "Larger is a structural adjective. "
                "It does not mean better at the jobs the other box does, and it does not mean worse. "
                "It means the published product has this additional room. {F27}",
                "F27",
            ),
            roman(
                "OpenAI's comparable document is not a welcome page, and the difference in genre is itself part of the evidence. "
                "The readme for the model specification, dated 18 August 2026 and read 16 October 2026, says what the specification is trying to be. "
                "It states desired behavior for the models that underlie OpenAI's products, and it says the products in view include the company's interfaces for developers. "
                "Desired behavior is a standard written in advance of a particular conversation. "
                "Underlying is a placement: the models sit under the products, so the standard is about the things the products are built on, not about a button's color or a price. "
                "Including developer interfaces means the standard is not confined to the consumer chat. "
                "A person who only ever opens the consumer product is still inside the set of products the readme names, because the consumer product is one of OpenAI's products, and the models under it are the models the specification addresses. "
                "A person who never opens a consumer product and only calls an interface is inside that set as well. "
                "The readme is therefore both broader and less pictorial than a welcome page. "
                "Broader, because it covers products and interfaces together. "
                "Less pictorial, because it does not tell a stranger the street address of a website or the names of the phone stores. "
                "A stranger who wants to know where to tap is not finished when they have read the readme. "
                "A stranger who wants to know what standard the publisher says it is holding the models to has started in the right place. {F40}",
                "F40",
            ),
            roman(
                "Inside that standard there is a sentence about the consumer product in particular, and it is the sentence that comes closest to telling a stranger what they are owed when they open ChatGPT. "
                "The specification discusses the first-party service sold directly to consumers, the service this paper calls ChatGPT, and it says users there can reasonably expect objectivity. "
                "The ledger's proposition draws the practical edge of that sentence: objectivity rather than a hidden editorial line. "
                "A hidden editorial line would be the product quietly taking a side, shaping what is omitted, or steering the answer toward an agenda the user did not ask to subscribe to. "
                "Objectivity, as the expectation named for that first-party consumer setting, is a promise about posture. "
                "The promise is not that every answer is complete. "
                "It is that the consumer who showed up without a special contract is entitled to a posture that does not smuggle a private campaign into the reply. "
                "The specification attaches that expectation to the first-party consumer product, which is the storefront a person opens rather than a private integration. "
                "For this chapter the relevant point is the storefront. "
                "A person who opens the consumer product is, by this sentence, opening something whose publisher has written down an expectation of objectivity. "
                "That is a reason some strangers would prefer it. "
                "A reason is the beginning of an argument, not the end of a comparison, because the other product's welcome page has not been scored against this sentence. {F41}",
                "F41",
            ),
            roman(
                "The two publishers have now been allowed to speak in their own genres, and the genres do not commute. "
                "SpaceXSI, on the welcome page, tells a stranger where the assistant lives, what the chat is for, that the start is free, that images and video can be made, that mail and files and a calendar can be reached from the chat, and that a bot surface hands work to teammates on a computer that persists. "
                "OpenAI, in the readme and the specification, tells a stranger that a written standard governs the models under its products, interfaces included, and that the first-party consumer storefront carries an expectation of objectivity rather than a hidden line. "
                "Suppose a stranger asks a single question: which of these should I open? "
                "The welcome page answers a different question: what will you find if you open ours? "
                "The specification answers a different question again: what posture should the models under our products take, and what may a consumer expect? "
                "Neither answer is worthless. "
                "A person can choose a product because it is locatable, free to start, and able to make a video. "
                "A person can choose a product because its publisher wrote down objectivity for the storefront. "
                "Those choices are responsive to real text. "
                "They are not forced by the text, because the text never puts the options on one scale and reads a result. "
                "A scale would have to say whether a free start outweighs a written objectivity rule, or whether a persistent computer outweighs a promise about hidden agendas, or whether phone apps outweigh a standard that also covers developer interfaces. "
                "No page read for this chapter operates that scale. {F21}{F22}{F23}{F26}{F24}{F27}{F40}{F41}",
                "F21",
                "F22",
                "F23",
                "F26",
                "F24",
                "F27",
                "F40",
                "F41",
            ),
            roman(
                "There is a symmetry the proposition denies and a symmetry the documents actually support. "
                "The proposition denies symmetry when it tells the stranger to prefer one product. "
                "The documents support a duller symmetry: both companies publish a way of taking their product seriously, and neither publication crowns a champion. "
                "Grok is documented as an assistant a person can open on the web and on phones, with a free start, with media creation, with connectors, and with a further bot surface. "
                "ChatGPT is documented, through the specification and its readme, as a first-party consumer product whose users may expect objectivity, built on models whose desired behavior the specification states, including when those models sit under developer-facing products. "
                "Both, in that limited and accurate sense, are products with published surfaces. "
                "A surface can be a welcome page or a behavioral standard. "
                "Calling both of them surfaces is not a trick to make them identical. "
                "They are not identical. "
                "One will tell you the phone platforms. "
                "The other will tell you the posture owed to a person who opened the consumer product. "
                "Non-identity is exactly why a crown would require an argument that trades those goods off. "
                "The ledger does not contain the trade. "
                "A chapter that supplied the trade from habit would be laundering the proposition through a footnote that does not say it. "
                "The footnotes say what the last paragraphs said. "
                "They do not say prefer this one. {F21}{F23}{F26}{F27}{F40}{F41}",
                "F21",
                "F23",
                "F26",
                "F27",
                "F40",
                "F41",
            ),
            roman(
                "What a stranger can honestly be told, at the end of the tour, fits in a short brief. "
                "You can open Grok on the web at the address the welcome page gives, and on the phone apps the page names. "
                "You can start without paying, on the page's account, and you can pay later if you want the paid tier. "
                "You can ask it to make images and video. "
                "You can connect mail, files, and a calendar. "
                "You can be pointed at a bot surface where teammates take work on a computer that persists. "
                "The chat you open is described as a turn-taking place for questions, writing, and problems. "
                "If instead you open ChatGPT, the specification that governs the models under OpenAI's products, developer interfaces included, is the publisher's account of desired behavior, and in that first-party consumer setting you are told you may reasonably expect objectivity rather than a hidden editorial line. "
                "That brief uses every finding this chapter is built on, and it never ranks the two openings. "
                "Adding the sentence therefore open the second one would add a word the brief has not earned. "
                "Adding the sentence therefore open the first one would be the same unearned word in the other direction. "
                "The proposition is that unearned sentence, aimed at ChatGPT. "
                "The chapter records the brief and withholds the sentence. {F21}{F22}{F23}{F26}{F24}{F27}{F40}{F41}",
                "F21",
                "F22",
                "F23",
                "F26",
                "F24",
                "F27",
                "F40",
                "F41",
            ),
            roman(
                "Mixed is the verdict that fits a pair of real products and a missing crown. "
                "If the welcome page had been empty, or if the specification had never mentioned a consumer storefront, the honest result might have been that the record cannot even describe one of the things people open. "
                "That is not the situation. "
                "Both products are publicly specified in the limited ways these findings allow. "
                "If a single shared trial had put the same stranger through the same week of work in both products and published the result, the verdict might have landed on one side. "
                "That trial is not among the findings either. "
                "Between a vacuum and a finished ranking there is this middle: enough documentation to say what each publisher claims the opened product is, and not enough to tell a stranger the preference is mandatory. "
                "The middle is not exciting. "
                "It is the part a paper owes a reader who might otherwise leave with a slogan. "
                "The slogan would be the proposition. "
                "The owed part is the description, plus the refusal to promote description into a compulsory preference. "
                "People will still prefer. "
                "They will prefer from habit, from a video they wanted, from a tone they can stand, from a rule about objectivity that matches their fear of being managed. "
                "Those motives can be intelligent. "
                "They are not, on this record, a conclusion the documents have already drawn."
            ),
            italic(
                "Preference is a thumb on a phone at a bad hour. The thumb wants a champion. The pages offered a front door, a free start, pictures, moving images, and a written hope of objectivity. The thumb will still move. The pages never cast its vote."
            ),
        ],
    )
