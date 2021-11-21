label act1_3:

    pause 1.5
    scene BG school with fade
    define astrid_temp = "Girl"

    "Found it!"

    "This place is massive, are all schools like this?"

    "The large entrance doors are dwarfed by the humongous stone columns lining the front of the building. People are flooding out and filling the parking lot."

    play sound "audio/chattering.mp3"
    # add the crowd png when made

    "Other than narrowly avoiding leaving cars, nobody is staring at me."

    "The letter said someone would meet me outside the school, but there are so many people my rendezvous could be anyone. If everyone is leaving the school, I should wait to see who stays, they’ll be the club member."

    "All sorts of students are leaving. The array of people who go to this school seems vast."

    "One guy looked like a gorilla who’d fit well on the ship. This other kid might get blown under water by a small wave."

    "You’d think they’d be put into weight groups so the bigger ones don’t demolish the tiny children."

    with fade
    stop sound fadeout 2.0

    "Standing alone on the sidewalk, it takes about fifteen minutes for the clumps of students and faculty to disperse."

    "There are a few stranglers hanging around and talking. But this one girl has been standing on the stairs looking directly at me for a bit now."

    "She’s the only person standing alone. This couldn’t be who I was waiting for? If she was expecting the Captain, this is who they sent to greet him?"

    show a_d at center with dissolve

    MC "Uh, hello. You waiting for me lass?"

    # I redefine Astrid so much to change her name per the situation
    # I will also use the what_outline parameter to show feedback for positive choices
    $ a = Character('Girl', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])
    a "{cps=80}Ahhoooo{/cps}{cps=5}OOOOOOOOOOOO{/cps}{cps=50}oooooy Matey!{/cps}"

    #$ astrid_temp = "Astrid of Bellewood"
    $ a = Character('Astrid of Bellewood', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])
    a "{cps=75}I’m Officer Astrid of Bellewood at {color=#5FAFF6}Seaborough{/color} High School! Permission To Speak Easy Captain, Sir?!{/cps}"

    "Poseidon help me this girl is..."

    menu:# MC's different reactions to first meeting Astrid
        "She’s Enthusiastic":

            MC "Are you insane?"

            MC "No need to yell at me, Astrid of Bellewood."

            a "Thank you Captain. Bellewood is actually my last name, I just thought it would sound cooler in my introduction."

            MC "Can I just call you Astrid?"
            $ a = Character('Astrid', color="#FF79E6", callback=astrid_voice)

            a "Aye aye Captain!"

            MC "Fine Astrid, you can simply call me [player_name] no need to use titles like that on land."

            a "Aye aye [player_name]!"

            jump school_entry

        "She’s Amazing":

            MC "That’s incredible, at ease Astrid of Bellewood."

            $ Astrid_affinity += 1

            $ a = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (1, "#000000") ])
            a "{color=#50A23B}Thank you Captain. Bellewood is actually my last name, I just thought it would sound cooler.{/color}"
            #{color=#00ff00}{/color}
            #play good boy points sound effect

            MC "It sure did sailor."

            jump school_entry

        "She’s Beautiful":

            "She’s stunningly beautiful!"

            $ Astrid_affinity += 3
            MC "Umm, at ease Astrid of Bellewood."

            $ a = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (1, "#000000") ])# turn outline on
            a "{color=#00ff00}Thank you Captain. Bellewood is actually my last name, I just thought it would sound cooler said like that.{/color}"
            #play good boy points sound effect

            MC "I’d agree. You can just call me [player_name]."

            $ a = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])# turn outline off
            a "Aye aye Captain [player_name]!"

            jump school_entry

        "{i}She has brain rot{/i}":

            MC "Have you acquired brian rot sailor?"

            $ Astrid_affinity -= 3
            $ a = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (1, "#000000") ])
            a "{color=#f00}No Captain, Sir!{/color}"
            # play bad boy sound effect

            MC "Then why are you screaming bloody murder at me?"

            $ a = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])
            a "To show my respect Captain, Sir!"

            MC "You can just call me [player_name], stop yelling please."

            a "Aye aye Captain [player_name]!"

            a "You can just call me Astrid, Captain [player_name]."
            $ a = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])

            jump school_entry

    label school_entry:

        $ a = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])
        a "Welcome to {color=#5FAFF6}Seaborough{/color} high school."

        a "I’m the current president of the Pirate Culture Club here. I’ll assume from your breezy shirt and filthy pants you’re a pirate of {color=#f00}The Red Plague{/color}."

        "Are my pants filthy?"

        "Covertly, I rub my thumb against the side of the leg. A black residue stains comes off on me. I thought these pants were a dark color."

        "What color are my pants?!"

        MC "Yes, that’s me. I’m the first mate."

        MC "The um, Captain sent me instead. We are here on important business and he was needed elsewhere."

        a "That makes sense. It was a longshot to try to get the big demon to show up at a high school anyway."

        "The big demon?"

        a "Well [player_name] you seem pretty cool."

        a "Come on inside and meet the rest of the club. They should be almost done setting up."

        "{cps=10}I seem cool!{/cps}"

        "{cps=20}A girl my age thinks I’m cool!{/cps}"

        "Cool is good, I'm almost certain of it."

        MC "That’s cool, lead the way."

        scene BG hw with fade

        "Astrid is guiding me through a labyrinth of dull hallways. Every corridor looks identical to the last, only a few pieces of colored paper lining the door frames give off any sense of divergency."

        "They’re so eerily empty, aif someone was meant to jump out and scare me. Our footsteps echo off the walls, enhanced by the silence. Astrid stops at a closed door on our left side."

        show a_d at center with dissolve
        a "This is it, our humble club appointed classroom. It isn't very flashy, so don't expect it to be overflowing with pirate stuff."

        a "Are you ready to meet everyone?"

        menu:
            "As ready as I can be":

                MC "Arrrrrgh, you bet Astrid."

                a "Definitely give them your best pirate \"arrrr\" right away. It’ll solidify you right away."

                jump classrooom_one

            "No wait":

                MC "Wait Astrid."

                a "Yeah? What’s up?"

                jump classroom_hesitation

        label classroom_hesitation:

            menu:
                "Anything I should know?":

                    MC "Anything I should know before going in?"

                    a "Hmmmmmmmmmm."

                    a "Don’t expect a big crowd. It’s like, just us on the e-board and a few straggling members who were in there before I went to get you."

                    a "We advertised that a real pirate would be coming but either nobody believed us or nobody cared. There’s some benefits to being a smaller club, but yeah not too much."

                    MC "Oh, I’m sorry about that."

                    a "Don’t be. We aren’t a huge club for more than a few reasons. Most of the pirate stuff is just an excuse for us all to hangout."

                    MC "I understand."

                    a "But we do like pirate things. You’re gonna be great in there, I’m sure of it [player_name]."

                    MC "Thank you Astrid. I’ll put my best foot forward as they say."

                    a "Great, but I don’t think anyone says that anymore."

                    jump classrooom_one

                "Anything I should say?":

                    MC "Anything I should say to them?"

                    a "Give everyone a good story and a hardy \"arrrrrrgh\". Also they’re probably going to ask you a bunch of questions."

                    a "I’m holding all mine in right now by a thread. Why did I say that?"

                    "Her gaze swiftly averts to the lockers on the wall. No problem answering questions, but if they start getting repetitive I’ll cut her off."

                    MC "I’ll give it the ol’pirate try."

                    a "Is that a thing?"

                    MC "Not yet, pirates aren’t too keen on learning new lingo."

                    a "Well maybe you can pick up some new ones here."

                    jump classrooom_one

        label classrooom_one:

            #open door sounds
            scene BG cr with fade

            "The door opens to a barren classroom with no more than eight people in it. There are some skulls and hearts drawn on the whiteboard, yet the rest of the room has been thoroughly cleaned."

            "Or at least has been kept this clean intentionally. It reminds me of how the ship looked with none of the supplies on it when."

            show a_d at center

            a "{cps=80}Everyone! Attention!{/cps}"

            if player_identity == "f":
                a "This is [player_name]. She’s a member of {color=#f00}The Red Plague{/color} pirate ship that terrorizes the Gulf of Mexico and all the surrounding waters."
            elif player_identity == "m":
                a "This is [player_name]. He’s a member of {color=#f00}The Red Plague{/color} pirate ship that terrorizes the Gulf of Mexico and all the surrounding waters."
            else:
                a "This is [player_name]. They're a member of {color=#f00}The Red Plague{/color} pirate ship that terrorizes the Gulf of Mexico and all the surrounding waters."

            a "Why don’t you introduce yourself [player_name]? Say a little about yourself too."
            hide a_d with dissolve
            show b_d at right
            show g_d at center
            show f_d at left
            MC "Yeah, I’m capable of that."

            $ f_met = 0
            $ g_met = 0
            $ b_met = 0

            menu:
                "Be honest with them":

                    MC "Hello everybody. My name is [player_name], but you already knew that. I’ve been a pirate my whole life and served on {color=#f00}The Red Plague{/color} during that time."

                    MC "Most days at sea are treacherous and exhausting, but the life is free and can be very rewarding. I had to work my way towards  becoming the first mate in that time."

                    MC "However, ranks only come with more responsibility on pirate ships. It doesn’t automatically earn you respect."

                    "Someone is holding their hand above their head all of a sudden. Did I do something wrong? Is this a test?"

                    "If I pause Astrid should get the hint."

                    a "Oh!"

                    a "That’s a high school thing. We raise our hands when we have a question as to not blurt them out when someone is talking."

                    a "That’s Fiona, she’s our Vice President."

                    hide g_d
                    hide b_d
                    show f_d at center with dissolve

                    MC "What’s your question Fiona?"

                    $ f = Character('Fiona', color="#E44D1A", callback=fiona_voice)# Fiona
                    f "What earns you respect on pirate ships? Do you have to be a big strong man to get it?"

                    "Her tone makes it sound like she already knows the answer. Captain does a similar trick."

                    MC "What earns you respect?"

                    MC "From my experience, it’s feats and age. I feel as if I’ve done some pretty heroic things for the greater crew, but I’m treated like I was kidnapped yesterday."

                    MC "As for your second concern, our ship has had many prominent women figures throughout its voyage. And I’ve met a handful of retired female Captains in our travels."

                    MC "On the sea, when you’re fighting for everything you got, the only thing that matters is your merit."

                    f "{color=#50A23B}Well that’s a pleasant surprise.{/color}"

                    MC "Being a pirate is all about how good you are at the job. There have been some amazing pirates who are unbearable to talk to and be around."

                    MC "But when the going gets tough, a great pirate tightens their buckle and draws their sword."

                    "The room rings with a  small wave of applause. I’ve never been clapped at before."

                    $ Fi_affinty += 1
                    $ f_met += 1
                    jump classrooom_two

                "Exaggerate to sound cool":

                    MC "Ahoy everyone! I’m the Dreaded Pirate [player_name]."

                    MC "{color=#f00}The Red Plague{/color} and I have been ruling the southern seas for over fifty years. I’ve seen the coolest things the world has to offer and I haven’t paid for a single thing in my entire life."

                    MC "We steal exports, we swipe imports, we take minerals, products, people, and sink ships of anyone who offends our noses. Our brutal tactics made us a scourge of the Atalantic."

                    "Some girl in front is raising her arm above her head. Is she calling me out? Does Astrid know what she’s doing?"

                    a "Oh!"

                    a "That’s a high school thing. We raise our hands when we have a question as to not blurt them out when someone is talking."

                    a "That’s G, she’s our club’s Secretary."

                    hide f_d
                    hide b_d
                    show g_d at center with dissolve

                    MC "Aye lass, what’s yer question?"

                    $ g = Character('G', color="#DFDABB", callback=g_voice)# Geraldine
                    g "Hi [player_name], loving the accent by the way. Question."

                    g "What’s the coolest thing you’ve seen while stealing something? Like anything wackier than the average haul?"

                    "She called me out!"

                    MC "Well, let me think on that. Hmmmmmmm."

                    MC "It would have to be that time I saw Poseidon himself do his duty. We stole a Mexican vessel’s shipment full of beers and sodas."

                    MC "Their boss begged the Captain on his hands and knees to spare their lives. He offered to share his best whiskey with the Captain to convince him."

                    MC "The drink was so good that, according to the Demonic Pirate himself, he allowed them to pass his sea."

                    MC "As we sailed away from the ship a storm started to shake up the waves. I turned towards the ship and one sailor was loading a rocket propelled grenade and aimed it at our tail."

                    MC "Before I could brace for impact, an uncharacteristically powerful wave for that stage of the storm was knocked into the Mexican ship."

                    MC "The sailor must have been hit hard because his ship exploded right as they got hit. And our lives were saved by his divine decision."

                    g "That sounds so cool. Did the ship sink?"

                    MC "Straight into Davy Jones."

                    g "I feel so much better now that I know Poseidon is real. Did you guys know this and not tell me?"

                    $ G_affinity += 1
                    $ g_met += 1
                    jump classrooom_two

                "Scare them away from piracy":

                    MC "Alright lassies here’s the dark truth from a subordinate of the Demonic Pirate Ricardo himself."

                    MC "Piracy is incredibly dangerous. Our lives are on the line everyday. We could be shot at, thrown overboard, or starved at sea."

                    MC "Constantly fighting for life and death just for a sliver of profits is a dreary way to live."

                    MC "Our living quarters are dank and grim. I had to burn through skin and bones to get a proper bed when I was fifteen."

                    MC "Pirates are the worst type of people. They’re remorseless thieves and you’re treated like dirt unless you’re in charge."

                    "Some girl in front is raising her arm up in the air. Is she trying to question me? Does Astrid know what she wants me to do?"

                    a "Oh! That’s a high school thing."

                    a "We raise our hands when we have a question as to not blurt them out when someone is talking. That’s Behati, our club's Treasurer."

                    hide g_d
                    hide f_d
                    show b_d at center with dissolve

                    $ b = Character('Behati', color="#5E0F60", callback=b_voice)# Behati
                    MC "Aye lass, what’s the problem?"

                    b "Y-yes hello, [player_name] isn’t it true that eight-six to ninety-nine percent of total goods stolen are raw material exports that the government plans to lose in their budgets?"

                    b "Ones that crews are instructed to not fight over and to protect themselves? Wouldn’t that make the act of piracy a part of the system as a whole and not an outlier?"

                    "What is she even talking about?"

                    MC "Do I look like someone who's familiar with your mainland statistics?"

                    b "Well y-you can account for your own ship’s actions, r-right?"

                    MC "Aye, well it’s true that American vessels tend to avoid us at all costs, others aren’t so cautious."

                    MC "We don’t steal from just governments. Other pirates and pleasure cruises are prime targets for loot of all kinds."

                    b "Are t-those unaccounted for in your main piracy focus?"

                    b "B-because how would you know where another pirate ship is going to be?"

                    b "Or if, if some oil millionaire’s kid is going on a joyride?"

                    MC "Behati was it?"

                    b "Yes that’s me."

                    MC "Pirates don’t have quotas or missions."

                    MC "We take advantage of opportunities and solve problems we come across with the tools at our disposal. The grand plan is wild riches and being free."

                    MC "No matter the costs."

                    b "T-thank you for your honesty. That’s a lot to consider."

                    $ Be_affinity += 1
                    $ b_met += 1
                    jump classrooom_two

        label classrooom_two:

    return
