label act1_4:


$ mc = Character("[player_name]", color="#990033", callback=voice)# redefine bc I want to deal with it

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

show BG black with dissolve
pause 3.0
play effect "audio/thunder.ogg"
show BG 4 with hpunch
play music "audio/storm1.mp3" loop
pause 5.0
jump ship_start

label ship_start:

    show BG nightdeck1 with dissolve

    # JoeJoe freaking dies the movie
    # show joejoe dying quickly
    jj "{cps=20}Ahhhhgrrrrh!{/cps}"

    jj "{cps=25}[player_name], get out of here! Find the Captain!{/cps}"

    jj "{cps=25}Find the Captain!{/cps}"

    jj "{cps=20}Ahhhhhhhhhhhhhgggggguuuuuuuuuuu!{/cps}"
    # hide JoeJoe after death

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

    jump pirate_fight1

    label pirate_fight1:

        $ quick_menu = False

        menu:

            "Swing right!":

                show sword swing at sword with ease
                play effect "audio/sword_swing.mp3"

                show BG nightdeck1 with flash
                show pirate1 slash at wiggle

                show sword at sword with ease
                p "Ahhrggggghh!"

                hide pirate1 slash with dissolve

            "Swing left!":

                show sword swing at sword with ease
                play effect "audio/sword_clash.ogg"
                show BG nightdeck1 with flash

                show sword at sword with ease
                p "Arrrgh, not good enough!"

                jump pirate_fight1

            "Go for the legs!":

                show sword swing at sword with ease
                play effect "audio/sword_clash.ogg"
                show BG nightdeck1 with flash

                show sword at sword with ease
                p "Arrrgh, goin' fer me legs, ah?"

                jump pirate_fight1

    $ quick_menu = True

    "There isn’t enough intel, I don't know how many of them there are or if I could kill them all."

    "Getting surrounded is an easy possibility when you don’t know how many enemies you have. Especially when you don’t know where they’re coming from."

    show BG nightdeck2 with dissolve

    "Poseidon appears to not be on our side tonight."

    show pirate2 with dissolve

    p "Yer a dead man matey!"

    define matey = 0 # to determine if another pirate joins the fray
    define x_naut = 0 # additional dialoge check
    define pirate1_x = 1 # alive status
    define pirate2_x = 1 # alive status


    jump pirate_fight2

    label pirate_fight2:

        # list of respones between slashes
        define dying = ["I have to thin their numbers or I'll be turned into drift wood.", "Need to take'em out!", "I should avoid being dog piled.", "I have to cut their numbers down for everyone's sake."]
        define rand2 = renpy.random.randint(0, 3)

        $ quick_menu = False
        define notded = dying[rand2]
        if matey >= 2 and matey != 4:

            if x_naut == 0:
                show pirate3 at left with moveinleft

                p "Mind if I CUT in?"
                $ x_naut += 1

            $ notded = dying[rand2]
            mc "[notded]"

            menu:

                "Swing right at the first one!" if pirate1_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_swing.mp3"

                    show BG nightdeck2 with flash
                    show pirate2 slash at wiggle

                    show sword at sword with ease
                    p "Ahhhhh, damn ye!"

                    hide pirate2 slash with dissolve
                    show pirate3 at center with ease
                    $ pirate1_x -= 1

                    if pirate1_x == 0 and pirate2_x == 0:
                        jump final_bout
                    else:
                        jump pirate_fight2

                "Swing left at the first one!" if pirate1_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Not on yer life!"

                    $ matey += 1

                    jump pirate_fight2

                "Take out the legs of the first one!" if pirate1_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Can't have those!"

                    $ matey += 1

                    jump pirate_fight2

                "Swing right at the second one!" if pirate2_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Can't have those!"

                    $ matey += 1

                    jump pirate_fight2

                "Swing left at the second one!" if pirate2_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Not on yer life!"

                    $ matey += 1

                    jump pirate_fight2

                "Take out the legs of the second one!" if pirate2_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_swing.mp3"

                    show BG nightdeck2 with flash
                    show pirate3 slash at wiggle

                    show sword at sword with ease
                    p "Curse yeeeeee!"

                    hide pirate3 slash with dissolve
                    $ pirate2_x -= 1

                    if pirate1_x == 0 and pirate2_x == 0:
                        jump final_bout
                    else:
                        jump pirate_fight2

        elif matey == 4:

            show sword swing at sword with ease
            play effect "audio/sword_swing.mp3"
            show BG nightdeck2 with deathflash

            show sword at sword with ease
            mc "Uh no, I didn't get to save,"

            mc "Father, forgive me..."

            jump game_over

        menu:

            "Swing right!":

                show sword swing at sword with ease
                play effect "audio/sword_swing.mp3"

                show BG nightdeck2 with flash
                show pirate2 slash at wiggle

                show sword at sword with ease
                p "Ahhhhh, damn ye!"

                hide pirate2 slash with dissolve

            "Swing left!":

                show sword swing at sword with ease
                play effect "audio/sword_clash.ogg"
                show BG nightdeck2 with flash

                show sword at sword with ease
                p "Not on yer life!"

                $ matey += 1

                jump pirate_fight2

            "Take out the legs!":

                show sword swing at sword with ease
                play effect "audio/sword_clash.ogg"
                show BG nightdeck2 with flash

                show sword at sword with ease
                p "Can't have those!"

                $ matey += 1

                jump pirate_fight2

    label final_bout:

        define matey2 = 0 # to determine if another pirate joins the fray
        define x_nautz = 0 # additional dialoge check
        define x_nautzz = 0 # additional dialoge check
        define pirate3_x = 1 # alive status
        define pirate4_x = 1 # alive status
        define pirate5_x = 1 # alive status

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

        jump pirate_fight3

    label pirate_fight3:

        $ quick_menu = False

        if matey2 >= 1 and matey2 < 3:

            if x_nautz == 0:

                show pirate5 at centerlefter with moveinleft

                p "Need a hand?"
                $ x_nautz += 1

            $ notded = dying[rand2]
            mc "[notded]"

            menu:

                "Swing right at the first one!" if pirate3_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Har har harrr!"

                    $ matey2 += 1

                    jump pirate_fight3

                "Swing left at the first one!" if pirate3_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_swing.mp3"

                    show BG nightdeck2 with flash
                    show pirate4 slash at wiggle

                    show sword at sword with ease
                    p "I regret nothing..."

                    hide pirate4 slash with dissolve
                    $ pirate3_x -= 1

                    if pirate3_x == 0 and pirate4_x == 0 and pirate5_x:
                        jump down_with_the_ship
                    else:
                        jump pirate_fight3

                "Take out the legs of the first one!" if pirate3_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Try and take'em!"

                    $ matey2 += 1

                    jump pirate_fight3

                "Swing right at the second one!" if pirate4_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Yurr a dead man!"

                    $ matey2 += 1

                    jump pirate_fight3

                "Swing left at the second one!" if pirate4_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Why'duncha giv'er up?"

                    $ matey2 += 1

                    jump pirate_fight3

                "Take out the legs of the second one!" if pirate4_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_swing.mp3"

                    show BG nightdeck2 with flash
                    show pirate5 slash at wiggle

                    show sword at sword with ease
                    p "I'll see you in Hell!"

                    hide pirate5 slash with dissolve
                    $ pirate4_x -= 1

                    if pirate3_x == 0 and pirate4_x == 0 and pirate5_x:
                        jump down_with_the_ship
                    else:
                        jump pirate_fight3

        elif matey2 >= 3:

            if x_nautzz == 0:

                show pirate6 at centerrighter behind sword with moveinbottom

                p "Time to meet Davey Jones!"
                $ x_nautzz += 1

            $ notded = dying[rand2]
            mc "[notded]"

            menu:

                "Swing right at the first one!" if pirate3_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Har har harrr!"

                    $ matey2 += 1

                    jump pirate_fight3

                "Swing left at the first one!" if pirate3_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_swing.mp3"

                    show BG nightdeck2 with flash
                    show pirate4 slash at wiggle

                    show sword at sword with ease
                    p "I regret nothing..."

                    hide pirate4 slash with dissolve
                    $ pirate3_x -= 1

                    if pirate3_x == 0 and pirate4_x == 0 and pirate5_x == 0:
                        jump down_with_the_ship
                    else:
                        jump pirate_fight3

                "Take out the legs of the first one!" if pirate3_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Try and take'em!"

                    $ matey2 += 1

                    jump pirate_fight3

                "Swing right at the second one!" if pirate4_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Yurr a dead man!"

                    $ matey2 += 1

                    jump pirate_fight3

                "Swing left at the second one!" if pirate4_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Why'duncha giv'er up?"

                    $ matey2 += 1

                    jump pirate_fight3

                "Take out the legs of the second one!" if pirate4_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_swing.mp3"

                    show BG nightdeck2 with flash
                    show pirate5 slash at wiggle

                    show sword at sword with ease
                    p "I'll see you in Hell!"

                    hide pirate5 slash with dissolve
                    $ pirate4_x -= 1

                    if pirate3_x == 0 and pirate4_x == 0 and pirate5_x == 0:
                        jump down_with_the_ship
                    else:
                        jump pirate_fight3

                "Swing right at the third one!" if pirate5_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_swing.mp3"

                    show BG nightdeck2 with flash
                    show pirate6 slash at wiggle

                    show sword at sword with ease
                    p "Shannon, farewell."

                    hide pirate6 slash with dissolve
                    $ pirate5_x -= 1

                    if pirate3_x == 0 and pirate4_x == 0 and pirate5_x == 0:
                        jump down_with_the_ship
                    else:
                        jump pirate_fight3

                "Swing left at the third one!" if pirate5_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Nice try!"

                    $ matey2 += 1

                    jump pirate_fight3

                "Take out the legs of the third one!" if pirate5_x == 1:

                    show sword swing at sword with ease
                    play effect "audio/sword_clash.ogg"
                    show BG nightdeck2 with flash

                    show sword at sword with ease
                    p "Try and take'em!"

                    $ matey2 += 1

                    jump pirate_fight3

        elif matey2 == 6:

            show sword swing at sword with ease
            play effect "audio/sword_swing.mp3"
            show BG nightdeck2 with deathflash

            show sword at sword with ease
            mc "Uh crap, I didn't get a chance to,"

            mc "Father, please forgive..."

            jump game_over

        menu:

            "Swing right!":

                show sword swing at sword with ease
                play effect "audio/sword_clash.ogg"
                show BG nightdeck2 with flash

                show sword at sword with ease
                p "Noice try numbskull."

                $ matey2 += 1

                jump pirate_fight3

            "Swing left!":

                show sword swing at sword with ease
                play effect "audio/sword_swing.mp3"

                show BG nightdeck2 with flash
                show pirate4 slash at wiggle

                show sword at sword with ease
                p "Fack'en ell!"

                hide pirate4 slash with dissolve
                jump down_with_the_ship

            "Take out the legs!":

                show sword swing at sword with ease
                play effect "audio/sword_clash.ogg"
                show BG nightdeck2 with flash

                show sword at sword with ease
                p "Try'in to take me boot?"

                $ matey2 += 1

                jump pirate_fight3

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

        show captain with dissolve

        "One, two, five, how many bodies are there?"

        "All these pirates flocked to the wheel?"

        mc "Did you kill them all Captain?"

        if player_identity == "f":
            Cap "Aye lass it’s me. And I did."
        else:
            Cap "Aye lad it’s me. And I did."

        Cap "Looks like they got the jump on us aye?"

        play effect "audio/cough.ogg"
        pause 5.25

        mc "You’ve been shot!"

        "Multiple holes and lashes all over his body as if he jumped on an entire army."

        "His coat is soaked in blood and most of it looks like his. I don’t know if he’s gonna make it."

        mc "Captain hang on, Two Hands will be here soon and we’ll finish this."

        Cap "Aye don’t think so matey. At least six men got past me, well armed too."

        Cap "I’m afraid Two Hands is as good as gone. Unless he found some more hands?"

        Cap "Har har haaaa!"
        play effect "audio/cough2.ogg"
        pause 3.25

        mc "Captain, what do you do? What should I do?"

        Cap "It appears like arrr sun is setting."

        Cap "The Red Plague will not see the calm after this storm."

        mc "This can’t be how it ends Captain. We can keep fighting!"

        Cap "[player_name] look at me!"

        Cap " Look at me my child!"

        Cap "This is the end for me, for the Plague. But this ain't where yer story ends."

        Cap "Look behind me. Take it and go."

        show BG nightdeck3 at zoom
        hide captain
        mc "A dingy"

        show BG nightdeck3 at redo with ease
        show captain

        Cap "Take it and go [player_name]."
        play effect "audio/cough2.ogg"
        pause 3.25

        Cap "There ain't much time left. Keep the legend alive."

        Cap "Become the pirate ye were born te be."

        "The wind is stirring up the smoke. It’s only a matter of time before the ship meets its end."

        "If I stay I’ll either be roasted by the flames or buried under the sea floor."

        mc "Captain come with me, we can escape tog-"
        play effect "audio/thunder.ogg"
        show BG nightdeck3 with flash_lighting
        Cap "Ar Ye Daft?!"

        Cap "A Captain goes down with his ship! Ye know that by now!"

        Cap "Besides, I’ll be dead weight before ye hit the water."

        Cap "Go [player_name], live, I believe ye."

        mc "Captain I can’t go, I just-"

        p "Over here! I hear'em."

        p "Get to the helm now!"

        Cap "I’m not asking ye. This is an order."

        Cap "Go now!"

        mc "Aye Captain. I’ll go."

        mc "It was an honor serving in your crew. Thank you for everything Father,"

        mc "you’ll be with Mother soon-"

        Cap "… … … … …"

        mc "Farewell Captain. May you torment the Underworld for eternity."

        hide sword # incase its still there in some cases or my save skumming is catching up

        hide captain with dissolve
        show BG black with dissolve
        play effect "audio/splash.ogg"

        show BG escape with dissolve
        play effect "audio/fire.ogg" loop volume 5.0
        pause 5.0

        "A pirate’s dream of absolute freedom only dies when they are all good and dead. Every ounce of gunpowder or barrel of cannonballs couldn't kill this dream."

        "Some broken planks and burnt sails are just that. Nothing more than trash to let me engulf by the sea."

        play effect "audio/thunder.ogg"
        show BG escape with flash_lighting

        "Nothing stays where you left it. But isn't that exciting?"

        pause 10.0

        show BG black with dissolve
        jump act1_5

return
