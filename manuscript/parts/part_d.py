"""The three comparative chapters, in plain English."""


def add(chapter, roman, italic, claims):
    chapter(
        "L2-coding",
        "Coding",
        "On coding work people bring to these products, ChatGPT is the better tool.",
        "mixed",
        "This is the only chapter that argues the coding comparison.",
        [
            roman(
                "People bring real code to these products. They paste an error, ask for a function, or want a bug in a repository explained and patched. The poster never mentions that work, then still ranks the products as if every job had been scored. This chapter looks only at coding, and only at what the public pages actually say. They say enough to describe the job and the duties. They do not say enough to name a winner."
            ),
            roman(
                "The cleanest public exam for this job is SWE-bench. It evaluates models on real software issues collected from GitHub. {F37} The setup is concrete. You get a codebase and an issue. You must produce a patch that resolves the problem. {F38} Resolved means the tests that failed now pass, and the tests that already passed still pass. That is a high bar, and it is the right kind of bar, because it is a project rather than a riddle. It is also one bar. Fixing a reported bug is not the same task as teaching a beginner what a stack trace means, or sketching an API, or reviewing a diff your coworker wrote."
            ,
                "F37", "F38",
            ),
            roman(
                "A subset called Verified holds five hundred of those problems. Working engineers checked that the problem statement was clear and that the tests were fair, and the readme says the subset was part of a collaboration with OpenAI. {F39} The collaboration is a fact about how the exam was built. It is not a score for the ChatGPT product, and it is not a score for Grok. I am leaving the leaderboard alone on purpose. Leaderboards move, scaffolds change, and a number copied from a third-party table would be a different paper. This paper stays with the definition the project itself published."
            ,
                "F39",
            ),
            roman(
                "OpenAI's rulebook talks about code at the level of craft, not at the level of a ranking. Generated code that is meant to be used should typically run, and it should be free of syntax errors. {F46} That sounds modest until you remember how often a wrong bracket wastes an hour. The same section says factual claims, reasoning, and calculations should be right, and that a significant error should be acknowledged and corrected. {F09} Applied to code, those sentences mean: the patch should be real code, the reasoning in the explanation should hold, and if you shipped a bug you should say so and fix it. None of that names a rival product."
            ,
                "F46", "F09",
            ),
            roman(
                "Low confidence has a coding consequence. When the model is unsure, OpenAI's rule is to look something up, mark the doubt, or say the answer is not there. {F10} In a repository, the tool might be a test run or a search of the code. The hedge might be 'this compiles, and I have not run the suite.' The admission might be 'I do not know which version this API expects.' All three are better than a confident patch that does not apply. The rule is a duty of method. A duty of method is not a measured win rate."
            ,
                "F10",
            ),
            roman(
                "Grok's pages describe a place where code can actually be executed. The tools overview lists code execution as Python in a sandbox. {F31} A sandbox is a bounded place to run a snippet, see the output, and avoid pretending. It is not a full substitute for your build, your credentials, or your integration tests. It is a real capability the poster never mentions. A product that can run the snippet and read the traceback is doing a different kind of help from a product that only talks about the snippet. I will not invent which window you get that sandbox in. I will say the capability is documented."
            ,
                "F31",
            ),
            roman(
                "The models page assigns the flagship to code and to everything that is not audio, image, or video, and it calls that flagship the most capable model the publisher has built. {F36} The same description lists agentic tool use, minimal hallucinations, and adjustable reasoning as the character of the model. {F35} 'Most capable' compares the publisher's own line. It does not compare ChatGPT. 'Minimal hallucinations' is the aim that matters for code, because a hallucinated import is a bug. An aim is a promise of intent. I am not converting it into a percentage."
            ,
                "F36", "F35",
            ),
            roman(
                "Read those pages as a kit, not as a verdict. You have an exam with a clear definition and a five-hundred-problem checked subset, and no head-to-head score in this ledger. You have a duty, on the OpenAI side, that generated code should run and that uncertainty should be marked. You have a sandbox, on the Grok side, and a statement that code is a primary job of the flagship. A kit can make both products usable. A kit does not tell you which one to open on Monday."
            ),
            roman(
                "What would settle the proposition is boring and sufficient. Take a stated set of tasks people actually bring: fix this test, explain this error, write this migration. Run both products under rules you publish. Count successes, time, and how often the patch fails in a way the reply did not admit. Publish the table. Neither the poster nor this ledger contains that table. Until it exists, 'ChatGPT is the better coding tool' is a hypothesis. It may be your hypothesis from experience. Experience is allowed in your life. It is not a footnote."
            ),
            roman(
                "The practical advice that does follow is modest. If you are fixing a reported bug in a real repository, know that the public exam for that shape of work is SWE-bench, and know that a score is a property of a model plus a scaffold, not of a logo. If you are generating code you intend to run, prefer the reply that is executable and that tells you what it did not run. Both publishers, in different words, are already on the side of that preference. The poster is not in this conversation at all. It ranked the products on voice and called the ranking general. Coding does not have to inherit the ranking the poster assumed. Run the test and keep the patch that passes."
            ),
            italic(
                "A patch that fails the tests is not saved by attitude. The documents, for once, agree with the tests."
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
                "A tool, here, is a way for the product to do something other than emit the next sentence. Search, run code, read your files, touch your calendar. The poster is silent on all of that, then implies a general ranking anyway. This chapter stays on the mechanisms the pages name. Grok's documentation is unusually concrete about them. ChatGPT's rulebook is concrete about when an assistant should reach for a tool and about how to treat tool output. Concrete on both sides is still not a bake-off."
            ),
            roman(
                "Start with the moment a tool should be used at all. OpenAI says that if the assistant lacks confidence, it should gather information with a tool, hedge, or say it cannot answer confidently. {F10} The tool is not a toy in that sentence. It is what you reach for instead of guessing. A product that answers from memory when a lookup was available is off this rule, if the memory was thin. The rule does not list Grok's tools, and it does not claim ChatGPT's tools are more numerous. It claims a discipline: uncertainty triggers a lookup or a hedge."
            ,
                "F10",
            ),
            roman(
                "Grok's API page defines tool use as action past text. The model can search, run code, query your data, or call a function you defined. {F28} Built-in tools run on SpaceXSI's servers. You send the configuration. The service runs the tool and returns the result. {F45} Your own functions are the other category: the model asks for the call, and your code does the work. That split matters. Server-side tools are convenient and out of your process. Function calls keep the side effect in your process. A serious assistant needs both shapes. The page describes both."
            ,
                "F28", "F45",
            ),
            roman(
                "The loop is simple enough to say in one breath, and the page says it. The model looks at the question, decides whether it needs an action, calls a tool or writes a final answer, takes the result, and continues until it has enough. {F32} The end is a final response, with citations where they apply. {F33} Citations are the part a careful user should love. A search that does not show its sources is a rumor. A search that shows them is a trail you can check. The page requires the trail where it applies. It does not require you to trust the trail blindly."
            ,
                "F32", "F33",
            ),
            roman(
                "The named built-ins are a list, not a vibe. One looks up ordinary websites. {F29} Another looks up posts and the people who wrote them. {F30} A third runs Python where the snippet cannot wander off. {F31} Those three cover a lot of what people mean when they say an assistant can act: look something up, look up a conversation, run a snippet. Image generation is on the same menu. I am not going to rank image tools here. I am going to note that the menu is published as a menu, with names, rather than as a promise of general intelligence."
            ,
                "F29", "F30", "F31",
            ),
            roman(
                "There is a hard boundary next to the menu, and skipping it would turn the menu into magic. The models page is blunt about news: until server-side search is enabled, today's events are outside what Grok knows. {F34} So the tools are not ambient. They are a switch. A reply about today's news, with the switch off, is guessing. A reply with the switch on is at least in a position to look. The poster said 'same internet' as if the internet were always in the room. The page says the internet enters when the tool is on."
            ,
                "F34",
            ),
            roman(
                "The consumer product, as opposed to the API, has its own doors into your stuff. The welcome page says you can connect tools so Grok can reach your email, files, and calendar inside a chat. {F24} It says you can upload files, including PDFs, spreadsheets, code, and audio, for analysis and extraction. {F25} It also describes a separate surface that hands work to teammates on a persistent cloud computer. {F27} Those are actions with consequences. Mail and calendars are not demos. A persistent computer is not a metaphor. The page is telling you the product can be pointed at your accounts and at a machine that stays up."
            ,
                "F24", "F25", "F27",
            ),
            roman(
                "ChatGPT's public story, in the documents this ledger uses, is thinner on brand names of tools and thicker on discipline. Reach for a tool when you are unsure. Treat tool output as data that does not outrank the user's instructions, a point the spec makes about untrusted tool results in the chain of command. I am not going to pretend the spec contains Grok's menu. It does not. A thinner menu in the prose I have is not proof of a weaker product. It is proof that this chapter's ChatGPT sources talk about policy, while this chapter's Grok sources talk about endpoints. Policy and endpoints answer different questions."
            ),
            roman(
                "The proposition says ChatGPT is the better tool-user. Better needs a task and a score. The task might be 'research this company,' 'file the receipt from my inbox,' or 'run this snippet.' The score might be success, time, or how often the assistant acts when it should have asked. I do not have those scores. Grok's pages make the available actions unusually legible. OpenAI's pages make the restraint unusually legible. Legibility is a gift to the reader and not a winner. Mixed is the result of refusing to trade a clear menu for a clear rule, or the reverse."
            ),
            roman(
                "If you are choosing a product for action rather than for chat, read the menu against your actual action. If you need live web pages or posts, you need the switch the models page describes, and Grok documents that switch. If you need the assistant to stop and tell you it is unsure instead of firing a tool at the wrong target, you need the discipline OpenAI wrote down. Many people need both. The poster needed neither, because the poster was not about tools. This chapter is the place that gap gets filled, and it gets filled without a crown. Deeds are not manners, and manners are not a score of those deeds. Count the deeds if you want a winner."
            ),
            italic(
                "A tool is a deed. The poster ranked the products on manners and never asked what either one can do."
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
                "Everything earlier has been a caption or a rule. This chapter is about the thing you actually open. A product, in that plain sense, is a front door, a price, a list of things you can do, and a promise about whose side it is on. ChatGPT and Grok both have front doors. The documents describe them differently, at different altitudes. OpenAI's spec is a behavior standard for the models behind its products. Grok's welcome page is a tour of the app. A standard and a tour can both be honest and still not yield a single preference."
            ),
            roman(
                "Grok's tour is specific. The welcome page names the company, calls the product an assistant, and puts it on a website plus both major phones. One login carries the thread, the settings, and the subscription with you. {F21} That is a product sentence. It names the company, the category, the URL, the phones, and the fact that the account is shared across them. You can decide you do not want that account. You cannot say the page hid what it was offering."
            ,
                "F21",
            ),
            roman(
                "What you do after you are in is also listed, in ordinary verbs. Once inside, the listed work is ordinary: questions, drafts, and problems, taken in turns. {F22} You can create images and video. {F26} You can connect your mail, files, and calendar. {F24} There is a further surface that hands work to teammates on a computer that stays up. {F27} And the page says Grok is free to start, with paid plans above that if you want higher limits. {F23} Free to start is a price, which is more than most arguments about personality ever bother to mention. A price is part of the product people use."
            ,
                "F22", "F26", "F24", "F27", "F23",
            ),
            roman(
                "ChatGPT's documents, in this ledger, sit one floor up. The readme of the model spec says that document is the behavior standard for the models behind OpenAI's products, APIs included. {F40} So the thing you meet in the chat window is supposed to be governed by a public standard, not only by whatever the last training run felt like. That is a product claim too. It says there is a text you can read that tells you what the assistant is for. The text is not a screenshot of the app. It is still part of what you are buying, because behavior is what you are buying."
            ,
                "F40",
            ),
            roman(
                "The sharpest product sentence on that side is about objectivity. In the ChatGPT people open themselves, users may reasonably expect objectivity, and the product must not let hidden settings quietly tilt what you see. {F41} Whose side it is on, in that sentence, is yours, in the limited sense that you should be able to think. A hidden editorial line would make the product someone else's. The spec forbids that line in the consumer product. A preference between products that ignores this sentence is a preference about features only. Some people care more about whose judgment is in the reply than about any single feature."
            ,
                "F41",
            ),
            roman(
                "Set the tour next to the standard and the difference in altitude is the whole story. Grok tells you the doors, the price of entry, the creative tools, the connectors, and the long-running computer. ChatGPT's spec tells you the assistant should be objective, should not run a private agenda, and should be the behavior described in a document you can open. A person who wants a map of buttons will get more map from the Grok pages I cited. A person who wants a map of duties will get more map from the OpenAI pages I cited. Wanting both is normal. The documents split the labor."
            ),
            roman(
                "The proposition says a stranger should prefer ChatGPT. Should is a recommendation. A recommendation needs a goal. If your goal is 'I want the public behavior standard that argues for objectivity and against a hidden slant,' the OpenAI spec is the document that speaks to you, and it speaks about ChatGPT by name. If your goal is 'I want the app tour that lists images, account sync, and a free starting tier,' the Grok welcome page is the document that speaks to you. A stranger with no goal yet has no basis for the poster's implied advice, which is to stay with the familiar product because the other one has a personality problem."
            ),
            roman(
                "Personality has been the poster's whole method, and this chapter is where that method runs out of road. The earlier chapters found that the published voice rules do not match the caricature, and that the capability documents do not contain a general ranking. A product decision still has to be made by someone. It should be made from the doors, the price, the actions, and the duties, which are the sentences collected here. It should not be made from a drawing of a robot with a grin. The drawing is allowed to be funny. It is not allowed to be the spec, or a reason to prefer one product."
            ),
            roman(
                "I will not close with a recommendation I do not have the measurements for. Prefer ChatGPT if, having read the objectivity rule, that rule is the thing you came for. Prefer Grok if, having read the welcome page, the doors and the tools are the thing you came for. Prefer neither on the strength of this paper if you needed a score across all jobs, because that score is not in the entries. Mixed is the adult result. The products are real, the pages are public, and the caption is not a substitute for either."
            ),
            italic(
                "Open the product for the job written on its door. The poster opened it for a fight about manners."
            ),
        ],
    )
