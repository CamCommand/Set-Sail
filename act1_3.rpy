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

    show astrid_default at center with dissolve

    MC "Uh, hello. You waiting for me lass?"

    # I redefine Astrid so much to change her name per the situation
    # I will also use the what_outline parameter to show feedback for positive choices
    $ As = Character('Girl', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])
    As "{cps=80}Ahhoooo{/cps}{cps=5}OOOOOOOOOOOO{/cps}{cps=50}oooooy Matey!{/cps}"

    #$ astrid_temp = "Astrid of Bellewood"
    $ As = Character('Astrid of Bellewood', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])
    As "{cps=75}I’m Officer Astrid of Bellewood at Seaborough High School! Permission To Speak Easy Captain, Sir?!{/cps}"

    "Poseidon help me this girl is..."

    menu:# MC's different reactions to first meeting Astrid
        "She’s Enthusiastic":

            MC "Are you insane?"

            MC "No need to yell at me, Astrid of Bellewood."

            As "Thank you Captain. Bellewood is actually my last name, I just thought it would sound cooler in my introduction."

            MC "Can I just call you Astrid?"
            $ As = Character('Astrid', color="#FF79E6", callback=astrid_voice)

            As "Aye aye Captain!"

            MC "Fine Astrid, you can simply call me [player_name] no need to use titles like that on land."

            As "Aye aye [player_name]!"

            jump school_entry

        "She’s Amazing":

            MC "That’s incredible, at ease Astrid of Bellewood."

            $ Astrid_affinity += 1

            $ As = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (1, "#000000") ])
            As "{color=#50A23B}Thank you Captain. Bellewood is actually my last name, I just thought it would sound cooler.{/color}"
            #{color=#00ff00}{/color}
            #play good boy points sound effect

            MC "It sure did sailor."

            jump school_entry

        "She’s Beautiful":

            "She’s stunningly beautiful!"

            $ Astrid_affinity += 3
            MC "Umm, at ease Astrid of Bellewood."

            $ As = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (1, "#000000") ])# turn outline on
            As "{color=#00ff00}Thank you Captain. Bellewood is actually my last name, I just thought it would sound cooler said like that.{/color}"
            #play good boy points sound effect

            MC "I’d agree. You can just call me [player_name]."

            $ As = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])# turn outline off
            As "Aye aye Captain [player_name]!"

            jump school_entry

        "{i}She has brain rot{/i}":

            MC "Have you acquired brian rot sailor?"

            $ Astrid_affinity -= 3
            $ As = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (1, "#000000") ])
            As "{color=#f00}No Captain, Sir!{/color}"
            # play bad boy sound effect

            MC "Then why are you screaming bloody murder at me?"

            $ As = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])
            As "To show my respect Captain, Sir!"

            MC "You can just call me [player_name], stop yelling please."

            As "Aye aye Captain [player_name]!"

            As "You can just call me Astrid, Captain [player_name]."
            $ As = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])

            jump school_entry

    label school_entry:

        $ As = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])
        As "Welcome to Seaborough high school."

        As "I’m the current president of the Pirate Culture Club here. I’ll assume from your breezy shirt and filthy pants you’re a pirate of {color=#f00}The Red Plague{/color}."

        "Are my pants filthy?"

        "Covertly, I rub my thumb against the side of the leg. A black residue stains comes off on me. I thought these pants were a dark color."

        "What color are my pants?!"

        MC "Yes, that’s me. I’m the first mate."

        MC "The um, Captain sent me instead. We are here on important business and he was needed elsewhere."

        As "That makes sense. It was a longshot to try to get the big demon to show up at a high school anyway."

        "The big demon?"

        As "Well [player_name] you seem pretty cool."

        As "Come on inside and meet the rest of the club. They should be almost done setting up."

        "{cps=10}I seem cool!{/cps}"

        "{cps=20}A girl my age thinks I’m cool!{/cps}"

        "Cool is good, I'm almost certain of it."

        MC "Sounds cool, lead the way."

    return
