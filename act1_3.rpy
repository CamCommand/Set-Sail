# Cameron Drummond 2021-2022
# version 1.0.5
label act1_3:

    show BG black with fade
    scene BG school with fade

    play effect "audio/chattering.mp3" volume 2.0 fadeout 2.0
    show crowd with dissolve

    "Found it!"

    if activity_choice == "school":

        "Only wasted a few hours looking for it, thankfully I knew from books that the long yellow cars go to schools."

    else:

        "Those directions got me here no problem, but I knew from books to follow the long yellow cars here."

    "This place is massive, are all schools like this?"

    "The large entrance doors are dwarfed by the humongous stone columns lining the front of the building. People are flooding out and filling the parking lot."

    "Other than narrowly avoiding leaving cars, nobody is looking at me."

    "The letter said someone would meet me outside the school, but there are so many people around. My rendezvous could be anyone."

    "If everyone is leaving the school, I could wait to see who stays. I don't know what the club members will look like though."

    "All sorts of students are leaving. The array of people who go to this school seems vast."

    "One guy looks like a gorilla who’d fit well on a pirate ship."

    "That one kid over there might get blown away by a light breeze."

    "You’d think they’d put them into weight groups so the bigger ones don’t demolish the smaller ones."

    "If everyone is going home it might be easiest to wait out the crowd, see if the writer makes themselves visible."

    "I'll give it a few minutes."

    stop effect fadeout 2.0
    with fade
    hide crowd with dissolve

    "A few of the students and faculty leaving gave me strange looks. Now that I've seen what people my age wear I can't even blame them at this point."

    "I don't think I had anything to change into that wouldn't make me look like a pirate."

    if clothing_check == 1:

        "At least my shirt is clean."

    "If my sense of time wasn't dulled by all these new sensations, about fifteen minutes go by before the clumps of people disperse."

    "There are a few stranglers hanging around and talking. But that one girl standing on the stairs has been shooting me weird looks."

    "She’s the only one still around not doing anything. This couldn’t be who I was waiting for is it?"

    "If the club was expecting the Captain, they sent this girl to greet him?"

    show ast with dissolve

    mc "Uh, hello. You waiting for me lass?"

    show ast sup

    $ a = Character('Girl', color="#c83d32", callback=astrid_voice, who_outlines=[ (1, "#FFFFFF")])

    $ renpy.music.set_volume(0.00, delay=0, channel='music')

    play effect "audio/crash.mp3"

    a "{cps=70}Ahhoooo{/cps}{cps=15}OOOOOOOOOOOO{/cps}{cps=30}oooooy Matey!{/cps}"

    $ renpy.music.set_volume(1.00, delay=0, channel='music')

    $ a = Character('\nOfficer Astrid \n of Bellewood', color="#c83d32", callback=astrid_voice, what_outlines=[ (0, "#000000") ], who_outlines=[ (1, "#FFFFFF")])

    show ast emb with Dissolve(0.1)

    a "{cps=75} I’m Officer Astrid of Bellewood at Seaborough High School!{/cps}"

    a "Welcome To Our School! Permission To Speak Easy Captain, Sir?!"

    show ast happy with Dissolve(0.4)

    "Poseidon help me, this girl she's..."

    $ renpy.block_rollback()

    menu:

        "She’s Enthusiastic":

            $ quick_menu = False
            $ renpy.block_rollback()

            mc "Are you alright? Take it easy lass."

            $ quick_menu = True

            mc "No need to yell at me, Astrid of Bellewood."

            show ast smile with Dissolve(0.1)

            a "Thank you Captain. Bellewood is actually my last name, I just thought it would sound cooler for my intro."

            mc "Can I just call you Astrid?"

            $ a = Character('Astrid', color="#c83d32", callback=astrid_voice, who_outlines=[ (1, "#FFFFFF")])

            a "Aye aye Captain."

            mc "Fine Astrid, you can simply call me [player_name] no need to use titles like that on land."

            show ast happy with Dissolve(0.1)

            a "Aye aye [player_name]!"

            show ast smile

            jump school_entry

        "She’s Amazing":

            $ quick_menu = False
            $ renpy.block_rollback()

            mc "That’s incredible, at ease Astrid of Bellewood."

            $ quick_menu = True

            $ Astrid_affinity += 1
            play effect "audio/good.mp3"

            show ast emb with Dissolve(0.1)

            a "{color=#50A23B}Thank you Captain. Bellewood is actually my last name, I just thought it would sound cooler.{/color}"

            $ a = Character('Astrid', color="#c83d32", callback=astrid_voice, who_outlines=[ (1, "#FFFFFF")]) # remove outline on text

            mc "It sure did. I'm ready to enter if you'd escort me."

            a "Aye aye [player_name]!"

            show ast smile

            jump school_entry

        "She’s Beautiful":

            $ quick_menu = False
            $ renpy.block_rollback()

            "She’s stunning!"

            $ quick_menu = True

            mc "Umm, at ease Astrid of Bellewood."

            $ Astrid_affinity += 3
            play effect "audio/good.mp3"
            show ast emb with Dissolve(0.1)

            a "{color=#50A23B}Thank you Captain. Bellewood is actually my last name, I just thought it would sound cooler said like that.{/color}"

            $ a = Character('Astrid', color="#c83d32", callback=astrid_voice, who_outlines=[ (1, "#FFFFFF")]) # remove outline on text

            mc "I’d agree it does. You can just call me [player_name]."

            show ast happy

            mc "Shall we proceed miss Bellewood?"

            a "Aye aye [player_name]!"

            show ast smile

            jump school_entry

        "{i}Is her brain rotting?{/i}":

            $ quick_menu = False
            $ renpy.block_rollback()

            mc "Have you acquired brian rot sailor?"

            $ quick_menu = True

            $ Astrid_affinity -= 3
            play effect "audio/bad.mp3"
            $ a = Character('Astrid', color="#c83d32", callback=astrid_voice, who_outlines=[ (1, "#FFFFFF")], what_outlines=[ (1, "#000000") ])

            show ast sup with Dissolve(0.1)

            a "{color=#f00}No Captain, Sir!{/color}"

            mc "Then why are you screaming bloody murder at me?"

            show ast emb with Dissolve(0.1)
            $ a = Character('Astrid', color="#c83d32", callback=astrid_voice, who_outlines=[ (1, "#FFFFFF")]) # remove outline on text

            a "To show my respect Captain, Sir!"

            mc "You can just call me [player_name], stop yelling please."

            show ast sad with Dissolve(0.1)

            a "Aye aye Captain [player_name]."

            $ a = Character('Astrid', color="#c83d32", callback=astrid_voice, who_outlines=[ (1, "#FFFFFF")])

            a "You can call me Astrid, Captain [player_name]."

            mc "Nice to meet you lass, thanks for the invitation."

            mc "Drop the title too. Will you escort me inside?"

            a "Aye aye [player_name]!"

            show ast smile

            jump school_entry

    label school_entry:

        a "Welcome to Seaborough high school."

        a "I’m the current president of the Pirate Culture Club here."

        show ast with Dissolve(0.07)

        if clothing_check == 1:

            a "I’ll assume from your breezy shirt and filthy pants you’re a pirate of The Red Plague?"

            "Are my pants filthy?"

        else:

            a "I'll assume from your less than sparkling attire you're from the Red Plague?"

            "Am I that gross looking?"

        "Covertly rubbing my thumb against the side of the leg, a black residue stains comes off on me."

        "Damn me to Davy Jones', I thought these pants were a dark color on purpose."

        "What color were my pants originally"

        mc "Umm, yes, that’s me. I’m the first mate."

        mc "The Captain sent me instead. We are here on important business and he was needed elsewhere."

        show ast sad with Dissolve(0.1)

        a "That makes sense. It was a longshot to try to get the big demon to show up at a high school anyway."

        "The big demon?"

        "That's not a nickname I'm familiar with."

        show ast smile with Dissolve(0.1)

        a "Well [player_name] you seem pretty cool."

        a "Come on inside and meet the rest of the club. They should be almost done setting up."

        "{cps=10}I seem cool!{/cps}"

        "{cps=20}A girl my age thinks I’m cool!{/cps}"

        "Cool is good, I'm almost certain of it."

        mc "That’s cool too, lead the way."

        hide ast smile with dissolve

        stop music fadeout 2.0
        pause 0.5
        scene BG hw with fade
        pause 0.5

        play music track3 volume 0.5 fadein 1.5 fadeout 1.5

        "Astrid is guiding me through a labyrinth of dull hallways."

        "Every corridor looks identical to the last, only a few signs and posters lining the door frames give off any sense of divergency."

        "They’re so eerily empty, as if someone was meant to jump out and scare me."

        "Our footsteps echo off the walls, enhanced by the silence."

        "Aren't there other clubs happening? Where's all the gossip and fights I was expecting?"

        "Did Astrid do something to halt usual activities? She's stopping by one of the closed doors now, could this be a trap?"

        show ast smile with dissolve

        a "This is it, our humble club appointed classroom. It isn't very flashy, so don't expect it to be overflowing with pirate stuff."

        a "Are you ready to meet everyone?"

        $ renpy.block_rollback()

        menu:

            "As ready as I can be":

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "{cps=22}Arrrrrgh{/cps}, you bet Astrid."

                $ quick_menu = True

                show ast smile with Dissolve(0.1)

                a "Definitely give them your best pirate {cps=22}\"arrrr\"{/cps} right away. It’ll solidify you right away as a real pirate."

                jump classrooom_one

            "No wait":

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "Wait, Astrid."

                $ quick_menu = True

                show ast conf with Dissolve(0.1)

                a "Yeah? What’s up?"

                jump classroom_hesitation

        label classroom_hesitation:

            $ renpy.block_rollback()

            menu:

                "Anything I should know?":

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    mc "Anything I should know before going in?"

                    $ quick_menu = True

                    a "{cps=10}Hmmmmmmmmmm.{/cps}"

                    show ast with Dissolve(0.1)

                    a "Don’t expect a big crowd. It’s like, just us on the E-board and a few straggling members who were in there before I went to get you."

                    show ast sad with Dissolve(0.1)

                    a "We advertised that a real pirate would be coming but either nobody believed us or nobody cared. There’s some benefits to being a smaller club, but yeah, not too many."

                    mc "Oh, I’m sorry about that."

                    show ast smile with Dissolve(0.1)

                    a "Don’t be. We aren’t a huge club for more than a few reasons. Most of the pirate stuff is just an excuse for us all to hangout."

                    mc "I understand."

                    a "But we do like pirate things. You’re gonna be great in there, I’m sure of it [player_name]."

                    mc "Thank you Astrid. I’ll put my best foot forward as they say."

                    a "Great, easy enough when you don't have a peg leg."

                    jump classrooom_one

                "Anything I should say?":

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    mc "Anything I should say to them?"

                    $ quick_menu = True

                    show ast smile with Dissolve(0.1)

                    a "Show everyone a good time and some good hardy pirate stories."

                    a "Also they’re probably going to ask you a bunch of questions."

                    a "I’m holding all mine in right now by a thread."

                    show ast emb with Dissolve(0.05)

                    a "{cps=80}Why did I say that outloud?{/cps}"

                    "Her face bloomed brighter than before while she tries not to look at me."

                    "I have no problem answering questions, but if they start getting repetitive I’ll cut them off."

                    mc "I’ll give it the ol’pirate try."

                    show ast conf with Dissolve(0.1)

                    a "Is that a thing?"

                    mc "Not yet, pirates aren’t too keen on learning new lingo."

                    show ast smile with Dissolve(0.1)

                    a "Well maybe you can pick up some new ones here."

                    jump classrooom_one

                "Is this a trap?":

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    mc "Is all this a trap to lure me in and steal my secrets?"

                    $ quick_menu = True

                    a "No, why do you have a lot of them?"

                    mc "Yes, wait no, I mean there is, but no."

                    mc "I can’t tell you everything about my crew or it could jeopardize our safety."

                    show ast smile

                    a "Then just tell us the parts about you if you’re comfortable with that."

                    mc "Alright that could work. But just so you know I can break out of any knot you tie me in."

                    show ast happy with Dissolve(0.1)

                    a "I guess we’ll have to get more creative."

                    jump classrooom_one

        label classrooom_one:

            play effect "audio/doorclose.ogg"
            scene BG cr with fade

            "The door opens to a large classroom with no more than eight people in it."

            "There are some skulls and hearts drawn on the whiteboard next to the club's name, yet the rest of the room has been thoroughly cleaned."

            "Or at least has been kept this clean intentionally. It reminds me of how the ship looked with none of the supplies on it when I left."

            "Everyone perks up when Astrid enters the room."

            show ast at center with dissolve

            a "{cps=80}Everyone! Attention!{/cps}"

            if player_identity == "f":

                a "This is [player_name]. She’s a member of The Red Plague pirate ship that terrorizes the Gulf of Mexico and all its surrounding waters."

            elif player_identity == "m":

                a "This is [player_name]. He’s a member of The Red Plague pirate ship that terrorizes the Gulf of Mexico and all its surrounding waters."

            else:

                a "This is [player_name]. They're a member of The Red Plague pirate ship that terrorizes the Gulf of Mexico and all its surrounding waters."

            a "Why don’t you introduce yourself [player_name]? Say a little about yourself too."

            hide ast with dissolve
            show be at right
            show ge int at center
            show fiona at left
            with dissolve

            mc "Alright, I’m capable of that."

            # check is characters have met yet
            define f_met = 0
            define g_met = 0
            define b_met = 0

            $ renpy.block_rollback()

            menu:

                "Be honest with them":

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    mc "Hello everybody. My name is [player_name], but you already knew that. I’ve been a pirate my whole life and served on The Red Plague during that time."

                    $ quick_menu = True

                    mc "Most days at sea are treacherous and exhausting, but the life is free and can be very rewarding."

                    mc "I had to work my way towards becoming the first mate in that time."

                    mc "However, ranks only come with more responsibility on pirate ships. It doesn’t automatically earn you respect."

                    "Someone is holding their hand above their head all of a sudden. Did I do something wrong? Is this a test?"

                    "If I pause Astrid should get the hint."

                    a "Oh!"

                    a "That’s a high school thing. We raise our hands when we have a question so as to not blurt them out when someone is talking."

                    a "That’s Fiona, she’s our Vice President."

                    hide ge
                    hide be
                    with dissolve
                    show fiona at center with moveinright

                    mc "What’s your question Fiona?"

                    $ f = Character('Fiona', color="#d1c1ff", callback=fiona_voice, who_outlines=[ (1, "#000000")])

                    show fiona sad with Dissolve(0.1)

                    f "Hey, what earns you respect on pirate ships? Do you have to be a big strong man to get it?"

                    "Her tone makes it sound like she already knows the answer. Captain does a similar thing. It's kind of annoying."

                    mc "What earns you respect?"

                    mc "From my experience, it’s feats and age."

                    mc "I feel as if I’ve done some pretty heroic things for the greater crew, but I’m treated like I was kidnapped yesterday."

                    "Well, not by everyone."

                    mc "As for your second concern, our ship has had many prominent women figures throughout its voyage. And I’ve met a handful of retired female Captains in our travels."

                    mc "On the sea, when you’re fighting for everything you got, the only thing that matters is your merit."

                    show fiona with Dissolve(0.1)

                    f "Well that’s a pleasant surprise."

                    mc "Being a pirate is all about how good you are at the job. There have been some amazing pirates who are unbearable to talk to and be around."

                    f "Do you all have swords?"

                    mc "For the most part yes. Some people I know use less conventional tools like sickles and flails."

                    mc "But when the going gets tough, a great pirate tightens their buckle and draws their blade."

                    "The room rings with a  small wave of applause. I’ve never been clapped at before."

                    "That was such a cheesy line too. I might as well have read it off the back of an adventure novel."

                    hide fiona with dissolve

                    $ Fi_affinity += 1
                    $ f_met += 1
                    jump classrooom_two

                "Exaggerate to sound cool":

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    mc "Ahoy everyone! I’m the Dreaded Pirate [player_name]."

                    $ quick_menu = True

                    mc "The Red Plague and I have been ruling the southern seas for over fifty years."

                    mc "I’ve seen the coolest things the world has to offer and I haven’t paid for a single one of them my entire life."

                    mc "We steal exports, we swipe imports, we take minerals, products, people, and sink ships of anyone who offends our noses."

                    mc "Our brutal tactics made us a scourge of the Atlantic."

                    "Some girl in front is raising her arm above her head. Is she calling me out? Does Astrid know what she’s doing?"

                    a "Oh!"

                    a "That’s a high school thing. We raise our hands when we have a question so as to not blurt them out when someone is talking."

                    a "That’s Geraldine, she’s our club’s Secretary."

                    hide fiona
                    hide be
                    with dissolve

                    mc "Aye lass, what’s yer question?"

                    $ g = Character('G', color="#2ef2f4", callback=g_voice, who_outlines=[ (1, "#000000")])

                    show ge smile with Dissolve(0.1)

                    g "Hi [player_name], you can call me G. Love the accent by the way. {cps=30}Question...{/cps}"

                    show ge int with Dissolve(0.1)

                    g "What’s the coolest thing you’ve seen while stealing something? Like anything wackier than the average haul?"

                    "She's calling me out!"

                    mc "Well, let me think on that, {cps=30}Uhhhh...{/cps}"

                    mc "It would have to be that time I saw Poseidon himself perform a miracle."

                    mc "We stole a Mexican vessel’s shipment full of beers and sodas. And their boss begged the Captain on his hands and knees to spare their lives."

                    mc "He offered to share his best whiskey with the Captain to convince him they were worth sparing."

                    mc "The drink was so good, that according to the Demonic Pirate himself, he allowed them to pass his waters."

                    mc "As we were sailing away from the ship a storm started to shake up the waves."

                    mc "I turned towards the ship and one sailor was loading a rocket propelled grenade and aimed it at our tail."

                    show ge smug with Dissolve(0.1)

                    g "Pirates do have RPGs I knew it! You owe me five bucks Be."

                    a "G let [player_name] finish."

                    show ge int with Dissolve(0.1)

                    g "Oh, sorry, go on."

                    mc "Alright, before I could brace for impact, an uncharacteristically powerful wave for that stage of the storm knocked into the Mexican ship."

                    mc "The sailor got knocked over and their ship bursted into multiple explosions."

                    mc "Our lives were saved by His divine decision."

                    g "That sounds so cool. Did the rest of the ship sink?"

                    mc "Whatever was left went straight to Davy Jones."

                    show ge happy with Dissolve(0.1)

                    g "I feel so much better now that I know Poseidon is real. Astrid, did you know that and not tell me?"

                    hide ge happy with moveoutbottom
                    $ G_affinity += 1
                    $ g_met += 1
                    jump classrooom_two

                "Scare them away from piracy":

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    mc "Alright lassies, here’s the dark truth from a subordinate of the Demonic Pirate Ricardo himself."

                    $ quick_menu = True

                    mc "Piracy is incredibly dangerous. Our lives are on the line everyday. We could be shot at, thrown overboard, or starved at sea."

                    mc "Constantly fighting for life and death just for a sliver of profits is a dreary way to live."

                    mc "Our living quarters are dank and grim. I had to burn through skin and bones to get a proper bed when I was younger."

                    mc "Pirates are the worst type of people. They’re remorseless thieves and you’re treated like dirt unless you’re in charge."

                    "Some girl in front is raising her arm up in the air. Is she trying to question me? Does Astrid know what she wants me to do?"

                    a "Oh! That’s a high school thing."

                    a "We raise our hands when we have a question so as to not blurt them out when someone is talking."

                    a "That’s Behati, our club's Treasurer."

                    hide ge
                    hide fiona
                    with dissolve
                    show be at center with moveinleft

                    $ b = Character('Behati', color="#ffcb00", callback=b_voice, who_outlines=[ (1, "#000000")])
                    mc "Aye lass, what’s the problem?"

                    show be emb with Dissolve(0.1)

                    b "Y-yes hello, [player_name]."

                    show be quiz with Dissolve(0.1)

                    b "Isn’t it true that eighty-six to ninety-nine percent of total goods stolen are raw material exports that the government plans to lose in their budgets?"

                    b "Ones that crews are instructed to not fight over and to protect themselves?"

                    b "Wouldn’t that make the act of piracy a part of the system as a whole and not an outlier?"

                    "What is she even talking about?"

                    mc "Do I look like someone who's familiar with your mainland statistics?"

                    show be skeptical with Dissolve(0.1)

                    b "Well y-you can account for your own ship’s actions, r-right?"

                    mc "Aye, well it’s true that American vessels tend to avoid us at all costs, others aren’t so cautious."

                    mc "We don’t steal from just governments. Other pirates and pleasure cruises are prime targets for loot of all kinds."

                    show be quiz with Dissolve(0.1)

                    b "Are t-those unaccounted for in your main piracy focus?"

                    b "B-because how would you know where another pirate ship is going to be?"

                    b "Or if, if some oil millionaire’s kid is going on a joyride?"

                    mc "Behati was it?"

                    show be emb

                    b "Yeah?"

                    mc "Pirates don’t have quotas or missions."

                    mc "We take advantage of opportunities and solve problems we come across with the tools at our disposal. The grand plan is wild riches and being free."

                    mc "No matter the costs."

                    show be with Dissolve(0.1)

                    b "T-thank you for your honesty. That’s a lot to digest, I’ll adjust my later questions accordingly."
                    hide be with dissolve

                    "She looks so relieved just to sit back down."

                    $ Be_affinity += 1
                    $ b_met += 1
                    jump classrooom_two

        label classrooom_two:

            # activity variables for menu
            $ activity_check = 0
            $ food_ate = 0
            $ b_check = 0

            hide ge
            hide fiona
            hide be
            with dissolve
            show ast smile at center with dissolve

            a "That was a pretty good introduction. Thank you [player_name], I think we all learned a little more from that."

            a "Why don’t we eat some of the food that G brought and we can kinda just talk some more. You can spread the culture on us as thick as you want."

            show ast emb

            a "Astrid, phrasing. Come on."

            hide ast emb with dissolve

            "The people not paying attention perked up for the food to rush the table. I expected to monologue more, guess it’s less pressure on me now."

            "Giving speeches is exhausting, no wonder Captain sounds as grizzled as he does. He’s had to speak over the ocean his entire life."

            "Well, his \"speeches\" are more like screaming matches, but still. What should I do now?"

            "Do they want me to socialize and answer more questions?"

            jump classroom_choice

        label classroom_choice:

            define x = 0 # very simple line check
            # keeps track of conversation moments
            define b_convo = 0
            define f_convo = 0
            define g_convo = 0
            define a_convo = 0

            $ renpy.block_rollback()

            menu:

                "Socialize":

                    jump social

                "Get some food" if food_ate == 0:

                    jump food

                "Excuse myself briefly" if b_check == 0:

                    jump washroom

                "Leave" if activity_check >= 2 and g_met >= 1 and b_met >= 1 and f_met >= 1:

                    jump leave

        label social:

            # Leaving menu list of respones
            define leave = ["Maybe not right now.", "Wait a second.", "Not just yet."]
            define rand1 = renpy.random.randint(0, 2)
            define bye = ""

            # for Woman Respecter achievement
            define persistent.woman1 = 0
            define persistent.woman2 = 0
            define persistent.woman3 = 0
            define persistent.woman4 = 0

            # just a check to do an intro line if first time choosing this option
            if x == 0:

                "This is what I wanted to do on land. Talk to people my own age, I should take advantage of this moment."

                $ x += 1

            $ renpy.block_rollback()

            "Who should I talk to?"

            menu:

                "Behati" if b_met >= 1:

                    jump behati

                "Girl with large spectacles" if b_met == 0:

                    jump behati

                "Fiona" if f_met >= 1:
                    jump fiona

                "Taller girl" if f_met == 0:

                    jump fiona

                "G" if g_met >= 1:

                    jump g

                "Pale girl" if g_met == 0:

                    jump g

                "Astrid" if a_convo < 3:

                    jump astrid

                "No wait":

                    $ bye = leave[rand1]
                    "[bye]"
                    jump classroom_choice

        label behati:

            if b_convo == 0:

                if b_met == 0:

                    show be at center with dissolve

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    mc "Hello, it’s nice to meet you young lady. Are you a valued member of the club or just came to see a pirate?"

                    $ quick_menu = True

                    show be emb with Dissolve(0.1)
                    $ b = Character('Girl', color="#ffcb00", callback=b_voice, who_outlines=[ (1, "#000000")])

                    b "Y-yes hi I am. I mean, t-thank you for c-coming t-today."

                    show be emb at wiggle

                    b "It-it, is an honor to h-have the Red-"

                    mc "Are you nervous about something lass?"

                    b "Meeting a real p-pirate is overwhelming. I don’t, well I can’t. No, I-I d-don’t know what say, I-I mean."

                    show be emb at bounce

                    b "Oh my God I forgot to say my name too!"

                    mc "It’s alright, I’m not going to hurt you in any way."

                    mc "Just calm down and listen to the waves-"

                    b "There are no waves!"

                    mc "What I mean is-"

                    $ b = Character('Behati', color="#ffcb00", callback=b_voice, who_outlines=[ (1, "#000000")])

                    b "Behati!"

                    b "That's my name."

                    "I've never seen anyone this nervous about anything."

                    "And I've watched men walk the plank."

                    "Maybe my introduction was too much?"

                    mc "Nice to meet you Behati. Sorry if my introduction gave off a threatening tone."

                    mc "I was just trying to show everyone that being a pirate has its glory but it is very dangerous. Trying to be realistic, you know?"

                    show be shocked

                    b "It’s okay, I’m fine. I just need to breathe."

                    show be with Dissolve(0.1)

                    b "But, you’re not giving the Pirate Culture Club enough credit. We aren’t just a bunch of weebs, we appreciate the life you live. It’s admirable."

                    "The stuttering stopped fast once she got her name out there. She might just not be good at introducing herself?"

                else:

                    show be at center with dissolve

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    mc "Well, what did you think of my opening Behati?"

                    $ quick_menu = True

                    mc "Maybe I said a little too much. It was to show everyone that being a pirate isn’t what you think it might be."

                    b "Hey [player_name]. It wasn't bad at all."

                    b "It was definitely a shock, but you shouldn’t underestimate us."

                    b "We aren’t just a bunch of weebs, we appreciate the life you live. It’s admirable."

                mc "What do you mean?"

                show be emb with Dissolve(0.1)

                b "I mean we all love something about being a pirate that we can’t fully enjoy in our own lives."

                mc "Like what?"

                show be emb at wiggle

                b "I don’t want to speak for anyone else here other than myself. There’s a ninety percent chance they’ll tell you themselves."

                mc "That’s alright, but what about you Behati? What do you think about pirates?"

                show be quiz

                b "{cps=15} M-me? I ummmmmmm. I am.{/cps}"

                b "I’m used to figuring out stuff I like pretty fast."

                b "When I was younger I saw one movie about Somlian pirates and was swept up by everything pirates are."

                show be with Dissolve(0.1)

                b "The open seas, stealing to survive, all the interesting uses of old and new technology."

                b "It’s such a rich history, I’ve been wiki dumping on new pirate stuff almost every month for the past two years."

                mc "What’s a \"wiki dump\"?"

                show be shocked

                b "Oh my God, does your ship not get Wi-Fi? Batteries for a Mi-Fi box even? A single hard drive someone updates?"

                mc "Since those words mean nothing to me, I’ll say no."

                b "Do you know what the internet is at least?"

                mc "I have a vague understanding. It’s like videos and music right?"

                show be skeptical with Dissolve(0.1)

                "Behati’s face seems worried. I should have had a better definition prepared, knowing that the internet is important to people our age."

                b "Well yes but there’s so much more. Movies, music, videos, games, the solar system of information!"

                show be with Dissolve(0.1)

                b "But it also has sites called wikis. It’s like all the information we have on super easy to read pages all linked together."

                b "With pictures and citations and there’s a page for everything. They’re constantly updated so you’re never behind and it's and and the-"

                mc "So like a really long book?"

                show be skeptical with Dissolve(0.1)

                "She exhales loudly into her hands. How long would she have kept going if I didn’t stop her?"

                b "Think the biggest encyclopedia ever."

                mc "That definitely sounds great for everyone."

                show be with Dissolve(0.1)

                b "There’s even a page on The Red Plague. It’s not well documented because a ton of historic pirating is told through legal documents after they’ve been hanged or died."

                b "However, your ship is often recorded as the reason for lost products publicly for some companies. I wonder why there’s only a few?"

                mc "That's so great. It feels wrong, but just true enough to keep the mythos alive."

                mc "Most of our mysticism comes from word of mouth."

                show be quiz with Dissolve(0.1)

                b "Yeah it’s pretty cool, I wish there was more info though."

                mc "Cool. Yes that is cool."

                show be

                b "Heh ha, very cool."

                b "And if you can prove who you are you can edit it yourself."

                mc "I could write a book?"

                show be skeptical with Dissolve(0.1)

                b "Well you can edit your ship’s wiki page, sure. Help fill out the page but keep the details ambiguous so you’re still scary."

                mc "I’ll think of stuff to add and get back to you. Thanks Behati."

                show be emb

                b "No, I can't do anything unless you have public docu-"

                show be with Dissolve(0.1)

                b "Nevermind, if you think of anything let me know."

                $ b_convo += 1
                $ b_met += 1
                $ activity_check += 1
                hide be emb with dissolve
                jump social

            elif b_convo == 1:

                show be at center with dissolve

                $ quick_menu = False
                $ renpy.block_rollback()

                b "Hey [player_name], did you think of anything you wanted to add to your wiki page?"

                $ quick_menu = True

                mc "Yes! Something very cool."

                show be quiz with Dissolve(0.1)

                b "What is it?"

                mc "This great tale on how we ran over a blue whale from the bow of the ship."

                mc "The heroics of harvesting the resources, risking our own lives. The whole crew pitched in this once and a lifetime-"

                show be skeptical with Dissolve(0.1)

                b "{cps=15}Ummmmm. But, that’s not.{/cps}"

                mc "What you don’t think it’s true?"

                b "No it’s just that, this isn’t a book."

                show be with Dissolve(0.1)

                b "Wikis are supposed to be informational. They aren’t the place for hearsay stories or non-informative tales."

                mc "Alright, even though this is entirely an informative tale, I know what you mean."

                "That's really disappointing. I thought I could get a scribe to tell our tales for free. Most scribes aren’t worth the ink they charge for."

                show be quiz

                b "Something like, how many pirates are on the ship?"

                mc "I’d never reveal that information. But also I don’t know and it’s always changing anyway."

                b "Do you have any siblings onboard? Maybe like a special pirate task force for important battles?"

                mc "What are you talking about?"

                show be emb

                b "Okay so some of us are also weebs, don’t worry about it."

                b "Both my brothers left for college last year, so I’ve been able to use the big T.V. after school for anime."

                b "It's on my mind is all. Everything is on my mind. Why did I bring up anime to a real pirate?"

                "What is she trying to say? I think the whale story may have thrown her off?"

                "I can still steer the conversation away from the awkward wiki misunderstanding."

                mc "Your brothers are seeking higher education? That’s interesting, do you want to do the same?"

                show be with Dissolve(0.1)

                b "Yeah, I want to do the same."

                b "Jack and Tye both went to New York to study business, but I think I’ll stay in state. Try to become a teacher."

                show be quiz with Dissolve(0.1)

                b "Not sure what kind of teacher yet, so many subjects interest me. It’s not like I could choose the curriculum myself. That part sucks."

                mc "There are lots of illiterate pirates, if you want you could teach language on a pirate ship. Plenty of ships would pay for less stupid help."

                show be shocked with Dissolve(0.1)

                b "Oh my, being on a pirate ship sounds overwhelming. I’d want to do so much learning myself. I’ve never even shot a gun before."

                mc "Do you want to?"

                show be emb

                b "Really badly yes. Is that weird?"

                show be quiz with Dissolve(0.1)

                b "I’ve read so much about older and new pistols. The mechanisms are so fascinating to me."

                mc "Is there lots you gravitate towards about the pirate culture?"

                show be with Dissolve(0.1)

                b "The club has been a big influence on me, but yeah, it all seems so cool."

                b "If I could teach a pirate class I would. But the school would have to let me bring in firearms."

                mc "Ha hahaha! Be sure they aren’t loaded at least."

                show be skeptical with Dissolve(0.1)

                b "No way, I’m firing it. I read that old flintlocks make sounds louder than desert eagles but have less kickback. I have to know if that’s true."

                mc "I can confirm they are very loud."

                show be quiz with Dissolve(0.1)

                b "Something might be louder actually. Wait, I have to look this up."

                show be quiz at sitting with ease

                "Behati pulls out her device I’ve seen her look at before and begins tapping furiously. It seems like I’ve lost her to the wikis."

                $ b_convo += 1
                hide be quiz with dissolve
                jump social

            elif b_convo == 2:

                show be quiz at sitting with dissolve

                $ quick_menu = False
                $ renpy.block_rollback()

                "Behati is vigorously reading her device. I don’t know if she could hear me even if I tried."

                $ quick_menu = True

                if book_choice == "smart":

                    show be quiz at center with ease

                    b "Hey [player_name]. What’s sticking in your waistband? Is that a book or something?"

                    "How did she notice? She didn’t even glance at me, seemingly."

                    mc "Yes, it’s a book. I grabbed this book from a store after I got off the ship. Thought it could be an interesting read."

                    show be shocked with Dissolve(0.1)

                    b "Oh! It’s a Gail Mcryson book!"

                    b "Her books are all super interesting. I have a bunch stacked up under my bed I got for my birthday. You’re interested in space?"

                    mc "Well, I’m not entirely sure yet. This could be the deciding factor."

                    show be with Dissolve(0.1)

                    b "Then I think you’re gonna become obsessed like me after reading it."

                    show be emb with Dissolve(0.1)

                    "She’s clearly passionate about her interests but I can tell she's not the most prideful of them."

                    "All I learn out at sea is how to be a pirate. Here is where I think the most knowledge lies."

                    mc "You don't have to be embarrassed about what you like."

                    mc "I'm the only pirate onboard who likes to read. I get where you're coming from."

                    show be happy with Dissolve(0.1)

                    b "Maybe we'll talk later? Kay?"

                    mc "Alright, sure thing Behati."

                    show be skeptical

                    b "I got some more homework to work on. But thank you."

                    hide be skeptical with dissolve

                    $ book_choice = "used" # just to know when the variable is used
                    $ b_convo += 1
                    $ Be_affinity += 1
                    $ activity_check += 1
                    jump social

                else:

                    show be quiz at center with ease

                    b "I’m checking online if I could reasonably get an old timey gun."

                    mc "That’s cool. Need my advice?"

                    b "I mean. I don’t know what would work or be better if I could get one."

                    show be shocked with Dissolve(0.1)

                    b "But it looks like they are all really expensive and I’m not sure yet how legal it would be for a minor to own one."

                    mc "That’s unfortunate."

                    mc "To make the process cheaper, you should look for a gun that takes bullets."

                    mc "Straight gunpowder guns are a pain and finding raw materials for them is borderline impossible."

                    "Or at least that's what I'm told."

                    show be happy with Dissolve(0.1)

                    b "Thanks, that’s good advice."

                    b "Would you show me how to use one?"

                    mc "Why not?"

                    "Probably won't ever be around here again."

                    show be with dissolve

                    b "Thanks for the hollow agreement. I know you need to uphold the mission once you leave today."

                    mc "And what mission is that?"

                    b "You tell me when you figure that out."

                    b "Maybe we'll talk later? Kay? I got some homework I need to make up."

                    mc "Alright, sure thing Behati. I'll leave you to it."

                    "What is my mission after all this?"

                    hide be with dissolve
                    $ b_convo += 1
                    $ Be_affinity += 1
                    $ activity_check += 1
                    jump social

            else:

                show be quiz at sitting with dissolve

                $ quick_menu = False
                $ renpy.block_rollback()

                "Behati is vigorously reading her device and checking her papers."

                $ quick_menu = True

                "I don’t know if she could hear me even if I tried, she's so focused."

                "Wonder if I should get one of those things if they’re as cool as she says."

                if persistent.woman1 == 0:

                    $ persistent.woman1 += 1

                if persistent.woman1 == 1 and persistent.woman2 == 1 and persistent.woman3 == 1 and persistent.woman4 == 1:

                    $ achievement.grant("Woman Respecter")
                    $ achievement.sync()

                hide be quiz with dissolve
                jump social

        label fiona:

            show fiona sad at center with dissolve

            if f_convo == 0:

                if f_met == 0:

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    mc "Hey, what's happening, cool club member?"

                    $ quick_menu = True

                    "Who just said that?"

                    $ f = Character('Tall Girl', color="#d1c1ff", callback=fiona_voice, who_outlines=[ (1, "#000000")])

                    show fiona angry with Dissolve(0.1)

                    f "You wanna try that again, matey?"

                    mc "{cps=20}Ugh, ummmmmmmm, I uhm.{/cps} Hello, I’m [player_name], sorry. How are you today?"

                    $ f = Character('Fiona', color="#d1c1ff", callback=fiona_voice, who_outlines=[ (1, "#000000")])

                    show fiona with Dissolve(0.1)

                    f "That’s better. I’m Fiona."

                    f "You don’t have to try so hard to talk to us. You’re a fearsome pirate not a high schooler."

                    mc "But I’m talking to high schoolers, not other pirates? How would you want one of your friends to greet you?"

                    show fiona laugh

                    f "Sup cock sucker, what’s goin’ on?"

                    show fiona

                    f "Then I’d say \"who’s cock?\" and we’d all laugh and just move on with the conversation."

                    mc "{cps=20}Uuuuuuuh. I uh, don’t know how I’d.{/cps}"

                    show fiona laugh

                    f "I’m joking dude relax. Tell me a pirating thing."

                    show fiona with Dissolve(0.1)

                    mc "Umm, let me think..."

                    mc "Most pirating rule breakers get marooned, but sometimes we will also tie someone to the side of the boat and pull them from the other side."

                    mc "The barnacles under the ship tearing their skin off, killing them slowly. You’d be lucky to drown."

                    f "Okay first, very metal. Second, next time just say \"Hey what’s up?\"."

                    $ f_met += 1

                else:

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    mc "Hello Fiona, what are you up to?"

                    $ quick_menu = True

                    show fiona sad with Dissolve(0.1)

                    f "Just texting my cock sucking friend, tell me a pirating thing I can share with them."

                    mc "Is that a good thing to call your friend?"

                    f "Sometimes, it is for me. You don't call other pirates that?"

                    mc "I'd be risking my life if I did."

                    f "So what's a big scary thing you guys do?"

                    mc "Um, let me think..."

                    mc "Did you know most pirating rule breakers get marooned, but sometimes we will also tie someone to the side of the boat and pull them from the other side."

                    mc "The barnacles under the ship tearing their skin off, killing them slowly. You’d be lucky to drown."

                    show fiona with Dissolve(0.1)

                    f "Okay first, very metal. Second, I can't text them that."

                "I’m having a hard time getting a read on Fiona. In a way she’s a lot like other female pirates I’ve met, but something is...funny about her."

                mc "Alright, next time I’ll be more relaxed about it."

                f "No I mean like that was really hardcore. So what's your favorite part about being a pirate?"

                mc "My favorite part?"

                mc "I’d say it has to be the freedom. I don’t know any other lifestyle, but I feel the most like myself out at sea."

                f "Feel most like yourself huh?"

                show fiona frown with Dissolve(0.1)

                f "That sounds really nice, on land we don’t always get that luxury. We have to fight tooth and nail just to do the simple stuff."

                "Fiona’s gaze rolls around the room. I think I'm getting the sense on why being a pirate is so appealing to her."

                "Everything is about your merit, nobody is treated wrong based on stuff that doesn't matter if they can do the work. It's a true sense of freedom when everybody respects yours."

                mc "Hey Fiona."

                show fiona sad with Dissolve(0.3)

                f "Yup?"

                mc "The most important thing you can do is find where you are most comfortable and be yourself."

                mc "All I know is pirating, but if it made me feel bad and unappreciated, then it’d be time for a change. You know what I mean?"

                show fiona with Dissolve(0.1)

                f "Yeah, I get it. I appreciate that sentiment."

                f "I don’t have a ton of options though. Just sort of hold out till college."

                mc "Is college a good place for that?"

                f "That’s what I’ve been told at least."

                f "But I don’t mean to sound too down about it. I have good friends here. Astrid and I are gonna try getting into the same school."

                mc "That sounds great Fiona. I hope it all works out. I wish you a bountiful haul in your future."

                show fiona laugh with Dissolve(0.2)

                f "Ha ha. Aye aye Captain."

                $ f_convo += 1
                $ activity_check += 1
                hide fiona laugh with dissolve
                jump social

            elif f_convo == 1:

                $ quick_menu = False
                $ renpy.block_rollback()

                f "What’s the magic words?"

                $ quick_menu = True

                mc "What’s up...?"

                show fiona laugh with Dissolve(0.2)

                f "What's up cock sucker!"

                mc "What's up cock sucker?"

                f "I don’t don’t know, depends on who’s cock?"

                mc "That is a pretty fun introduction, even if it makes me uneasy."

                show fiona with Dissolve(0.1)

                f "I know, right? I’m gonna normalize it as much as I can. Try to use it in a movie to get it to stick."

                mc "I’d have to find a way to watch it then."

                if book_choice == "nerdy":

                    show fiona sad with Dissolve(0.1)

                    f "Did you steal a book from us?"

                    mc "What? No! You mean this thing?"

                    mc "I got this from a book store. It looked interesting, thought I’d read it later."

                    show fiona with Dissolve(0.1)

                    f "Rune is pretty good."

                    f "They’re always saying they’re gonna make a movie based on it but haven’t yet. If you stick with it I think you’d like it."

                    mc "I read a little bit, not sure if it’s something that will stick with me."

                    f "Well there’s lots of moving parts in the series and the light dark fantasy elements are super enticing. I don’t even read that much and I liked it."

                    mc "Isn’t light dark fantasy a contradiction?"

                    show fiona angry

                    f "No, light as in not as heavy and dark as in, well it can be dark but it’s not too dark."

                    f "They aren’t throwing dead babies at each other and saying the n-word but the themes are serious."

                    mc "Okay that sounds cool. I’ll give it a chance."

                    show fiona with Dissolve(0.1)

                    f "How nice of you to not immediately dismiss literary genius. Are all pirates as gracious as you?"

                    mc "I’ve only known a few pirates who were brave enough to hold a book."

                    f "It’s not like everyone our age is buried in a book."

                    show fiona frown with Dissolve(0.1)

                    f "The disdain some of us have for reading makes me super comfortable. G said she didn’t finish a single novel until she was fourteen."

                    mc "Really? Aren’t you required to read in school?"

                    show fiona

                    f "Yes! Yes we are supposed to read to get past the first grade!"

                    show ge at left with slide

                    g "Reading is boring. Do cooler things like skateboarding and drugs."

                    hide ge with moveoutleft

                    f "She’s insane. Watching her pay attention in class is like watching the five stages of grief in fifty-two minutes."

                    $ f_convo += 1
                    $ Fi_affinity += 1
                    $ book_choice = "used"

                f "Do you get time to watch any movies or read at all?"

                mc "I know what a movie is, but have never seen one. When my work is done for the day I find reading eases me into a comfortable mindset."

                f "You get to read what you want at least?"

                mc "There’s nobody censoring my library, why would anyone do that?"

                show fiona frown with Dissolve(0.1)

                f "In school, there’s a thick list of books we aren’t allowed to read."

                mc "Because they’re bad?"

                show fiona laugh with Dissolve(0.2)

                f "Ha, yeah some, but no."

                show fiona angry with Dissolve(0.1)

                if badwords == True:

                    f "Most of them are {b}dumb{/b} political pandering and some are seen as history that contradicts the propaganda they feed us here."

                else:

                    f "Most of them are bullshit political pandering and some are seen as history that contradicts the propaganda they feed us here."

                f "I just stick to online stuff mostly. Big open sea of reading there."

                mc "You should read what you want to read Fiona, don’t let anyone stop you."

                show fiona

                f "Spoken like a true pirate, I expected nothing less."

                f "We’ve come further in the past decade with multicultural and sexually diverse reading topics, but this isn’t a great place to live as far as cutting edge comes."

                if badwords == True:
                    f "Some of these {b}frickin{/b} meatheads will just {b}poop{/b} on you for no reason other than you’re different."
                else:
                    f "Some of these fucking meatheads will just shit on you for no reason other than you’re different."

                show fiona sad with Dissolve(0.1)

                f "It’s exhausting to be around these people. Not in the club at least."

                mc "At least pirating and by association, this club, are very accepting. The sheer amount of violence you experience as a pirate is daunting."

                mc "If you focus on it, life is bleak. Highlighting the good parts in your head really shifts your mood."

                show fiona sad at wiggle

                f "Yeeeeaaaaah. For the last thread of my mental health's sake, that sounds like the healthy thing to do."

                show fiona with Dissolve(0.1)

                f "Thanks [player_name], you didn’t need to talk me down there. Your chill tone was helpful."

                f "Sometimes Astrid will argue with me or Behati will nervously talk me out of it. But I usually just need someone to hear me."

                mc "Not a problem. You have the mentality of an aged pirate, I do that sometimes for the new crew members."

                $ f_convo += 1
                hide fiona with dissolve
                jump social

            elif f_convo == 2:

                $ quick_menu = False
                $ renpy.block_rollback()

                f "What's the magic intro?"

                $ quick_menu = True

                mc "What’s up cock sucker?"

                show fiona laugh with Dissolve(0.2)

                f "I don’t know, depends on who’s cock?"

                show fiona

                f "People will start to talk if we keep meeting like this."

                "There’s like six people in this room, I don’t know what she means. What would Astrid say?"

                mc "Will people spread bad rumors? I think my reputation in Seaborough will survive."

                f "It could happen. If Astrid wasn’t so pretty and popular she might have been a social outcast by now."

                f "She basically runs this club in secret. A hush hush sort of deal."

                mc "I understand, it's an incognito type situation. As long as the Captain won’t punish you for it, I get it."

                show fiona angry with Dissolve(0.1)

                f "I don’t think the principal cares what the students do if it doesn’t break the bylaws, but we are an officially sanctioned club. We got the whole package."

                f "A faculty supervisor that doesn’t come to school any more, at least three members, and an E-board. Enough to schedule meetings and have the room to ourselves."

                mc "A pirate ship really only needs a Captain and people to make the vessel sail."

                show fiona sad with Dissolve(0.1)

                f "How many people does it take to make a ship go?"

                mc "Four to five as a rough minimum. Depends how capable the crew is."

                show fiona

                f "I’ll start assembling the sailors. See you on the high seas, we'll be the best dressed pirates."

                mc "I’ll keep my eye out for you, Fearsome Pirate Fiona."

                f "I need to think of a ship name. Something to scare the people I want to scare. How about…"

                f "The Queer Steer!"

                mc "What about the…"

                mc "Nude Spear of God!"

                show fiona laugh with Dissolve(0.2)

                f "Where did that come from?"

                f "That is so perfectly extra, I love it."

                f "Hehe, thanks for humoring me matey."

                "Where did that come from?"

                mc "Sure thing cock sucker."

                hide fiona laugh with dissolve

                $ f_convo += 1
                $ activity_check += 1
                $ Fi_affinity += 1
                jump social

            else:

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "Hey cock sucker."

                $ quick_menu = True

                show fiona sad with Dissolve(0.1)

                f "Hey matey. I know I said to be more relaxed when saying hi, but you gotta mix it up too."

                mc "If you think you’re tired of sex jokes you’re the one who has to let me know."

                f "Very true. I’ll be hung before that happens."

                mc "See you at the gallows then."

                show fiona with Dissolve(0.1)

                if persistent.woman2 == 0:

                    $ persistent.woman2 += 1

                if persistent.woman1 == 1 and persistent.woman2 == 1 and persistent.woman3 == 1 and persistent.woman4 == 1:

                    $ achievement.grant("Woman Respecter")
                    $ achievement.sync()

                hide fiona with dissolve
                jump social

        label g:

            show ge at center with dissolve

            if g_convo == 0:

                $ quick_menu = False
                $ renpy.block_rollback()

                if g_met == 0:

                    mc "How are you today lass?"

                    $ quick_menu = True

                    $ g = Character('Pale Girl', color="#2ef2f4", callback=g_voice, who_outlines=[ (1, "#000000")])

                    show ge happy with Dissolve(0.1)

                    g "Awful, I failed a math exam today."

                    mc "Oh, will you be flogged for your failure?"

                    show ge smile with Dissolve(0.1)

                    g "Nah man, I’ll just shove the test under my bed with the rest of them."

                    mc "You can simply hide your failures like that?"

                    show ge with Dissolve(0.1)

                    g "For sure, they won’t catch up to me that fast. And when they do I’ll figure it out."

                    $ g = Character('Geraldine', color="#2ef2f4", callback=g_voice, who_outlines=[ (1, "#000000")])

                    g "Behati helps me cram when it gets serious. I’m Geraldine by the way."

                    $ g = Character('G', color="#2ef2f4", callback=g_voice, who_outlines=[ (1, "#000000")])

                    g "I don’t know if you heard anyone say my name or not. But my friends call me G."

                    mc "Why only one letter?"

                    show ge happy with Dissolve(0.1)

                    g "It’s quicker and doesn’t make me sound like some heiress to an embroidered pillow fortune."

                    mc "Your name is what you make it, not what is expected of it."

                    show ge smile with Dissolve(0.1)

                    g "Now that’s some pirate wisdom for yeah. Tell me more pirate stuff."

                    $ g_met += 1

                else:

                    $ g = Character('G', color="#2ef2f4", callback=g_voice, who_outlines=[ (1, "#000000")])

                    mc "Hello again G. How are you?"

                    $ quick_menu = True

                    show ge happy with Dissolve(0.1)

                    g "I failed a freaking math test today. Very unepic of me."

                    mc "Oh, will you be flogged for your failure?"

                    g "Nah man, I’ll just shove it under my bed with the rest of them."

                    mc "You can simply hide your failures like that?"

                    show ge with Dissolve(0.1)

                    g "For sure, they won’t catch up to me that fast. And when they do I’ll figure it out."

                    show ge smile with Dissolve(0.1)

                    g "Behati helps me cram. She’s good like that."

                    mc "You shouldn’t rely on others to bail you out of your mistakes, making improvements will show that you're worthy to help."

                    show ge mad with Dissolve(0.2)

                    g "That’s some pirate bull right there. I can win anyone over with my perfect charm."

                    show ge smile

                    g "Tell me some cool pirate stuff."

                "Pirate stuff? Could she be more vague? She’s been smiling a lot, maybe tell a funny story."

                mc "So it’s against pirate code to coerce your preferred gender onto the ship. It won’t get you killed, but you’ll be punished harshly."

                show ge with Dissolve(0.1)

                g "Oh yeah?"

                mc "One time these two new pirates, both really burly looking guys were sneaking some prostitutes onboard and the Captain and I caught them red handed."

                g "Uh oh, tough luck for them."

                mc "Here's what happened next. We still have to officially accuse them of the code violation, even if it’s obvious."

                mc "So when we did that they denied the crime and claimed they were kicking them off. The story was that they were stowaways."

                show ge int with Dissolve(0.1)

                g "Really? That’s what they went with?"

                mc "We weren’t buying it and the Captain was getting increasingly upset at them. Our growing skepticism could only be squashed by one thing."

                mc "To prove that they didn’t care about the woman, that way, they slowly brought their faces closer."

                show ge int at bounce

                if badwords == True:

                    g "No {b}Gosh Darn Diddly{/b} Way!"

                else:

                    g "No Fucking Way!"

                mc "Yeah, it was slow, painful, and super weird to watch. They clearly weren’t into it while they're going at it."

                mc "The Captain kept staring them down so it lasted almost two minutes. But it felt like two hours just watching them."

                show ge happy with Dissolve(0.1)

                g "That is so unbelievably funny!"

                mc "They proved themselves enough so we let them get away with it. From then on they avoided each other as much as possible."

                mc "Even to the point of eating their meals on different decks."

                mc "Although, strangely they both left the crew at the same time."

                g "I smell a best selling pirate romance novel in the works."

                show ge smile with Dissolve(0.1)

                g "I’m a big fan of just the raunchiest gay fanfics I can find."

                mc "Is that a popular genre on land?"

                g "Let’s just say there are plenty of options to wet your palette with. I’ll text you some links later."

                mc "Alright, I’ll text you too G."

                $ g_convo += 1
                $ activity_check += 1
                hide ge with dissolve

                "What does \"text\" mean?"

                jump social

            elif g_convo == 1:

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "Hello again Geraldine."

                $ quick_menu = True
                show ge sad with Dissolve(0.1)

                mc "Oh, my bad sorry."

                mc "Hello again G."

                show ge smile with Dissolve(0.1)

                g "What’s the haps pirate pal?"

                mc "Everyone here is super nice. I’ve been told pirates were treated poorly in normal society. Is high school different?"

                show ge sad with Dissolve(0.1)

                g "It's a high school man, what the heck were you actually expecting?"

                show ge smile with Dissolve(0.1)

                if badwords == True:
                    g "This club isn't the norm. We try to keep this place a sanctuary from the vitriol that students spew, but {b}things{/b} happen."
                else:
                    g "This club isn't the norm. We try to keep this place a sanctuary from the vitriol that students spew, but shit happen."

                show ge mad

                g "The Spanish club is always testing my patience."

                if book_choice == "funny":

                    show ge int with Dissolve(0.1)

                    g "Whatcha got there?"

                    mc "Oh this? I found this book on the street and thought I’d keep it for novelty purposes."

                    show ge smug with Dissolve(0.1)

                    g "Right on the street. And my phone fell off the back of a truck."

                    show ge happy at wiggle with Dissolve(0.1)

                    g "Oh my God!"

                    show ge smile

                    g "A Pirate carrying around a pirate joke book? Now that’s the start of a bad joke."

                    if player_identity == "m":

                        g "Which you seem loaded with there big guy."

                    else:

                        g "Which you seem loaded with dude."

                    mc "Yeah that is sort of funny. You want to hear some terrible pirate jokes?"

                    g "Hit me."

                    play effect "audio/pages.wav"

                    mc "\"Why is pirating so addictive?\""

                    show ge int with Dissolve(0.1)

                    g "The free oppium?"

                    mc "No, that stuff’s expensive."

                    mc "\"When you lose your first hand, you get hooked!\""

                    show ge happy with Dissolve(0.1)

                    g "That was wonderfully cringe, my body will nourish that for years to come."

                    show ge int

                    g "Do pirates actually use hook hands?"

                    mc "Some do, most who lose hands get a hook. They’ve come a long way now. Most are equipped with extra features like blades and spoons."

                    g "Blades and spoons, that’s an entire arsenal right there."

                    mc "Exactly."

                    play effect "audio/pages.wav"
                    mc "Can you explain this one to me? I don't get it."

                    show ge smile with Dissolve(0.1)

                    g "Yeah sure what’s it say?"

                    mc "\"How does a pirate call his mate? On his aye phone.\""

                    mc "If my phonics are correct then I don’t know what an {i}I Phone{/i} is?"

                    show ge happy with Dissolve(0.1)

                    "G snickers behind her hands and pulls one of the screen devices everyone has from her pocket."

                    show ge smile with Dissolve(0.1)

                    g "Phones are what these are. Everyone has one. This specific brand is called an iPhone."

                    mc "So this pirate joke wasn’t actually aimed at pirates then?"

                    g "Well I don’t see why they would do that. You’d just steal them, they’d make no money."

                    mc "A fair point, still feels silly."

                    g "Best not to think about a joke book too seriously. Or else you’ll miss the punchline."

                    # arm punch
                    show ge smile with ease:
                        xpos 0.53
                    show ge smile with ease:
                        xpos 0.5

                    "She digs into my arm with a swift jab then grabs her iPhone."

                    show ge

                    g "One second, I got to respond to this."

                    $ G_affinity += 1

                else:

                    mc "Is it really bad here?"

                    show ge with Dissolve(0.1)

                    g "I’m sure it’s not as violent as a pirate ship. But you have a choice at least."

                    show ge sad with Dissolve(0.1)

                    g "We’re forced to come to school."

                    "She thinks I have a choice. After eighteen years I’ve only been given permission to prace around the mainland without a care."

                    "Leaving on my own accord would have been a death sentence. It might be the same here, should I ask?"

                    mc "Can’t be all bad. You can choose your friends, go home at the end of the day, weekends off sounds nice?"

                    show ge int with Dissolve(0.1)

                    g "Do you not get weekends?"

                    mc "I didn’t know what the days of the week were until I was ten. Doesn’t matter too much at sea when there’s work that needs to be done."

                    g "Do you have any spare time?"

                    mc "Oh yeah, pirates hate doing work. There’s just so much work to be done we have to finish or we all die."

                    show ge

                    mc "But when that’s done you can do whatever you want."

                    mc "Enjoy your hobbies, casual conversation, anything you want really within Code."

                    show ge int with Dissolve(0.1)

                    g "The Pirate Code?"

                    mc "Yes, that exact one. We all have to follow it or nothing gets done and piracy becomes chaos."

                    show ge sad with Dissolve(0.1)

                    g "Must be nice. My parents force me to work in their deli after I’m done with school work."

                    g "I barely have time for anything. The club’s a small reprieve from all that, but still."

                    "That sounds really sad. Admiring the pirate life because yours is without freedom."

                    "A pirate culture club isn't the worst form of escapism that exists. What would Astrid think is a good thing to say at a time like this?"

                    mc "{cps=25}Arrrrrrgggggh.{/cps} Well aye hope aye made teday salty enough for ye lass."

                    show ge happy with Dissolve(0.1)

                    g "Haha. Yeah this was fun, I appreciate you coming aboard matey."

                    show ge smile

                    g "I thought \"aye\" meant yes though?"

                    mc "It does, but it sounds nice to say, right?"

                    # arm punch
                    show ge smile with ease:
                        xpos 0.53
                    show ge smile with ease:
                        xpos 0.5

                    "She digs into my arm with a swift jab then grabs her handheld device."

                    show ge

                    g "One second, I got to respond to this."

                $ g_convo += 1
                hide ge with dissolve
                jump social

            elif g_convo == 2:

                $ quick_menu = False
                $ renpy.block_rollback()

                # for Gamer Achievement
                define persistent.game4_count = 0

                mc "What’s going on G?"

                $ quick_menu = True

                g "Oh, I got a notification for a game I was playing. Have to do the dailys or else the anxiety kicks in."

                if game_played != "":

                    mc "Sounds cool. I played my first video games today before coming here."

                    show ge int with Dissolve(0.1)

                    g "Oh yeah? What did you play?"

                    mc "I played the [game_played] game."

                    g "Damn that’s retro. Did you go to that arcade by the harbor?"

                    mc "Yes I did, why? Is that bad?"

                    show ge smug with Dissolve(0.1)

                    g "Not explicitly, I can’t believe that was your first experience."

                    show ge smile with ease:
                        ypos 1.05

                    g "Here, wait one second."

                    play effect "audio/rummage2.mp3"

                    "G pulls out her backpack and rummages around for a few seconds. She pulls out another device with two screens instead of one."

                    show ge smug with ease:
                        ypos 1.00

                    if badwords == True:
                        g "Let me run you a classic game that hasn’t aged like {b}raw meat{/b}."
                    else:
                        g "Let me run you a classic game that hasn’t aged like dogshit."

                    mc "What’s it called?"

                    g "Don’t worry about it, just follow the onscreen directions and play for a couple of minutes."

                    mc "Aye, sure thing."

                    show ge int with Dissolve(0.1)

                    g "You don’t say aye aye?"

                    mc "I said yes already, why would I say it twice?"

                    show ge smile

                    g "For historical accuracy."

                    mc "Not sure that’s right."

                    show ds at ds_slide
                    pause 1.5
                    play effect "audio/laser1.wav"

                    "The font of the title is too weird for me to make it out. However, the game is really fun."

                    play effect "audio/laser1.wav"
                    queue effect "audio/laser1.wav"

                    "I’m a little jet flying and spinning around the sky shooting shapes."

                    play effect "audio/laser2.wav"
                    queue effect "audio/laser1.wav"
                    "There’s little animals yelling at me to do better but this is my first time so I don’t know why they are yelling at me?"

                    play effect "audio/laser2.wav"
                    queue effect "audio/laser2.wav"
                    "I keep getting shot from behind by enemies I miss."

                    play effect "audio/laser2.wav"
                    queue effect "audio/laser2.wav"
                    queue effect "audio/laser2.wav"
                    "It's fun for a few minutes, but after I died three times I had to hand the device back to G."

                    hide ds with moveoutbottom

                    if persistent.game4_count == 0:

                        $ persistent.game4_count = 1
                        $ persistent.game_count += 1
                        #$ achievement.progress("G A M E R", persistent.game_count)

                    if persistent.game_count == 4:

                        $ achievement.grant("G A M E R")
                        $ achievement.sync()

                    mc "That was fun, I think I’m really starting to like video games."

                    show ge happy with Dissolve(0.1)

                    g "Of course you are. You’re one of us now."

                    mc "What do you mean?"

                    g "{cps=40}One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us.{/cps}"

                    "Her repetition gets slower and hands grow closer to my face."

                    "After backing away slowly she stopped and laughed to herself for a good second."

                    $ g_convo += 1
                    hide ge happy with dissolve
                    jump social

                else:

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    show ge int

                    g "You ever played a video game before?"

                    $ quick_menu = True

                    mc "No, never. I’ve heard of them, but never had a chance to."

                    show ge smile with Dissolve(0.1)

                    g "Well this is a good chance. I can’t believe I get to coordinate your first experience."

                    show ge smile with ease:
                        ypos 1.05

                    g "Here, wait one second."

                    play effect "audio/rummage2.mp3"

                    "G pulls out her backpack and rummages around for a few seconds. She pulls out another device with two screens instead of one."

                    show ge smug with ease:
                        ypos 1.00

                    if badwords == True:
                        g "Let me run you a classic game that hasn’t aged like {b}raw meat{/b}."
                    else:
                        g "Let me run you a classic game that hasn’t aged like dogshit."

                    mc "What’s it called?"

                    g "Don’t worry about it, just follow the onscreen directions and play for a couple of minutes."

                    mc "Aye, sure thing."

                    show ge int with Dissolve(0.1)

                    g "You don’t say aye aye?"

                    mc "I said yes already, why would I say it twice?"

                    show ge smile

                    g "For historical accuracy."

                    mc "Not sure that’s right."

                    show ds at ds_slide
                    pause 1.5
                    play effect "audio/laser1.wav"

                    "The font of the title is too weird for me to make it out. However, the game is really fun."

                    play effect "audio/laser1.wav"
                    queue effect "audio/laser1.wav"

                    "I’m a little jet flying and spinning around the sky shooting shapes."

                    play effect "audio/laser2.wav"
                    queue effect "audio/laser1.wav"
                    "There’s little animals yelling at me to do better but this is my first time so I don’t know why they are yelling at me?"

                    play effect "audio/laser2.wav"
                    queue effect "audio/laser2.wav"
                    "I keep getting shot from behind by enemies I miss."

                    play effect "audio/laser2.wav"
                    queue effect "audio/laser2.wav"
                    queue effect "audio/laser2.wav"
                    "It's fun for a few minutes, but after I died three times I had to hand the device back to G."

                    hide ds with moveoutbottom

                    if persistent.game4_count == 0:

                        $ persistent.game4_count += 1
                        $ persistent.game_count += 1
                        #$ achievement.progress("G A M E R", persistent.book_count)

                    if persistent.game_count == 4:

                        $ achievement.grant("G A M E R")
                        $ achievement.sync()

                    mc "That was fun, I think I’m really starting to like video games."

                    show ge happy

                    g "Of course you are. You’re one of us now."

                    mc "What do you mean?"

                    g "{cps=40}One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us.{/cps}"

                    "Her repetition gets slower and hands grow closer to my face."

                    show ge smug with Dissolve(0.1)

                    g "I’ll make a gamer out of you if you give me the chance. Don’t tempt me!"

                    mc "I'll watch my step."

                    $ g_convo += 1
                    $ activity_check += 1
                    hide ge smug with dissolve
                    jump social

            elif g_convo == 3:

                g "Have you assimilated yet pirate pal?"

                mc "I’m not sure. People seem to be fine with me."

                show ge mad

                g "Not good enough, go talk to more people. Become one with the Pirate Culture Club."

                mc "But I’m already a-"

                show ge happy with Dissolve(0.1)

                g "{cps=30}One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us.{/cps}"

                mc "You really like this club G?"

                show ge int with Dissolve(0.1)

                g "Yeah, duh. That's why I'm here all the time."

                g "Why do you ask?"

                mc "I had this club pegged all wrong. Didn't think you'd all be so friendly and not crazy."

                show ge smile

                g "Oh, for sure we're crazy dude."

                mc "You all aren't that crazy."

                mc "I've met people who thought they were the kings of the world while dancing around like monkeys."

                show ge smug with Dissolve(0.1)

                g "Well Fiona's pretty sure of herself."

                mc "I disagree, you are all really cool. I'm glad I came."

                show ge happy with Dissolve(0.1)

                g "Cool enough to let us on your ship?"

                mc "That's not a question of you being cool, more hardy."

                g "I don't know about hardy, but I can party hardy with the best of them."

                g "Pirates must throw some wild ragers."

                mc "Sometimes, after a good haul, we'll drink the night away, but the best ones are on pirate islands."

                g "Oh yeah? What's it like there?"

                mc "Pirate islands are all fun all the time. Well, at least for the most part."

                mc "If you don't have to keep track of inventory, repairs, reputation, or your blood alcohol level. Then it's a lot of food and debauchery."

                g "Nevermind, I don't want to see your ship. You have to stay here at school and spread some of that sweet sweet pirate life to the people."

                g "Enroll in our school and become one of us."

                mc "Well I can't do that, I have to get back to my ship and-"

                g "{cps=30}One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us.{/cps}"

                hide ge happy with dissolve

                $ G_affinity += 1
                $ g_convo += 1
                jump social

            else:

                mc "G is there a-"

                show ge happy with Dissolve(0.1)

                g "{cps=30}One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us. One of us.{/cps}"

                mc "I see that you're busy being fake crazy still."

                if persistent.woman3 == 0:

                    $ persistent.woman3 += 1

                if persistent.woman1 == 1 and persistent.woman2 == 1 and persistent.woman3 == 1 and persistent.woman4 == 1:

                    $ achievement.grant("Woman Respecter")
                    $ achievement.sync()

                hide ge happy with dissolve
                jump social

        label astrid:

            show ast at center with dissolve

            if a_convo == 0:

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    mc "Hey Astrid? How’d you like my introduction?"

                    $ quick_menu = True

                    show ast smile with Dissolve(0.1)

                    a "It was something for sure. You should go talk to some other club members though."

                    mc "But I’m here to talk to you. Is that a problem?"

                    show ast sad with Dissolve(0.1)

                    a "I guess not. I don’t want people to think the President is hogging all the pirate for herself."

                    mc "They could easily walk up to me and introduce themself as easily as I can."

                    show ast conf with Dissolve(0.1)

                    a "Approaching a veteran pirate might not be as easy for my friends as it is for you."

                    mc "That would make sense, but I'm basically the most relatable teen out there."

                    show ast happy with Dissolve(0.1)

                    a "For sure, hundred percent."

                    mc "Did you want to ask me any questions?"

                    show ast with Dissolve(0.1)

                    a "Yeah I had a bunch if you wouldn’t mind me asking a few."

                    mc "Go ahead."

                    show ast

                    a "Okay, like don’t take this wrong but can you tell me what your Captain’s like?"

                    mc "My Captain? Alright."

                    mc "He’s earned the title The Demonic Pirate a hundred times over in my lifetime alone."

                    a "I heard he sinks ships on a whim and leaves no survivors."

                    mc "No, he’s more tactical than that. You have to leave survivors sometimes to spread fear across the world."

                    mc "Personally I think it's wasteful when we sink ships, but it instills fear at any distance when we fire at the top deck."

                    mc "The bigger the crew, the scarier it is to see ten or twenty men die to one cannonball shot."

                    show ast sup with Dissolve(0.1)

                    a "Wow, that is brutal."

                    a "How does he treat his crew if he's so demonic?"

                    mc "Like how a cruel and powerful God treats their subjects."

                    show ast

                    a "What does that even mean?"

                    mc "It means he’s strong and old and you think he’d swing his weight around too much but he doesn't."

                    mc "He knows he can, but every once and a while he has to come down to demonstrate why he’s in charge."

                    a "I’m sorry I called your accurate description into question."

                    a "It sounds like the Greek Gods starting wars amongst their subjects over petty arguments. If they want the mortals to do anything they have to be powerful, but humble."

                    mc "Yes, exactly like that."

                    mc "But don’t dread the symbolism. I’d die for that man, he’s the type of Captain that will go down with the ship."

                    mc "That’s the sign of a person to follow into the Underworld. And no Greek God would do that for anyone mortal."

                    a "I’d like to not be the type of President that is compared to Greek tragedies, but we don’t often engage in life or death combat so I might be safe."

                    mc "Not often?"

                    show ast sad with Dissolve(0.1)

                    a "No, not very often. Don’t bring up {i}The Great Budget Meeting of ‘16{/i} to anyone though."

                    a "I couldn't stomach hearing about that another time."

                    mc "Some battles are meant not to be retold, they live in the survivor’s hearts and scars."

                    show ast smile with Dissolve(0.1)

                    a "Damn straight."

                    a "You should go talk to someone else now. Tell them a heroic tale of piracy for me."

                    a "Don't worry, I'll be listening."

                    $ a_convo += 1
                    $ activity_check += 1
                    hide ast smile with dissolve
                    jump social

            elif a_convo == 1:

                $ quick_menu = False
                $ renpy.block_rollback()

                a "Did you talk to the others yet?"

                $ quick_menu = True

                mc "Don’t worry President, I’ll make sure nobody spreads any nasty rumors about us talking so much."

                show ast sad with Dissolve(0.1)

                a "No, you’re supposed to spread the pirate-ness to the Pirate Culture Club, not just talk to me."

                if b_convo >= 1 or f_convo >= 1 or g_convo >= 1:

                    mc "You aren't the only person I've talked to. You know that, you've been standing right here."

                else:

                    mc "I guess I could spread out a little more, but I like talking to you too."

                    show ast emb with Dissolve(0.1)

                mc "Plus, people can hear us from right here. We’re all in the same room after all."

                show ast with Dissolve(0.1)

                a "That’s true."

                a "You aren't acting like I thought a pirate of the Red Plague would."

                mc "What, like a greasy monster?"

                show ast sup with Dissolve(0.1)

                a "Well, no, but like."

                mc "You wouldn’t want me to act like I have to onboard the ship to get along with the others."

                show ast

                mc "I wanted to try talking more normally with land people today so I left that [player_name] on the ship."

                show ast smile with Dissolve(0.1)

                a "Oh, well I appreciate that."

                show ast happy

                a "But I was kinda hoping you'd be a little sexist so I could see Fiona get really mad."

                a "Just go wild on a misogynist pirate for the meme."

                mc "Well you never had to worry about that. We can be bad, but not unfairly bad."

                show ast happy

                mc "We only tolerate bad behavior because we’d die without the work everyone puts into the crew."

                show ast

                a "That's good I guess. Trusting everyone and all."

                if book_choice == "exciting":

                    show ast with Dissolve(0.1)

                    a "By the way, what’s that you have under your shirt?"

                    mc "Oh, I took this book from a store before coming here. Thought it might look good in my humble collection."

                    show ast happy with Dissolve(0.1)

                    a "You like the Parry Baxton series? The movies are so fun to rewatch."

                    mc "I’m not sure yet. I only read the first bits so far. Seems good though."

                    show ast happy at wiggle

                    a "I’ve seen the movies so many times. My parents run a movie theater so I watch a lot of movies."

                    mc "I’ve never seen one before, how exactly do they work?"

                    mc "Like, how do the movies...move?"

                    a "The short explanation is we project a moving image onto a wall and people pay us to do that."

                    mc "That is definitely something I’d like to experience one day."

                    show ast emb with Dissolve(0.1)

                    a "Would you like to come by and see one after this is done?"

                    mc "I would love, {cps=25}I mean uhhhh.{/cps} I would love to {cps=20}gooooooooo,{/cps} but."

                    show ast sad with Dissolve(0.3)

                    "Poseidon’s holy trident, I’ve never been asked to do anything without being forced to."

                    "Especially not a fun sounding activity as well. But damn it I can't."

                    mc "Going to a movie theater with you sounds like fun Astrid. But I have to return to my ship after this or they might leave me behind."

                    a "Yeah, that’s fine of course you have to do that. I don’t know what I was expecting."

                    mc "But, if I’m ever back here again I could sneak off and we could all see a movie together? I want to see the most popular film out that year."

                    show ast happy with Dissolve(0.1)

                    a "Awesome, bet. I’m totally down for that."

                    $ Astrid_affinity += 1

                show ast with Dissolve(0.1)

                a "So {cps=20}ummmmmm{/cps}, have you ever wanted to captain your own ship?"

                mc "Wow, that’s uh."

                mc "I’ve never really thought about it before. I can’t imagine my Captain ever retiring so..."

                a "Is he one of those guys you just look at and think that they will live forever?"

                mc "Something like that, yes."

                mc "He has that kind of salty sea aura to him. Like he’s already a specter of the high seas that's there to torment anyone in his waters."

                show ast smile with Dissolve(0.1)

                a "That’s some eerie imagery. Might have dodged a bullet there by getting you to come instead."

                mc "Thanks, I appreciate that."

                a "No, I mean it. It’s been cool having you here today."

                mc "Ha, I wasn’t being sarcastic. I’ve been scolded because it isn’t a very good look for serious pirates, whatever that means."

                a "Well what jerk decides that? Sarcasm is our generation's life blood. You use it as much as you want [player_name]."

                mc "Thanks, I was on my hands and knees waiting for your permission Madame President."

                show ast happy with Dissolve(0.1)

                a "There you freaking go! That’s the youthful disregard we all have inside of us."

                show ast

                a "But seriously, go talk to someone else before I get berated for hogging you."

                mc "Alright Astrid."

                $ a_convo += 1
                hide ast with dissolve
                jump social

            elif a_convo == 2:

                $ quick_menu = False
                $ renpy.block_rollback()

                a "Fine [player_name], since my allure is so captivating, tell me something."

                show ast smile with Dissolve(0.1)

                $ quick_menu = True

                a "What’s your favorite thing to steal?"

                mc "That’s the easy one."

                mc "Well yeah, that’s it actually. Whatever is easiest to steal."

                mc "Something I want and they won’t miss. I like when I’m not risking my life over something we are just going to end up selling."

                show ast sup with Dissolve(0.1)

                a "Oh, wow. That’s a more serious answer than I was expecting. I was hoping you’d say diamonds or something."

                mc "No, people will kill for those and I’d rather not be on the receiving end of that intention if possible."

                show ast smile with Dissolve(0.1)

                a "I really like stealing movies. I’ll sit in the free movies I get from my parent’s theater and record them on video tapes and upload them online."

                mc "Do you make money on that?"

                a "I wouldn’t charge people for that. But the industry takes a small hit and that's where the rush comes from."

                if badwords == True:

                    a "My folks get {b}hecking{/b} mad at me for it, it’s really amusing watching their heads explode over a 720p recording of some cheapo horror film."

                else:

                    a "My folks get hella mad at me for it, it’s really amusing watching their heads explode over a 720p recording of some cheapo horror film."

                mc "Rebel where you can I guess. No job is worth losing your skin over, make sure you’re careful."

                mc "I don’t know how serious that is here, but it doesn’t sound worth losing your freedom over a seven twenty pee."

                show ast happy with Dissolve(0.1)

                a "Yeah, my vast amount of freedom. Full of my own choices and self determination."

                mc "Florida must be nice if it has all that."

                show ast sad with Dissolve(1.0)
                show ast smile with Dissolve(0.4)

                a "I’m gonna get some more food. Please make sure you talk to the other club members. Do it for me please?"

                mc "Aye President. I’ll spread the good word of cannon cleaning techniques in your name."

                a "Much appreciated, thank you. I'll be around if you need anything."

                if persistent.woman4 == 0:

                    $ persistent.woman4 += 1

                if persistent.woman1 == 1 and persistent.woman2 == 1 and persistent.woman3 == 1 and persistent.woman4 == 1:

                    $ achievement.grant("Woman Respecter")
                    $ achievement.sync()

                $ a_convo += 1
                $ activity_check += 1
                hide ast smile with dissolve
                jump social

        label washroom:

            $ quick_menu = False
            $ renpy.block_rollback()

            "My stomach is hurting suddenly. Is this for the incoming social anxiety or was it something I ate?"

            $ quick_menu = True

            "Hopefully the washrooms are cleaner here then on the ship. Keeping the latrine clean for more than three days on the Plague would take God-like abilities."

            show ast at center with dissolve

            mc "Hey Astrid, where is the nearest washroom from here?"

            a "There’s one in this wing. Take a left and they’re the two wider doors across the hall."

            mc "Thank you very much."

            hide ast with dissolve
            scene BG hw with fade

            "The wider doors are easily visible right out of the classroom."

            pause 1.0
            scene BG wc1 with fade

            $ activity_check += 1 # to complicated to put after every jump after the fact
            $ b_check += 1        # also this

            mc "{cps=20}Ummmm. I’m not so sure, what do these mean?{/cps}"

            "What are these symbols? One is a person but the other is a triangle person? What’s the difference?"

            "I don’t want to get kicked out for using the wrong one, or more likely be put in an awkward situation. Think [player_name], think."

            "Am I a triangle person or a slim person? I feel slim but does this shirt make me look more triangular? Does this have to be so difficult?"

            if f_met == 0:

                $ f = Character('Tall Girl', color="#d1c1ff", callback=fiona_voice, who_outlines=[ (1, "#000000")])

                show fiona sad at left with moveinleft

                f "You having a problem matey?"

                mc "Oh yeah, I am. Please excuse my lack of land iconography but what do these symbols mean?"

                mc "Do they stop me from entering them?"

                show fiona with Dissolve(0.1)

                f "You’re on the right track there. One’s for boys and the other’s for girls. Is that a problem for you?"

                mc "Hmmmmmm…"

                if player_identity == "m":

                    mc "No, I’ll use the men's one. Thank you."

                    mc "You were in the club room right?"

                    $ f = Character('Fiona', color="#d1c1ff", callback=fiona_voice, who_outlines=[ (1, "#000000")])
                    $ f_met += 1

                    f "Yeah, my name’s Fiona. See you back in there."

                    hide fiona with dissolve

                    "Fiona pushes past me and goes into the girls bathroom."

                    scene BG wc2 with fade

                    "Surprisingly, there are multiple facilities inside the huge room on this side."

                    "I must have picked the best one then."

                    "The smell of lemons hits my face like a morning breeze. It's all so much better than what the ship provides."

                    "I should just do my business and return to the clubroom. If this is what all washrooms are like on land then I shall remember them fondly."

                    play effect "audio/flush.ogg"
                    scene BG hw with fade
                    scene BG cr with fade

                    jump classroom_choice

                elif player_identity == "f":

                    mc "No, I’ll use the girl’s one. Thank you."

                    mc "You were in the club room right?"

                    $ f = Character('Fiona', color="#d1c1ff", callback=fiona_voice, who_outlines=[ (1, "#000000")])
                    $ f_met += 1

                    f "Yeah, my name’s Fiona. Come with me, I’ll be there if we run into any more gendered symbols."

                    hide fiona with dissolve

                    "Fiona pushes past me and goes into the girl's bathroom."

                    scene BG wc3 with fade

                    "I follow behind her, confused by what she meant by that. If that was an omen I should mentally prepare."

                    "To my surprise, there are multiple facilities inside this huge washroom."

                    "I must have picked the best one then."

                    "The aroma of sour smelling bleach hits my face like cleaning the ship at dawn."

                    show fiona at right with moveinright

                    mc "Are all of them this big?"

                    f "All of what?"

                    mc "All washrooms on land?"

                    show fiona sad with Dissolve(0.1)

                    f "No, but the school ones have to support a lot of people at once. They aren’t as accommodating as they look."

                    mc "What do you mean? There seems to be plenty of soap, multiple stalls, and enough wipe paper to kill a shark."

                    f "Wipe paper?"

                    show fiona angry with Dissolve(0.1)

                    f "Okay yeah, but there’s only one diabled stall in this entire building and no gender neutral options."

                    mc "I’m sure someone with an artificial leg could fit in one of these. Can not every gender use the girl’s room?"

                    mc "Is that taboo?"

                    f "Doubly wrong matey."

                    f "I mean like people in wheelchairs or mobility scooters. There’s three students who need that accommodation here."

                    show fiona frown with Dissolve(0.1)

                    f "We aren’t actually allowed to use which room we are most comfortable with. People get weirdly mad about that."

                    f "You either have to fight really hard or roll over and deal with it."

                    mc "I see. That is strange. But fighting for something shows it's important to you."

                    mc "On ships and pirate islands we just have the one type of door. Sometimes it has a W.C. on it or a moon carving."

                    show fiona angry

                    if badwords == True:

                        f "That's the way it should be. Cis {b}activity{/b} here is unbearable sometimes."

                    else:

                        f "That's the way it should be. Cis shit here is unbearable sometimes."

                    if badwords == True:
                        mc "Cis {b}activity{/b}?"
                    else:
                        mc "Cis shit?"

                    f "Nevermind, just do your business so we can get back to everyone."

                    hide fiona angry with dissolve

                    "She’s right, it feels weird just being in a gendered room and for a whole conversation to happen in one."

                    "If this is what all washrooms are like on land then I shall remember them fondly."

                    play effect "audio/flush.ogg"

                    scene BG hw with fade
                    scene BG cr with fade
                    jump classroom_choice

                else:

                    mc "Yes, sort of. I still don’t know which one to use. Do you understand what I mean?"

                    show fiona angry with Dissolve(0.1)

                    if badwords == True:

                        f "Yeah I get it. This stupid het norm school {b}really{/b} sucks."

                    else:

                        f "Yeah I get it. This stupid het norm school fucking sucks."

                    $ f_met += 1

                    show fiona sad with Dissolve(0.1)

                    f "I know you don’t know me, but come in the girls room with me I’ll make sure nobody bugs us."

                    $ f = Character('Fiona', color="#d1c1ff", callback=fiona_voice, who_outlines=[ (1, "#000000")])

                    f "My name's Fiona though. So now you know me."

                    mc "Thank you Fiona. I appreciate that."

                    hide fiona sad with dissolve

                    "Fiona pushes past me and goes into the girl's bathroom."

                    scene BG wc3 with fade

                    "I follow behind her, confused by what she meant by that."

                    "Are people going to harass us while we use it?"

                    "There are multiple facilities inside this huge washroom, it's so nice in here."

                    "Fiona must have known the best one to use, the aroma of sour smelling bleach hits my face like cleaning the ship at dawn."

                    show fiona at right with dissolve

                    mc "Are all of them this big?"

                    f "All of what?"

                    mc "All washrooms on land?"

                    show fiona sad with Dissolve(0.1)

                    f "No, but the school ones have to support a lot of people at once. They aren’t as accommodating as they look."

                    mc "What do you mean? There seems to be plenty of soap, multiple stalls, and enough wipe paper to kill a shark."

                    f "Wipe paper?"

                    show fiona angry with Dissolve(0.1)

                    f "Yeah, but there’s only one diabled stall in this entire building and no gender neutral options."

                    mc "I’m sure someone with an artificial leg could fit in one of these. Can not every gender use the girl’s room?"

                    mc "Is that taboo?"

                    f "Doubly wrong matey."

                    f "I mean like people in wheelchairs or mobility scooters. There’s three students who need that accommodation here."

                    show fiona frown with Dissolve(0.1)

                    f "We aren’t allowed to use which room we are most comfortable with. People get weirdly mad about that."

                    f "You either have to fight really hard or roll over and deal with it."

                    mc "I see. That is strange. But fighting for something shows it's important to you."

                    mc "On ships and pirate islands we just have the one type of door. Sometimes it has a W.C. on it or a moon carving."

                    show fiona angry

                    if badwords == True:

                        f "That's the way it should be. Cis {b}activity{/b} here is unbearable sometimes."

                    else:

                        f "That's the way it should be. Cis shit here is unbearable sometimes."

                    if badwords == True:
                        mc "Cis {b}activity{/b}?"
                    else:
                        mc "Cis shit?"

                    show fiona sad with Dissolve(0.1)

                    f "Nevermind, just do your business so we can get back to everyone."

                    hide fiona sad with dissolve

                    "She’s right, it feels weird just being in a gendered room and for a whole conversation to happen in one."

                    "If this is what all washrooms are like on land then I shall remember them fondly."

                    play effect "audio/flush.ogg"

                    scene BG hw with fade
                    scene BG cr with fade
                    jump classroom_choice

            else:

                $ f = Character('Fiona', color="#d1c1ff", callback=fiona_voice, who_outlines=[ (1, "#000000")])

                show fiona sad at left with moveinleft

                f "You having a problem matey?"

                mc "Oh, Fiona."

                mc "Could you please excuse my lack of land iconography but what do these symbols mean? Do they stop me from entering them?"

                f "You’re on the right track there. One’s for boys and the other’s for girls. Is that a problem for you?"

                mc "Hmmmmmm…"

                if player_identity == "m":

                    mc "No, I’ll use the men's one. Thanks Fiona."

                    show fiona with dissolve

                    f "No problemo matey. See you back at the party."

                    hide fiona with dissolve

                    "Fiona pushes past me and goes into the girls bathroom."

                    scene BG wc2 with fade

                    "Surprisingly, there are multiple facilities inside the huge room on this side."

                    "I must have picked the best one then."

                    "The smell of lemons hits my face like a morning breeze. It's all so much better than what the ship provides."

                    "I should just do my business and return to the clubroom. If this is what all washrooms are like on land then I shall remember them fondly."

                    play effect "audio/flush.ogg"
                    scene BG hw with fade
                    scene BG cr with fade

                    jump classroom_choice

                elif player_identity == "f":

                    mc "No, I’ll use the girl’s one. Thanks for the help Fiona."

                    hide fiona with dissolve

                    "Fiona pushes past me and goes into the girl's bathroom."

                    scene BG wc3 with fade

                    "I follow behind her, confused by what she meant by that. If that was an omen I should mentally prepare."

                    "To my surprise, there are multiple facilities inside this huge washroom."

                    "I must have picked the best one then."

                    "The aroma of sour smelling bleach hits my face like cleaning the ship at dawn."

                    show fiona at right with moveinright

                    mc "Are all of them this big?"

                    f "All of what?"

                    mc "All washrooms on land?"

                    show fiona sad with Dissolve(0.1)

                    f "No, but the school ones have to support a lot of people at once. They aren’t as accommodating as they look."

                    mc "What do you mean? There seems to be plenty of soap, multiple stalls, and enough wipe paper to kill a shark."

                    f "Wipe paper?"

                    show fiona angry with Dissolve(0.1)

                    f "Okay yeah, but there’s only one diabled stall in this entire building and no gender neutral options."

                    mc "I’m sure someone with an artificial leg could fit in one of these. Can not every gender use the girl’s room?"

                    mc "Is that taboo?"

                    f "Doubly wrong matey."

                    f "I mean like people in wheelchairs or mobility scooters. There’s three students who need that accommodation here."

                    show fiona frown with Dissolve(0.1)

                    f "We aren’t actually allowed to use which room we are most comfortable with. People get weirdly mad about that."

                    f "You either have to fight really hard or roll over and deal with it."

                    mc "I see. That is strange. But fighting for something shows it's important to you."

                    mc "On ships and pirate islands we just have the one type of door. Sometimes it has a W.C. on it or a moon carving."

                    show fiona angry

                    if badwords == True:

                        f "That's the way it should be. Cis {b}activity{/b} here is unbearable sometimes."

                    else:

                        f "That's the way it should be. Cis shit here is unbearable sometimes."

                    if badwords == True:
                        mc "Cis {b}activity{/b}?"
                    else:
                        mc "Cis shit?"

                    f "Nevermind, just do your business so we can get back to everyone."

                    hide fiona angry with dissolve

                    "She’s right, it feels weird just being in a gendered room and for a whole conversation to happen in one."

                    "If this is what all washrooms are like on land then I shall remember them fondly."

                    play effect "audio/flush.ogg"

                    scene BG hw with fade
                    scene BG cr with fade
                    jump classroom_choice

                else:

                    mc "Yes, sort of. I still don’t know which one to use. Do you understand what I mean Fiona?"

                    show fiona angry with dissolve

                    if badwords == True:

                        f "Yeah I get it. This stupid het norm school {b}really{/b} sucks."

                    else:

                        f "Yeah I get it. This stupid het norm school fucking sucks."

                    f "I know you don’t know me that well, but come in the girls room with me I’ll make sure nobody bugs us."

                    mc "Thank you Fiona. I appreciate that."

                    hide fiona sad with dissolve

                    "Fiona pushes past me and goes into the girl's bathroom."

                    scene BG wc3 with fade

                    "I follow behind her, confused by what she meant by that."

                    "Are people going to harass us while we use it?"

                    "There are multiple facilities inside this huge washroom, it's so nice in here."

                    "Fiona must have known the best one to use, the aroma of sour smelling bleach hits my face like cleaning the ship at dawn."

                    show fiona at right with dissolve

                    mc "Are all of them this big?"

                    f "All of what?"

                    mc "All washrooms on land?"

                    show fiona sad with Dissolve(0.1)

                    f "No, but the school ones have to support a lot of people at once. They aren’t as accommodating as they look."

                    mc "What do you mean? There seems to be plenty of soap, multiple stalls, and enough wipe paper to kill a shark."

                    f "Wipe paper?"

                    show fiona angry with Dissolve(0.1)

                    f "Yeah, but there’s only one diabled stall in this entire building and no gender neutral options."

                    mc "I’m sure someone with an artificial leg could fit in one of these. Can not every gender use the girl’s room?"

                    mc "Is that taboo?"

                    f "Doubly wrong matey."

                    f "I mean like people in wheelchairs or mobility scooters. There’s three students who need that accommodation here."

                    show fiona frown with Dissolve(0.1)

                    f "We aren’t allowed to use which room we are most comfortable with. People get weirdly mad about that."

                    f "You either have to fight really hard or roll over and deal with it."

                    mc "I see. That is strange. But fighting for something shows it's important to you."

                    mc "On ships and pirate islands we just have the one type of door. Sometimes it has a W.C. on it or a moon carving."

                    show fiona angry

                    if badwords == True:

                        f "That's the way it should be. Cis {b}activity{/b} here is unbearable sometimes."

                    else:

                        f "That's the way it should be. Cis shit here is unbearable sometimes."

                    if badwords == True:
                        mc "Cis {b}activity{/b}?"
                    else:
                        mc "Cis shit?"

                    show fiona sad with Dissolve(0.1)

                    f "Nevermind, just do your business so we can get back to everyone."

                    hide fiona sad with dissolve

                    "She’s right, it feels weird just being in a gendered room and for a whole conversation to happen in one."

                    "If this is what all washrooms are like on land then I shall remember them fondly."

                    play effect "audio/flush.ogg"

                    scene BG hw with fade
                    scene BG cr with fade
                    jump classroom_choice

        label food:

            $ quick_menu = False
            $ renpy.block_rollback()

            mc "I can’t turn down free food. What kind of pirate would I be?"

            $ quick_menu = True

            "The people who burst towards the food after I spoke have left. Apparently they weren’t as interested as the club heads are."

            "A side table by the window is laid out with plastic wrapped food. My eye is drawn to the..."

            menu:

                "Grilled Chicken":
                    jump chicken

                "Really Long Sandwich" if b_convo != 3:
                    jump sandwich

                "Fresh Fruits":
                    jump fruits

            label chicken:

                $ quick_menu = False
                $ renpy.block_rollback()

                "The grilled chicken breasts look so good. I can’t tell if it's warm or cold but I want to eat it super bad."

                $ quick_menu = True

                "There are little plastic plates to put the food on. Are these easier to clean?"

                "Only the ranked crew members get the metal plates, the rest of the crew use the wooden ones. Not that we even had enough metal ones for everyone."

                "They’re terrible to wash but can’t easily break and can be recycled from old planks on the ship."

                "..."

                "The chicken is so juicy. I haven't had meat this good in a while."

                "If everything today was a waste, this moment is worth the world."

                show ge smile with dissolve

                if g_met == 0:

                    $ g = Character('Girl', color="#2ef2f4", callback=g_voice, who_outlines=[ (1, "#000000")])

                g "You liking the food?"

                mc "Yeah this is great. You make it?"

                g "No, I just took it from my parent’s deli."

                mc "So this was stolen and I didn’t have to do anything? That makes it taste even better!"

                show ge sad with Dissolve(0.1)

                g "It does? I sort of feel guilty. I think some of this stuff was supposed to go to someone’s Bat Mitzvah."

                mc "I don’t know what that is? Is it like a celebration of some kind?"

                g "Something like that..."

                if g_met == 0:

                    $ g = Character('G', color="#2ef2f4", callback=g_voice, who_outlines=[ (1, "#000000")])

                    g "I’m Geraldine by the way. I don’t know if you heard anyone say my name. My friends call me G."

                    mc "Really? I actually knew a pirate named Geraldine."

                else:

                    mc "You know G, I actually knew a pirate named Geraldine."

                show ge int with Dissolve(0.1)

                g "Really? What was she like?"

                "Swallowing the last of what remained on my plate, I try to recall the most flattering memory of ol Geraldine."

                mc "She was the biggest woman I’ve ever seen."

                show ge mad with Dissolve(0.1)

                g "What!?"

                mc "She was built like a mighty killer whale. And killed like one too."

                show ge

                mc "Unapologetically ruthless, when she served her special slop mix to us some pirates would try to insult her looks and she would say terrible things about their mothers."

                show ge happy

                g "Haaah ahh ah! Yeah like what?"

                mc "She’d say horrible things. Like when they called her fat she would say something like,"

                if badwords == True:

                    mc "\"At least if I gave birth to an ugly {b}man{/b} like yerself I’d have the decency to eat ya and save me the trouble of looking like I passed around a goat.\""

                else:

                    mc "\"At least if I gave birth to an ugly fuck like yerself I’d have the decency to eat ya and save me the trouble of looking like I passed around a goat.\""

                show ge happy at wiggle

                if badwords == True:

                    g "BWAHahahahahaha! That's {b} really darn hilarious{/b}. And she’d do that how often?"

                else:

                    g "BWAHahahahahaha! That's fucking hilarious. And she’d do that how often?"

                "She almost choked trying to get that out. Her entire body has gone limp from laughter."

                "A few club members around us giggle along, but are drowned out by G’s roars."

                "If I recall correctly, some books I read implied teenagers find being mean really funny."

                "Can’t disagree, in most cases that's true."

                mc "Almost every night she’d bring a pirate on the verge of tears. Once someone threw a punch at her and she caught his hand and put it in the boiling hot soup."

                g "Oh my God I can picture it now."

                g "One time."

                "She's trying to catch her breath."

                show ge smile with Dissolve(0.1)

                g "One time, I told my mom to eat my dick after she yelled at me for being on my phone and I got grounded for a week."

                show ge sad

                g "I wish I could be that tough more often."

                show ge smile with Dissolve(0.1)

                g "This Geraldine is now the me I will strive to be. Minus the whale part."

                mc "She was definitely an inspiring woman."

                g "I have to go tell Be about this, she’ll flip."

                hide ge smile with moveoutleft

                if b_convo >= 1:

                    "Before I could ask what she meant my \"flip\" G shuffled to another table to talk to Behati."

                else:

                    "Before I could ask what she meant my \"flip\" G shuffled to another table to talk to her friend."

                $ g_met += 1
                $ G_affinity += 1
                $ activity_check += 1
                $ food_ate += 1

                jump classroom_choice

            label sandwich:

                $ quick_menu = False
                $ renpy.block_rollback()

                "Poseidon help me, that sandwich is half my size!"

                $ quick_menu = True

                "Oh?"

                "It’s cut into slices others are taking. Was it too presumptuous to think it was all a gift for the Captain? I’d totally expect him to eat it all."

                if b_met == 0:

                    show be emb with dissolve

                    $ b = Character('Girl', color="#ffcb00", callback=b_voice, who_outlines=[ (1, "#000000")])

                    b "Do y-you like the sandwiches?"

                    "This girl with large spectacles appeared behind me almost making me drop my slice."

                    "She seems nervous to talk to me, couldn’t imagine what she’d be like if the Captain show’d up."

                    mc "Yes, this tastes great. I’ve never had anything like it."

                    show be emb at wiggle

                    b "That’s g-g-good. Do you w-want anything to d-drink?"

                    mc "Well I was told there was no alcohol, so do you have water at least, ummm? What’s your name?"

                    $ b = Character('Behati', color="#ffcb00", callback=b_voice, who_outlines=[ (1, "#000000")])
                    $ b_met +=1

                    b "I-I'm. Uhhhhh. B-be-be-ha-ha"

                    b "{cps=100}I’m Behati. Here’s some water we took from the tap and put in a pitcher!{/cps}"

                    play effect "audio/water.ogg" volume .8
                    show be at wiggle
                    "She pours me a cup of water as fast as she said that, spilling a fair amount of it on the table."

                    show be shocked with Dissolve(0.1)

                else:

                    show be emb with dissolve

                    $ b = Character('Behati', color="#ffcb00", callback=b_voice, who_outlines=[ (1, "#000000")])

                    b "Do you like the sandwiches?"

                    "It’s Behati. Her questions were very data driven, wonder if that’s how she’s like all the time?"

                    "I really don’t know all of the ships' intakes and outputs. Besides how many ships we sink."

                    "Flavio mostly takes care of the number stuff."

                    mc "Yes, this tastes great. I’ve never had anything like it."

                    show be with Dissolve(0.1)

                    b "That’s good. Do you want anything to drink?"

                    mc "Water if you have it."

                    b "Let me pour you some, here’s some water we took from the tap and put in a pitcher."

                    play effect "audio/water.ogg" volume .8
                    show be shocked with wiggle
                    "She pours me a cup of water while shaking the pitcher, spilling a little bit on the table."

                mc "{cps=20}Ummmm Beh-{/cps}"

                show be emb at wiggle

                b "{cps=80}Did you know our school is the closest in the district with the amount of lead legally allowed in the tap water by zero point zero zero two percent parts-per-billion?{/cps}"

                mc "No, I didn’t know that. I just got here, remember?"

                show be skeptical with Dissolve(0.1)

                b "Yeah of course, totally, duh, that was a stupid question."

                "She takes a long and shaky sip from her plastic cup. This girl is more on edge than I was."

                "I should try to calm her down and get to know what’s happening better."

                mc "Behati, tell me what it’s like in the Pirate Culture Club."

                show be shocked

                b "Well. It’s a great time, really."

                show be with Dissolve(0.1)

                b "Astrid is a great President and we don’t have much of a budget so a Treasurer doesn’t have much to worry about. So I do very little work."

                b "I spend the extra time either doing mine or G’s homework."

                mc "Do you make a lot of friends here?"

                show be skeptical

                b "No no no. Not really."

                show be with Dissolve(0.1)

                b "We’re all friends on the E-board. This is the only time I ever see G during school now."

                b "People used to call us G and Be when we hung out. Ha ha. But now only Ash does to tease me."

                mc "Which one is Ash?"

                b "Ash was sitting next to me during your introduction."

                show be skeptical with Dissolve(0.1)

                b "But after you were done he took two pieces of chicken and bailed."

                b "Probably won’t see him again till Monday."

                mc "Everyone here seems pretty nice. I might look around some more before I leave."

                show be quiz with Dissolve(0.1)

                b "If you have any questions just let me know. I know all about the school."

                show be

                b "I also know a lot about pirates that came from Seaborough, but not everything. Maybe you could fill in my gaps?"

                hide be happy with dissolve

                "Behati does a weird thing with her eyes and walks away quickly."

                $ b_met += 1
                $ Be_affinity += 1
                $ activity_check += 1
                $ food_ate += 1

                jump classroom_choice

            label fruits:

                if food_check == 1:

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    "They have more fruits!"

                    $ quick_menu = True

                    "That apple I took left me wanting more. Plus I can sneak some of these out of here for later."

                else:

                    $ quick_menu = False
                    $ renpy.block_rollback()

                    "A pirate can’t risk avoiding their fruits. Don’t want history to repeat itself."

                    $ quick_menu = True

                show ast conf at center with dissolve

                a "You’re only taking the fruit? Is that a pirate thing?"

                show ast smile with Dissolve(0.1)

                a "Avoiding the dreaded skurvy?"

                mc "What? No."

                mc "Well, yes."

                mc "Scurvy is still a common problem because we can’t keep fruits on the ship for very long. I get maybe one lemon or something before we're out for too long."

                a "Well take as many as you’d like. It doesn’t seem like anyone wants them anyway."

                mc "Normally if nobody wants something a pirate won’t take it. This is a notable exception."

                show ast conf with Dissolve(0.1)

                a "You don’t steal fruit being sold from ships?"

                mc "If we can tell that a shipment contains perishable foods we don’t take it."

                mc "Those are harder to sell because nobody wants to buy’em from pirates. It takes longer to sell on top of them having an expiration date."

                a "Why don’t you sell them to other pirates?"

                mc "That is...definitely an option I had not considered."

                show ast with Dissolve(0.1)

                a "Historically I know that pirates steal anything that’s valuable, but I have to ask."

                show ast smile with Dissolve(0.1)

                a "How often do you steal gold or treasure?"

                "Astrid’s eyes are almost sparkling at the question. Does she think gold comes from the sea?"

                "Who’s just sailing around with gold bars? It’ll get stolen easily if it ever stays with us longer than an hour."

                mc "{cps=20}Ummmmmm{/cps}, sometimes when we steal from arcistorats that have nice stuff we can pawn."

                show ast sad with Dissolve(0.1)

                a "So no gold?"

                mc "I can’t recall ever finding any gold, no, sorry. Is that expected of us?"

                a "Well like, in the movies pirates are always finding buried treasure and gold coins to bury on a deserted island."

                mc "Well Astrid, when was the last time you saw gold?"

                show ast with Dissolve(0.1)

                a "There’s a pawn shop downtown, so every time I walk by it."

                mc "Is a pirate supposed to walk up to some dinky pawn shop and sell a heap of gold they stole? Would that be worth our time?"

                a "Gold is valuable so I don’t see why not?"

                "She isn’t wrong but I haven’t seen any gold so I don’t know what we’d do with it if we had any."

                mc "We tend to sell our booty to either the intended buyer at a higher price or to businesses that need the material."

                a "Do you at least store the good stuff in treasure chests?"

                mc "Astrid, being a pirate isn’t so cut and dry. We’re very adaptable, as much as we try to keep a scheduled ship, things break or weather happens."

                mc "We have to be fluid like the water and do the best we can with what’s presented to us."

                show ast smile

                mc "Yes, and sometimes there are treasure chests."

                a "Yeah I knew all that. But this is why I asked you to come."

                a "We wanted to learn more from a real pirate. I was just hoping some of the stuff from movies were true."

                show ast sad with Dissolve(0.1)

                a "Just to keep the fantasy up a while longer."

                mc "It’s just that, well."

                mc "What else do movie pirate’s do?"

                show ast

                a "Uh, do you have a cool sword?"

                a "One which often clashes with other pirates in dangerous conflicts?"

                mc "Not at the moment."

                mc "I was messing around on the top deck and a wave slammed my hand on the bow and knocked it into the water."

                show ast happy with Dissolve(0.1)

                a "That's pretty funny."

                mc "I have a gun though."

                show ast sup with Dissolve(0.1)

                a "You do?! What kind? Can I see it?"

                mc "I left it on the ship for legal reasons."

                mc "It’s an old Smith and Wesson model. 32. calibur with real ivory grip."

                mc "I stole it from some Latin guy’s yacht."

                show ast happy

                a "Really? That sounds so cool!"

                a "Something with real ivory would be worth thousands. If it’s old it would be even more."

                mc "Well I can’t sell it or I’d be without a weapon."

                show ast smile

                a "But you could buy more weapons."

                mc "What if I used my gun to steal more guns and money instead?"

                show ast

                a "Because you could only fire six shots and the guns you could buy or steal can fire lots more way faster."

                mc "I’m pretty good at stealing things Astrid."

                show ast smile with Dissolve(0.1)

                a "You haven’t met the gun nuts around here have you?"

                a "You pull a pistol on them, you’d hit the floor faster than sodas exploding in my car."

                mc "Ha ha haaaaa. You're saying I'd explode? Maybe you’re right lass."

                mc "I’ve shot plenty of people if that fits your movie pirate persona."

                show ast smile at wiggle

                "Astrid giggles a little bit and puts down her empty plate. We both look around and the club has mostly finished eating."

                a "It does. Thank you [player_name], you’re a young Bobby Tepp."

                show ast with dissolve

                "Is that a pirate I'm supposed to know?"

                a "I'm glad we got to meet today."

                mc "Thanks Astrid, that means a lot."

                hide ast with dissolve
                $ Astrid_affinity += 1
                $ activity_check += 1
                $ food_ate += 1

                jump classroom_choice

        label leave:

            $ quick_menu = False
            $ renpy.block_rollback()

            mc "Hey Astrid, I think I’m going to leave. It’s getting late and I’m under threat of being left behind if the ship leaves without me."

            $ quick_menu = True

            show ast at centerlefter with dissolve
            a "That’s alright, we aren’t holding you hostage."

            show ge smile at g_school_right with dissolve
            g "Speak for yourself, [player_name] stay here and be our new club advisor."

            show be skeptical at righter with dissolve
            b "G, they’re not a teacher. Advisors have to work here."

            show ge smug with Dissolve(0.1)
            g "Theft of identity! Pretend like you went to Florida State and are super qualified to work here."

            show be with Dissolve(0.1)

            a "We’re letting [player_name] go. Stop messing around."

            show fiona frown at lefter with dissolve

            f "I agree. Our advisor is deathly sick and can only come into work once a week."

            f "Well, she’s actually forced to come in, but that’s another problem."

            mc "Lasses, my calling is the sea. It’s up to you to change your own situations."

            show ast smile

            a "Well said. I can’t thank you enough for coming to talk with us. We all appreciate it."

            show ge smile with Dissolve(0.1)

            g "Girls' right. Thanks for coming to talk to us. It was really cool meeting a real pirate."

            mc "It was my pleasure G, I…"

            show be emb with Dissolve(0.1)

            b "{cps=90}Thank You For Teaching Me More About Pirates [player_name]! I’ll Never Forget This!{/cps}"

            show fiona sad
            show ast sup
            show ge int
            with Dissolve(0.1)

            f "Woah."

            a "Behati! Inside voice please."

            show ast
            show ge

            b "I’m sorry, I’m sorry. I’m just so thankful for you coming here. I’ve ever met anyone as worldly as a real pirate."

            f "You don’t get enough worldly from the Florida common man?"

            show be skeptical

            b "Haha, hardly."

            show be happy

            b "You’ve shifted my views on how pirates perceive themselves and given me more context for the data out there."

            mc "No problem Behati. I’m glad my lack of information was useful information."

            show fiona with Dissolve(0.1)

            f "Thanks for showing up. I can imagine a bunch of seaside teenagers didn’t hold your attention this afternoon."

            mc "Fiona this was better than anticipated. You all taught me a bunch as well."

            f "That’s nice to know."

            show ge happy with Dissolve(0.1)

            g "Next time you’re sinking a ship think of us, okay?"

            mc "With pleasure G. I’ll make your name's an omen of misfortune."

            g "Hell yes! That sounds perfect, my mythos begins now."

            show be with Dissolve(0.1)

            b "You best go before we start writing a sea shanty for you."

            show ast sup with Dissolve(0.1)

            a "Oh my God I forgot to ask you about my shanties!"

            hide ast sup with moveoutleft
            show fiona laugh
            show be shocked
            show ge int
            with Dissolve(0.1)

            $ renpy.music.set_volume(0.00, delay=0, channel='music')

            ev "{cps=35}GO NOW, QUICKLY!{/cps}"

            $ renpy.music.set_volume(1.00, delay=0, channel='music')

            mc "Alright I’m gone! Fare thee well mateys!"

            play effect "audio/doorclose.ogg"
            pause 1.5

            if Be_affinity > Astrid_affinity and Be_affinity > G_affinity and Be_affinity > Fi_affinity:

                show be happy with Dissolve(0.1)

                b "See ya sea cowboy."

                $ achievement.grant("Breathtaking Behati")
                $ achievement.sync()

            elif G_affinity > Astrid_affinity and G_affinity > Be_affinity and G_affinity > Fi_affinity:

                show ge smug with Dissolve(0.1)

                g "Next time I see you it’ll be at the end of my sword."

                $ achievement.grant("G The Great")
                $ achievement.sync()

            elif Fi_affinity > Astrid_affinity and Fi_affinity > Be_affinity and Fi_affinity > G_affinity:

                show fiona sad with Dissolve(0.1)

                f "Back to a life of swashbuckling for them and exams for us."

                $ achievement.grant("Fab Fiona")
                $ achievement.sync()

            elif Astrid_affinity > Fi_affinity and Astrid_affinity > Be_affinity and Astrid_affinity > G_affinity:

                show ast sup at centerleft with moveinleft

                a "Nooooo, did you let them leave? I wanted to sing something for them."

                $ achievement.grant("#1 Astrid Fan")
                $ achievement.sync()

            hide ast
            hide be
            hide fiona
            hide ge
            with dissolve

            stop music fadeout 2.0
            jump act1_4

    return
