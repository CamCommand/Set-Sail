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
play sound "audio/thunder.ogg"
show BG 4 with hpunch
play music "audio/storm1.mp3" loop
pause 5.0
jump ship_start

label ship_start:

    show BG nightdeck1 with dissolve

    # JoeJoe freaking dies the movie
    # show joejoe dying quickly
    jj "{cps=70}Ahhhhgrrrrh!{/cps}"

    jj "{cps=55}[player_name], get out of here! Find the Captain!{/cps}"

    jj "{cps=55}Find the Captain!{/cps}"

    jj "{cps=70}Ahhhhhhhhhhhhhgggggguuuuuuuuuuu!{/cps}"
    # hide JoeJoe after death

    mc "JoeJoe no! Don’t stop fighting!"

    mc "JoeJoe...is..."

    "This can’t be happening. Where did these other pirates come from?"

    "They came out of nowhere, how did they board the ship without anyone noticing in time?"

    "Crawling from below the deck and from the sides of the boat. It’s like an infestation."

    "This storm is the perfect cover for a raid. These pirates aren’ taking some pot shot, this was a well coordinated attack. "

    show sword at sword
    play sound "audio/sworddraw.ogg"

    "My gun is disassembled in my room, this will have to do."

    "I have to find out who’s still fighting. There’s no telling how many of these lunatics got onboard."

    "We need to band together to protect whoever is steering the ship."

    "Hopefully the Captain has a handle on the situation."

    show pirate1 at center with dissolve

    p "Well look at ye."

    p "It’s some punk who-!"
    play sound "audio/swipe.mp3"# why isn't this playing???

    show pirate1 slash at wiggle

    p "Ahhrggggghh!"

    hide pirate1 slash

    "There isn’t enough intel, I don't know how many of them there are or if I could kill them all."

    "Getting surrounded is an easy possibility when you don’t know how many enemies you have. Especially when you don’t know everywhere they’re coming from."

    "Poseidon appears to not be on our side tonight."

return
