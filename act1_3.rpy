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

    return
