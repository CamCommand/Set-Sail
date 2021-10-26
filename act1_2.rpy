label act1_2:
    play music "audio/ocean2.wav"

    th "Land Ho!"

    if content_check == 0:
        play sound "audio/bookclose.wav"

        MC "The rest of this book is probably going to be barnacles. Maybe I do need new books."

    elif content_check == 1:
        MC  "Ahhh"

        MC "May have not been the cure my shoulders were looking for, but that still felt good."

    else:
        play sound "audio/crysniff2.wav"

        MC "Get it together, you're a pirate not a swabbie."


    "Time to find out what land life has to offer."

    "Would Captain get the hint if I asked to get him something unimportant so that I could escape without attracting any attention from the crew doing my work? It could be futile, Feno may have made the schedule change apparent and the pirates already know."

    "I might end up just having to bite the bullet on this if he doesn’t help."

    scene BG topdeck

    "Everyone is unloading from the ship onto a boardwalk."

    "The port is partially empty. Maybe the town warned everyone of our arrival?"

    "I can see people by the market. All sorts of types trying to avoid eye contact with the Red Plague. It’s towering over the stands and buildings lining the end of the harbor."

    "As if a sea monster poked it’s gigantic head out of the water to eye it’s next meal and everyone ignored it thinking it would shield them. I could be overthinking this."

    "Plenty of pirate ships could come here, it might be commonplace. Let’s check if the Captain is on the quarterdeck."

    show flavio at right
    show captain at center

    fla "A postman handed me this upon our arrival Captain. It’s got your name on it. Well just your title actually."

    Cap "\"To The Demonic Pirate Ricardo of the Red Plague\",  I don’t see a seal on it. Mustn’t be important. Wasn’t the Mayor supposed to make sure nobody would disturb us?"

    fla "Well the landlubber was terrified just handing it to me. Mustn't be important Captain. Just a poor prank, sorry to bother ye."

    Cap "Aye, don’t worry bout mere paper. Get rid of it and get what we came here for damn it!."

    fla "Aye aye Captain!"

    hide flavio with moveoutleft
    scene BG deckview
    show flavio with moveinright

    MC "Oh Flavio, have you seen the Captain?"

    fla "The Captain wishes for us to get what we came here for [player_name]."

    MC "Whatcha got there?"

    fla "Oh this? It was a letter to the Captain. It appears very crude so he wouldn’t open it. If it ain't from a noble or a politician why open it right?"

    MC "Yeah you’re right. Mind if I take a look though?"

    fla "He told me to get rid of it. Ye take care of that for me?"

    MC "No problem Flavio."

    fla "Aye aye [player_name]. One less thing I have to do."

    hide flavio with moveoutleft

    "What random person would write to the Captain? Maybe we have a relative here?"

    "It would be amazing if I could meet them. The Captain wouldn’t mind me looking through his trash, especially if he didn’t look at it."

    play sound "audio/letteropen.wav"

    "The outside may have been crude, but the handwriting is beautiful. Compared to my sea scratch it almost looks printed."

    nvl show dissolve

    n "{font=Cursive_Option.ttf}Dear The Demonic Pirate Ricardo,"

    n "{font=Cursive_Option.ttf}Word around Seaborough is that the Red Plague is coming to port this week. We welcome you with open arms and are honored that you have chosen to use our amenities instead of pillaging them. It is the wish of ours at the Pirate Culture club at Seaborough High School that you would join us this afternoon to talk with our members about your life at sea."

    n "{font=Cursive_Option.ttf}\nYour freedom and lifestyle has inspired many students here past the threat you could wreak. We can provide food and drink (non alcoholic unfortunately) to those that are willing to share your adventures with us. A club representative will be waiting for you outside the school main entrance located at 232 Sunkissed Drive. We eagerly await your arrival Captain."

    n "{font=Cursive_Option.ttf}\n\nSincerely,"

    n "{font=Cursive_Option.ttf}The Pirate Culture Club <3{/font}"

    pause 1.5
    nvl clear

    MC "You have to be kidding me."

    "A pirate culture club. Seriously?"

    "They asked the most fearsome pirate this side of Cuba to come over and talk? What do these kids think would happen to them?"

    "I can’t believe I thought this would be something important. Captain has good instincts for this type of thing. I should dispose of it as ordered."

    "Although, this is an invitation to a school. Where best to learn about people my age then a building full of them?"

    "It would be my pleasure to set these weirdos straight about being a pirate as well. I don’t see why I shouldn’t go."

    "If they think being a pirate is all glamour and riches these guys have another thing coming. I’ll give them enough horror stories so that they’ll never set foot in Posidon’s territory again."

    "Let’s get off the ship and have a look around first. At this point everyone looks so busy loading supplies I can slip by easily without them noticing."

    # "You've reached the end of the script Cam."
