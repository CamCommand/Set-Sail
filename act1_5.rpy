init python:

    # splitting the mc's name in half
    def getSplit(s):

        s = player_name
        a = len(s)
        s1 = slice(0,len(s)//2)
        s2 = slice(len(s)//2, len(s))
        s3 = s[s2].capitalize()

        return s[s1] + " and the other " + s3


label act1_5:

    show BG shore with dissolve
    play music "music/BelowDeck.mp3" volume 1.0 fadein 1.5 fadeout 1.5
    play effect "audio/shore.ogg" volume 0.8 fadeout 1.0

    $ renpy.block_rollback()
    $ quick_menu = False

    "Washing up on a rocky shore after that night doesn’t feel thematically appropriate."

    $ quick_menu = True

    "A part of me hoped the dingy would be shredded by a whirlpool in a reef somewhere. That way I wouldn’t have to come up with a next step."

    "But here I am instead."

    "On some beach."

    "In the middle of nowhere."

    "Well, maybe not nowhere. I can faintly here some civilization behind me."

    "Not sure where this \"where\" is, but I hope it isn’t South America. I haven’t spoken Spanish in five years at least."

    "There was plenty of reason to use it, however the past eight years or so the number of Spanish speaking crew mates dwindled until it was just me and Captain."

    "And he didn't exactly talk to me that much so really it's his..."

    "..."

    "Nevermind."

    "If I’m in America, I could be arrested if I’m found out I’m the first mate of The Red Plague."

    "I've never seen a wanted poster of myself, but alone I'm powerless on land."

    "I have no crew, no influence, and no money to worm my way out of trouble."

    "Is there even a point acknowledging the worst night of my life?"

    "How long do I have to just sit with it before moving on?"

    "Poseidon has allowed me to touch land again, yet what is his plan for me? There’s nothing left for me to do."

    "I wonder if anyone else made it out?"

    "I heard Iron Hip yell first under the deck. He must have emptied the entire clip before his screams stopped."

    "JoeJoe easily could overpower three grown adults, but based on Flavio’s..."

    pause 2.0

    "Based on how I found Flavio I don’t think they were playing fair."

    "Yet nobody but me will remember their last moments. Their crimes will be revered but them as people will be forgotten."

    stop effect fadeout 3.5

    "It’s unbelievable that the Captain saved me. Why would he let me go free?"

    "He told me to keep pirating, but what does that mean? There's nothing I can do in this state."

    play effect "audio/stomach.ogg"
    pause 2.0

    "I wish I had grabbed some rations. Haven't eaten anything since high rise yesturday."

    "But before finding something to eat, there’s something that needs to be done."

    show BG black with fade
    show BG shore_sword with fade

    $ persistent.menuflag = 1

    if persistent.menuflag_count == 1:

        $ persistent.menuflag_count += 1

    pause 3.0
    nvl show

    n "The most important tenets of Anarchy are as follows. Freedom, the rejection of hierarchies, and fairness for all."

    n "These pillars stand proud in the Pirate Code. The rules every good pirate lived by and what every great pirate dies by. Where everyone gets a fair shake at life."

    n "This life."

    n "This way of being, it’s not an easy one."

    n "The world has rejected us pirates for thousands of years, but we kept fighting to stay alive and to stay free. We didn’t disappear into history books, we continued to cripple the legs of high society."

    n "Enraging our enemies and strengthening our own bonds. \"A pirate’s life for me!\" is what we all said in unison in the face of a corrupt world that didn’t make sense to us."

    n "This saying shortens our lifespan but enhances our lives. This was a sacrifice we all took on willingly. My comrades paid the ultimate price for their choices, and in the end, I bet they were happy."

    n "They achieved the happiness they sought out for. Is that not a reason to celebrate their lives? Celebrate the lives of the freest people on both sides of the equator?"

    n "Simply believing that is true wouldn’t suffice if I hadn't lived it along with them. I will live the rest of my life, celebrating theirs."

    n "Whenever I’m eating food that doesn’t taste like wood I’ll remember Donatello who could spice up a turd to make it a blessing from the Gods."

    n "Everytime I draw a pistol I’ll remember Iron Hip, who could empty a gun into an enemy's chest faster than anyone I ever knew."

    n "I’ll never forget how ol’ Two Hands used both his hands in every task he did, no matter the risks. His efficiency was immeasurable."

    n "And most of all, I’ll remember my Captain and his ideology of brutal honor down to his very last moment. I will take the lessons you all taught me and carry them to my own end."

    n "The freedom of this lawless lifestyle was not just a chaotic band of misfits committing crimes against the ruly. It was an organized fraternal bond that gave said misfits a place to call home."

    n "I realize that now more than ever."

    n "Until Posideon deems it to be my final act, I will continue on all your legacies. May you all be guided to the afterlife safely and with peace in your souls."

    n "This grave itself cannot express the size of our loss, but it represents more than anyone will ever understand. The Red Plague and it’s crew will be marked into eternity by my hands."

    n " Thank you for everything Captain."

    n "To The Red Plague and all who called it sanctuary."

    nvl clear
    hide window

    pause 3.0

    "Hopefully this will be enough for them."

    "I don't exactly have the resources for a proper pirate funeral, but I think they'd apperciate this much."

    "..."

    "Time to find out where I washed up."

    "I should turn my shirt inside out, it just occurred to me how much blood has seeped into it."

    "Don’t think any of it is mine, thankfully. Nobody will let me near them if I look this bad."

    "It may be time to sell my earrings for something to ration. If they take earrings as payment still."

    "That sort of old pirate tradition might not be as viable today as it use to."

    "I’ve never heard a story of anyone actually using them to get emergency funds or to barter for anything."

    "If silver hasn’t gone down in price, at least one of my studs should buy me a sandwich."

    pause 2.0

    show BG black with fade
    show BG streetpost with fade
    stop music fadeout 2.0
    play music "music/PirateTimes.mp3" volume 1.0 fadein 1.5

    "The coastline’s piles of trash hinted towards this being the mainland and not an island."

    "Based on the candy wrappers and garbage bags my final guess is that I’m back in America."

    "However, on the beach and since I’ve been walking I've been seeing these blue paper sheets everywhere."

    "Maybe I’m someplace else after all? Or more likely some useless product fell out of popularity."

    "There are a few people wearing them as masks that I’ve seen, but not enough compared to how many are on the ground."

    "They aren’t very cool looking masks, so it could be a medical thing. Or everyone got really ugly in the past couple of years."

    "No matter the reason concealing my face might be a good idea."

    mc "Excuse me fellas, why are you wearing masks today?"

    cr "Get bent you anti-vaxx jackass!"

    mc "Thank you all for your time."

    mc "Two legged swines."

    "What is an \"anti-vaxx\"?"

    "They assumed I was one, so I guess it’s a new infighting group thing."

    "Like the Catholics and Protestants or Cowboys and Aliens."

    "The split must be the ones wearing the masks are anti-anti-vaxxers and the ones without are the anti-vaxxers."

    "Navigating between these groups could be difficult if I want to talk to anyone."

    "What side should I pick?"

    define mask = 0     # boolean for having a mask
    define doll_met = 0 # if the player meets Doll

    menu:

        "Anti-anti-vaxxers":

            $ quick_menu = False
            $ renpy.block_rollback()

            "If it’s a medical thing, I should find a mask to wear. Who knows what gross disease they’re trying to avoid."

            $ quick_menu = True

            "Plus hiding my identity doesn't sound too bad either."

            "It wouldn’t seem clean to dry one off from the ground. Maybe an anti-anti-vaxx shop could give me one."

            show BG black with fade
            show BG dollcorner with fade

            jump mask

        "Anti-vaxxers":

            $ quick_menu = False
            $ renpy.block_rollback()

            "There are more people here without masks than with, playing to the stronger side would be the safest thing to do."

            $ quick_menu = True

            "Best to stay with the winning team, if those passerbys were anything to go off of this sounds like a serious disagreement."

            show BG black with fade
            show BG signcorner with fade

            jump nomask

        "Play them both":

            $ quick_menu = False
            $ renpy.block_rollback()

            "If I find a mask it might be beneficial to play both sides."

            $ quick_menu = True

            "Getting one off the ground would defeat the medical purpose of one."

            "Maybe an anti-anti-vaxx shop could give me one."

            show BG black with dissolve
            pause 1.5
            show BG dollcorner with dissolve

            jump mask

    label mask:

        "Most of these shops are shut down. Windows and doors are boarded up, and seemingly have been like that for a while."

        "There are a few empty and unkempt houses scattered around the neighborhood. There could have been a depression as well as a disease."

        mc "What happened here?"

        show doll mad with dissolve

        $ doll_met = 1

        dl "What’s wrong with you? You new to the world or something’?"

        "Woah!"

        "Some street urchin peaked behind a pillar to say that. Freaked me out."

        mc "Hello, um, yes."

        mc "Why are all these buildings closed off?"

        $ dl = Character('Street Urchin', color = "#740E86", callback=hobo_voice)
        show doll at wiggle with Dissolve(0.1)

        dl "{cps=10}Ha haha!{/cps}"

        dl "Have you been at sea for a long time or somethin’?"

        "She doesn't appear to be hostile. Not that I trust her, but my guard doesn't have to be up so high."

        mc "Something like that. Could you fill me in?"

        dl "Oh really now? I was just playing."

        show doll mad with Dissolve(0.1)

        dl "Yeah kid there was a big sick, thee ol’ black plague part two, a crippling pandemic if you will."

        dl "No pun intended or somethin’."

        show doll at wiggle with Dissolve(0.1)

        dl "{cps=10}Hehehehehehe!{/cps}"

        mc "Miss, are you one of the anti-vaxx people?"

        $ dl = Character('Doll', color = "#740E86", callback=hobo_voice)
        dl "You can call me Doll sweetheart, haven’t been called Miss in a long time."

        dl "I’m not against the jab but there really isn't a way for me to avoid the filth out here by myself."

        dl "Do you want a mask sweetheart?"

        mc "Yeah I was looking for one."

        dl "One second sweetheart."

        show doll with ease:
            ypos 1.05

        play effect "audio/rummage2.mp3"

        "Doll swings her backpack around to her stomach and opens it up. I didn't notice she had one until now."

        "She pulls out a plastic sealed white mask and offers it to me."

        show doll with ease:
            ypos 1.00

        mc "That looks really nice, thank you."

        mc "Would one of my earrings be enough for it?"

        $ mask += 1

        dl "Oh don’t worry ‘bout it sweetheart just take it."

        dl "Like I said, I don’t need’em."

        mc "Thank you Doll, you’ve shown me a great kindness."

        dl "Yeah yeah, I don’t need to be buttered up."

        dl "Take it and have a good time in what's left of Seaborough. You don’t need to owe a debt to some old lady."

        mc "Wait what did you say? That name?"

        dl "You’re in Seaborough sweetheart. Welcome to Florida, don’t catch the rona."

        show doll at wiggle

        dl "{cps=30}Hehehehehe!{/cps}"

        hide doll with dissolve

        jump return2sender

    label nomask:

        "Most of these shops are shut down. Windows and doors are boarded up, and seemingly have been like that for a while."

        "There are a few empty and unkempt houses scattered around the neighborhood. There could have been a depression as well as a disease."

        "There's this place, it seems empty but the glowing sign says it’s open."

        "There’s another weird sign by the door."

        "\"Welcome, Face coverings required for individuals aged kindergarten and up. Please wear your mask properly, Covering your nose and mouth.\""

        "\"Wearing a mask protects others from COVID-19. Thank you.\""

        "So it’s a disease called COVID-19. That’s a weird name?"

        "Maybe they found it nineteen years ago? Am I supposed to know what a covid is?"

        "Also what’s a kindergarten?"

        "The world seems to have changed a lot in a few years. No way I could have kept up."

        "I should have asked more questions when I was in Seaborough."

        "Wait, Seaborough. How was that spelt again?"

        "What is that sign in the corner?"

        "\"Support your local business. Seaborough needs your support!\""

        "I don't believe it."

        jump return2sender

    label return2sender:

        define earrings = 1           # if you still have your earrings
        define may_position = ""      # what May is from MC's view
        define may_name = "Woman"     # Whatever fake name May gives MC

        $ m = Character("[may_name]", color="#0A4AF6",  callback=may_voice)

        "I’m back in that town!"

        "All those years ago I had the greatest time on the mainland and Poseidon has brought me back!"

        "This is a sign by the Gods that I need to do something here!"

        "To figure out what it is I have to do I should retrace my steps."

        "After walking around where did I go first?"
        #$ activity_choice = "school"  # for testing purposes

        menu:

            "Schoolhouse":

                $ quick_menu = False
                $ renpy.block_rollback()

                "The school!"

                "I should go see if the girls are still there."

                $ quick_menu = True

                "They’d still be in high school right?"

                "I wasn’t gone for that long, I’m sure they’re just chilling in the club room like last time I was there."

                "The school shouldn’t be that far from here. I’ll get there before the club meeting ends."

                "Then Posiedon will reveal to me what I should do next."

                if activity_choice == "school":

                    jump school2

                else:

                    "Wait, I didn’t go to the school first."

                    "I stopped by the [activity_choice] first then found my way to the school."

                    "There’s little chance any of the girls are there anyway."

                    "I’ll run to the [activity_choice], something relevant to my journey has to appear there."

                    "If not, then I’m sleeping on a bench tonight."

                    if activity_choice == "bookstore":

                            jump bookstore2

                    elif activity_choice == "arcade":

                            jump arcade2

                    else:

                            jump market2

            "Bookstore":

                jump bookstore2

            "The Market":

                jump market2

            "Arcade Bar":

                jump arcade2

    label school2:

        show BG black with fade
        show BG schoolpost with fade

        "The school grounds are vacant. Give or take a few cars, and I don’t hear anything either."

        "Has everyone left or are they all still inside doing book papers things?"

        "I can’t remember when school let out last time and I shouldn’t just walk in there looking the way I do now."

        "I’m still drenched in sea water and blood, they’d sick the law on me."

        "Should’ve stolen some clean clothes before coming here. Not that there were clothing stores with loose security around."

        "Astrid was waiting for me on the stoop when I got here, but she has no reason to be here now."

        "So how do I get in? I wish there was some way to contact Astrid."

        "She’s likely onto bigger and better things at this point, no reason for her to stick around."

        "The rest of the eboard as well. Staying four additional years here doesn't sound like something they'd all do."

        "That afternoon with the Pirate Culture Club was fun, but I could tell they wanted to go somewhere else with their lives."

        "I hope they all got there, wherever they are."

        show may with dissolve

        m "Hey you!"

        mc "Me?"

        m "Yes you!"

        mc "Do you need something?"

        m "This is school property, should you be here?"

        mc "I {cps=15}ummmmmmmmm.{/cps}"

        menu:

            "I'm a student":

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "I’m a student here, who are you?"

                $ quick_menu = True

                "She looks disheveled and tired. In addition to the fact that she's in front of the school and not in it, she can’t be a teacher."

                "I’ll call her bluff and see how she responds."

                show may flip with Dissolve(0.3)

                m "Oh really?"

                m "Well how come you’re not in class right now?"

                m "Why are you dressed like that?"

                "Why am I dressed like that?"

                "Why are you dressed like that?"

                "She smells like she just came off a ship herself and she’s accusing me of being out of place?"

                mc "Finishing up the exercise class now. I’m sweaty because of all the running."

                m "Well I’m the new gym teacher, and that’s why I’m also sweaty."

                "This woman is lying to me too!"

                m "You don't look like you're in my class."

                $ may_name = "Mrs. Paul"

                $ may_position = "\"teacher\""

                mc "I'm not in your class. Who are you even?"

                mc "If you're new I haven't met you yet Miss..."

                "Just need to catch her in the lie."

                show may smile with Dissolve(0.3)

                m "I’m Mrs. Paul, nice to meet you."

                m "Could you remind me which way the gymnasium is? Because like I mentioned, I’m new."

                mc "Sure Mrs. Paul, it’s around the back on the right."

                "Well something is over there at least."

                mc "I have another lap to do so I’ll see you in there."

                m "Thanks, make sure you shower when you’re done."

                show may sad with Dissolve(0.1)

                m "Wait, where are the other students?"

                mc "What other students?"

                show may with Dissolve(0.1)

                m "The ones in your other class."

                "This is getting risky. I'll have to take one final shot to crush both our stories."

                mc "I'm not sure where everyone is."

                mc "Maybe they're with your students?"

                show may at wiggle
                pause 1.0

                "We silently stare each other down, neither of us making a single move."

                "I've won."

                mc "Have a nice day Mrs. Paul."

                m "Yeah, you too. Don’t be late for class."

                mc "I won’t. Bye now."

                m "Yeah, bye."

                hide may with dissolve

                "I knew she was full of shite! There was no way she was really a teacher."

                "I'll take this chance to leave as well."

                "The girls aren’t here and if lying to another criminal is that hard, I don’t think I’d have much luck if the police are called."

                "Normally giving up so easily isn't in my playbook, but I'm getting super hungry."

                "A better solution might come to me after some calories."

                "Time to prioritize food before Posideon’s destiny can grasp me properly. There might be some cheap seafood back by the shore."

            "I'm a teacher":

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "I’m a teacher here, who are you?"

                $ quick_menu = True

                "She doesn’t look like anyone’s parent based on how tired and frazzled she looks."

                "If she was, she'd be at work or something, so let’s see if she calls my bluff or not."

                show may smile with Dissolve(0.1)

                m "Oh, excuse me then."

                $ may_name = "Mrs. Padilla"
                $ may_position = "\"teacher\""

                m "My name is Mrs. Padilla. I’m a recent graduate and am here to drop off my resume for the teaching job here."

                mc "That’s fine, no harm done."

                mc "Excuse me, I’m the sports teacher. That's why I'm all sweaty."

                mc "You can drop off your resume in the main office."

                m "You’re the gym teacher?"

                show may sad with Dissolve(0.1)

                m "Where are your students? And your whistle?"

                "Shite, she's flipping it on me now!"

                mc "They’re {cps=5}uh,{/cps} running laps."

                m "There’s a track here?"

                mc "Yes, it’s on the other side of the school."

                show may smile with Dissolve(0.1)

                m "Oh thank you for the help, and you’re..."

                mc "I’m Dr. [player_name]."

                "Why did I say doctor!"

                show may fl

                m "Oh, thank you Dr. [player_name]."

                "I think I gained her trust. Flexing authority got me unearned respect."

                "As long as I don’t claim a role that requires identification, this might open some golden opportunities."

                "Swindle a idiot or two to make some money."

                show may fl at zoom_may

                m "Maybe we’ll be coworkers soon. I’d love for you to show me around sometime."

                m "What number is your classroom?"

                mc "I’m number..."

                define num = 0

                menu:

                    "9":

                        $ num = 9

                    "127":

                        $ num = 127

                    "266":

                        $ num = 266

                    "1010":

                        $ num = 1010

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "I'm room [num], if I’m held up I'll be there after school."

                $ quick_menu = True

                mc "Normally I get home before the other teachers."

                show may smile at redochar

                m "I thought you were the gym teacher, why do you have a classroom?"

                "{cps=20}Uh oh.{/cps}"

                mc "Do gym teachers not have classrooms where you're from?"

                show may sad

                m "{cps=20}Hmmmmmmmm.{/cps}"

                show may smile with Dissolve(0.1)

                m "Alrighty, see you soon around then."

                hide may with dissolve

                "Without another word she wanders off around the school."

                "I'll take this chance to leave before she comes back. No idea if the track is back there or not."

                "The girls aren’t here and if lying to another criminal is that hard, I don’t think I’d have much luck if the police are called."

                "Normally giving up so easily isn't in my playbook, but I'm getting super hungry."

                "A better solution might come to me after some calories."

                "Time to prioritize food before Posideon’s destiny can grasp me properly. There might be some cheap seafood back by the shore."

            "Flip it on her":

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "I'm allowed to stand in the car lot. You look more sketchy than me!"

                $ quick_menu = True

                "Compared to everyone I saw around town or at school she is the most out of place."

                "She smells about as bad as I do and I doubt she's on a mission from Posiedon."

                "I’d bet she’s trying to intimidate something out of me. Well it isn't going to work lady."

                $ may_name = "Mrs. Panza"
                $ may_position = "\"nurse\""

                show may at wiggle

                m "Excuse me! I’m the school’s nurse Mrs. Panza."

                m "Who are you?"

                "Like Hell she’s a nurse!"

                "She must also think I’m suspicious. Let’s see who’s bluff lasts the longest."

                mc "You are? I’ve never met you?"

                show may flip with Dissolve(0.3)

                m "I’m only here on rotating days, it’s possible you’ve missed me."

                mc "Which days?"

                m "Mondays and Fridays."

                mc "Really?"

                mc "Because I stopped by the nurse’s office on Friday and I didn’t see you there."

                m "Last Friday?"

                mc "Yes, last Friday."

                m "Why were you in school last Friday? We didn't have school."

                "That's a risky card to play Mrs. Panza, but I can counter it."

                mc "The student’s didn’t have school, faculty meeting, you had to be there."

                "So glad I remembered what faculty meetings are."

                m "That only applies to the teachers, not the nurses."

                "Shite!"

                mc "But we had a discussion set aside for supply budgeting, this included the nurses."

                m "Were you at a meeting or did you stop by the office?"

                show may smile with Dissolve(0.3)

                m "Which is it?"

                "Oh, you think you're so clever!"

                mc "It was both, I stopped by the office to look for Miss. Conners."

                "Throw another character in there, knock her off balance."

                m "Miss Conners is on her honeymoon, she wouldn’t have been there."

                "Yeah, like you know Miss Connners!"

                mc "Miss Conners and I don’t get along very well, I went to get her and strike up a conversation."

                mc "She didn’t tell me she was gone."

                m "Weren't you sent to get her for the meeting?"

                mc "Yes that’s how I know you weren’t there."

                m "If you were sent to get Miss Conners then others should have known she wasn’t here."

                mc "It was an honest mistake and I thought the nurses weren’t supposed to be at the school?"

                m "At the school or at the meeting?"

                mc "At the meeting!"

                m "The one on Friday, the day that I don’t come!"

                mc "Because you’re on your honeymoon!"

                m "Yes!"

                show may

                "Got her!"

                mc "So are you Miss Conners or Mrs. Panza?"

                m "Who’s Mrs. Panza? I’m just the substitute nurse!"

                mc "You said that was your name?"

                m "I didn’t tell you my name, I said I was a nurse."

                mc "Yes you did!"

                m "Well that isn’t my name."

                "..."

                $ May_affinity += 1

                "We silently stare each other down, neither of us making a single move. We both look more out of breath than when we got here."

                mc "I have to go to my next class."

                m "I’m needed at my next appointment."

                show may at left with moveoutleft
                show may smile with Dissolve(0.1)

                play effect "audio/good.mp3"
                m "{color=#50A23B}Hey kid, not bad.{/color}"

                hide may with moveoutleft

                "I'll take this chance to leave if she comes back."

                "The girls aren’t here and if lying to another criminal is that hard, I don’t think I’d have much luck if the police are called."

                "Normally giving up so easily isn't in my playbook, but I'm getting super hungry."

                "A better solution might come to me after some calories."

                "Time to prioritize food before Posideon’s destiny can grasp me properly. There might be some cheap seafood back by the shore."

                jump act1_6


        jump act1_6

    label bookstore2:

        $ quick_menu = False
        $ renpy.block_rollback()

        "I’ll return to the bookstore!"

        $ quick_menu = True

        "If I’ve learned anything else about this world that wasn’t from pirates, it was from books."

        "Even what a bookstore actually was from the labels on the spines of my first few volumes."

        if activity_choice == "bookstore":

            "That's where I went first, I met that librarian who let me steal that book."

            "Or did I just steal by myself alone?"

            "What was her name? Yomo? Yacko?"

            "Either way, the answer’s I’m looking for could be there. Maybe a clue to the next step of my journey?"

            "Who knows? Maybe there will be clean clothes if luck will spare some."

            show BG black with dissolve
            pause 1.0
            show BG nobook with dissolve

            "This can’t be it."

            "There’s nothing here, the sign and books are gone. It can’t be closed."

            "All the closed businesses look alike, but the faded remains of the shop’s raven logo are too familiar."

            "A peek inside shows the shelves have been stripped clean of their contents. Thick layers of dust indicate it’s been closed for a long time now."

            mc "Damn it all, this can’t be it!"

            "Is this COVID’s doing?"

            play effect "audio/banging.ogg" loop

            "If I was to find it closed down, what is there to discover? There’s no way the door could be-"

            stop effect
            play effect "audio/dooropen.ogg"
            pause 0.75

            mc "Well, that’ll do the trick."

            show BG insidestore with dissolve

            "My view from the windows shielded my nose from the unknown stench that now lives in the abandoned building."

            "Dust mixes horribly with wet sewage dripping from pipes pooling on the floor. Puddles of the liquid find dips on the ground all throughout the store."

            "The only illumination comes from the sun barely sneaking behind the clouds, leaking through the windows."

            mc "There’s nothing left."

            "The sanded wood panels that once held such amazing works of literature have been lost to the darkness."

            mc "Except..."

            "What is this doing here?"

            show tome at bottom with dissolve

            define tome_choice = 1

            "How could something so large be left behind?"

            $ may_name = "Girl Voice"
            m "Excuse me, who’s in here?"

            $ may_position = "theif"

            "Oh barnacles!"

            play effect "audio/duck.ogg"

            "I duck behind some debris, there's no chance anyone can see me in this lighting."

            "Do old buildings still count as trespassing? This could get bad."

            m "I saw you go in here. This place looks empty as Hell, not much to steal."

            "She’s right, there’s nothing in here."

            "She doesn’t sound hostile. How should I approach this?"

            jump choice_emptystore

        else:

            mc "Wait!"

            "I don’t remember actually going in there at all."

            "There was a long walk before heading to the school, but entering the bookstore never happened. I just walked past it."

            if activity_choice == "school":

                "Making my way towards the club might be the best course of action. The girls could still be there, or they need my help."

                "Whatever is thrown at me can be handled, as long as I stay focused."

                jump school2

            elif activity_choice == "arcade":

                "Instead, I chose to go to the arcade first then found my way to the school."

                "I’ll run back there, something relevant to my journey has to appear there. If not, then I’m sleeping on a bench tonight."

                jump arcade2

            else:

                "Instead, I chose to go to the market first then found my way to the school."

                "I’ll run back there, something relevant to my journey has to appear there. If not, then I’m sleeping on a bench tonight."

                jump market2

    label arcade2:

        $ quick_menu = False
        $ renpy.block_rollback()

        "Back to the arcade!"

        $ quick_menu = True

        "Is that where I went back then? Maybe technology has evolved to the point where video games can help me guide my life?"

        if activity_choice == "arcade":

            "The bartender might bestow some of his wisdom on my situation."

            "They didn’t seem like the type to rat out a pirate. No matter the reason for it, Poseidon wants me back to that place."

            "The place shouldn’t be far from here."

            show BG black with dissolve
            pause 1.5
            show BG dollcorner2 with dissolve

            "Seemingly endless strips of vacant and boarded up shops blend into each other."

            "A CVS, whatever that stands for, and Burger King are the only open businesses that seem to be hanging on."

            "What services are those stores providing that are so important?"

            "Sandwiches and, um, creamy vegetable soup?"

            "The video games were so cool, so why isn’t it here anymore? The place must have been around here, but there’s nothing there anymore."

            "I suppose video games aren’t as valuable as food."

            "Damn, this COVID thing really took the fun out of land life. It doesn’t look like there’s any fun to have with all these shops closed up."

            "Maybe these women know if the store moved or not?"

            show m_d at center with dissolve
            show doll mad at left with dissolve
            $ dl = Character('Lady 2', color = "#740E86", callback=hobo_voice)
            $ may_name = "Lady 1"
            $ m = Character([may_name], color="#0A4AF6",  callback=may_voice)

            mc "Excuse me ladies."

            m "Uh yeah? What’s up?"

            if doll_met == 0:

                mc "Do you know if that arcade bar is still open or if it moved somewhere?"

                if player_identity == "m":

                    m "Doesn’t look like anything’s open hotstuff."

                else:

                    show doll with dissolve

                    dl "Nothing like that’s still open sweetheart."

            else:

                $ dl = Character('Doll ', color = "#740E86", callback=hobo_voice)
                $ may_name = "Lady"
                $ m = Character([may_name], color="#0A4AF6",  callback=may_voice)

                mc "Nice to see you again Doll. Seems like I’ve wandered in a circle."

                show doll with dissolve

                dl "Hey sweetheart, what’s up?"

                mc "Do you know if that arcade bar is still open or if it moved somewhere?"

                if player_identity == "m":

                    m "Doesn’t look like anything’s open hotstuff."

                else:

                    dl "Nothing like that’s still open this late in the game sweetheart."

            mc "Yeah, guess there isn’t anymore."

            m "You looking for someone there?"

            show m_d at zoom_may
            $ may_position = "mom"

            mc "Not, particularly. Can I help you, Miss?"

            show m_d at redochar

            m "You could. I’m actually expecting and need to buy some diapers. But they’re so expensive now."

            m "Would you lend me some money?"

            mc "You’re expecting…a baby?"

            show doll at wiggle

            if doll_met == 1:

                dl "She was telling me somethin’ about it, the poor thing."

            else:

                dl "Somethin’ don’t feel right about poor girl like you without a baby daddy."

            m "Doctor says it's twins."

            mc "{cps=20}You don’t um,{/cps}"

            mc "I mean you don’t look pregnant."

            m "Awe, thanks hun. Well aren’t you sweeter than sugar?"

            show m_d at zoom_may

            m "Even with the baby belly, it’s best to keep my figure looking good no matter what."

            m "You know, just in case ~ <3"

            show m_d at redochar

            mc "Right, just in case something important comes up."

            if player_identity == "m":

                m "So you could spare some money for a woman in desperate need of some masculine generosity?"

            else:

                m "So you could spare some money for a mom in desperate need of some understanding generosity?"

            if doll_met == 1:

                dl "Don't worry about me sweetheart, I’ll make it through somethin’ fine."

            else:

                dl "If you’re giving, give to the mom sweetheart. Doll will make it somethin’ fine without it."

                $ dl = Character('Doll ', color = "#740E86", callback=hobo_voice)

            menu:

                "Sure Miss":

                    "She’s probably lying, if she’s hitting up someone like me for money."

                    "However, even if there’s a slim chance she probably needs it more than me. It’s sad, but I should help in some way."

                    $ May_affinity += 1

                    mc "Sure, I could give you something. I don’t have any cash but I was going to sell my earrings."

                    mc "They’re solid silver, hopefully you can get something for them."

                    $ earrings -= 1

                    play effect "audio/good.mp3"
                    m "{color=#50A23B}Oh my gosh, thank you so much, God bless you!{/color}"

                    m "There’s a pawn shop around the corner. I’m gonna go see how much I can get for them."

                    if player_identity == "m":

                        m "Can you wait here for a few minutes?"

                        m "When I come back I’ll give you a well deserved reward ~ <3"

                        mc "Uh, yeah, I can’t sit for a bit."

                        hide m_d with moveinleft

                        "She makes a seductive motion with her hand and runs off."

                        "Maybe a reward isn’t so bad, sensual or not. I’ll take a seat and wait for her."

                        if doll_met == 1:

                            dl "Oh sweetheart, you’re too kind."

                            dl "But I don’t know if that was smart."

                        else:

                            dl "Hehehehehe!"

                            dl "Hook, line and sinker sweetheart."

                        show BG black with dissolve
                        pause 1.5
                        show BG dollcorner with dissolve

                        dl "I don’t think she’s coming back sweetheart."

                        "Scammed by a land woman. The boys would be ashamed of me."

                        "Should I go after her?"

                        "No, nothing that can be done about it now."

                        "I’m too tired to be angry and too sad to pull out the pirate’s wrath."

                        "Hopefully she gets some use out of the money."

                        if doll_met == 1:

                            mc "See you around Doll, I’m needed elsewhere."

                            dl "Good luck out there sweetheart. Don’t lose your shirt next."

                        else:

                            mc "Nice meeting you Doll, I’m needed elsewhere."

                            dl "Good luck out their sweetheart. Don’t lose your shirt next."


                        "I should move along before I’m considered an easy mark by the locals."

                    else:

                        m "You’re the best, I can’t thank you enough babe."

                        show m_d at zoom_may # make a closer zoom

                        m "Thank you so so much, I’ll name the babies after you if you want."

                        mc "That’s alright, just get what you need."

                        m "No that’s not alright. What is it?"

                        mc "It’s [player_name]."

                        m "Okay [player_name]."

                        python: # splitting the player's name in half for May's baby joke

                            namesplit = getSplit([player_name])

                        m "I'll name one [namesplit]. Bye bye ~ <3"

                        mc "Bye?"

                        hide m_d with dissolve

                        if doll_met == 1:

                            dl "Oh sweetheart, you’re too kind."

                            dl "But I don’t know if that was smart, but you'll get a legacy out of it."

                            dl "Hehehehe!"

                        else:

                            dl "Hehehehehe!"

                            dl "Hook, line and stinkers. At least you'll get some babies out of this."

                        "Hopefully that wasn’t a huge mistake. I’m too tired to have to enact some form of pirate’s wrath on her."

                        "There is still a chance she was pregnant so either way I should move along before I’m considered an easy mark by the locals."

                        if doll_met == 1:

                            mc "Nice talking to you again."

                        else:

                            mc "Nice talking to you."

                        dl "See you around sweetheart. Don’t lose your pants or somethin’."


                        show BG black with dissolve
                        pause 1.5

                        jump act1_6

                "Can't spare anything":

                    "There’s no barnacle splitting way this woman is pregnant with twins!"

                    "Not that I have any money to give her anyway. And like Hell is she getting my earrings."

                    mc "Sorry, I don’t have any money so spare."

                    $ May_affinity -= 1

                    play effect "audio/bad.mp3"
                    m "{cps=20}Ahhhhhhh, really?{/cps}"

                    m "I’d take anything you’d be willing to part with, nothin’ to pawn?"

                    mc "I don’t have anything myself. I got into town not long ago."

                    if doll_met == 1:

                        mc "Doll here can attest to that."

                    if player_identity == "m":

                        m "Are you sure?"

                        show m_d with zoom_may

                        m "I could make it worth your while."

                        "She’s making seductive motions with her hands at me. The desperation of this woman!"

                        "I already said no."

                        "As great as a quicke would be right now, she’s obviously bad news."

                    else:

                        m "Are you sure?"

                        show m_d at zoom_may

                        m "If my pregnancy isn't sufficient enough to convince you, is there anything I could interest you in?"

                        m "Do you have any, alternative tastes I could wet?"

                        "I’m not sure I’d be down with what she’s implying to do to me."

                        "This person has barely met me and she’s coming onto me like her life depends on it. I should let her down easy and walk away."

                    show m_d at redochar

                    mc "Sorry Miss, there’s nothing you can do for me right now."

                    m "Right now?"

                    m "What about a little taste of what I can do?"

                    show m_d at zoom_may # make a closer zoom

                    mc "{cps=90}Ahhhhhhhh! Step off me!{/cps}"

                    "She latched onto me!"

                    "Her chest is intensely warm and there’s a pull on my collar, it’s choking me."

                    "What’s she trying to do to me?!"

                    show m_d at redochar

                    mc "That wasn’t called for lady!"

                    mc "Stay the hell away from me!"

                    m "I’m sowry. I thought you’d like it like that."

                    m "Have a nice day anyway."

                    hide m_d with moveoutleft

                    dl "Oh lord that was hectic."

                    dl "You see my hands? They’re shaking."

                    "That person was crazy!"

                    "Begging me for money and trying to seduce me in one short conversation."

                    "Not that I had anything worth stealing, but come on. Do I like look I have anything of value on me?"

                    "I was lost at sea less than twelve hours ago, nothing but my earrings are worth the copper to you."

                    dl "Missing somethin’ sweetheart?"

                    "Oh no, what did she?"

                    $ earrings -= 1

                    "Where are my studs?"

                    pause 1.5

                    "She took my bloody earrings!"

                    "Where did she go! I’m gonna-"

                    dl "She’s gone sweetheart, and she isn't coming back with change."

                    "Disappeared without a trace, it wasn’t my yelling that shook her. It was because she got what she wanted."

                    "That unbelievable-,"

                    "I’m gonna-,"

                    "Do nothing."

                    "There’s nothing I can do now, she could be anywhere. I’m too tired to have to enact some form of pirate’s wrath on her or whatever I’d do."

                    "And there’s no easy way to track her down without paying someone else. I should move on before I’m seen as an easy mark."

                    if doll_met == 1:

                        mc "Nice talking to you again."

                    else:

                        mc "Nice talking to you."


                    dl "See you around sweetheart. Don’t lose your pants or somethin’."

                    "But if I ever see her again there will be Hell to pay."

                    jump act1_6


        elif activity_choice == "bookstore":

            "No, I can’t be playing games at a time like this. There wasn’t time for the arcade, I skipped it way back when."

            "I went to the [activity_choice], then found my way to the school. I should go there first."

            "Something relevant to my journey has to appear there, I feel it must be true. If not, then I’m sleeping on a bench by the shore tonight."

            jump bookstore2

        elif activity_choice == "school":

            "No, I can’t be playing games at a time like this. There wasn’t time for the arcade, I skipped it way back when."

            "I rushed straight towards the school when we docked."

            "Making my way towards the club might be the best course. The girls could still be there, or they need my help."

            "Whatever is thrown at me can be handled, as long as I stay focused."

            jump school2

        else:

            "No, I can’t be playing games at a time like this. There wasn’t time for the arcade, I skipped it way back when."

            "I went to the [activity_choice], then found my way to the school. I should go there first."

            "Something relevant to my journey has to appear there, I feel it must be true. If not, then I’m sleeping on a bench by the shore tonight."

            jump market2

    label market2:

        define may_talk = 0 # in this scene May could walk MC to the cafe
        $ quick_menu = False
        $ renpy.block_rollback()

        "Maybe the market is around here somewhere? I could use a quick bite to eat."

        $ quick_menu = True

        "It’s about midday, the stands should still be open."

        if activity_choice == "market":

            $ may_talk += 1

            "The market had so many delicious looking options. It was so easy to snag a fruit."

            "A full stomach might bring me closer to whatever Poseidon wants me to do. Gods willing at least."

            show BG black with dissolve
            pause 1.5
            show BG marketpost with dissolve

            "I’m almost positive this is the lot where the market was."

            "This looks like the only place it could be unless it was on a street that slipped my mind."

            "There are scratches and scuffs on the concrete. Coupled with trashed masks dripped on the edges of the sidewalk, I’ll assume there isn’t anything left of the market."

            "Is it not here all the time, or is this COVID’s fault?"

            play effect "audio/stomach.ogg"

            "I’m starting to hurt more and there’s nothing to eat around here. Barren buildings and trashed streets, there’s nothing here to steal."

            "The wind going through the trees carries silence throughout the empty lot."

            "There’s no hum of Seaborough’s town folks around me with little to no people walking around together."

            "It’s like a completely different place than the one I visited."

            "What happened to this town, it was so pleasant the first time I was here?"

            "It could have been my rose tinted glasses from my first full land experience, but clearly it’s gone downhill."

            mc "What am I supposed to do out here Poseidon!"

            $ m = Character('Lady', color="#0A4AF6",  callback=may_voice)

            show m_d with dissolve

            m "Hey excuse me."

            mc "Oh, hello, sorry for screaming. I didn't think anyone was near me."

            m "It’s okay. I’m just wandering around and saw you standing alone."

            m "Could you spare some change for a struggling mother?"

            m "I don’t mean to bother you if you’re having a moment, but I don’t know if my family can eat tonight."

            $ may_position = "nice lady"

            mc "I’m not doing so well food wise myself, sorry. I don’t have anything to spare."

            m "Oh, I’m sorry, my bad. I didn’t know."

            m "Are you sure there’s nothing you could share?"

            mc "Do you have food to trade? Because if not I can’t help you."

            m "Are you really hungry too? You don’t look so hot, are you okay sweetheart?"

            "For a beggar this woman is acting really nice. I shouldn’t be hard on a fellow human down on their luck."

            mc "I’ll be alright, thanks. I don’t mean to come off agitated."

            mc "I’m just super hungry and thought a market would be here."

            m "Doesn’t look like any kind of market is here?"

            mc "Well it was here last time I was here. But that was a long time ago."

            m "Hey don’t worry about it too much kid. What’s your name?"

            "Her tone shifted? She sounds a lot less deprived now."

            mc "My name is [player_name], why do you ask?"

            m "I scrounged up some change and you also look like you’ve had a tough day."

            m "There’s a cafe a few streets over I was planning on going to later. You want to come with me, I can get you a muffin or something cheap."

            mc "That’s really kind of you Miss. That sounds lovely, will they let us in?"

            m "If we got money I think the store won't care at this point. Best not to waste time then [player_name]"

            m "You like coffee?"

            mc "I’ve had it sparingly, but I’ll drink it. What’s your name by the way?"

            $ m = Character('Hanna', color="#0A4AF6",  callback=may_voice)

            m "My name? It’s uhhh, Hanna. You can just call me Hann or whatever."

            mc "I appreciate the help Hann."

            mc "You were right, it’s been a trying day. A coffee and a muffin would hit the spot."

            m "Oh yeah? Wanna talk about it?"

            mc "Hmmmmm. I’m not so sure that’s a good idea."

            mc "A little too personal to say to someone I just met."

            m "That’s fair. I’ll do the same then."

            m "So what do you want to talk about?"

            mc "I’m sorry your kids are struggling. What’re their names or names?"

            m "Their names are um."

            m "I just have one daughter, her name is Barbera."

            mc "Well Hanna, you tell Barbera from me that she has an amazing mom."

            m "Thanks, I will."

            m "You mentioned you weren’t from around here? Or you just got here?"

            mc "Yeah, my uh. My family’s from Cuba on my Father's side."

            m "Where are you from though?"

            mc "I said Cuba."

            m "Yes but where in Cuba?"

            m "Havana, Santa Carla, the Sierra Maestra?"

            mc "Well, I actually spent most of my time in the Bahamas."

            mc "My Father has a…hotel there. I say Cuba because it’s easier."

            if player_identity == "f":

                m "So what’s a rich gal from the Bahamas doing in the Florida slums post pandemic?"

            elif player_identity == "m":

                m "So what’s a rich guy from the Bahamas doing in the Florida slums post pandemic?"

            else:

                m "So what’s a rich guy from the Bahamas doing in the Florida slums post pandemic?"

                mc "Just rich person actually, but um..."

            mc "I’m not entirely here by choice, but I’m hoping to find my next big thing."

            m "Well I doubt it’ll be in this dinky cafe, but I hope you find it soon."

            m "It ain't easy out there for sure. But coffee makes you feel better."

            hide m_d with dissolve

            show BG black with dissolve
            pause 1.5

            show m_d with dissolve

            jump act1_6

        else:

            "No wait, there isn’t time for a snack. It doesn’t matter how hungry I feel."

            if activity_choice == "bookstore":

                "I went to the [activity_choice], then I found my way to the school. I should go there first then get something to eat."

                "If it’s relevant to my journey a sign has to appear, I feel it in my gut next to the hunger."

                "If not, then I’m sleeping on a bench and sucking on leather tonight."

                jump bookstore2

            elif activity_choice == "school":

                "I rushed straight towards the school when I got here. Let's go there first then get something to eat."

                "Making my way towards the club might be the best course. The girls could still be there, or they need my help."

                "Whatever is thrown at me can be handled, as long as I stay focused."

                jump school2

            else:

                "I went to the [activity_choice], then I found my way to the school. I should go there first then get something to eat."

                "If it’s relevant to my journey a sign has to appear, I feel it in my gut next to the hunger."

                "If not, then I’m sleeping on a bench and sucking on leather tonight."

                jump arcade2

label choice_emptystore:

    menu:

        "Engage":

            jump engage

        "Hide":

            jump hiding

        "The book" if tome_choice == 1:

            jump ARG

    label engage:

        hide tome with dissolve
        $ quick_menu = False
        $ renpy.block_rollback()

        "Let’s try to diffuse the situation. Talking my way out of stealing nothing shouldn’t be hard."

        $ quick_menu = True

        mc "Hello, yes you caught me."

        mc "But nothing is happening. Could I just leave now?"

        show m_d with dissolve
        "Revealing myself to the voice, a tall woman is standing in the doorway."

        "She looks exacerbated by something she was doing previously."

        "None of her clothing indicated she is of an authority, but the lighting hides the possibility of a weapon."

        m "There doesn’t seem to be anything here worth taking or am I just late to the party?"

        mc "No, there’s nothing here."

        mc "I visited this store a long time ago and was just sad to see it gone."

        m "I see. So I’m guessing they aren’t hiring?"

        mc "Afraid not."

        m "Well, if there’s nothing here then I don’t know why I’m here."

        m "Wait a second…"

        show m_d at centerleft with moveinleft
        play effect "audio/metalcrash.ogg"
        "The woman moves behind the counter and starts hitting the rusty register with some metal pole."

        mc "What are you doing?"

        m "Checking for some chump change."

        m "If you ain't stealing nothing then I’m gonna try."

        mc "Not that it looks like it’s going to open, but why would they leave any money in there?"

        m "Not looking to win the lottery. But a cup of coffee sounds nice."

        "She raises the pole over her head and smashes the top of the machine with it. From the smile on her face it must have cracked open."

        m "Aaaaaaaaand that’s a buck fifty."

        m "See? You don’t know till you break it."

        mc "You wouldn’t happen to want to split that with me would you?"

        m "And why would I do that?"

        mc "Because I’m an accomplice?"

        m "That’s right, you’re associated with the crime of the century."

        m "Best be paid off before you turn me in for this heinous crime."

        mc "Really? That’d be great!"

        m "Afraid not sweetie."

        hide m_d with dissolve

        mc "What a weird lady. Can’t believe I didn’t check the register myself though."

        mc "That cup of coffee could have been mine."

        "Lost opportunity aside, there doesn’t seem to be a reason to hang around any longer."

        "If that was the authorities I would have had nothing to go off of."

        "It’s time to prioritize food before Posideon’s destiny can grasp me properly. There might be some cheap seafood around the shore somewhere."

        jump act1_6

    label hiding:

        hide tome with dissolve
        $ quick_menu = False
        $ renpy.block_rollback()

        "I should lay low. That was the original plan, right?"

        $ quick_menu = True

        m "{cps=20}Heeeeelloooooooooo?{/cps}"

        m "Unless you weasled your way into a crack in the wall I saw you come in here."

        m "No? Oh well, more for me."

        "Footsteps go along the front of the store but stop by the counter."

        "Everything is silent, did she find m-"

        play effect "audio/metalcrash.ogg" loop

        "What is she doing!?"
        pause 1.5
        stop effect

        m "Ha ha!"

        m "Easy money comes to those with the brains to harness it."

        "The rushed body quickly exits the building without another word."

        "I’m lucky that it was some lunatic instead of a police officer or something."

        "Did she say easy money? Was there cash in here all along?"

        "On the counter there’s a busted metal box I didn’t notice before."

        "That must have been a secret treasure chest of some kind. There could have been thousands in this, it's so large."

        "That woman stole what Poseidon laid out for me to find, damn it all!"

        "I should just leave before I squander another opportunity."

        "It’s time to prioritize food before Posideon’s destiny can grasp me properly. There might be some cheap seafood around the shore somewhere."

        jump act1_6

    label ARG:

        $ quick_menu = False
        $ renpy.block_rollback()

        define tome_title = "KeyError: FileCannotParse"

        "What about that book? Why was this book left behind?"

        $ quick_menu = True

        "Calling it a book might not be appropriate."

        "It’s a dark purple like I’ve never seen before for a cover. Leathery like older books, it’s more like a tome."

        "It’s pages are wrinkly yet it’s as heavy as a cannonball."

        "And there's no title or author on the cover or spine."

        "I can’t date it, how old is this thing?"

        "Should I even open it?"

        menu:

            "Open it":

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "Now I’m too curious. Could this be an ancient Greek tome?"

                $ quick_menu = True

                $ tome_choice -= 1

                hide tome with dissolve
                jump act1_0

            "Leave it":

                $ quick_menu = False
                $ renpy.block_rollback()

                "No, I don’t think so. I have to make sure this voice doesn’t get me in trouble."

                $ quick_menu = True

                "This book is obviously cursed or something awfully evil."

                "Not like reading some ruined old book will get me a meal tonight."

                "Even Poseidon would have picked something more obviously helpful."

                $ tome_choice -= 1

                hide tome with dissolve
                jump choice_emptystore

return
