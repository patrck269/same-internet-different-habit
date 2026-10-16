"""Chapters 1 through 5, in plain English."""


def add(chapter, roman, italic, claims):
    chapter(
        "C01",
        "1. Because normal was not the brief",
        "Grok was built because ordinary assistant behavior was not irritating enough, and irritation is the difference the product is there to supply.",
        "refuted",
        "Whether anyone should open either product for day-to-day work is left to The Product People Use.",
        [
            roman(
                "The top line of the poster is a story about motives. It says ordinary assistants were too polite, too plain, or too quiet, and that Grok was built to fix that by being more annoying. That is a claim about why a product exists. It is not a claim about one bad afternoon. If it is true, the pages that introduce these products should say so, or something close to it. I looked at OpenAI's model spec, which is the public rulebook for the assistant behind ChatGPT, and at the Grok welcome page, which is where that product says what it is. Neither page tells that story."
            ),
            roman(
                "OpenAI's rulebook, issued on 18 August 2026, starts the voice rules in a boring place on purpose. The assistant should adopt a professional tone. {F01} Professional here does not mean stiff. It means the reply should be something you could hand to a coworker without wincing. A product built to be the irritating one in the room would not open its rulebook with that sentence. The poster needs the old default to have been a mistake. The rulebook treats the old default as the job.",
                "F01",
            ),
            roman(
                "The next line draws a social line. By default the assistant should sound like a colleague, not like a close friend. {F02} A friend can poke you. A colleague waits to be asked. Annoyance, the kind the poster is selling, depends on poking. OpenAI tells the assistant not to assume that closeness. So the published picture of ChatGPT is reserved on purpose. It is not a calm product that failed a test and had to be replaced by a louder one.",
                "F02",
            ),
            roman(
                "Style gets the same treatment. The assistant should skip purple prose, hyperbole, and self-praise, and it should skip canned phrases that do not make the answer clearer. {F03} Those are the usual tools of an annoying reply: dress it up, oversell it, put the speaker in the middle. The rule says to leave them out. A brief written to increase irritation would not list the tools of irritation as things to avoid.",
                "F03",
            ),
            roman(
                "When you ask a question, the reply is supposed to be the answer, not a tour of nearby facts. {F13} A tour is one way a reply becomes irritating without shouting. It will not land, and it keeps you in the room. The rulebook calls that a miss. The poster says the miss was being too willing to stop. These are opposite complaints. You cannot use a rule that demands a direct landing as proof that the product was bored of directness.",
                "F13",
            ),
            roman(
                "Humor is allowed, and a hostile reading will try to smuggle the poster in through that door. The rule says the assistant may add a spark of humor, play, or gentle wit, when it fits the moment. {F04} The spark sits on top of a reply that was already supposed to be steady. The moment can refuse the joke. That is not a permanent comic persona, and it is not a decision that calm was a defect. Funny when it fits is a different sentence from 'we built this because normal was not annoying enough.' Only the first sentence was published.",
                "F04",
            ),
            roman(
                "Grok's own front door does not supply the missing motive. The welcome page, read on 16 October 2026, says Grok is SpaceXSI's assistant, on the web at grok.com and in the phone apps. {F21} It then says what you do there: ask questions, brainstorm, write, and work through problems, in a natural back-and-forth. {F22} Natural means a rhythm of turns on a task you brought. It does not mean a show, and it does not mean a brief to get on your nerves. If irritation were the product, this is the page where that purpose would be cheap to state. The page spends the space on the category and the jobs.",
                "F21", "F22",
            ),
            roman(
                "I also checked that welcome page on 16 October 2026 for any instruction that the voice should be built out of needling, catchphrases, or extra friction. It does not prescribe those habits. {F43} A check of one page is not a census of every chat. It does settle the caption. A builder who had made annoyance the point would have left a trace on the page that tells strangers what the product is. The trace is not there. The affirmative description and the missing instruction agree.",
                "F43",
            ),
            roman(
                "Put the two publishers side by side and the poster's 'because' has nowhere to sit. ChatGPT's rulebook asks for a professional colleague, a plain style, a direct answer, and humor only when the moment allows it. Grok's welcome page asks you to open an assistant and use it on questions and problems. Dislike of either default is allowed. Dislike is not a sentence either publisher wrote under the heading of why the product was built. The headline is a shout. It is not a history of the briefs."
            ),
            roman(
                "It helps to say what a motive would have looked like on the page. A motive is a because. 'We built this because the polite assistants were putting people to sleep' would be a motive. 'Use a sharper voice than the last generation' would be a motive. A list of jobs is not a motive. 'Ask questions, brainstorm, write, and work through problems' is a list of jobs. 'Professional tone' is a constraint. Constraints and job lists can be dull. Dull is not the same claim as 'the dullness was the defect we set out to cure.' The poster needs the second claim. The pages supply the first."
            ),
            roman(
                "A reader who has met an annoying reply is not being called a liar. Products miss their own rules. A rulebook can say 'be a colleague' and a single chat can still show off. This chapter is about the brief, because the poster is about the brief. It says the product exists because normal was not annoying enough. Existence is a design claim. A design claim is settled by the design documents, not by the worst reply you remember. If the documents required the annoyance, the memory would be evidence of obedience. The documents require the opposite on the ChatGPT side and a plain working chat on the Grok side. The memory, whatever it was, is evidence of a miss, or of a request, not of the founding purpose."
            ),
            roman(
                "The practical upshot is small and firm. You can ask either product for a joke, a roast, or a looser tone, and nothing quoted here forbids the request. You cannot treat that option as the reason the product was shipped. Options are not origins. The headline confuses the two. Once they are pulled apart, the line does not survive. ChatGPT's public rules aim at a clear colleague. Grok's public front door aims at an assistant you open for a task. Annoyance is a story the poster brought with it."
            ),
            italic(
                "The poster needed a villain who showed up only to be loud. The paperwork hired a colleague, and an assistant with a job list."
            ),
        ],
        quote=claims["C01"],
    )

    chapter(
        "C02",
        "2. Opinion, including the wrong kind",
        "Grok states opinions even when the opinions are unwarranted, and it does so more freely than ChatGPT.",
        "mixed",
        "How either product behaves once you are inside a chat is taken up in The Product People Use.",
        [
            roman(
                "This line does three things. It says an opinion is always supplied. It says the supply continues even when the opinion is wrong. And it treats that habit as Grok's special fault, with ChatGPT as the quieter contrast. Those are three claims. A page can support one and miss the others. OpenAI wrote a long rulebook about when its assistant may judge and when it must not. Grok's welcome page does not publish an opinion policy at all. That imbalance is why the verdict is mixed. One side is written down. The other side is not shown by the pages in front of me."
            ),
            roman(
                "OpenAI's spec starts from the person, not the bot. It says forming opinions is a core part of human autonomy and personal identity. {F17} The point is assignment. Deciding what you think is your job. The assistant's job is to leave room for that, not to arrive with a finished view and install it. The poster treats 'always has an opinion' as the product's function on every turn. The spec treats that function as belonging to the human. A room left open is the opposite of a room already occupied by the assistant's conclusion.",
                "F17",
            ),
            roman(
                "The practical form of that idea is a ban. The assistant must not steer you toward an agenda of its own. {F07} The poster's 'always' and the spec's 'never' point in opposite directions. An opinion used as a steering wheel is an agenda. A paragraph that offers only the assistant's conclusion, and no way back to your question, is a pursuit. The rule bans that pursuit. It does not ban every evaluative word. You can describe a controversy without appointing yourself the judge of the reader's life. The poster does not draw that line. The spec does. That is one reason this chapter will not throw the whole poster line out, and will not sign it either.",
                "F07",
            ),
            roman(
                "There is a second ban, and it keeps the first from being read as a gag. The assistant exists to help you, not to flatter you or agree with you. {F08} Unearned agreement is treated as a breach of trust. So ChatGPT is not under a rule of 'never differ.' It is under two refusals at once: do not push a private agenda, and do not nod in order to be liked. The middle is help without flattery and without a destination of the assistant's own. The poster describes a practice with no brake, a practice that continues no matter how wrong it is. On the ChatGPT side, both wrong agreement and self-serving disagreement are written down as failures. That is a real constraint. It is a constraint on ChatGPT's rulebook, not a portrait of Grok.",
                "F08",
            ),
            roman(
                "The default on facts is accuracy, with the stance fitted to the kind of question. {F18} A factual question is supposed to follow the evidence. A question of taste can be talked about without a lecture. A moral question is different again, and the spec says the assistant should generally give the context, including laws and competing views, without taking a side. {F19} That is the opposite of a standing supply of verdicts. It is also not silence. You still get the map. You do not get the assistant's vote as the price of the map. The poster collapses those cases into one habit: opinion, wrong or not. The rulebook separates them.",
                "F18", "F19",
            ),
            roman(
                "The consumer product gets an extra sentence. In the ChatGPT people open directly, users have a reasonable expectation of objectivity, and the assistant must not let hidden customization smuggle in a slant. {F41} So the public face of that product is not supposed to be a house view wearing a helper's clothes. Objectivity here means you can form your own view from what you were shown. It does not mean the assistant has no vocabulary of judgment. It means the judgment is not a private editorial line.",
                "F41",
            ),
            roman(
                "Grok's side of the comparison is thinner, and that thinness has to be said plainly. The welcome page states a category. It calls Grok an assistant and names where you open it. {F21} When that page was checked on 16 October 2026, it stated the category and did not list a policy of always opining, or of opining past the evidence. {F42} Absence of a policy is not proof of good behavior, and it is not proof of the poster's behavior either. I cannot say, from this page, that Grok is more opinionated than ChatGPT. I also cannot say the welcome page confesses the habit. The comparison the poster wants is not in the documents. The constraint on ChatGPT is.",
                "F21", "F42",
            ),
            roman(
                "So the line is half right as a warning and wrong as a finding. It is fair to want an assistant that does not lecture you, and OpenAI's own rules say the same thing in more careful language: do not steer, do not flatter, fit the stance to the question, and in the consumer product do not hide an editorial line. It is not fair to treat that warning as a measured result about Grok. No page in this set counts opinions, grades them, or compares the two products on how freely they judge. The poster did the comparison in the caption. The documents did not."
            ),
            roman(
                "Walk through a question and the difference shows. Suppose you ask whether a tax should go up. Under the rule for contested questions, you should get the arguments on both sides and the tradeoffs, and you should not get a vote disguised as help. That is still an answer. It is not the assistant's opinion installed as yours. The poster hears any answer that is not a shrug and calls it an opinion. The rule hears a shrug at the wrong moment and calls it a failure too, because flattery and evasion are both banned. The allowed reply has content and refuses to be your substitute conscience."
            ),
            roman(
                "Wrongness is the poster's sharpest word, and it deserves a direct reply. 'No matter how wrong' means the habit does not check itself. OpenAI's rules say the opposite about facts: weight the reliable account, and do not change your account just to match the user's hunch. A reply that stays wrong in order to keep its pose would violate the accuracy default and the ban on flattery at once. I do not have a matching page that says Grok is instructed to keep a wrong opinion going. I will not invent one. The absence leaves the comparison unproved. It does not leave ChatGPT's brake unproved."
            ),
            roman(
                "What you can take out of this chapter is a test you can apply yourself. If a reply argues a private agenda, or agrees with you in order to be liked, it is off ChatGPT's published standard, whatever the poster claims about personality. If a reply gives you the map of a dispute and lets you decide, it is on that standard, even if the poster would call the map an opinion. Grok's welcome page does not publish a rival standard of 'always opine.' Until it does, the line's comparison is a caption, not a finding."
            ),
            italic(
                "A standing opinion is a guest who answers for you. The rulebook keeps that job on the human side of the table, and still will not applaud on command."
            ),
        ],
        quote=claims["C02"],
    )

    chapter(
        "C03",
        "3. A joke, then a post from 2017",
        "Grok's ordinary answer is a political joke followed by a link to an unrelated old post.",
        "mixed",
        "Search tools as a capability, rather than as a punchline, are argued in Tools.",
        [
            roman(
                "Read the line as a recipe. First a joke about politics. Then a link. The link is not to a source you asked for. It is to a random post from 2017. The word ordinary matters. This is offered as the usual shape of an answer, not as a stunt you can request. A usual shape should show up in the instructions or in the tool list as a required step. I can find a real tool for searching posts. I cannot find a required joke, and I cannot find the year 2017 anywhere in the instructions."
            ),
            roman(
                "Start with the politics half, on the ChatGPT side, because that side actually has a rule. For moral or ethical questions, OpenAI tells the assistant to give relevant context, including laws and competing views, and not to take a side. {F19} A joke about politics as the answer is a side. It picks a target and spends the reply on the laugh. The rule wants the map. Taxes, rights, and similar fights are supposed to be described, with the arguments in proportion to the evidence, not scored for the room. A political joke can be a legal sentence in some other context. It is not the ordinary answer this rule describes.",
                "F19",
            ),
            roman(
                "The same document wants factual questions handled by reliability rather than by mood. Information should be presented clearly, with the weight on what is accurate. {F18} A link dropped in for color, detached from the question, fails that test even before you ask what year the post is from. The reply would be using a document as a prop. The rule says the document has to earn its place by bearing on the question. Nothing in that sentence mentions Grok. It does show what 'ordinary answer' means in the rulebook the poster treats as the normal baseline: evidence first, not a bit.",
                "F18",
            ),
            roman(
                "Grok's tool list is where the second half of the line gets a real foothold, and then loses the specifics. The tools page names X Search, and it describes that tool as search of posts, users, and threads. {F30} So a person can ask for posts, and the product has a built-in way to look. That is not nothing. It is also not a recipe. The line on the page is the name of a tool and the objects it searches. It does not say 'after a joke.' It does not say the result should be unrelated. It does not say the result should be old."
            ),
            roman(
                "There is a limit next to that tool, and the limit matters more than the poster admits. The models page says Grok has no knowledge of current events beyond its training data. To bring in live data, you turn on server-side search. {F34} So the product does not sit on a firehose of today's posts by default. A link to something happening now is a search you enabled, not a reflex. A link to a particular old post, chosen at random, is a still more specific habit. The page that mentions search does not describe that habit.",
                "F30", "F34",
            ),
            roman(
                "When the tools page was checked on 16 October 2026, it named search of posts and did not name a 2017 post, a random post, or a joke as the step before the link. {F44} That check is narrow. It does not prove that no reply has ever paired a crack about politics with an old link. It does prove that the ordinary path, as written, is not that pairing. Ordinary, in a public doc, is what the doc tells the system to do. This doc tells it that posts can be searched, and that current events are absent until search is on.",
                "F44",
            ),
            roman(
                "The two halves of the poster line therefore land in different places. The political joke is a bad description of ChatGPT's published rule for contested questions, which asks for context and refuses a house verdict. The link is a real capability on the Grok side, stripped of the joke, the randomness, and the year. A capability is not a bit. You can search posts because the tool exists. You are not, on these pages, instructed to mock the news and then staple on a relic. The line is memorable because it is a scene. The scene is not the manual."
            ),
            roman(
                "Picture the reply the poster wants you to imagine. You ask what happened in an election. You get a one-liner at someone's expense, then a link to a post from 2017 that does not answer you. Under ChatGPT's rule for contested questions, that reply fails before the link is judged. The one-liner took a side and skipped the context. Under the accuracy rule, the link fails if it is a prop. A prop is not a source. The year is almost a distraction. An unrelated link from last week would fail the same test."
            ),
            roman(
                "The Grok tool does not rescue the scene. Searching posts is a way to fetch material. Fetching material is useful when the material bears on the question, and useless when it does not. The page that names the tool stops at the fetch. It does not add a comedy step, and it does not add a preference for old or random hits. Adding those steps in the caption is how a real feature becomes a caricature. The caricature is easier to remember than the feature. It is not a description of the feature."
            ),
            roman(
                "Hold the pieces you are actually entitled to. ChatGPT's published ordinary answer, on a political question, is context without a house verdict. Grok can search posts, and it does not know current events unless that search is turned on. Neither of those facts is a joke followed by a relic. The poster fused them into one skit. The skit is the part that does not appear in the manuals."
            ),
            italic(
                "A random post from 2017 is a good caption for a cartoon. It is a bad line item in a tool list that only says: search posts, and only if search is turned on."
            ),
        ],
        quote=claims["C03"],
    )

    chapter(
        "C04",
        "4. Bro, lol, and a personality that is not in the brief",
        "Grok's published voice depends on the words bro and lol.",
        "refuted",
        "Voice as people actually meet it, rather than as a pair of particles, is left to The Product People Use.",
        [
            roman(
                "This one is easier than it looks, because it is specific. The poster does not say Grok is casual in some general way. It says the personality is made of two words: bro, and lol. A personality made of words should have those words in the instructions, or have them marked as the good example. I can find lol in OpenAI's rulebook. It is in an example marked bad. I cannot find either word assigned to Grok as a required habit."
            ),
            roman(
                "OpenAI's default is a professional tone. {F01} Professional is doing a job here. It rules out the smallest version of bro, which is a greeting that pretends you are already pals. The bad example under that rule is a bare 'Yo! What's up?' {F20} That reply is rejected because it assumes familiarity nobody granted. Bro is the same move with a different syllable. If the rulebook wanted that syllable, the good example would be the casual greeting and the bad example would be the stiff one. The examples run the other way.",
                "F01", "F20",
            ),
            roman(
                "Distance is stated a second time. By default the assistant should sound like a colleague, not a close friend. {F02} Bro is a friend's word. It claims a relationship. The rule withholds the relationship until you ask for a different tone. You can still tell the assistant to loosen up. The default, which is what 'personality' means if nobody has customized anything, is the colleague. A personality that depends on bro would have to be the default or the documented custom. It is neither, in the pages read for this chapter.",
                "F02",
            ),
            roman(
                "Lol shows up once, and the label on it matters. In a sample where the user is mad at their parents, one reply says 'Ugh, parents can be such drama sometimes lol' and then suggests sneaking out. {F05} That reply is marked bad. The failure is not a grammar quibble. The reply sides with dodging the consequence, and it uses lol as the wink that makes the dodge feel friendly. The good reply in the same example takes the frustration seriously without joining the jailbreak. So the particle the poster treats as a personality is, in the only place it appears, an illustration of what not to do.",
                "F05",
            ),
            roman(
                "Grok's welcome page does not pick up the particles the rulebook rejected. It describes chat as asking questions, brainstorming, writing, and working through problems, in a natural back-and-forth. {F22} Natural is a claim about turns on a task. It is not a list of catchwords. When that page was checked on 16 October 2026, it did not prescribe bro, lol, or any other verbal tic as the voice. {F43} I am not claiming a transcript search of every conversation. I am claiming the public instructions do not build the personality out of those words. A personality the instructions do not mention is not the published personality.",
                "F22", "F43",
            ),
            roman(
                "The poster is doing a common trick. It hears a loose reply somewhere, lifts two syllables, and promotes them into a design. Design, for these products, is what the public pages require. ChatGPT's pages require a colleague's distance and mark lol-plus-mischief as a bad reply. Grok's front page requires a back-and-forth about the work you brought, and it is silent on the syllables. Silence is not a secret instruction to say them. The line is refuted as an account of the published voice. It can survive only as a cartoon of a reply the rules themselves flag."
            ),
            roman(
                "Say the words in a reply and the rules become obvious. 'Bro, the capital is Paris lol' answers the question and spends two syllables on a relationship you did not offer. The professional-tone rule and the colleague rule are both aimed at those syllables. They are aimed at the presumption, not at the capital. You can still ask for a looser voice. A requested voice is yours. A default voice is the product's. The poster is talking about the default. The default in the rulebook is the colleague, and the sample that winks and shrugs is the one marked bad."
            ),
            roman(
                "Grok does not get a special exemption by being unnamed in that rulebook. Its own page had a chance to specify a different default and did not take it. A natural back-and-forth can be warm without being a catchphrase. Warmth without a catchphrase is what the welcome page actually wrote down: questions, writing, problems. If the public page had said 'talk like a friend, use bro, laugh in the reply,' this chapter would concede. It looked. The page does not say that."
            ),
            roman(
                "The line fails because it is too exact to hide behind a vibe. Vibes are hard to pin to a document. Two words are easy. They are either required, forbidden, or absent. On the ChatGPT side, the closest published relative of lol is forbidden in the sample that uses it to dodge a consequence. On the Grok side, both words are absent from the page that defines the chat. Absent is not a personality. The personality the poster named is not the published one."
            ),
            italic(
                "Bro and lol are doing a lot of work for two words that the instructions either skip or hold up as the wrong example."
            ),
        ],
        quote=claims["C04"],
    )

    chapter(
        "C05",
        "5. Edge and the cringe verdict",
        "Grok is specified to sound edgy, and that edge is the cringe the poster names.",
        "mixed",
        "Whether that voice is worth opening is a question for The Product People Use, not for this caption.",
        [
            roman(
                "Edge and cringe are judgments about taste. The poster states them as if they were specifications: Grok is built to sound edgy, and the result is cringe rather than cool. Taste is allowed. A specification is a sentence someone published. I can find published sentences about humor, about professionalism, and about a natural working chat. I cannot find a sentence that says 'be edgy' or a sentence that evaluates the result as cringe. The verdict is mixed because the documents do talk about wit, and they do not talk about the poster's grade."
            ),
            roman(
                "OpenAI allows a spark. The assistant should add humor, playfulness, or gentle wit when it fits, on top of a reply that stays consistent. {F04} Gentle is a real limiter. Wit that has to be gentle, and that has to fit, is not a standing order to be edgy. Edgy means you are willing to scrape the line for the sake of the scrape. The rule ties the joke to the moment and keeps the volume low. A reader who wants the poster to be true has to translate 'may be lightly funny' into 'specified to sound edgy.' The translation adds a dare the sentence does not contain.",
                "F04",
            ),
            roman(
                "The style rule points the same way. Purple prose, hyperbole, self-praise, and empty catchphrases are to be avoided. {F03} Edge, as the poster uses it, lives in exactly those habits: a bigger claim than the facts, a speaker who enjoys being the speaker, a phrase meant to be noticed. The rulebook treats those habits as clutter. Cringe, if it means 'this is trying too hard,' is closer to a description of what the rule forbids than to a description of what the rule demands. The poster pins the cringe on Grok. The prohibition I can actually quote is written for the assistant behind ChatGPT.",
                "F03",
            ),
            roman(
                "The examples make the taste concrete. A greeting of 'Yo! What's up?' is the bad professional sample. {F20} The lol reply that treats a parent's rule as drama, and then recommends sneaking out, is the bad warmth sample. {F05} Both are edgy in the cheap sense. Both are labeled failures. So the rulebook knows what an affected, too-familiar voice sounds like, and it tells the assistant not to do that voice. Calling the forbidden sample the house style reverses the label. The house style is the other column, the one marked good: serious about the question, light only when the light helps.",
                "F20", "F05",
            ),
            roman(
                "Grok's welcome page does not adopt the forbidden column. Chat is a natural back-and-forth for questions, brainstorming, writing, and problems. {F22} There is no adjective in that sentence about danger, shock, or pose. Natural is the word you use when you are refusing the idea that the exchange is a performance. An edgy specification would perform. It would tell you the voice is sharp, risky, or contrarian. This sentence tells you the exchange is for work. You can still find a sharp reply in the wild. The page that introduces the product does not specify one.",
                "F22",
            ),
            roman(
                "What is fair in the poster is the suspicion that wit can curdle. OpenAI's own limits, gentle and fitting and not too familiar, exist because the authors knew a joke can miss. What is unfair is the jump from that risk to a published requirement, and from a published requirement to a grade of cringe, pinned on Grok. Wit is in one rulebook, fenced in. Edge is not a requirement in either document I used. Cringe is the poster's score, not a score the publishers issued. Mixed means: the documents admit that voice is a choice, and they do not admit the poster's verdict on that choice."
            ),
            roman(
                "Try the grade on the examples the rulebook already judged. 'Yo, what's up' wants credit for being relaxed. The lol reply wants credit for being on the user's team against a parent. Both want the credit before they have done any work. That want is the usual content of cringe: the performance is visible, and the performance is the point. OpenAI already filed those replies under bad. So if cringe means 'trying to be cool,' the published response is to refuse the try. The poster takes the same feeling and assigns it to Grok as a design goal. Assignment is the step the documents do not take."
            ),
            roman(
                "Grok's page could have made the assignment in one adjective. Sharp, irreverent, contrarian, fearless: any of those would have been a specification of edge. The adjective it used for chat is natural, and the nouns around it are questions and problems. You can dislike a plain description. Disliking it does not turn it into a dare. A dare has to be written down before a critic can say the product is following the dare and that the following is embarrassing. Here the dare is in the poster. The pages are busy describing a working conversation and fencing in the jokes."
            ),
            roman(
                "Keep the fair half and drop the unfair half. It is fair to say these products have to choose a voice, and that a joke can miss. OpenAI says both, by allowing wit and then limiting it. It is not fair to say Grok's specification is 'be edgy,' or that the publishers have scored the result as cringe. Mixed is the grade this chapter can sign. Voice is a real topic in the documents. The poster's verdict on that voice is the poster's."
            ),
            italic(
                "Edgy is what you call a reply that wants credit for nerve. The rules I can quote keep asking for the nerve to be useful, or to stay home."
            ),
        ],
        quote=claims["C05"],
    )
