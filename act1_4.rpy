# Cameron Drummond 2021-2022
# version 1.0.5
label act1_4:

# thankfully this game runs smoothly and extra nesting doesn't visually effect runtime
# I know the If-soup for the pirate fights are bad

# But I had to redesign the fight after adding image buttons
# also this fight was intended to be like this but it was too fun
# think of the pirate#_x variables as dynamic HP
# in the future, have the fight.rpy sections handle everything for the characters on screen
# and this file will only call them when needed

# for future reading purposes
# matey and matey2 keep track of how many pirates should be on screen
# pirate#_x variables are the "HP" or tracker for the pirates
# pirate#-1_x and pirate#-1 slash is the image associated with pirate#_x
# death_count is exactly what it sounds like
# xnautz and xnautzz are for extra lines when pirates appear for intimidation
# the labels pirate_fight#_# are for when a pirate dies (which would have been better handled on the fight.rpy)
# fight.rpy is for reasigning vars to pirate#_x and determining to go to the looping labels of pirate_fight#_re
# or to a label pirate_fight#_# to watch the mc defeat a pirate
# the labels also check if the player can move on from that fight scene
# and using death_count to call a game_over screen

stop music fadeout 2.0
show BG school2 with dissolve
pause 1.0
play music track2 volume 0.5 fadein 1.5 fadeout 1.5

"Coming out of the school the sun is starting to set. To see a sunset from land and not the sea is sort of, underwhelming."

"Instead of the light reflecting off the pristine water, it’s bouncing off concrete and buildings."

"The shadows of the trees are nice, but it’s just not the same as the majesty of the ocean."

"Comparing sunsets doesn't stop me from enjoying them though."

"That trip did not go as I had planned."

"I was expecting them to act like rich kids or someone annoying like that."

"Some pompous wannabes pretending to act like pirates, flexing how naive they are."

"But instead they were a group of genuine people my age who wanted to know more about me and pirates."

"To say I'm shocked is an understatement."

"Discussing the life I live outside my own bubble for an afternoon was refreshing."

"Not to mention hearing non pirate related problems for once."

"All of that really puts my land confliction in perspective. I feel a bit more at ease after talking to them."

show BG black with dissolve
show BG walksunset with fade

"There’s a quiet hum of the town through the trees."

"It's not like before with all the people around, a busy day is coming to an end for Seaborough."

"I assumed that since all the people were here on the mainland, that places like this would never sleep."

"Not like at sea, where the waves drown out any silence and storms grab your attention greater than any conversation would."

"There's back breaking work and random fights to boot. With barely ever a quiet moment."

"..."

"I still belong out there though, surfing on the endless waters."

"Out there I thrive and am revered. Even if the whole crew doesn’t treat me like it, I know they need me."

"It’s the subtle things that keep the peace between everyone. A good deed here or there."

"Getting a second serving of food, someone cleaning your space without asking, the way ol Two Hands makes sure I get my work done on time so that he has someone to play chess with later."

"Even if he deserved it, I shouldn't have blown up at him."

"I have people in my life who already value me, there’s little need to look towards the mainland for alternatives."

"Now that I’m an adult, opportunities might start opening up for me."

"If the Captain acknowledges it, then there could be something down the line waiting for me."

"Other than whatever he got me for my birthday, which hopefully isn't a hand-me-down. Who knows what's next out there?"

"One day, I could have my own crew to command. Or control a second ship in the armada!"

"Who cares, it's my fantasy! I could be the next Demonic Pirate Captain!"

play effect "audio/seagulls.mp3"

"The sound of the waves and seagulls closing in breaks me from my illusions."

"Or delusions."

"I'm about to experience my very own golden age of piracy. Time to see what life hurls at me next."

stop music fadeout 2.0
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

    mc "JoeJoe...can't..."

    "You'll be alright, I swear."

    "This can’t be happening. Where did these other pirates come from?"

    "There was no sign of an attack incoming, how did they board the ship without anyone noticing in time?"

    "They're crawling from below the deck and the sides of the boat. It’s like an infestation!"

    "These pirates weren’t taking some pot shot, this was a well coordinated attack."

    "It started when the storm began, the perfect time for a night raid."

    "My gun is disassembled in my room, not that shooting in the dark would be helpful."

    show sword at sword with Dissolve(0.2)
    play effect "audio/sworddraw.ogg"

    "The Ocean's Spike will do nicely. Hasn't failed me yet."

    "I have to find out who’s still fighting. There’s no telling how many of these lunatics got onboard."

    "We need to band together to protect whoever is steering the ship."

    "One of us could steer out of the storm. Then we could fight off this attack easier."

    "Hopefully the Captain has a handle on the situation."

    show pirate1 with dissolve
    p "Well look at ye. They let kids roam 'round a graveyard?"

    p "Hey boys, we got another-"

    call screen pirate_fight1_0

    # to check if you perfectly slay each enemy b4 more can arrive for the Master Sword achievement
    define pirate_perfect1 = 0
    define pirate_perfect2 = 0
    define pirate_perfect3 = 0

    label pirate_fight1_re:

        if pirate_perfect1 == 0:

            $ pirate_perfect1 += 1

        show sword swing at sword with ease
        play effect "audio/sword_clash.ogg"
        show BG nightdeck1 with flash

        show sword at sword with ease
        $ p_line = pirate_lines[random_line]
        p "[p_line]"
        call screen pirate_fight1_0

    label pirate_fight1:

        $ quick_menu = False
        $ renpy.block_rollback()

        show sword swing at sword with ease
        play effect "audio/sword_swing.mp3"

        show BG nightdeck1 with flash
        show pirate1 slash at wiggle

        show sword at sword with ease
        p "Ahhrggggghh!"

        hide pirate1 slash with moveoutbottom

    $ quick_menu = True

    "There isn’t enough intel, I don't know how many of them there are or if I could kill them all."

    "Getting surrounded is a likely possibility when you don’t know how many enemies you have. Especially when you don’t know where they’re coming from."

    "I should strike first and not get overwhelmed."

    show BG nightdeck2 with dissolve
    $ renpy.music.set_volume(1.50, delay=0, channel='music')

    "Poseidon appears to not be on our side tonight."

    "The storm is only just starting. When it gets worse the attackers will have the perfect opportunity to finish us off."

    "Unless the wind does the job first."

    "I passed a few indiscernible bodies so far. Not enough to total our crew, so where is everyone?"

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

        if pirate_perfect2 == 0:

            $ pirate_perfect2 += 1

        $ quick_menu = False
        $ renpy.block_rollback()

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

            if pirate1_x == 3 and pirate2_x != 3:

                show sword swing at sword with ease
                play effect "audio/sword_clash.ogg"
                show BG nightdeck2 with flash

                show sword at sword with ease
                $ random_line = renpy.random.randint(0, 3)
                $ p_line = pirate_lines[random_line]
                p "[p_line]"

                $ matey += 1
                $ death_count -= 1

                call screen pirate_fight2_0

            elif pirate1_x == 3 or pirate2_x == 3:

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

        $ quick_menu = False
        $ renpy.block_rollback()

        if pirate1_x == 1:

            show sword swing at sword with ease
            play effect "audio/sword_swing.mp3"

            show BG nightdeck2 with flash
            show pirate2 slash at wiggle

            show sword at sword with ease
            p "Ahhhhh, damn ye!"

            hide pirate2 slash with moveoutbottom

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

        $ quick_menu = False
        $ renpy.block_rollback()

        if pirate2_x == 1:

            show sword swing at sword with ease
            play effect "audio/sword_swing.mp3"

            show BG nightdeck2 with flash
            show pirate3 slash at wiggle

            show sword at sword with ease
            p "Curse yeeeeee!"

            hide pirate3 slash with moveoutbottom

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

        $ quick_menu = False
        $ renpy.block_rollback()

        "These guys finished off a few of ours."

        $ quick_menu = True

        "Markey and Maverick..."

        "Their throats are gone."

        "..."

        "They were tasked with covering the cannons tonight, they didn't stand a chance against such a sneak attack."

        "Who's still fighting? There's no way we were all taken out in our sleep!"

        "The Plague isn’t made up of a bunch of pushovers. We're the strongest crew this side of South America!"

        "What kind of pirates do these people think they are to pull off such an attack?"

        show pirate4 at center with dissolve
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

        if pirate_perfect3 == 0:

            $ pirate_perfect3 += 1

        $ quick_menu = False
        $ renpy.block_rollback()

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
                $ pirate4_x = 3

                p "Need a hand?"
                $ x_nautz += 1
                call screen pirate_fight3_1

        elif matey2 == 1 or matey2 == 2 and death_count != 0: # only 2 pirates are here

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

                $ pirate5_x = 3
                show pirate6 at centerrighter behind sword with moveinbottom

                p "Time to meet Davy Jones!"

                $ x_nautzz += 1

                if x_nautzz == 1 and death_count != 0:
                    call screen pirate_fight3_2

            if pirate3_x == 3 and pirate4_x == 3:

                call screen pirate_fight3_1

            elif pirate3_x != 3 and pirate4_x == 3 and pirate5_x != 3:

                call screen pirate_fight3_4

            elif pirate4_x == 3 and pirate5_x == 3:

                call screen pirate_fight3_3

            else:

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

            if pirate3_x == 3 and pirate4_x == 3 and pirate5_x == 3:

                call screen pirate_fight3_2

            if pirate3_x != 3 and pirate4_x == 3 and pirate5_x == 3:

                call screen pirate_fight3_3

            if pirate3_x != 3 and pirate4_x != 3 and pirate5_x == 3:

                call screen pirate_fight3_5

            if pirate3_x == 3 and pirate4_x != 3 and pirate5_x == 3:

                call screen pirate_fight3_6

            if pirate3_x == 3 and pirate4_x == 3 and pirate5_x != 3:

                call screen pirate_fight3_1

            if pirate3_x != 3 and pirate4_x == 3 and pirate5_x != 3:

                call screen pirate_fight3_4

            else:

                jump pirate_fight3_re

    label pirate_fight3_1:

        if pirate3_x == 1 and matey2 >= 3:

            show sword swing at sword with ease
            play effect "audio/sword_swing.mp3"

            show BG nightdeck2 with flash
            show pirate4 slash at wiggle

            show sword at sword with ease
            p "Ahhhhh, damn ye!"

            hide pirate4 slash with moveoutbottom

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

            hide pirate4 slash with moveoutbottom

            $ pirate3_x = 0
            $ death_count += 1

            if pirate3_x == 0 and pirate4_x == 0: # pirate 3 and 4 are dead without 5

                jump down_with_the_ship

            elif matey2 == 0:

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

            if badwords == True:

                p "I'll see ye in {b}H E Double Hockey Sticks{/b}!"

            else:

                p "I'll see ye in Hell!"

            hide pirate5 slash with moveoutbottom

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
            if badwords == True:

                p "I'll see ye in {b}H E Double Hockey Sticks{/b}!"

            else:

                p "I'll see ye in Hell!"

            hide pirate5 slash with moveoutbottom

            hide pirate5 slash with moveoutbottom

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

            hide pirate6 slash with moveoutbottom

            $ pirate5_x = 0
            $ death_count += 1

            if pirate3_x == 0 and pirate4_x == 0 and pirate5_x == 0:

                jump down_with_the_ship

            elif pirate3_x != 0 and pirate4_x != 0: # pirate 3 and 4 are alive

                call screen pirate_fight3_1

            elif pirate3_x == 0 and pirate4_x != 0: # pirate 4 is alive

                call screen pirate_fight3_4


    label down_with_the_ship:

        $ quick_menu = False
        $ renpy.block_rollback()

        if pirate_perfect1 == 0 and pirate_perfect2 == 0 and pirate_perfect3 == 0:

            $ achievement.grant("Master Sword")
            $ achievement.sync()

        hide sword with Dissolve(0.2)

        mc "Flavio, say something matey."

        $ quick_menu = True

        "The bullet went clean through his head."

        "The horror still stained on Flavio’s face says more than that he just lost a duel. His arms and torso have slash marks all over them."

        if matey2 >= 2:

            "Just like now, he was ganged up on. I couldn’t have saved him."

        else:

            "He was ganged up on. I couldn’t have saved him."

        "He was never the greatest fighter, but this wasn’t fair."

        mc "We’ll get out of this Flavio, you rest here."

        play effect "audio/fire.ogg" loop

        "Hopefully the Captain is holding out alright."

        "I'm not sure if the ship can go too much longer in this storm without someone at the helm."

        "Is that a crackling?"

        "A fire!"

        "Where is it coming from?"

        "Above?"

        "The top deck is too wet to start one. But below..."

        "Right below our noses, they're snuffing us out!"

        "The storm won’t put anything out if the ship’s already a charred mess of driftwood."

        "These bastards!"

        "They aren’t here to rob us, they’re taking out the Plague for good."

        "Our past crimes have come back to damn us like a vengeful revenant."

        "There's no glory in this, we're done for at this rate."

        show pirate8 with dissolve

        p "Ye-"

        mc "Get out of my way!"

        show sword swing at sword with Dissolve(0.1)
        play effect "audio/sword_swing.mp3"

        show BG nightdeck2 with flash
        show pirate8 slash at wiggle

        show sword at sword with ease
        hide pirate8 slash with moveoutbottom

        th "[player_name] behind ye!"

        show pirate1 at left with dissolve

        show sword swing at sword with ease
        play effect "audio/sword_clash.ogg"
        show BG nightdeck2 with flash
        show sword at sword with ease

        show sword swing at sword with ease
        play effect "audio/sword_swing.mp3"
        show BG nightdeck2 with flash
        show pirate1 slash at wiggle

        show sword at sword with ease
        hide pirate1 slash with moveoutbottom

        mc "Stay down ye wrinkly mutt!"

        hide sword with Dissolve(0.1)
        show twohands scared dark with dissolve

        mc "Two Hands! Are you alright?"

        mc "Have both your hands? Where’s the Captain?"

        if player_identity == "f":

            th "Aye lass I’ll live a little longer!"

        else:

            th "Aye lad I’ll live a little longer!"

        show twohands sweaty dark

        th "Both claws intact as you can see."

        th "Da Captains fighting to steer thee ship."

        mc "Is anyone else still fighting? Who’s alive?"

        th "Arrrrrrggghh."

        th "I’ve seen more corpses den pirates now. I don’t know whos still kicking."

        th "It may be just you and me now."

        mc "We have to help the Captain and regain control of the ship."

        if player_identity == "f":

            th "Aye lass, I’ll clear the way of remaining renegades."

        else:

            th "Aye lad, I’ll clear the way of remaining renegades."

        show twohands angry dark with Dissolve(0.1)

        th "Time to take our ship back."

        mc "Let me help."

        th "Not on yer life!"

        th "Help thee Captain and steer us outta dis storm."

        mc "You can't tell me what to do!"

        th "Aye, I'm telling ye now!"

        show twohands angry dark flip with Dissolve(0.1)
        th "Fight me you cowards!"

        mc "Thank you, Hans"

        hide twohands angry dark flip with moveoutleft
        th "{cps=30}Arrrrrrrrrrrgggggggggggh!{/cps}"

        "Without a shred of hesitation, Two Hands rushes on ahead."

        "Were there never a pirate braver him?"

        play effect "audio/sword_clash.ogg" volume .5
        queue effect "audio/sword_clash.ogg" volume .5
        pause 0.3

        th "...I’ll cut yer throats!"

        "I won’t let his sacrifice lay dead at sea."

        stop effect fadeout 1.0
        pause 1.0
        show BG nightdeck3 with dissolve

        "Avoiding the sounds of gunshots and clashing swords, I’m able to get to the poop deck undetected."

        "If I make it out of this, Two Hands can have all my sweets for the rest of the year."

        "The rest of my life, if he makes it back too."

        "There’s a pile of bodies stacked up by the wheel with one person sitting up against it."

        "The figure is struggling to hold their gun straight."

        mc "Captain, is that you?"

        hide sword
        show cap bloody at sitting with dissolve

        "One, two, five, how many bodies are there?"

        "All these pirates flocked to the wheel?"

        mc "Did you kill them all Captain?"

        if player_identity == "f":

            Cap "Aye lass it’s me. And I did."

        else:

            Cap "Aye lad it’s me. And I did."

        Cap "Looks like they got the jump on us aye?"

        show cap bloody yelling with Dissolve(0.1)

        play effect "audio/cough.ogg"
        pause 5.25

        show cap bloody with Dissolve(0.1)

        mc "You’ve been shot!"

        "Multiple holes and lashes all over his body, as if he jumped on an entire army."

        "His coat is soaked in blood and most of it looks like his. I don’t know if he’s gonna make it."

        mc "Captain hang on, Two Hands will be here soon and we’ll finish this."

        Cap "Don’t think so matey. At least six men got past me, well armed too."

        Cap "I’m afraid Two Hands is as good as gone. Unless he found some more hands?"

        show cap bloody yelling

        Cap "Har har haaaa!"

        play effect "audio/cough2.ogg"
        pause 3.25

        show cap bloody with Dissolve(0.1)

        mc "Captain, what do you think? What should I do?"

        Cap "It appears like arrr sun is setting."

        Cap "The Red Plague will not see the calm after this storm."

        mc "This can’t be how it ends Captain. We can keep fighting!"

        show cap bloody yelling

        Cap "[player_name] look at me!"

        Cap "Look at me, my child!"

        Cap "This is the end for me, for the Plague. But this ain't where yer story ends."

        Cap "Look behind me. Take it and go."

        show BG nightdeck3 at zoom
        hide cap bloody yelling

        mc "A dinghy?"

        show BG nightdeck3 at redo with ease
        show cap bloody at sitting

        Cap "Take it and go [player_name]."

        show cap bloody yelling with Dissolve(0.1)

        play effect "audio/cough2.ogg"
        pause 3.25

        show cap bloody with Dissolve(0.1)

        Cap "There ain't much time left. Keep the legend alive."

        Cap "Become the pirate ye were born te be."

        "The wind is stirring up the smoke. It’s only a matter of time before the ship meets its end."

        "If I stay I’ll either be roasted by the flames or buried under the sea floor."

        mc "Captain come with me, we can escape tog-"

        play effect "audio/thunder.ogg"
        show BG nightdeck3 with flash_lighting

        show cap bloody yelling

        Cap "Ar Ye Daft?!"

        Cap "A Captain goes down with his ship! Ye know that by now!"

        Cap "Besides, I’ll be dead weight before ye hit the water."

        Cap "Go [player_name], live, I believe ye."

        mc "Captain I can’t go, I just-"

        p "Over here! I hear'em."

        p "Get to the helm now!"

        Cap "I’m not asking ye. This is an order."

        Cap "Go now!"

        show cap bloody with Dissolve(0.1)

        mc "Aye Captain. I’ll go."

        mc "It was an honor serving in your crew. Thank you for everything Father."

        Cap "{cps=15}… … … … …{/cps}"

        mc "Farewell Captain. May you torment the Underworld for eternity, you’ll be with Mother soon."

        hide sword # incase its still there in some cases or my save skumming is catching up with me

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

        "Some broken planks and burnt sails are just that. Nothing more than trash to let be engulfed by the sea."

        "Nothing stays where you left it. But isn't that exciting?"

        "Who told me those words? I can't recall."

        pause 10.0

        stop effect fadeout 2.0
        stop music fadeout 1.5
        show BG black with dissolve
        pause 1.0
        jump act1_5

return
