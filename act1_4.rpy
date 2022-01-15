label act1_4:

# redefine bc I want to deal with it
$ mc = Character("[player_name]", color="#990033", callback=voice)

show BG schoolan with dissolve

"Coming out of the school the sun is starting to set. To see a sunset from land and not the sea is sort of, underwhelming."

"Instead of the light reflecting off the pristine water, it’s bouncing on concrete and buildings."

"The shadows of the trees are nice, but it’s just not the same."

"That trip did not go as I had planned it."

"I think I expected the {i}Admiral's son{/i} treatment from them, some pompous wannabes pretending to act like pirates."

"A group of genuine people my age who wanted to know more about me and pirates, that was a shock."

"Talking about the life I live outside of my own bubble for an afternoon was humbling."

"All of that really puts my land confliction in perspective."

show BG walksunset with dissolve

"There’s a quiet hum of the town through the trees."

"Not like before with all the people around, a sleepy days end feeling."

"I assumed that since all the people were here that this place would never sleep."

"Not like at sea, where the waves drown out any silence and storms grab your attention greater than any conversation would."

"I belong out there, soaring on the ocean’s surface."

"Out there I’m needed and revered. Even if the whole crew doesn’t treat me like it, I know they need me."

"It’s the subtle things that keep the peace between everyone. A good deed here or there."

"Getting a second serving of food, someone cleaning your pistol without asking, the way Ol’ Two Hands makes sure I get my work done on time so that he has someone to play chess with later."

"I have people in my life who already value me, there’s little need to look towards the mainland for alternatives."

"Now that I’m an adult, opportunities might start opening up for me."

"If the Captain acknowledges it, then there could be something down the line waiting for me."

"One day I could have my own crew. I could be the next Demonic Pirate Captain."

"Who knows? Let’s see what life hurls at me next."

"The next few years may be my best yet."

window hide
show BG black with dissolve
pause 3.0

play effect "audio/thunder.ogg"
show BG 4 with hpunch

play music "audio/storm1.mp3" loop
pause 5.0
jump ship_start

label ship_start:

    define pirate_lines = ["Arrrgh, not good enough!", "Arrrgh, where ye goin', ah?", "Har har harrr!", "Yurr a dead man!"]
    define random_line = renpy.random.randint(0, 3)

    show BG nightdeck1 with dissolve

    jj "{cps=20}Ahhhhgrrrrh!{/cps}"

    jj "{cps=25}[player_name], get out of here! Find the Captain!{/cps}"

    jj "{cps=25}Find the Captain!{/cps}"

    jj "{cps=20}Ahhhhhhhhhhhhhgggggguuuuuuuuuuu!{/cps}"

    mc "JoeJoe no! Don’t stop fighting!"

    mc "JoeJoe...is..."

    "This can’t be happening. Where did these other pirates come from?"

    "They came out of nowhere, how did they board the ship without anyone noticing in time?"

    "Crawling from below the deck and from the sides of the boat. It’s like an infestation."

    "This storm is the perfect cover for a raid. These pirates aren’ taking some pot shot, this was a well coordinated attack. "

    show sword at sword
    play effect "audio/sworddraw.ogg"

    "My gun is disassembled in my room, this will have to do."

    "I have to find out who’s still fighting. There’s no telling how many of these lunatics got onboard."

    "We need to band together to protect whoever is steering the ship."

    "Hopefully the Captain has a handle on the situation."

    show pirate1 with dissolve
    p "Well look at ye. They let kids roam 'round a graveyard?"

    p "Hey boys, we got another-!"

    call screen pirate_fight1_0

    label pirate_fight1_re:

        show sword swing at sword with ease
        play effect "audio/sword_clash.ogg"
        show BG nightdeck1 with flash

        show sword at sword with ease
        $ p_line = pirate_lines[random_line]
        p "[p_line]"
        call screen pirate_fight1_0


    label pirate_fight1:

        $ quick_menu = False

        show sword swing at sword with ease
        play effect "audio/sword_swing.mp3"

        show BG nightdeck1 with flash
        show pirate1 slash at wiggle

        show sword at sword with ease
        p "Ahhrggggghh!"

        hide pirate1 slash with dissolve


    $ quick_menu = True

    "There isn’t enough intel, I don't know how many of them there are or if I could kill them all."

    "Getting surrounded is an easy possibility when you don’t know how many enemies you have. Especially when you don’t know where they’re coming from."

    show BG nightdeck2 with dissolve

    "Poseidon appears to not be on our side tonight."

    show pirate2 with dissolve

    p "Yer a dead man matey!"

    define matey = 0 # to determine if another pirate joins the fray
    define death_count = 3 # count for death in the second fight
    define x_naut = 0 # additional dialoge check
    define pirate1_x = 2 # alive status
    define pirate2_x = 2 # alive status

    # list of respones between slashes
    define dying = ["I have to thin their numbers or I'll be turned into drift wood.", "Need to take'em out!", "I should avoid being dog piled.", "I have to cut their numbers down for everyone's sake."]
    define rand2 = renpy.random.randint(0, 3)

    call screen pirate_fight2_0

    label pirate_fight2_re: # loop when character clashes swords with pirates second fight

        $ quick_menu = False
        $ notded = dying[rand2]

        if death_count == 0:

                jump game_over

        if matey < 2 and death_count != 0: # only the first pirate is here

            if pirate1_x == 3:

                show sword swing at sword with ease
                play effect "audio/sword_clash.ogg"
                show BG nightdeck2 with flash

                show sword at sword with ease
                $ random_line = renpy.random.randint(0, 3)
                $ p_line = pirate_lines[random_line]
                p "[p_line]"

                $ matey += 1
                $ death_count -= 1

                if x_naut == 0 and matey == 2: # appearence of 2nd pirate

                    show pirate3 at left with moveinleft

                    p "Mind if I CUT in?"
                    $ x_naut += 1
                    call screen pirate_fight2_1

                call screen pirate_fight2_0

            if matey >= 2 and matey != 4:

                jump pirate_fight2_re

            else:

                call screen pirate_fight2_0

        elif matey >= 2 and death_count != 0: # second pirate appears

            if pirate1_x == 3 or pirate2_x == 3:

                show sword swing at sword with ease
                play effect "audio/sword_clash.ogg"
                show BG nightdeck2 with flash

                show sword at sword with ease
                $ random_line = renpy.random.randint(0, 3)
                $ p_line = pirate_lines[random_line]
                p "[p_line]"

                $ matey += 1
                $ death_count -= 1

                call screen pirate_fight2_1

    label pirate_fight2_1: # when pirate 1 of the fight dies

        if pirate1_x == 1:

            show sword swing at sword with ease
            play effect "audio/sword_swing.mp3"

            show BG nightdeck2 with flash
            show pirate2 slash at wiggle

            show sword at sword with ease
            p "Ahhhhh, damn ye!"

            hide pirate2 slash with dissolve

            $ pirate1_x = 0
            $ death_count += 1

            if pirate1_x == 0 and pirate2_x == 0:
                jump final_bout
            elif matey < 2:
                jump final_bout
            else:
                show pirate3 at center with moveinleft
                call screen pirate_fight2_2


    label pirate_fight2_2: # if and when pirate 2 of the fight dies

        if pirate2_x == 1:

            show sword swing at sword with ease
            play effect "audio/sword_swing.mp3"

            show BG nightdeck2 with flash
            show pirate3 slash at wiggle

            show sword at sword with ease
            p "Curse yeeeeee!"

            hide pirate3 slash with dissolve

            $ pirate2_x = 0
            $ death_count += 1

            if pirate1_x == 0 and pirate2_x == 0:
                jump final_bout
            else:
                call screen pirate_fight2_0

    label final_bout:

        define matey2 = 0 # to determine if another pirate joins the fray
        define x_nautz = 0 # additional dialoge check
        define x_nautzz = 0 # additional dialoge check
        define pirate3_x = 2 # alive status
        define pirate4_x = 2 # alive status
        define pirate5_x = 2 # alive status
        $ death_count = 5 # count for death in the third fight

        $ quick_menu = True

        "Where is everyone? There must be someone around to help."

        "There is no way anyone has stoppenotd fighting!"

        "The Plague isn’t made up of pushovers."

        "What kind of pirates are these people to pull off such a direct attack?"

        show pirate4 at center with dissolve# change this pirate
        p "Say a prayer sea dog!"

        show flavio scared at leftbottom with dissolve

        fla "No wait I-"

        play effect "audio/bam.ogg"
        show BG nightdeck2 with flash
        show flavio scared with ease: # Flavio gets shot off screen
            xpos -1000 ypos 2000

        mc "{cps=10}Flavio!{/cps}"

        p "Ye wanna try me now scumbag?"

        call screen pirate_fight3_0

    label pirate_fight3_re: # loop when character clashes swords with pirates last fight

        $ quick_menu = False
        $ notded = dying[rand2]

        if death_count == 0:

                jump game_over

        if matey2 == 0 and death_count != 0: # only 1st first pirate is here

            show sword swing at sword with ease
            play effect "audio/sword_clash.ogg"
            show BG nightdeck2 with flash

            show sword at sword with ease
            $ random_line = renpy.random.randint(0, 3)
            $ p_line = pirate_lines[random_line]
            p "[p_line]"

            $ matey2 += 1
            $ death_count -= 1

            if x_nautz == 0 and matey2 == 1: # appearence of 2nd pirate

                show pirate5 at left with moveinleft

                p "Need a hand?"
                $ x_nautz += 1
                call screen pirate_fight3_1

        elif matey2 >= 1 and death_count != 0: # only 2 pirates are here

            show sword swing at sword with ease
            play effect "audio/sword_clash.ogg"
            show BG nightdeck2 with flash

            show sword at sword with ease
            $ random_line = renpy.random.randint(0, 3)
            $ p_line = pirate_lines[random_line]
            p "[p_line]"

            $ matey2 += 1
            $ death_count -= 1

            if x_nautzz == 0 and matey2 == 3: # appearence of 3rd pirate

                show pirate6 at centerrighter behind sword with moveinbottom

                p "Time to meet Davey Jones!"
                $ x_nautzz += 1
                call screen pirate_fight3_2

            call screen pirate_fight3_1

        elif matey2 >= 3 and death_count != 0: # only 3 pirates are here

            show sword swing at sword with ease
            play effect "audio/sword_clash.ogg"
            show BG nightdeck2 with flash

            show sword at sword with ease
            $ random_line = renpy.random.randint(0, 3)
            $ p_line = pirate_lines[random_line]
            p "[p_line]"

            $ matey2 += 1
            $ death_count -= 1

            jump pirate_fight3_re

    label pirate_fight3_1:

        if pirate3_x == 1 and matey2 >= 3:

            show sword swing at sword with ease
            play effect "audio/sword_swing.mp3"

            show BG nightdeck2 with flash
            show pirate4 slash at wiggle

            show sword at sword with ease
            p "Ahhhhh, damn ye!"

            hide pirate4 slash with dissolve

            $ pirate3_x = 0
            $ death_count += 1

            if pirate3_x == 0 and pirate4_x == 0 and pirate5_x == 0:

                jump down_with_the_ship

            elif matey2 == 0:

                jump down_with_the_ship

            elif pirate4_x != 0 and pirate5_x != 0: # pirate 4 and 5 are alive

                call screen pirate_fight3_3

            elif pirate4_x != 0 and pirate5_x == 0: # pirate 4 is alive

                call screen pirate_fight3_4

            elif pirate4_x == 0 and pirate5_x != 0: # pirate 5 is alive

                call screen pirate_fight3_5

        else:

            show sword swing at sword with ease
            play effect "audio/sword_swing.mp3"

            show BG nightdeck2 with flash
            show pirate4 slash at wiggle

            show sword at sword with ease
            p "Ahhhhh, damn ye!"

            hide pirate4 slash with dissolve

            $ pirate3_x = 0
            $ death_count += 1

            if pirate3_x == 0 and pirate4_x == 0: # pirate 3 and 4 are dead without 5

                jump down_with_the_ship

            elif pirate3_x == 0 and pirate4_x != 0: # pirate 3 is dead and 4 is alive without 5

                call screen pirate_fight3_4

            elif pirate3_x != 0 and pirate4_x == 0: # pirate 4 is dead and 3 is alive wthout 5

                call screen pirate_fight3_0

    label pirate_fight3_2:

        if pirate4_x == 1 and matey2 >= 3:

            show sword swing at sword with ease
            play effect "audio/sword_swing.mp3"

            show BG nightdeck2 with flash
            show pirate5 slash at wiggle

            show sword at sword with ease
            p "I'll see ye in Hell!"

            hide pirate5 slash with dissolve

            $ pirate4_x = 0
            $ death_count += 1

            if pirate3_x == 0 and pirate4_x == 0 and pirate5_x == 0:

                jump down_with_the_ship

            elif pirate3_x != 0 and pirate4_x != 0 and pirate5_x == 0:

                call screen pirate_fight3_1

            elif pirate3_x == 0 and pirate4_x != 0 and pirate5_x != 0:

                call screen pirate_fight3_3

            elif pirate3_x == 0 and pirate4_x == 0 and pirate5_x != 0:

                call screen pirate_fight3_5

            elif pirate3_x != 0 and pirate5_x != 0: # pirate 3 and 5 are alive

                call screen pirate_fight3_6

            elif pirate3_x != 0 and pirate5_x == 0: # pirate 3 is alive

                call screen pirate_fight3_0

            elif pirate3_x == 0 and pirate5_x != 0: # pirate 5 is alive

                call screen pirate_fight3_5

        else:

            show sword swing at sword with ease
            play effect "audio/sword_swing.mp3"

            show BG nightdeck2 with flash
            show pirate5 slash at wiggle

            show sword at sword with ease
            p "I'll see ye in Hell!"

            hide pirate5 slash with dissolve

            $ pirate4_x = 0
            $ death_count += 1

            if pirate3_x == 0 and pirate4_x == 0: # pirate 3 and 4 are dead without 5

                jump down_with_the_ship

            elif pirate3_x == 0 and pirate4_x != 0: # pirate 3 is dead and 4 is alive without 5

                call screen pirate_fight3_4

            elif pirate3_x != 0 and pirate4_x == 0: # pirate 4 is dead and 3 is alive wthout 5

                call screen pirate_fight3_0

    label pirate_fight3_3:

        if pirate5_x == 1:

            show sword swing at sword with ease
            play effect "audio/sword_swing.mp3"

            show BG nightdeck2 with flash
            show pirate6 slash at wiggle

            show sword at sword with ease
            p "Shannon, farewell."

            hide pirate6 slash with dissolve

            $ pirate5_x = 0
            $ death_count += 1

            if pirate3_x == 0 and pirate4_x == 0 and pirate5_x == 0:

                jump down_with_the_ship

            elif pirate3_x != 0 and pirate4_x != 0: # pirate 3 and 4 are alive

                call screen pirate_fight3_1

            elif pirate3_x == 0 and pirate4_x != 0: # pirate 4 is alive

                call screen pirate_fight3_4

    label down_with_the_ship:

        hide sword
        mc "Flavio, say something matey."
        $ quick_menu = True

        "The bullet went clean through his head."

        "The horror still stained on Flavio’s face tells me more than that he just lost a duel. His arms and torso have slash marks all over them."

        if matey2 >= 2:
            "Just like now, he was ganged up on. I couldn’t have save him."
        else:
            "He was ganged up on. I couldn’t have save him."

        "He was never the greatest fighter, but this wasn’t fair."

        mc "We’ll get out of this Flavio, you rest here."

        play effect "audio/fire.ogg" loop

        "Hopefully the Captain is holding out alright."

        "Is that a crackling?"

        "A fire!"

        "Where is it coming from?"

        "Above?"

        "Top deck is too wet to start one. But below..."

        "Right below our noses, they're snuffing us out!"

        "The storm won’t put anything out if the ship’s a charred mess of driftwood."

        "These bastards. They aren’t here to rob us, they’re taking out the Plague for good."

        "Our crimes have come back to damn us like a vengeful revenant."

        show pirate8 with dissolve

        p "Ye-"

        mc "Get out of my way!"

        show sword swing at sword with ease
        play effect "audio/sword_swing.mp3"

        show BG nightdeck2 with flash
        show pirate8 slash at wiggle

        show sword at sword with ease
        hide pirate8 slash with dissolve

        th "[player_name] behind ye!"

        show pirate8 at left with dissolve

        show sword swing at sword with ease
        play effect "audio/sword_clash.ogg"
        show BG nightdeck2 with flash
        show sword at sword with ease

        show sword swing at sword with ease
        play effect "audio/sword_swing.mp3"
        show BG nightdeck2 with flash
        show pirate8 slash with dissolve

        show sword at sword with ease
        hide pirate8 slash with dissolve

        hide sword with ease
        show twohands scared dark with dissolve

        mc "Two Hands! Are you alright?"

        mc "Have both your hands? Where’s the Captain?"

        if player_identity == "f":
            th "Aye lass I’ll live a little longer!"
        else:
            th "Aye lad I’ll live a little longer!"

        show twohands sweaty dark with ease

        th "Both claws intact as you can see."

        th "Da Captains fighting to steer thee ship."

        mc "Is anyone else still fighting? Who’s alive?"

        th "Arrrrrrggghh."

        show twohands dark with ease

        th "I’ve seen more corpses den pirates now. I don’t know whos still kicking."

        th "It may be just you and me now."

        mc "We have to help the Captain and regain control of the ship."

        if player_identity == "f":
            th "Aye lass, I’ll clear the way of remaining renegades."
        else:
            th "Aye lad, I’ll clear the way of remaining renegades."

        show twohands angry dark with ease

        th "Time to take our ship back."

        mc "Let me help."

        th "Not on yer life!"

        th "Help thee Captain and steer us outta dis storm."

        mc "You can't tell me what to do!"

        th "Aye, I'm telling ye now!"

        show twohands angry dark flip with ease
        th "Fight me you cowards!"

        mc "Thank you Hans"

        hide twohands angry dark flip with moveoutleft
        th "Arrrrrgh!"

        "Without a shred of hesitation, Two Hands rushes on ahead."

        "Were there never a pirate braver him?"

        th "...I’ll cut yer throats..."

        "I won’t let his sacrifice lay dead at sea."

        stop effect fadeout 3.0
        show BG nightdeck3 with dissolve

        "Avoiding the sounds of gunshots and clashing swords I’m able to get to the poop deck undetected."

        "If I make it out of this, Two Hands can have any of my sweets for the rest of the year."

        "The rest of my life, if he makes it back too."

        "There’s a pile of bodies stacked up by the wheel with one person sitting up against it."

        "The figure is struggling to hold their gun straight."

        mc "Captain is that you?"

        hide sword
        show cap bloody at ground with dissolve

        "One, two, five, how many bodies are there?"

        "All these pirates flocked to the wheel?"

        mc "Did you kill them all Captain?"

        if player_identity == "f":

            Cap "Aye lass it’s me. And I did."

        else:

            Cap "Aye lad it’s me. And I did."

        Cap "Looks like they got the jump on us aye?"

        show cap bloody yelling with dissolve

        play effect "audio/cough.ogg"
        pause 5.25

        show cap bloody with dissolve

        mc "You’ve been shot!"

        "Multiple holes and lashes all over his body as if he jumped on an entire army."

        "His coat is soaked in blood and most of it looks like his. I don’t know if he’s gonna make it."

        mc "Captain hang on, Two Hands will be here soon and we’ll finish this."

        Cap "Aye don’t think so matey. At least six men got past me, well armed too."

        Cap "I’m afraid Two Hands is as good as gone. Unless he found some more hands?"

        show cap bloody yelling with dissolve

        Cap "Har har haaaa!"

        play effect "audio/cough2.ogg"
        pause 3.25

        show cap bloody with dissolve

        mc "Captain, what do you do? What should I do?"

        Cap "It appears like arrr sun is setting."

        Cap "The Red Plague will not see the calm after this storm."

        mc "This can’t be how it ends Captain. We can keep fighting!"

        show cap bloody yelling with dissolve

        Cap "[player_name] look at me!"

        Cap "Look at me my child!"

        Cap "This is the end for me, for the Plague. But this ain't where yer story ends."

        Cap "Look behind me. Take it and go."

        show BG nightdeck3 at zoom
        hide cap bloody yelling

        mc "A dingy"

        show BG nightdeck3 at redo with ease
        show cap bloody

        Cap "Take it and go [player_name]."

        show cap bloody yelling with dissolve

        play effect "audio/cough2.ogg"
        pause 3.25

        show cap bloody with dissolve

        Cap "There ain't much time left. Keep the legend alive."

        Cap "Become the pirate ye were born te be."

        "The wind is stirring up the smoke. It’s only a matter of time before the ship meets its end."

        "If I stay I’ll either be roasted by the flames or buried under the sea floor."

        mc "Captain come with me, we can escape tog-"

        play effect "audio/thunder.ogg"
        show BG nightdeck3 with flash_lighting

        show cap bloody yelling with dissolve

        Cap "Ar Ye Daft?!"

        Cap "A Captain goes down with his ship! Ye know that by now!"

        Cap "Besides, I’ll be dead weight before ye hit the water."

        Cap "Go [player_name], live, I believe ye."

        mc "Captain I can’t go, I just-"

        p "Over here! I hear'em."

        p "Get to the helm now!"

        Cap "I’m not asking ye. This is an order."

        Cap "Go now!"

        show cap bloody with dissolve

        mc "Aye Captain. I’ll go."

        mc "It was an honor serving in your crew. Thank you for everything Father,"

        mc "you’ll be with Mother soon-"

        Cap "… … … … …"

        mc "Farewell Captain. May you torment the Underworld for eternity."

        hide sword # incase its still there in some cases or my save skumming is catching up

        hide cap with dissolve
        show BG black with dissolve
        play effect "audio/splash.ogg"
        pause 1.5

        show BG escape with dissolve

        play effect "audio/thunder.ogg"
        show BG escape with flash_lighting
        pause 2.5

        play effect "audio/fire.ogg" fadein 2.0 loop volume 5.0

        "A pirate’s dream of absolute freedom only dies when they are all good and dead. Every ounce of gunpowder or barrel of cannonballs couldn't kill this dream."

        "Some broken planks and burnt sails are just that. Nothing more than trash to let me engulf by the sea."

        "Nothing stays where you left it. But isn't that exciting?"

        pause 10.0

        stop effect
        show BG black with fade
        jump act1_5

return
