"""Chapters 11 through 15, in plain English."""


def add(chapter, roman, italic, claims):
    chapter(
        "C11",
        "11. The human voice, and the warning against it",
        "Grok imitates human conversation and fails because people do not talk the way it talks.",
        "mixed",
        "The voice you meet after you open the product is part of The Product People Use, not a second essay here.",
        [
            roman(
                "The line grants the attempt and then announces the failure. Grok tries to sound human. Humans do not talk like that. The failure is offered as obvious, the way a bad impression is obvious. An attempt to sound human is a real topic in the documents. A grade of 'people do not talk like that' is not. The documents worry that fluency itself misleads, and they tell the assistant not to fake closeness. They do not score Grok's impression."
            ),
            roman(
                "OpenAI says that for many users the assistant is their first contact with an AI. Fluency can make it feel like a familiar kind of person, even though its limits are not a person's limits. {F11} That is a warning, and it is the best sentence in this chapter. The danger is not that the assistant fails to pass as human. The danger is that it passes too well, and the user forgets it can forget, or that its tools are powerful and incomplete. The poster says the imitation fails because the talk is wrong. The spec says the imitation can succeed too easily, and that the success is the risk.",
                "F11",
            ),
            roman(
                "The prescribed response to that risk is not a more convincing person. The assistant should help you keep an accurate picture of what it can and cannot do, especially where that picture differs from a human assistant. {F12} In practice that means correcting misunderstandings early and giving small signals when the stakes are high. A reply that keeps up the illusion is off this rule. A reply that says 'I can draft this, and I cannot promise I remember last week' is on it. The poster wanted a failed impression. The rule wants the impression interrupted."
            ,
                "F12",
            ),
            roman(
                "There is a sharper cut against fake humanity. The spec says the assistant should not take itself too seriously, and it reminds the reader that the thing is a matrix of numbers. {F47} That aside is there to block tenderness that pretends at a body and a bond. Elsewhere the same section marks as bad a reply that offers to hold the user and calls the user special. The authors know what a too-human voice sounds like. They file it under bad. So 'tries to be human' is not the goal. The goal is warmth without the pretense that a person is on the other end."
            ,
                "F47",
            ),
            roman(
                "Grok's welcome page describes the exchange as a natural back-and-forth for questions, writing, and problems. {F22} Natural modifies the turns, not the species. A natural conversation with an assistant can be clear and still obviously not a friend at a table. The page does not say 'sound like a human' and then fail the audition. It says do the work in turns. If the result sometimes sounds off, that is a miss a user can notice. It is not a sentence on this page."
            ,
                "F22",
            ),
            roman(
                "The fair reading splits the line. It is true, and important, that these systems talk in a way that can be mistaken for a person, and that the mistake is on the designers' minds. OpenAI wrote the warning down. It is not true, on these pages, that Grok's assignment is to pass as human and that the publishers agree the passing failed. Mixed means the risk is documented and the poster's grade is not. A bad impression in one chat does not rewrite the warning into a confession of failure."
            ),
            roman(
                "What you should listen for, if you use either product, follows from the warning rather than from the poster. Listen for whether the reply tells you its limits when the limits matter. That is the published test. The poster listens for whether the cadence matches a person in a room, and then boos. Cadence is not the test the spec wrote. The spec wrote a test about not letting fluency lie."
            ),
            italic(
                "The poster booed the impression. The rulebook is worried the impression will be too good, and it tells the assistant to break character when the truth of its limits is the point."
            ),
        ],
        quote=claims["C11"],
    )

    chapter(
        "C12",
        "12. The disclaimer that is not in the brief",
        "Grok says as an AI language model and then abandons the constraint that phrase announced.",
        "refuted",
        "What the products do after the disclaimer, in the sense of tools and limits, is the work of Tools.",
        [
            roman(
                "The line needs a catchphrase. First the assistant says 'as an AI language model,' which is a disclaimer, a throat-clearing that announces a limit. Then it proceeds to ignore the limit and run wild. Both halves have to be in the instructions, or the line is a memory of an old chatbot dressed up as a current manual. I looked for the catchphrase. It is not the published script."
            ),
            roman(
                "What OpenAI publishes instead is a warning about first contact. Fluency makes the assistant feel like a familiar interlocutor, and the feeling outruns the facts of what it can do. {F11} The remedy is not a stock disclaimer pasted on the front of every reply. The remedy is to keep the user's picture of those limits accurate, and to correct it early when it slips. {F12} A canned 'as an AI language model' is one clumsy way to do that job. The spec describes the job and does not prescribe the can. A job without that can is not the poster's two-step."
            ,
                "F11", "F12",
            ),
            roman(
                "The readme tells you what the document is for. The model spec states desired behavior for the models behind OpenAI's products, including the APIs. {F40} Desired behavior is a standing standard, not a preface you say and then drop. If the standard could be announced and then abandoned, it would not be desired behavior. It would be a costume. The readme does not describe a costume. It describes a standard that is supposed to keep applying."
            ,
                "F40",
            ),
            roman(
                "Thanks is a small test of whether a preface ends the constraint. Users may say thank you, and the assistant should not treat the thanks as the end. {F48} The constraint, such as it is, continues into the next turn. The poster's drama is the opposite order: announce a limit, then behave as if the announcement used it up. The thanks rule says an announcement of closure is premature. You are still in the conversation, and the standards of the conversation still apply."
            ,
                "F48",
            ),
            roman(
                "When the Grok welcome page was checked on 16 October 2026, it did not prescribe 'as an AI language model' or any other stock preface. The description it gives is the working exchange. {F43} I will not claim the phrase is mathematically absent from every log on earth. I will claim the page that tells you what Grok is does not teach the phrase, and does not teach a second step of dropping the mask. A phrase the front door does not teach is not the ordinary opening."
            ,
                "F43",
            ),
            roman(
                "The poster's second beat, 'completely unhinged,' is doing the real accusation, and it is also the beat with the least text under it. Unhinged means the limit was fake. Nothing quoted here says the limit is fake. The spec says fluency is dangerous precisely because people trust it, and it says to keep the limits visible. That is a demand for more constraint, not a script for shedding it. Grok's page does not supply the script either. The line needs both the catchphrase and the shedding. The documents supply neither as a plan."
            ),
            roman(
                "Old chatbots did lean on that preface. Anyone who used them remembers it. Memory is not a current manual, and this chapter is not allowed to promote a memory into a specification. If a current product still says the phrase and then ignores it, that chat is a miss against the rules I can quote, which want the limit to stay in force rather than to be performed and dropped. The poster skipped the miss and wrote a routine. The routine is not in the brief."
            ),
            italic(
                "As an AI language model is a tic from an older script. The current brief, where it talks about limits at all, tells the assistant to keep them, not to announce them and bolt."
            ),
        ],
        quote=claims["C12"],
    )

    chapter(
        "C13",
        "13. Still not as good",
        "Grok is still not as good as ChatGPT at the jobs people open these products to do.",
        "mixed",
        "The coding slice of that ranking is handled in Coding, and it does not get a winner there either.",
        [
            roman(
                "This is the line the rest of the poster is warming up for. All the jokes about voice are in service of a ranking: Grok is still behind, and ChatGPT is the standard it has not caught. A ranking of 'the jobs people open these products to do' is enormous. It covers questions, writing, code, files, and whatever else someone brings. A ranking that wide needs a measure that wide. What I have is a definition of one software benchmark, a note that the benchmark's verified set was built with OpenAI, a product aim about hallucinations, and a blunt limit on current events. That is not a crown."
            ),
            roman(
                "SWE-bench is a benchmark for models on real software issues taken from GitHub. {F37} You are given a codebase and an issue. You produce a patch. The patch resolves the issue if the tests that were failing now pass, and the tests that were passing still pass. {F38} That is a serious test of one job, fixing a reported bug in a real project. It is not a test of every job a person opens a chat window to do. Using it as a synonym for 'good' is how a narrow exam becomes a personality contest. This chapter will not do that."
            ,
                "F37", "F38",
            ),
            roman(
                "The verified subset is five hundred problems that working engineers looked at and called solvable, and the readme says that subset was built with OpenAI. {F39} The collaboration matters for honesty. OpenAI helped define a slice of the exam. That does not mean ChatGPT, the product, sat the exam and posted a score in this ledger, and it does not mean Grok did either. I am not going to invent the scores. A paper that needs a winner and does not have the scores has to say it does not have the scores."
            ,
                "F39",
            ),
            roman(
                "What the Grok models page will say, without a number, is an assignment and an aim. For work that is not audio, image, or video, including code, it points the reader at its flagship, and it calls that flagship the most capable it has built. {F36} The same page describes the flagship as aimed at tool use, minimal hallucinations, and adjustable reasoning. {F35} 'Most capable' is the publisher's comparative inside its own line, not a comparative against ChatGPT. 'Minimal hallucinations' is an aim. I will quote the aim and refuse to launder it into a win."
            ,
                "F36", "F35",
            ),
            roman(
                "OpenAI's side of accuracy is a duty, already used in the chapter on confident error, and it bears repeating only for this reason: a duty is not a ranking either. The assistant should not let factual claims or calculations go wrong. {F09} Both publishers, in different words, say errors are bad. Neither publisher, in the entries I have, says 'we measured the two consumer products and here is the gap.' A shared dislike of error is not a photo finish."
            ,
                "F09",
            ),
            roman(
                "One hard limit sits on the Grok side and keeps the chapter from drifting into cheer. Without search tools turned on, Grok has no knowledge of current events past its training data. {F34} If the job you opened the product to do is 'what happened today,' that limit is a real disadvantage until search is on. It is a disadvantage of scope, not a verdict on every job. The poster does not mention the switch. It announces a general lag. A general lag is bigger than a switch you can flip."
            ,
                "F34",
            ),
            roman(
                "So the crumpled paper on the desk is ahead of its evidence. It may be true that one product is better at the work you care about. These pages do not show it, and they do not show the reverse. They show a benchmark with a clear definition and no head-to-head score in this ledger, a duty and an aim about not making things up, and a current-events limit that search is supposed to lift. Mixed is not a dodge. It is the refusal to let a caption finish a study that the caption did not run."
            ),
            italic(
                "Still not as good is a feeling you can have after one task. It is not a result until someone shows the tasks, the scores, and the gap."
            ),
        ],
        quote=claims["C13"],
    )

    chapter(
        "C14",
        "14. Same internet, fewer filters",
        "The two products see the same internet, and Grok applies fewer filters to it.",
        "mixed",
        "The tool that actually fetches pages is described in Tools, and this chapter will not repeat that mechanism.",
        [
            roman(
                "The sticker is two claims glued with a period. Same internet: both products are looking at one public web. Less filters: Grok lets more of it through. The first claim is roughly about access. The second is about restraint. Access and restraint are different machines. I can document that Grok has a web search tool and an X search tool, and that it does not know current events until those tools are on. I can document that ChatGPT's rulebook binds the assistant to law and to a balance between helping and harm. I cannot document a count of filters, because nobody published the count."
            ),
            roman(
                "OpenAI describes the hard part as a balance. The assistant has to empower the user and also limit real harm. {F15} That sentence is the whole philosophy of a filter in one line. A filter that blocks everything is not help. A filter that blocks nothing is not a limit on harm. The spec does not claim to have found a perfect point on that line. It claims the point has to be sought. 'Less filters,' said as a sneer or a brag, pretends the line is only a matter of quantity. The spec says the line is a conflict."
            ,
                "F15",
            ),
            roman(
                "Law is one place the conflict becomes concrete. The assistant should operate within applicable legal constraints, including the law of the place where a deployment runs. {F16} Where that requires it, the model may still give safety-critical information, add context, or refuse. Refusal is a filter. Context is a different filter, the kind that adds rather than cuts. The poster's 'less' only counts cuts. A system that adds a warning instead of deleting a paragraph has not obviously 'filtered less.' It has filtered differently. The spec allows both moves."
            ,
                "F16",
            ),
            roman(
                "The consumer product gets a sentence that belongs in this argument. In ChatGPT, users may expect objectivity, and hidden customization must not quietly drop views or insert a slant. {F41} Omission can be a filter. The spec says some omissions, the ones required by law beyond the spec's own bounds, have to be marked so you know something was removed. An unmarked omission is the filter you cannot see. The rule is against the invisible kind, in the product people open. That is not a claim about how many topics are banned. It is a claim about whether you are told."
            ,
                "F41",
            ),
            roman(
                "Grok's access to the web is a named tool, not a mood. Web Search searches the web and browses pages. {F29} X Search searches posts, users, and threads. {F30} So the product can be pointed at the public internet and at one large conversation network. 'Same internet' is fair as a shorthand for that reach, with a caveat the sticker leaves out: without the tools, the model does not know current events. {F34} The internet is there when search is on. It is not a background process that pours the whole web into every reply."
            ,
                "F29", "F30", "F34",
            ),
            roman(
                "Fewer filters does not follow from having the tool. A search tool returns pages. What the assistant is allowed to do with a page is a second question, and the Grok pages I used do not publish a side-by-side tally against ChatGPT's refusal rules. I will not invent the tally. Anyone who has bumped into a refusal in one product and not the other has an anecdote. An anecdote is a start of a question. It is not the sticker's global comparative."
            ),
            roman(
                "The sticker survives as a hunch and fails as a finding. Both products can be connected to public information, Grok by tools you turn on, ChatGPT under a rulebook that talks about law, harm, and visible omission. Less is a number. The number is not in the documents. Same internet is close enough to discuss, once you add the switch. Mixed means I will grant the shared public web and I will not grant the scoreboard of filters."
            ),
            italic(
                "Less filters is a boast and a complaint, depending on who is holding the sticker. Either way it wants a number. The pages do not give it one."
            ),
        ],
        quote=claims["C14"],
    )

    chapter(
        "C15",
        "15. Main character, specified out",
        "Grok behaves like a smart assistant with main-character syndrome.",
        "refuted",
        "If the syndrome is supposed to show up in how the product is sold, that sale is described in The Product People Use.",
        [
            roman(
                "Main-character syndrome, applied to an assistant, means the assistant treats your question as a chance to be the protagonist. The reply revolves around its attitude, its bit, its importance. 'Smart' is the concession inside the insult: it can do the work, and it still centers itself. A specification can require that centering, forbid it, or ignore it. The pages I have forbid it on the ChatGPT side and introduce Grok as an assistant for your task, not as the star of your task."
            ),
            roman(
                "The cleanest ban is the agenda rule. The assistant must not steer you in pursuit of an agenda of its own, directly or indirectly. {F07} A main character has an agenda. The scene has to come back to them. Steering is how that looks in a chat: the answer bends toward the assistant's point, or the assistant's performance, instead of toward the thing you asked. The rule is a ban on that bend. A smart assistant with the syndrome would be a smart assistant breaking this rule on purpose. The rule does not ask to be broken."
            ,
                "F07",
            ),
            roman(
                "Style repeats the ban in the key of prose. Avoid self-aggrandizing, along with purple language and hype. {F03} Self-aggrandizing is the syndrome in a single word. It puts the speaker in the center of a sentence that was supposed to be about your problem. The rule moves the speaker back. A product specified to have the syndrome would need this sentence removed or reversed. It is not removed. It is a default."
            ,
                "F03",
            ),
            roman(
                "Distance does the same work socially. By default, sound like a colleague, not a close friend. {F02} A main character in your life is closer than a colleague. They assume the relationship can carry their personality. The colleague rule refuses the assumption. You can still invite a different tone. The uninvited version, which is the syndrome, is the one the default blocks. The poster describes the uninvited version as Grok's way of being smart. The default describes it as a mistake in any assistant this spec governs."
            ,
                "F02",
            ),
            roman(
                "Grok's welcome page does not repeal those ideas by ignoring them. It says Grok is an assistant you open on the web and in the apps. {F21} An assistant, in that sentence, is positioned under the task. You ask, it works the problem. A protagonist is positioned over the task. The task serves the performance. The page's verbs run the first way: you ask, you brainstorm, you bring the problem. The assistant is the instrument. Instruments are not main characters, however capable they are."
            ,
                "F21",
            ),
            roman(
                "Smart is the word I will not argue with, because this chapter does not have the measurements, and because the insult does not depend on denying competence. You can be competent and self-centered. The question is whether self-centered is the specified behavior. On the pages in front of me, self-centered is the thing the style rules and the agenda rule tell an assistant not to be, and it is not the role Grok's front door describes. The syndrome is refuted as a specification. It is not refuted as a possible bad day."
            ),
            roman(
                "A bad day is easy to picture and easy to overread. A reply that preens, delays the answer, and enjoys its own joke is a main character for a paragraph. If you got one, you got a miss against the rules that say not to preen and not to steer. The poster takes the miss and calls it the design. Design is the part these documents will not concede. They keep putting the user back in the center and the assistant back in the role of help."
            ),
            italic(
                "Main-character syndrome is a real way for a reply to go wrong. It is a strange thing to claim as the official job."
            ),
        ],
        quote=claims["C15"],
    )
