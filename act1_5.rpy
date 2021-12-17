label act1_5:

    show BG shore with dissolve
    play music "audio/shore.ogg"

    "Washing up on a rocky shore after that night doesn’t feel thematically appropriate."

    "A part of me hoped the dingy would be shredded by a whirlpool in a reef somewhere. That way I wouldn’t have to come up with a plan"

    "But here I am."

    "On some beach somewhere."

    "Not sure where, but I hope it isn’t South America. I haven’t spoken Spanish in five years at least."

    "Although, if I’m in America, I could be arrested if I’m found out I’m from the Red Plague."

    "Is there even a point acknowledging the worst night of my life?"

    "How long do I have to just sit with it before moving on?"

    "Poseidon has brought me to shore, what is his plan for me? There’s nothing left."

    "I wonder if anyone else made it out?"

    "I heard Iron Hip yell first under the deck. He must have emptied the entire clip before his screams stopped."

    "JoJo easily could overpower three grown adults, but based on Flavio’s..."

    pause 2.0
    "Based on how I found Flavio I don’t think they were playing fair."

    "Yet nobody but me will remember their last moments. Their crimes will be revered but them as people will be forgotten."

    "It’s unbelievable that the Captain saved me. Why would he let me go free?"

    "He told me to keep pirating, but what does he want me to do? What is there left for me to do?"

    play effect "audio/stomach.ogg"
    pause 2.0

    "I wish I had grabbed some rations."

    "Before finding something to eat, there’s something that needs to be done."

    show BG black with dissolve
    show BG shore_sword with dissolve

    # play some slow song here?
    pause 3.0
    nvl show

    n "The most important tenets of Anarchy are as follows. Freedom, the rejection of hierarchies, and fairness for all."

    n "These pillars stand proud in the Pirate Code. The rules every good pirate lived by and what every great pirate dies by. Where everyone gets a fair shake at life. This life. This way of being, it’s not an easy one."

    n "The world has rejected us pirates for thousands of years, but we kept fighting to stay alive and to stay free. We didn’t disappear into history books, we continued to cripple the legs of high society."

    n "Enraging our enemies and strengthening our own bonds. \"A pirate’s life for me!\" is what we all said in unison in the face of a crazy world that didn’t make sense to us."

    n "This saying shortens our lifespan but enhances our lives. This was a sacrifice we all took on willingly. My comrades paid the ultimate price for their choices, and in the end, I bet they were happy."

    nvl clear

    n "They achieved the happiness they sought out for, is that not a reason to celebrate their lives? Celebrate the lives of the freest people on both sides of the equator?"

    n "Simply believing that is true wouldn’t suffice if I hadn't lived it along with them. I will live the rest of my life, celebrating theirs."

    n "Whenever I’m eating food that doesn’t taste like wood I’ll remember Donatello who could spice up a turd to make it a blessing from Gods"

    n "Everytime I draw a pistol I’ll remember Iron Hip, who could empty a gun into an enemy's chest faster than anyone I ever knew."

    n " I’ll never forget how ol’ Two Hands used both his hands in every task he did, no matter the risks. His efficiency was immeasurable."

    nvl clear

    n "And most of all, I’ll remember my Captain and his ideology of brutal honor down to his very last moment. I will take the lessons you all taught me and carry them to my own end."

    n "Until Posideon deems it to be my final act, I will continue your legacy. May you all find be guided to the afterlife with safety and peace."

    n "This grave itself cannot express the size of the loss, but it represents more than anyone will ever understand. The Red Plague and it’s crew will power though into eternity by my hands. Thank you for everything Captain."

    nvl clear
    hide window

    "Hopefully this will be enough for them. Let's try to find out where I washed up."

    "I should turn my shirt inside out, it just occurred to me how much blood has seeped into it."

    "Don’t think any of it is mine, thankfully. Nobody will let me near food if I look this bad."

    "It may be time to sell my earrings for food. If they take earrings as payment still."

    "That’s what pirates have them for, but I’ve never heard a story of anyone actually using them to get emergency funds."

    "If silver hasn’t gone down in price, at least one of my studs should get me a sandwich."

    show BG streetpost with dissolve
    stop music fadeout 2.0

    "The coastline’s piles of trash hinted towards this being the mainland and not an island."

    "Based on the candy wrappers and garbage bags my final guess is that I’m back in America."

    "However, on the beach and since I’ve been walking I see these blue paper sheets everywhere."

    "Maybe I’m someplace else after all? Or more likely some useless product fell out of popularity."

    "There are a few people wearing them as masks that I’ve seen, but not enough compared to how many are on the ground."

    "They aren’t very cool looking masks, so it could be a medical thing. Or everyone got really ugly in a couple of years."

    mc "Excuse me fellas, why are you wearing masks today?"

    cr "Get bent you anti-vaxx jackass!"

    mc "Thank you all for your time."

    mc "Two legged swines."

    "They assumed I was an \"anti-vaxx\" so I guess it’s a new infighting group name."

    "The split must be the ones wearing the masks are anti-anti-vaxxers and the ones without are the anti-vaxxers."

    "Navigating between these groups could be difficult if I want to talk to anyone."

    define mask = 0 # boolean for having a mask

    menu:

        "Find a mask":

            $ quick_menu = False

            "If it’s a medical thing, I should find a mask to wear. Who knows what gross disease they’re trying to avoid."

            $ quick_menu = True

            "It wouldn’t seem clean to dry one off from the ground. Maybe an anti-anti-vaxx shop could give me one."

            show BG dollcorner with dissolve

            jump mask

        "Keep moving":

            $ quick_menu = False

            "There are more people here without masks than with, playing to the stronger side would be the safest thing to do."

            $ quick_menu = True

            "I’ll stick to the stronger side of the animal fights."

            show BG signcorner with dissolve

            jump nomask

        "Play them both":

            $ quick_menu = False

            "If I find a mask it might be beneficial to play both sides."

            $ quick_menu = True

            "Getting one off the ground would defeat the medical purpose of one."

            "Maybe an anti-anti-vaxx shop could give me one."

            show BG dollcorner with dissolve

            jump mask

    label mask:

        "Most of these shops are shut down. Windows and doors are boarded up, and seemingly have been like that for a while."

        "There are a few empty and unkempt houses scattered around the neighborhood. There could have been a depression as well as a disease."

        mc "What happened here?"

        show doll with dissolve

        dl "What’s wrong with you? You new to the world or something’?"

        "Woah!"

        "Some street urchin peaked behind a pillar to say that. That’s kind of freaky."

        mc "Hi, hello, yes."

        mc "Why are all these buildings closed off?"

        $ dl = Character('Street Urchin', color = "#740E86", callback=hobo_voice)
        dl "Ha haha!"

        dl "Have you been at sea for a long time or somethin’?"

        mc "Something like that. Could you fill me in?"

        dl "Oh really now? I was just playing."

        dl "Yeah kid there was a big sick, thee ol’ black plague part 2, a crippling pandemic if you will."

        dl "No pun intended or somethin’."

        dl "Hehehehehehe!"

        "She lifts up her left leg and it falls limp as she makes her joke."

        mc "Miss, are you one of the anti-vaxx people?"

        $ dl = Character('Doll', color = "#740E86", callback=hobo_voice)
        dl "You can call me Doll sweetheart, haven’t been called Miss in a long time."

        dl "I’m not against the jab but there really isn't a way for me to avoid the filth out here by myself."

        dl "Do you want a mask sweetheart?"

        mc "Yeah I was looking for one."

        dl "One second sweetheart."

        show doll at wiggle

        "Doll swings her backpack around to her stomach and opens it up. She pulls out a plastic sealed white mask."

        mc "That looks really nice, thank you."

        mc "Would one of my earrings be enough for it?"

        $ mask += 1

        dl "Oh don’t worry ‘bout it sweetheart just take it."

        dl "Like I said, I don’t need’em."

        mc "Thank you Doll, you’ve shown me a great kindness."

        dl "Yeah yeah, I don’t need to be buttered up."

        dl "Take it and have a good time in Seaborough. You don’t need to owe a debt to some old lady."

        mc "Wait what did you say? That name?"

        dl "You’re in Seaborough sweetheart. Welcome to Florida, don’t catch the rona."

        dl "Hehehehehe!"

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

        "What’s a kindergarten? I didn’t hear about any of this when I was in Seaborough."

        "Wait, Seaborough. How was that spelt again?"

        "What is that sign in the corner?"

        "\"Support your local business. Seaborough needs your support!\""

        jump return2sender

    label return2sender:

        define earrings = 1           # if you still have your earrings
        define may_position = ""      # what May is from MC's view
        define may_name = "Woman"     # Whatever fake name May gives MC

        $ activity_choice = "school"  # for testing purposesRR

        $ m = Character('[may_name]', color="#0A4AF6",  callback=may_voice)

        "I’m back in that town!"

        "Four years ago I had the greatest time on land here and Poseidon has brought me back! This is a sign by the Gods that I need to do something here!"

        "This is a sign by the Gods that I need to do something here! I should retrace my steps. Where did I go first back then?"

        menu:

            "The Schoolhouse":

                "The school! I should go see if the girls are still there."

                "They’d still be in high school right?"

                "I wasn’t gone for that long, I’m sure they’re just chilling in the club room like last time I was there."

                "The school shouldn’t be that far from here. I’ll get there before the club meeting ends."

                jump school2

            "Bookstore right?":

                jump bookstore2

            "Some Market":

                jump market2

            "Arcade Store":

                jump arcade2

    label school2:

        show BG schoolpost with dissolve

        "The school grounds are vacant. Give or take a few cars, I don’t hear anything either."

        "Has everyone left or are they all still inside doing papers or whatever kids do?"

        "I can’t remember when school let out last time and I shouldn’t just walk in there looking the way I do now."

        "I’m still drenched in sea water and blood, they’ll call the police on me."

        "Should’ve stolen some clean clothes or something before coming here. Or a watch so I know school is out by now."

        if activity_choice == "school":

            "{color=#2150E7}Astrid was waiting for me on the stoop when I got here, but she has no reason to be here now.{/color}"

            "She’s likely onto bigger and better things at this point, no reason to stick around. The rest of the eboard as well, four years might have been enough."

            "That afternoon with the Pirate Culture Club was fun, but I could tell they wanted to be somewhere else."

            "I hope they all got there."

            show m_d with dissolve

            m "Hey you!"

            mc "Yes? Do you need something?"

            m "This is school property, should you be here?"

            mc "I- ummmm."

            $ may_position = "school attendant"

            menu:

                "I'm a student":

                    mc "I’m a student here, who are you?"

                    "She looks disheveled and tired. In addition to the fact that she's in front of the school and not in it, she can’t be a teacher."

                    "I’ll call her bluff and see how she responds."

                    m "Oh really?"

                    m "Well how come you’re not in class right now?"

                    m "Why are you dressed like that?"

                    "Why am I dressed like that?"

                    "Why are you dressed like that?"

                    "She smells like she just came off a ship herself and she’s accusing me of being out of place?"

                    mc "Finishing up the gym class now. I’m sweaty because of all the running."

                    m "Well I’m the new gym teacher, and that’s why I’m also sweaty."

                    "This woman is lying to me too!"

                    $ may_name = "Mrs. Paul"

                    m "I’m Mrs. Paul, could you remind me which way the gymnasium is because I’m new?"

                    mc "Sure Mrs. Paul, it’s around the back on the right."

                    mc "I have another lap to do so I’ll see you in there."

                    m "Thanks, make sure you shower all that stuff off you when you’re done."

                    m "Wait, where are the other students?"

                    mc "Where are your students?"

                    "We silently stare each other down, neither of us making a single move."

                    mc "Have a nice day Mrs. Paul."

                    m "You too. Don’t be late for class."

                    mc "I won’t. Bye now."

                    m "Bye."

                    hide m_d with dissolve

                    "That’s my cue to leave."

                    "They aren’t here and if lying to another criminal is that hard, I don’t think I’d have much luck if the police are called."

                    "It’s time to prioritize food before Posideon’s destiny can grasp me properly. There might be some cheap seafood back by the shore."

                "I'm a teacher":

                    mc "I’m a teacher here, who are you?"

                    "She doesn’t look like anyone’s parent based on how tired and frazzled she looks."

                    "If she was, she'd be at work or something, so let’s see if she calls my bluff or not."

                    m "Oh, excuse me then."

                    $ may_name = "Mrs. Padilla"
                    m "My name is Mrs. Padilla. I’m a recent graduate and am here to drop off my resume for the teaching job here."

                    mc "That’s fine, no harm done."

                    mc "I’m the sports teacher, I’m sweaty like this all the time. You can drop off your resume in the main office."

                    m "You’re the gym teacher?"

                    m "Where are your students?"

                    mc "They’re umm, running laps."

                    m "There’s a track here?"

                    mc "Yes, it’s on the other side."

                    m "Oh thank you, and you’re…"

                    mc "I’m Dr. [player_name]."

                    "Why did I say doctor!?"

                    m "Oh, thank you Dr. [player_name]."

                    #zoom May in

                    m "Maybe we’ll be coworkers. See you soon."

                    hide m_d with dissolve

                    "That’s my cue to leave."

                    "They aren’t here and if lying to another criminal is that hard, I don’t think I’d have much luck if the police are called."

                    "It’s time to prioritize food before Posideon’s destiny can grasp me properly. There might be some cheap seafood back by the shore."

                "Flip it on her":

                    mc "I can be here. Should you be here?"

                    "Compared to everyone I saw around town or at school she is the most out of place."

                    "I’d bet she’s trying to intimidate something out of me."

                    $ may_name = "Mrs. Panza"
                    m "Excuse me! I’m the school’s nurse Mrs. Panza."

                    m "Who are you?"

                    "Like Hell she’s a nurse!"

                    "She must also think I’m suspicious. Let’s see who’s bluff lasts the longest."

                    mc "You are? I’ve never met you?"

                    m "I’m only here on rotating days, it’s possible you’ve missed me."

                    mc "Which days?"

                    m "Mondays and Fridays."

                    mc "Really?"

                    mc "Because I stopped by the nurse’s office on Friday and I didn’t see you there."

                    m "Last Friday?"

                    mc "Yes, last Friday."

                    m "Why were you in school last Friday? We didn't have school."

                    mc "The student’s didn’t have school, faculty meeting, you had to be there."

                    m "That only applies to the teachers, not the nurses."

                    mc "But we had a discussion set aside for supply budgeting, this included the nurses."

                    m "Were you at a meeting or did you stop by the office?"

                    m "Which is it?"

                    mc "It was both, I stopped by the office to look for Miss. Conners."

                    m "Miss Conners is on her honeymoon, she wouldn’t have been there."

                    mc "Miss Conners and I don’t get along very well, I went to get her to strike up a conversation."

                    mc "She didn’t tell me she was gone."

                    m "Were you set to get her for the meeting?"

                    mc "Yes that’s how I know you weren’t there."

                    m "If you were sent to get Miss Conners then others should have known she wasn’t here."

                    mc "It was an honest mistake and I thought the nurses weren’t supposed to be at the school?"

                    m "At the school or at the meeting?"

                    mc "At the meeting!"

                    m "The one on Friday, the day that I don’t come!"

                    mc "Because you’re on your honeymoon!"

                    m "Yes!"

                    mc "So are you Miss Conners or Mrs. Panza?"

                    m "Who’s Mrs. Panza? I’m just the substitute nurse!"

                    mc "You said that was your name?"

                    m "I didn’t tell you my name, I said I was a nurse."

                    mc "Yes you did!"

                    m "Well that isn’t my name."

                    $ May_affinity += 1

                    "We silently stare each other down, neither of us making a single move. We both look more out of breath than when we got here."

                    mc "I have to go to my next class."

                    m "I’m needed at my next appointment."

                    hide m_d with dissolve

                    "That’s my cue to leave."

                    "They aren’t here and if lying to another criminal is that hard, I don’t think I’d have much luck if the police are called."

                    "It’s time to prioritize food before Posideon’s destiny can grasp me properly. There might be some cheap seafood back by the shore."

        else:

            "Wait, I didn’t go to the school first."

            "I stopped by the [activity_choice] first then found my way to the school."

            "There’s little chance any of the girls are here anyway. I’ll run back to the [activity_choice], something relevant to my journey has to appear there."

            "If not, then I’m sleeping on a bench tonight."

            if activity_choice == "bookstore":

                    jump bookstore2

            elif activity_choice == "arcade":

                    jump arcade2

            else:

                    jump market2

        jump post_choice1

    label bookstore2:

        "I’ll return to the bookstore!"

        "If I’ve learned anything else about this world that wasn’t from pirates, it was from books."

        "Even what a bookstore actually was from the labels on the spines of my first few volumes."

        if activity_choice == "bookstore":

            show BG nobook with dissolve

            "That’s where I went first, I met that librarian who let me steal that book."

            "Or did I just steal by myself alone?"

            "What was her name? Yomo? Yacko?"

            "Either way, the answer’s I’m looking for could be there. Maybe a clue to the next step of my journey?"

            "Who knows? Maybe there will be clean clothes if luck will spare some."

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

            "Do old buildings still count as trespassing? This could get bad."

            m "I saw you go in here. This place looks empty as Hell, not much to steal."

            "She’s right, there’s nothing in here."

            "She doesn’t sound hostile. How should I approach this?"

            hide tome with ease

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

label choice_emptystore:

    menu:

        "Engage":

            jump engage

        "Hide":

            jump hideing

        "The book" if tome_choice == 1:

            jump ARG

    label engage:

        $ quick_menu = False

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

        jump post_choice1

    label hiding:

        $ quick_menu = False

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

        jump post_choice1

    label ARG:

        $ quick_menu = False
        define tome_title = "KeyError: FileCannotParse"

        "What about that book? Why was this book left behind?"

        $ quick_menu = True

        "Calling it a book might not be appropriate."

        "It’s a dark purple like I’ve never seen before for a cover. Leathery like older books, it’s more like a tome."

        "t’s pages are wrinkly yet it’s as heavy as a cannonball."

        "And there's no title or author on the cover or spine."

        "I can’t date it, how old is this thing?"

        "Should I even open it?"

        menu:

            "Open it":

                $ quick_menu = False

                mc "Now I’m too curious. Could this be an ancient Greek tome?"

                $ quick_menu = True

                mc "[tome_title]."
                #open file and read line per line while inserting “”-lower the brightness of BG to match the length of reading it

                ""

                return

            "Leave it":

                $ quick_menu = False

                "No, I don’t think so. I have to make sure this voice doesn’t get me in trouble."

                $ quick_menu = True

                "This book is obviously cursed or something awfully evil."

                "Not like reading some ruined old book will get me a meal tonight."

                "Even Poseidon would have picked something more obviously helpful."

                jump choice_emptystore

    label market2:

    label arcade2:

    label post_choice1:

        #have if prepared for if May hangs out

        "testing hoes"

return
