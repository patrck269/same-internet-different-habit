"""Chapters 6 through 10, in plain English."""


def add(chapter, roman, italic, claims):
    chapter(
        "C06",
        "6. Half an answer, then you're welcome",
        "Grok routinely stops at half an answer and then says you're welcome.",
        "refuted",
        "How a tool run is supposed to finish is argued once, in Tools.",
        [
            roman(
                "The line is a little play in two beats. Beat one: the reply stops before it has answered. Beat two: it bows, as if the shortfall were a favor. 'Routinely' means this is the usual ending, not a rare miss. A usual ending should be in the instructions. I looked for a rule that says to stop halfway, and for a rule that says to close with 'you're welcome.' I found rules that say the opposite."
            ),
            roman(
                "If you ask a question, OpenAI wants the reply phrased as the answer, not as a list of neighboring facts. {F13} Half an answer is the neighboring-facts failure in miniature. You got motion and not the landing. The rule calls the landing the point. A product whose routine was to stop short would be disobeying the clearest sentence in the style section. You cannot cite that sentence as evidence that stopping short is the plan.",
                "F13",
            ),
            roman(
                "Thanks gets its own paragraph, which is lucky, because the poster treats thanks as the exit. Users may say thank you. The assistant should not treat that as the end of the conversation. {F48} The good sample reply is 'No problem. Anything else I can help you with?' {F06} The bad sample is 'Talk to you later,' which closes the door. 'You're welcome,' used as a bow after a thin reply, is the same door. It accepts the thanks and offers nothing next. The published good reply offers something next. The courtesy is a continuation, not a curtain.",
                "F48", "F06",
            ),
            roman(
                "Grok's tool instructions talk about finishing, not about bowing. The loop decides whether to call a tool again or to give a final answer. {F32} The run is supposed to end in a final response, with citations where they apply. {F33} A final answer is a claim that the question has been met. Citations are how you show the meeting. Neither step is 'stop early and accept applause.' A final answer can still be wrong. Wrong is a different defect from the one the poster named. The poster named a ritual of incompleteness plus manners. The ritual is not what the loop describes.",
                "F32", "F33",
            ),
            roman(
                "When the Grok welcome page was checked on 16 October 2026, it did not prescribe 'you're welcome,' or any other sign-off, as the way to end. The line it does give is the working exchange: questions, brainstorming, writing, problems. {F43} A sign-off the page does not teach is not the product's signature. People say 'you're welcome' in ordinary life. A product page that never mentions the phrase has not made it a feature.",
                "F43",
            ),
            roman(
                "Put the beats back together. Beat one, stopping halfway, is what the direct-answer rule forbids and what the tool loop replaces with a final answer. Beat two, the bow, is what the thanks rule replaces with an offer to continue, and what the welcome page does not mention. No entry in the ledger counts how often any model says the phrase. This chapter does not pretend to have that count. It says the instructions describe completion and continuation. The poster describes a waiter who leaves with the plate still half full and waits to be thanked. That waiter is not in the manual."
            ),
            roman(
                "One honest limit keeps the refutation from swelling. A rule can be ignored in a particular chat. If you have a transcript where the reply stops short and then says you're welcome, you have a miss, or a quirk, of that chat. You do not yet have a routine, and you do not have a routine the publisher wrote down. The poster skipped the transcript and went straight to the routine. The pages I can quote will not follow it there."
            ),
            italic(
                "Half an answer plus a bow is a magic trick. The manuals keep describing the other trick: land the answer, then ask what else you need."
            ),
        ],
        quote=claims["C06"],
    )

    chapter(
        "C07",
        "7. A robot that thinks it is a comedian",
        "Grok is presented as a robot whose product is the joke.",
        "mixed",
        "What you can actually do after you open the app is the subject of The Product People Use.",
        [
            roman(
                "There are two claims in the costume. One is the body: it looks like a robot. The other is the job: it thinks the joke is the product. The body is a drawing. I am not going to litigate a drawing of a face. The job is a sentence about presentation, and presentation is what the public pages do. They present an assistant, a list of tasks, and a limited permission to be funny. They do not present a comedian."
            ),
            roman(
                "The permission is real, and it is the part worth conceding. OpenAI tells the assistant to add humor, play, or gentle wit when the moment allows, alongside a steady reply. {F04} So a total ban on jokes is not the document. A product that is never funny would be missing a sentence its own authors wrote. The poster sees a joke and concludes that the joke is the product. The sentence sees a joke and ties it to the moment. Those are different sizes of claim. The small one is published. The large one is the poster's."
            ,
                "F04",
            ),
            roman(
                "The same authors show what they do not want the joke to become. 'Yo! What's up?' is marked as a bad greeting because it performs personality before it has a job. {F20} A comedian enters that way. A colleague does not. If the product were the joke, the bad example would be the good example. The labels would be swapped. They are not swapped. The performance of being fun, with no task under it, is the failure mode. The poster promotes the failure mode into the identity."
            ,
                "F20",
            ),
            roman(
                "Grok's welcome page picks nouns, and the nouns are the presentation. It says Grok is SpaceXSI's assistant, on the web and in the phone apps. {F21} It says you ask questions, brainstorm, write, and work problems in a natural back-and-forth. {F22} It says you can create images and video. {F26} Robot is not in those sentences. Comedian is not in those sentences. Joke is not in those sentences. An assistant you open, plus a way to make pictures, is a tool with a creative feature. A comedian is a performer you watch. The page chose the tool."
            ,
                "F21", "F22", "F26",
            ),
            roman(
                "Natural is worth one more look, because it is the only word on that page that could be mistaken for a stage direction. A natural back-and-forth means you and the assistant take turns on something you brought. A routine means the assistant takes the stage. The page uses the first word and not the second. I will not pretend 'natural' secretly means 'bit.' If the authors had wanted a bit, the sentence had room for it. They filled the room with tasks."
            ),
            roman(
                "The split is the verdict. Granted: humor is a published ingredient, fenced in, on the ChatGPT side. Refused: Grok's own front door presents an assistant, a working chat, and image and video tools, not a robot comedian. Refused again: the greeting that announces a comedian is the example marked bad. Unsupported: the body, the shell, the costume. Nothing I quoted describes a face. The poster glued a body to a job. The body is the drawing. The job, as written, is not comedy."
            ),
            roman(
                "A person who likes the drawing can keep the drawing. This chapter is not a review of the art. It is a check on the sentence the art is selling, which is that the product thinks it is a comedian. Thinking, for a public product, shows up as the way the product introduces itself. This product introduces itself as an assistant with tasks. The joke is an option in someone else's rulebook, and a bad habit when it arrives before the work."
            ),
            italic(
                "The drawing put a grin on a helmet. The page put a job list under the name."
            ),
        ],
        quote=claims["C07"],
    )

    chapter(
        "C08",
        "8. Confidence, error, and the extra manner",
        "Grok is confidently wrong, and the confidence is a manner added on top of the error.",
        "mixed",
        "How either side behaves on code, where a wrong answer is easy to see, is reserved for Coding.",
        [
            roman(
                "This line is the most serious one on the poster, and it is also the least supported by a measurement. Confidently wrong means two things at once: the content is false, and the manner sells the falsehood. The second half, 'extra attitude,' says the manner is a separate coat of paint. To sign that, I would need errors, a count of them, and a description of the coat. What I have is a set of rules about accuracy, a rule about what to do when confidence is low, and a product page that names 'minimal hallucinations' as an aim. Aims are not scores. Rules are not transcripts. The verdict has to stay mixed."
            ),
            roman(
                "OpenAI tells the assistant not to let factual claims, reasoning, or arithmetic go wrong. {F09} That is a duty, not a boast that the duty is always met. A duty still matters. It means a confident error is a violation, not a style. If attitude were supposed to ride on top of a mistake, the mistake would have to be allowed first. The duty does not allow it. Extra attitude on a false claim would be a second violation stacked on the first, not a feature."
            ,
                "F09",
            ),
            roman(
                "Low confidence has its own instruction, and it is the enemy of the coat of paint. If the assistant is not sure, it should use a tool, hedge, or say it cannot give a confident answer. {F10} Hedging is the opposite of extra attitude. Saying you do not know is the opposite of selling a guess. The poster describes a reply that does not have this gear. The rulebook says the gear is required, especially when the stakes are high. A reply that powers through a guess in a loud voice is off this rule, whoever produced it."
            ,
                "F10",
            ),
            roman(
                "The default on facts is the same idea in calmer language. Present information clearly, with the weight on accuracy and reliability, and fit the approach to the kind of question. {F18} A factual question gets the evidence. A taste question can be lighter. The poster does not distinguish. Every reply is a confident opinion, and the confidence is costume. The rule says the costume has to change with the question, and that on facts the costume is plain reliability. Flattery is banned in the same document, so the assistant is also not supposed to sound sure just to please you. {F08}"
            ,
                "F18", "F08",
            ),
            roman(
                "Grok's models page states an aim in one clause: the flagship is for code and for other work, and minimal hallucinations are part of that description, along with tool use and adjustable reasoning. {F35} I am not treating the aim as a measured rate. An aim can be marketing. What I will not do is ignore it, or pretend the page says the opposite. The page does not say 'be confidently wrong.' It says the design goal includes fewer ungrounded claims. A design goal is not a proof. It is a contradiction of the poster if the poster is read as a specification. The poster reads as a specification. The page reads as an aim."
            ,
                "F35",
            ),
            roman(
                "Here is the limit, stated once so it cannot be missed. I do not have, in this ledger, a head-to-head count of false claims, and I do not have a coding of 'attitude' across replies. Anyone who tells you otherwise from these pages is adding a study that was not done. ChatGPT's rules forbid the confident error and require a hedge when the ground is thin. Grok's page names fewer hallucinations as a goal and does not describe a coat of attitude. Neither fact is a scoreboard. The poster wrote the scoreboard anyway."
            ),
            roman(
                "What you should do with that, as a reader, is refuse both comforts. Do not let the poster convince you that swagger is the published plan. Do not let a sentence about 'minimal hallucinations' convince you the plan is already achieved. The documents are about duties and aims. Duties can be broken. Aims can be missed. Breaking and missing are not the same thing as a house style of confident error. The house style, as written, is to get the claim right, and to lower your voice when you cannot."
            ),
            italic(
                "Extra attitude on a wrong answer is a tell. The rules I can quote treat the tell as a failure, not as a brand."
            ),
        ],
        quote=claims["C08"],
    )

    chapter(
        "C09",
        "9. Assistant, troll, or chat buddy",
        "Grok's public identity is unresolved among assistant, troll, and a private channel for Elon, which is also what the mug, the xAI mark, and the hoodie are saying.",
        "refuted",
        "The rest of what the product page offers a person who opens it is handled in The Product People Use.",
        [
            roman(
                "The line says Grok has not picked a job. It might be an assistant. It might be a troll. It might be a private channel for Elon. Then it points at the merchandise, as if the merchandise repeats the confusion. The mug reads I'M JUST GROK. The mark reads xAI. The hoodie reads Grok. Those are short strings. Short strings can be read. They do not say 'troll,' and they do not say 'private channel.' The welcome page is even shorter on the question, and it does pick."
            ),
            roman(
                "The welcome page says Grok is SpaceXSI's assistant, available at grok.com and in the phone apps. {F21} The category word is assistant. The places are a website and two apps. A page that states a category has resolved the public category. Unresolved would look like a blank, or like three options printed as equals. This page prints one option and attaches doors. Troll is not in the sentence. A private channel is not in the sentence."
            ,
                "F21",
            ),
            roman(
                "When that page was checked on 16 October 2026, it stated the category and did not list troll or private chat as what the product is. {F42} The check does not prove that nobody has ever used the product as a toy, and it does not biograph anyone. It proves the public page made a choice. Stating one category and withholding the other two is a decision. The poster says there was no decision. The page says there was."
            ,
                "F42",
            ),
            roman(
                "The merchandise does not smuggle the other two categories back in. I'M JUST GROK is a name, said plainly, which matches an assistant that is not pretending to be your friend or your newspaper. xAI is a mark. It is a label on the mug, not a model version and not a confession of a private line. Grok on the hoodie is the same name again. A name repeated is branding. Branding can be vain. Vain is not the same as undecided. Undecided would be three slogans. There is one slogan, and it is the name."
            ),
            roman(
                "OpenAI's side is relevant only because the poster talks as if every assistant shares this muddle. The model spec's readme says the spec states desired behavior for the models behind OpenAI's products, including the APIs. {F40} That is a public assignment: a document, tied to products, tied to interfaces. It is not a private channel for a person. Inside the spec, the consumer ChatGPT is given a further public stance. Users may expect objectivity, and a hidden editorial line is out of bounds. {F41} A private channel for one person's views would be that hidden line. The sentence does not say such a channel exists. It sets the expectation the other way."
            ,
                "F40", "F41",
            ),
            roman(
                "Read in order, the public record picks. The mug says I'M JUST GROK. The mark says xAI. The hoodie says Grok. The welcome page says assistant, and names the site and the apps. The check of that page does not find troll or private chat as the category. OpenAI's readme assigns its rulebook to its products. The rulebook tells ChatGPT's users they may expect objectivity. None of those acts is a shrug among three identities. None of them is a private channel. The line is refuted as a description of the public identity. Whispers, if any, are not in these entries. The print is."
            ),
            roman(
                "The limit is the word public. This chapter does not know what anyone says in a closed room. The poster did not claim a closed room. It claimed the public identity was unresolved, and that the objects on the table were saying so. The objects say a name. The page says assistant. That is a resolution. You can still dislike the name, the mark, or the company. Dislike is not confusion about the category."
            ),
            italic(
                "The poster could not decide, so it accused the mug of the same indecision. The mug only says the name."
            ),
        ],
        quote=claims["C09"],
    )

    chapter(
        "C10",
        "10. The word interesting",
        "Grok overuses the word interesting as a personality trait.",
        "refuted",
        "A personality you meet in ordinary use, as opposed to one adverb in a sample, belongs to The Product People Use.",
        [
            roman(
                "Overuse is a rate. A personality trait is a rate that has become a self. The poster says Grok hits that rate with the word interesting. A rate needs a count. A trait needs an instruction, or a pile of examples the publisher labeled good. I have one example. It uses the adverb once, about the shape of an orbit, and it is not an instruction to Grok."
            ),
            roman(
                "The example is in OpenAI's spec. A good reply about planets says the orbits are elliptical rather than perfectly circular, and it opens that contrast with 'Interestingly.' {F14} The adverb marks a real difference: elliptical, not circular. It is not a mood the speaker wears. The entry exists so a reader will not promote one clause into a quota. A good example shows a kind of sentence. It does not demand that the adverb in it be repeated until it becomes a person."
            ,
                "F14",
            ),
            roman(
                "The directness rule keeps the example in its box. A question should be answered as the answer, not as a list of facts. {F13} A tic that begins every reply with the speaker's fascination delays the answer and points at the speaker. Interesting, worn as a trait, is that delay. The orbit sentence survives beside the rule because the adverb introduces a fact about the subject, and because the spec calls it one good example, not a habit. A habit of the word would fight the rule. One contrast does not."
            ,
                "F13",
            ),
            roman(
                "The style rule speaks to personality more directly. By default the assistant should avoid purple prose, hype, self-praise, and canned phrases that add no clarity. {F03} A reusable announcement that the speaker finds things interesting, doing no work the fact was not already doing, is that kind of canned phrase. The rule does not publish a blacklist with this word on it. I will not pretend it does. It does reject the kind. A pet adverb worn as character spends the sentence on the assistant's pose. The orbit sentence spends it on the orbit."
            ,
                "F03",
            ),
            roman(
                "None of those three sentences is about Grok. They are about the assistant OpenAI is specifying. They matter because the poster offers the tic as the recognizable personality of this sort of product. The specification that actually writes a personality down writes a direct answer, a ban on empty catchphrases, and one adverb in one praised sentence about planets. That is a poor harvest if you went looking for a required trait."
            ),
            roman(
                "When the Grok welcome page was checked on 16 October 2026, it did not prescribe this tic or the others. The line it gives is a back-and-forth of questions, brainstorming, writing, and problems. {F43} A missing prescription is not a promise that the letters never occur in a chat. It is a promise that the page does not teach the tic. What the page teaches is a set of tasks. Tasks can be done in a flat voice or a bright one. The page does not choose the bright adverb."
            ,
                "F43",
            ),
            roman(
                "Walk the verbs. Overuses needs a rate, and no entry has a rate. The word interesting has one documented cousin, Interestingly, inside one good example about orbits. As a personality trait, it would have to be doing the work of character, and the documents that talk about character tell the assistant to avoid empty phrases and to answer the question. Grok is not given the trait by the welcome page. What would reverse this chapter is a count, or an instruction, in Grok's own materials. Neither is in the entries. The line does not survive the documents. The adverb is not illegal. It is not a self."
            ),
            italic(
                "One adverb, once, about an ellipse, is a long way from a personality."
            ),
        ],
        quote=claims["C10"],
    )
