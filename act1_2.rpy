# Cameron Drummond 2021-2022
# version 1.0.26
label act1_2:

    th "Land Ho!"

    if book_read == "gamer uno":

        play effect "audio/bookclose.wav"
        pause 0.5

        "The rest of this book is probably going to be barnacles. Maybe I do need new books."

        "The story seems fine, but even I can tell the characters are acting cheesy."

        "I also have no historical reference to anything they bring up fictitiously because I don't know what these games are."

        "That's a shame."

    elif book_read == "afterlife":

        play effect "audio/bookclose.wav"
        pause 0.5

        "According to this kid, no ferry ride to the Underworld from Charon and no panel of judges."

        "Just the one god and a bunch of fluffy angels."

        "I wonder how many people on land think about this stuff on the day-to-day?"

        "Oh well, what does a child know? I bet I've been closer to death than they were."

    elif book_read == "stripes":

        play effect "audio/bookclose.wav"
        pause 0.5

        "Flipping ahead through some chapter titles I can start with the assumption that this isn’t a glamorous lifestyle."

        "I would have never guessed living in a cell wasn't great."

        "This is too depressing for me right now."

    if content_check == 1:

        mc "{cps=20}Ahhhhh!{/cps}"

        mc "That may have not been the cure my shoulders were looking for, but it still felt good."

    elif content_check == 2:

        play effect "audio/crysniff2.wav" volume 0.5

        mc "Get it together, you're a pirate not a swabbie."

    "Time to find out what land life has to offer."

    "Would Captain get the hint if I asked to get him something unimportant?"

    "That way I could escape without attracting any attention from the crew doing my work?"

    "It could be futile, Flavio may have made the schedule change apparent and the pirates already know."

    "I might end up just having to bite the bullet on this if he doesn’t help."

    scene BG black with fade
    scene BG deckview2 with whiteflash

    show flavio at right
    show cap at center
    with dissolve

    fla "A postman handed me this upon our arrival Captain. It’s got your name on it. Well just your title actually."

    Cap "\"To The Demonic Pirate of The Red Plague\", I don’t see a seal on it."

    Cap "Mustn’t be important. Wasn’t the Gov'ner supposed to make sure nobody would disturb us?"

    fla "Well the landlubber was terrified just handing it to me. Mustn't be important Captain. Just a poor prank, sorry to bother ye."

    Cap "Aye, don’t worry bout mere paper. Get rid of it and get what we came here for damn it!"

    fla "Aye aye Captain! Right away."

    hide flavio with moveoutleft
    hide cap with dissolve

    show BG topdeck with fade

    "Everyone is unloading from the ship onto the dock."

    "The port is partially empty. Maybe the town warned everyone of our arrival?"

    "I can see people by the market. All sorts of types trying to avoid eye contact with The Red Plague."

    "It’s towering over the stands and buildings lining the end of the harbor."

    "As if a sea monster poked it’s gigantic head out of the water to eye it’s next meal and everyone ignored it thinking it would shield them."

    "Plenty of pirate ships could come here, it might be commonplace."

    "I'll check if the Captain is on the quarterdeck."

    show flavio with moveinright

    mc "Oh Flavio, have you seen the Captain?"

    fla "Aye, the Captain wishes for us to get what we came here for [player_name]."

    mc "Whatcha got there?"

    fla "Oh this? It was a letter to the Captain. It appears very crude so he wouldn’t open it."

    fla "If it isn't from a noble or a politician why open it right?"

    mc "You’re right matey. Mind if I take a look though?"

    fla "He told me to get rid of it. Ye take care of that for me?"

    mc "No problem Flavio."

    fla "Aye [player_name]. One less thing I have to do."

    fla "Thanks matey. Have a good time today."

    hide flavio with moveoutleft

    "What random person would write to the Captain? Maybe we have a relative here? It would be amazing if I could meet them."

    "The Captain wouldn’t mind me looking through his trash, especially if he didn’t look at it himself."

    play effect "audio/letteropen.wav"

    "The outside may have been crude, but the handwriting is beautiful. Compared to my sea scratch it almost looks printed."

    nvl show dissolve
    # Im so sorry this nvl looks this way, I just wanted it to be formated a certain way and the spacing made no sense
    n "{font=Cursive_Option.ttf}Dear The Demonic Pirate,{/font}{nw}"

    n "{font=Cursive_Option.ttf}Word around Seaborough is that The Red Plague is coming to port this week. We welcome you with open arms and are honored that you have chosen to use our amenities instead of pillaging them.{/font}{nw}"

    n "{font=Cursive_Option.ttf}It is the wish of ours in The Pirate Culture Club at Seaborough High School that you would join us this afternoon to talk with our members about your life at sea. Your freedom and lifestyle has inspired many students here past the threat you could wreak.{/font}{nw}"

    n "{font=Cursive_Option.ttf}We can provide food and drink (non alcoholic unfortunately) to those that are willing to share tales of adventures with us. A club representative will be waiting for you outside the school main entrance located here;{/font}{nw}"

    n "{font=Cursive_Option.ttf}125 Swift Street, Seaborough, Florida \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ We eagerly await your arrival \ Captain. \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Sincerely, {i}The Pirate Culture Club{/i}{/font}"

    pause 1.5
    nvl clear

    mc "You have to be kidding me."

    "A pirate culture club. Seriously?"

    "They asked the most fearsome pirate this side of Cuba to come over and talk? What do these kids think would happen to them?"

    "I can’t believe I thought this would be something important. Captain has good instincts for this type of thing."

    "I should dispose of it as ordered."

    "..."

    "Although, this is an invitation to a school."

    "Where best to learn about people my age then a building full of them?"

    "It would be my pleasure to set those barnacle heads straight about being a pirate as well. I don’t see why I shouldn’t go."

    "If they think being a pirate is all glamour and riches these guys have another thing coming."

    "I’ll give them enough horror stories so that they’ll never set foot in Poseidon’s territory again."

    "Let’s get off the ship and have a look around first. At this point everyone looks so busy loading supplies I can slip by easily without them noticing."

    stop music fadeout 2.0
    pause 2.0

    show BG harbor
    show crowd
    with dissolve

    define lady_pts = 0 # for annoying woman check into street label

    play music track2 volume 0.5 fadein 1.5 fadeout 1.5
    play effect "audio/chattering.mp3" volume 0.9 fadein 2.0

    "Just as I saw from the top deck. There are so many people minding their own business as if their lives depend on it."

    if clothing_check == 1:

        "Hopefully my cleaner outfit separates me from the seakissed pirates so that blending in isn’t a hurdle."

        "Although, people seem to be wearing t-shirts and shorts so I might look a little odd."

    else:

        "And now that I'm off the ship I remember that I didn't change clothes."

        "My work shirt looks like I treat it like a spare rag."

        "This isn't good, everyone's going to think I'm a pirate or worse,"

        "A sailor."

        "Wait, people are wearing all sorts of clothes. There doesn't seem to be a conformist way of dressing."

        "Despite the fact that it's hot here, people are even wearing layers."

        "Thank Poseidon I can pass this mess off as fashionable."

    "Let’s test that, hopefully my fake mainlander dialect can keep me passing."

    show lib with dissolve
    $ woman = Character('Woman',color="#07BB01", callback=lib_voice)# book store clerk

    mc "Excuse me ma’am, could I bother you for today’s date?"

    woman "Umm yeah, it’s the twenty-eighth."

    hide lib with Dissolve(0.3)

    "Wow, she rushed away faster than she was walking before. She didn’t scream or anything so I'll assume I'm normal enough."

    mc "The twenty-eighth, {cps=20}hmmmmmmmm.{/cps}"

    "I’ve been eighteen for a week without knowing. Sure, I’m not supposed to feel different, but I had a feeling it might've been yesterday."

    "The letter said this place was called Seaborough. Some of the signs on the eatteries confirm it."

    "Other than the more personal stuff Mom use to tell me, I’ve heard some interesting things about Florida. Mainly how there’s a bunch of old and crazy people here who have given up on life."

    "So I got to keep an eye out for lunatics, but also not to hurt anyone. Leaving my pistol onboard was a good idea, even if it leaves me naked."

    if clothing_check == 0:

        "Still can't believe I forgot to change. Must have been too excited."

    "All my manual labor keeps me in good physical condition. In a fight I can take care of myself, but losing the ship’s annual arm wrestling contest keeps me humble."

    "I have to wonder how often some of these people even look at a hammar, nonetheless do real labor."

    "Some of these people look like they could swallow a cannonball whole."

    "I should keep my expectations low and definitely not fight anybody."

    "Let’s dive in head first, walk around the harbor and see what there is to do."

    hide crowd with dissolve
    show BG black with fade
    show BG bogwalk
    with fade

    "Is this some kind of bog?"

    "No, it's by the sea so it's a marsh."

    "Accidentally wandered away from where all the shops and people were. Thought it would last longer."

    "That was all really interesting to see though. It feels so weird taking it all in like that so quickly."

    "I saw more people in the last few hours than I have had all year on the ship. Even large vessels we’ve ravaged, most of the crew stayed hidden while we stole their stuff."

    "Some of the outfits out here look ridiculous. Hats and attires I've never seen before. All with different symbols."

    "There was that police car that went by before. I wasn't as wary of the law as I should have been because that was the first car I’ve seen!"

    "It was much smaller than I expected, books kinda assume you know what they look like already besides the color."

    "They’ve been described to me by pirates with more land experience, but only enough to give me the general idea."

    "If retiring is ever an option for me, selling my ship and buying a car might be a fun idea. Travel the roads of the world now that the seas are conquered. Getting into car fights and run-ins with the law."

    "What a dumb idea though."

    "The ocean’s vastly more free, plus I know it already. If my car breaks down, I wouldn’t know how to fix it and oars wouldn’t be an alternative."

    mc "Maybe instead of having pirates aboard I’ll hire a pit crew."

    mc "Ha ha ha ha hargh!"

    define activity_choice = "default"
    "Alright, that's enough walking. What should I go back and visit?"

    $ renpy.block_rollback()

    menu:

        "Bookstore":

            $ activity_choice = "bookstore"
            jump bs

        "Market":

            $ activity_choice = "market"
            jump market

        "Arcade":

            $ activity_choice = "arcade"
            jump arcade

        "School":

            $ activity_choice = "school"
            jump street

    label bs:

        $ quick_menu = False
        $ renpy.block_rollback()

        # for the Book Worm Deluxe achievement
        define persistent.book4_count = 0
        define persistent.book5_count = 0
        define persistent.book6_count = 0
        define persistent.book7_count = 0

        # for the Sticky Fingers achievement
        define persistent.theft_count = 0
        define persistent.apple_check = 0
        define persistent.mask_check = 0

        mc "Wonder if they have any region specific books? Better question, do they have any books they wouldn’t notice go missing?"

        $ quick_menu = True

        show BG black with fade
        show BG harbor with fade
        pause 2.0

        "A large logo with a black bird displays a name, the Raven’s Nest. For some reason it’s spelt \"Raven’s Nezt\"."

        "No need to ask anybody about that, it’s probably a trendy land spelling."

        play effect "audio/dooropen.ogg"
        show BG bstore with fade

        "Books cover the aged wooden walls from top to bottom."

        "Everything is so wonderfully neat and organized. It makes my collection look like a pirate's booze cabinet after a successful plunder."

        "Tolstoy, Shakespear, Orwell, Twain, there are so many great authors all collected in one spot."

        "Normally I’d just snag the first book I see that I haven’t read, but there are so many good looking ones."

        "Which one would be perfect?"

        show lib with dissolve
        $ woman = Character('Clerk', color="#07BB01", callback=lib_voice)# Store clerk
        woman "Excuse me, do you need help with something?"

        mc "Oh, umm correct ma'am. I’m looking for a book."

        "It’s the woman who I asked the time from a few hours ago. Seems that she works here."

        "Or maybe she doesn’t and wants to help me? Let’s not over think this, I am going to steal a book from here anyway. Don’t want to look suspicious."

        woman "We have a few of those here. What kind of book you looking for?"

        mc "What kind of book? I want something,"

        define book_choice = "" # to determine type of book chosen for future reference at the school
        $ renpy.block_rollback()

        menu:

            "Exciting":

                $ book_choice = "Exciting"

                $ quick_menu = False
                $ renpy.block_rollback()

                "What kind of action adventures do landlubbers think is good for a book?"

                $ quick_menu = True

                "My life is already full of life threatening events, so I required vastly less escapism than someone in Florida."

                "Yet there are so many frontiers I’ve never thought to explore that could provide me with more relatable desires. Like space or something, I don’t know?"

                "Of course one book isn’t going to transform me into a different person. This isn't a difficult choice."

                mc "Do you have any exciting action books?"

                show lib smile

                woman "Hehe."

                "She laughed at me!"

                woman "Yeah let me find something a triller seeker like you would enjoy."

                "I hope I didn’t say that too weirdly."

                hide lib smile with moveoutright
                "She flew behind the front counter quickly and started shuffling through books. Is she trying to get rid of me or is she looking for a specific book?"

                show lib with easeinright
                woman "Have you read anything from the Parry Baxton series?"

                mc "No, I don’t think so. What’s it about?"

                woman "Why don’t you skim it and find out."

                mc "Yes, I guess I can do that, thank you."

                hide lib with easeoutright

                "She hands me the book and walks back to the counter. Clearly trying to look busy, so maybe she can’t talk to me."

                if persistent.book4_count == 0:

                    $ persistent.book4_count = 1
                    $ persistent.book_count += 1
                    #$ achievement.progress("Book Worm Deluxe", persistent.book_count)

                    $ persistent.theft_count += 1
                    #$ achievement.progress("Sticky Fingers", persistent.theft_count)

                if persistent.book_count == 7:

                    $ achievement.grant("Book Worm Deluxe")
                    $ achievement.sync()

                "I’m capable of reading a book summary, so why ask for someone to explain it to me."

                "{i}Parry Baxton{/i}, it seems to be part of a series."

                "I should stray away from young adult fiction at this point, it’s giving me bad ideas about young people. Plus bad ideas in general."

                mc "{cps=20}Hmmmmmmmmmmm?{/cps}"

                "Wait is this right? It’s about the Gods!"

                "The main character is the half blood daughter of Hades. They're trying to earn their place amongst the Gods."

                "That sounds interesting, although, if they get mythos wrong will that make me mad?"

                "I’ll read the first chapter, see how it makes me feel."

                play effect "audio/pages.wav"

                show BG black with fade
                show BG bstore with fade

                "..."

                "This is pretty dumb."

                "The plot seems engaging enough, but the characters sound so stupid. Or incompitent?"

                "Maybe these authors are right, maybe at this age, people of the land are simply barnacle heads until adulthood."

                "I’ll keep it either way, no reason not to at this point."

                "Where is that woman? I don’t want anyone to catch me."

                "I'm undetected, the store is practically empty. The woman is reading behind the counter. An easy swipe."

                if persistent.theft_count == 6:

                    $ achievement.grant("Sticky Fingers")
                    $ achievement.sync()

                "I should ask them how to get to the school. I didn’t see it on my walk and I don’t want to wander aimlessly looking for it."

                jump bstore_end

            "Smart":

                $ book_choice = "Smart"

                $ quick_menu = False
                $ renpy.block_rollback()

                "A science book could be enthralling. As long as it’s not a straight textbook."

                $ quick_menu = True

                "I’ve read one of those and I retained zero facts from it. Can't even remember the title."

                "Modern Biology something something."

                mc "Do you have any good science books?"

                show lib smile

                woman "Hehe."

                "She laughed at me!"

                woman "Yeah let me find something a lab coat like you would enjoy."

                "I hope I didn’t say that too weirdly."

                hide lib smile with moveoutright
                "She flew behind the front counter quickly and started shuffling through books. Is she trying to get rid of me or is she looking for a specific book?"

                show lib with moveinright

                woman "Have you read {i}The Night Sky{/i} yet?"

                mc "No, I don’t think so. What’s it about?"

                woman "Why don’t you skim it and find out."

                mc "Yes, I guess I can do that, thank you."

                hide lib with moveoutright

                "She hands me the book and walks back to the counter. Clearly trying to look busy, so maybe she can’t talk to me."

                if persistent.book5_count == 0:

                    $ persistent.book5_count = 1
                    $ persistent.book_count += 1
                    #$ achievement.progress("Book Worm Deluxe", persistent.book_count)

                    $ persistent.theft_count += 1
                    #$ achievement.progress("Sticky Fingers", persistent.theft_count)

                if persistent.book_count == 7:

                    $ achievement.grant("Book Worm Deluxe")
                    $ achievement.sync()

                "I’m capable of reading a book summary, so why ask for someone to explain it to me."

                "{i}The Night Sky{/i}, by Gail Mcryson."

                "Written by an astrophysicist about deep space. It’s nonfiction and heavy with science garggin, but it has the author's personal touch to it."

                "So it isn’t just a boring textbook thankfully, I’ve not read something like this before."

                "The night sky stares back at me all the time, I should learn more about it. Even if it won’t help me talk to people, it could be another conversation starter."

                "I’ll read the first chapter, see what I think."

                play effect "audio/pages.wav"

                show BG black with fade
                show BG bstore with fade

                "..."

                "This book is quite fascinating."

                "I thought all space stuff was astrology based off of mythos and what other pirates talk to me about. There’s so much more going on up there."

                "Other solar systems, antimatter, and I still don’t get what a quasar is but it sounds explosive."

                "I’ll nab it for later, no reason not to at this point. Where is that woman? I don’t want anyone to catch me."

                "I'm undetected, the store is practically empty. The woman is reading behind the counter. An easy swipe."

                if persistent.theft_count == 6:

                    $ achievement.grant("Sticky Fingers")
                    $ achievement.sync()

                "I should ask them how to get to the school. I didn’t see it on my walk and I don’t want to wander aimlessly looking for it."

                jump bstore_end

            "Funny":

                $ book_choice = "Funny"

                $ quick_menu = False
                $ renpy.block_rollback()

                "What if the kids start making fun of me? Even worse, what if they do and I don't know it?"

                $ quick_menu = True

                "How could I be certain what I’ve read and experienced has prepared me for the subtle ridicule of others?"

                "If I was able to make my own jokes, then it’s possible to even the playing field."

                mc "Do you have any comedy books?"

                show lib smile

                woman "Hehe."

                "She laughed at me!"

                woman "Yeah let me find something a jokester like you would enjoy."

                "I hope I didn’t say that too weirdly."

                hide lib smile with moveoutright
                "She flew behind the front counter quickly and started shuffling through books. Is she trying to get rid of me or is she looking for a specific book?"

                show lib with moveinright

                woman "Do you want like, a joke book?"

                mc "Yeah, why not? What’s your best joke book?"

                woman "{cps=20}Hmmmmmmmmmmm?{/cps}"

                woman "I don’t know if any joke books are good? This one is pirate themed if you’re into that sort of thing."

                mc "I guess I’ll look at that one then, thank you."

                hide lib with moveoutright

                "She hands me the thick book of pirate jokes and returns to her seat at the counter. Clearly trying to look busy, so maybe she can’t talk to me."

                if persistent.book7_count == 0:

                    $ persistent.book7_count = 1
                    $ persistent.book_count += 1
                    #$ achievement.progress("Book Worm Deluxe", persistent.book_count)

                    $ persistent.theft_count += 1
                    #$ achievement.progress("Sticky Fingers", persistent.theft_count)

                if persistent.book_count == 7:

                    $ achievement.grant("Book Worm Deluxe")
                    $ achievement.sync()

                "I’m capable of finding my own book if this one sucks."

                "{i}1001 Pirate Jokes{/i}."

                "That’s a strange total."

                play effect "audio/pages.wav"
                "\"How do pirates like to communicate?\""

                "\"Aye to aye!\""

                "I don’t get it."

                play effect "audio/pages.wav"
                "\"What’s a pirate’s favorite fish?\""

                "Personally I like tuna the best."

                "\"A Swordfish!\""

                "Well that was just lame. That isn’t even pirate nomenclature?"

                "Wouldn’t other people call them Marlins? These are just so bad I can’t take it."

                play effect "audio/pages.wav"
                play effect "audio/pages.wav" # play mutliple times for comedy
                play effect "audio/pages.wav"

                show BG black with fade
                show BG bstore with fade

                "..."

                "Dear Poseidon, how long have I been reading these?"

                "They kept getting worse but I couldn’t stop. What’s wrong with me?"

                "I would never repeat any of these out loud. Even if my life depended on it"

                "This would fit so well in my pocket though."

                "I’ll nab it for later, no reason not to at this point. Where is that woman? I don’t want anyone to catch me."

                "I'm undetected, the store is practically empty. The woman is reading behind the counter. An easy swipe."

                if persistent.theft_count == 6:

                    $ achievement.grant("Sticky Fingers")
                    $ achievement.sync()

                "I should ask them how to get to the school. I didn’t see it on my walk and I don’t want to wander aimlessly looking for it."

                jump bstore_end

            "Nerdy":

                $ book_choice = "Nerdy"

                $ quick_menu = False
                $ renpy.block_rollback()

                "The books back in my room don’t look like they’re going to be any pleasant entertainment at all."

                $ quick_menu = True

                "I want something meaty and wondrous, those are the types of books that lead me to reread them."

                mc "Do you have any good fantasy books?"

                show lib smile

                woman "Hehe."

                "She laughed at me!"

                woman "Yeah let me find something a nerd like you might enjoy."

                "I hope I didn’t say that too weirdly."

                hide lib smile with moveoutright

                "She flew behind the front counter quickly and started shuffling through books. Is she trying to get rid of me or is she looking for a specific book?"

                show lib with moveinright

                woman "Have you read {i}Rune{/i} yet?"

                mc "No, I don’t think so. What’s it about?"

                woman "Why don’t you skim it and find out."

                mc "Yes, I guess I can do that, thank you."

                hide lib with moveoutright

                "She hands me the book and walks back to the counter. Clearly trying to look busy, so maybe she can’t talk to me."

                if persistent.book6_count == 0:

                    $ persistent.book6_count = 1
                    $ persistent.book_count += 1
                    #$ achievement.progress("Book Worm Deluxe", persistent.book_count)

                    $ persistent.theft_count += 1
                    #$ achievement.progress("Sticky Fingers", persistent.theft_count)

                if persistent.book_count == 7:

                    $ achievement.grant("Book Worm Deluxe")
                    $ achievement.sync()

                "I’m capable of reading a book summary, so why ask for someone to explain it to me."

                "{i}Rune{/i}, by Ron John."

                "What a boring pen name."

                "It’s an apocalypse fantasy with wizards in the desert."

                "That’s what I gathered from the summary, but it’s like three hundred words of fantasy nonsense. Lots of words I don’t know nor understand."

                "I think I know what a rune is, but maybe not in this book’s context. It has an award sticker on it for copies sold."

                "Appears that it’ll have darker themes and it's popular, so this might be the upgrade in my reading I was looking for."

                "I’ll read the first chapter, see what I think."

                "The prologue is close to eighty pages. I feel an info dump coming up."

                play effect "audio/pages.wav"

                show BG black with fade
                show BG bstore with fade

                "..."

                "I still have no clue what this book is about. Did it confuse me more or has it numbed my brain?"

                "Looks like this one could be a multiple reread type of book. I’ll take all the content I can get."

                "Hopefully it’ll sit with me better after the first read. It barely fits in my pants without being noticable, I'll have to really try to sneak out with it."

                "I slid it on me without notice, the store is practically empty. The woman is reading behind the counter. An easy swipe."

                if persistent.theft_count == 6:

                    $ achievement.grant("Sticky Fingers")
                    $ achievement.sync()

                "I should ask them how to get to the school. I didn’t see it on my walk and I don’t want to wander aimlessly looking for it."

                jump bstore_end

    label bstore_end:

                mc "Excuse me, ma'am?"

                show lib with dissolve

                woman "Yeah, hi again. Did you decide on a book?"

                mc "Umm, no. I liked what you recommended but I left my wallet at home."

                woman "Oh, well I can hold it on the side for you if you want."

                mc "No that’s fine, I’ll come back later for it."

                "Hopefully she forgets about this and doesn’t keep the store open for my blatant lie. Is it still appropriate to ask for directions?"

                "Oh!"

                "I didn't notice her name tag."

                $ woman = Character('Yoko',color="#07BB01", callback=lib_voice)
                mc "Yoko."

                mc "Could you give me directions to Seaborough high school? I need to meet a friend there, but I’ve never been."

                woman "Yeah sure. Don’t you have any kind of map app though?"

                "No, the letter didn’t come with a map unfortunately. Just tell me already."

                mc "Uh no, I don’t have one. Is it far away?"

                woman "Not really. Go left out of the store, take the first left and it’s a mile up the road. You can’t miss it."

                mc "Thank you Yoko. Have a nice afternoon."

                woman "You too. Please come again."

                hide lib with dissolve

                "{i}Please come again?{/i}"

                "Was that a formality or a personal request?"

                "Did she want me to spend money? Now I feel kind of bad about stealing from her."

                define forgot_book = 0

                menu:

                    "She was kind of cute":

                        $ quick_menu = False
                        $ renpy.block_rollback()

                        "She was cute looking. Maybe I should sneak back in later and put the book back."

                        $ quick_menu = True

                        "If I remember and there is time after school I'll come back."

                        $ forgot_book = 1

                        jump act1_3

                    "She was nice":

                        $ quick_menu = False
                        $ renpy.block_rollback()

                        "She was nice to me. It makes me feel a little bad."

                        $ quick_menu = True

                        "I'm so use to stealing from people of ill gotten wealth, this feels wrong."

                        "If I remember and there is time after school I'll come back."

                        $ forgot_book = 1

                        jump act1_3

                    "Who cares":

                        $ quick_menu = False
                        $ renpy.block_rollback()

                        "It doesn't matter to me. I steal all the time."

                        $ quick_menu = True

                        "I also just met her."

                        "Let's just focus on getting to that school. I have to see how many sails these kids are missing if they were expecting the Captain to just talk to them."

                        jump act1_3

    label market:

        define food_check = 0 # This will be used later to determine if mc is hungry at school
        $ quick_menu = False
        $ renpy.block_rollback()

        mc "Something to eat sounds nice. I’m sure nobody will miss one apple."

        $ quick_menu = True

        show BG black with fade
        show BG market with fade
        show crowd with dissolve

        play effect "audio/chattering.mp3" volume 1.5 loop

        "A few business buildings widen away from each other to reveal an alley path. There's a whole side street with tons of vendors lined up."

        "Mostly foods, but some of this stuff is weird to me to sell by fish and vegetables."

        "There’s multiple candle stands, one with soaps, and random crafts. Each of them have large banners with their website names I presume."

        "Someone explained what \"dot com\" meant to me, but it has not been saved to memory."

        "I don’t understand how someone could make a living off of these, say those cartoon print earrings. They’re strange."

        "Yet, being a pirate doesn’t give me the best business sense so can I really judge?"

        "People are gathering around fruit stands. I could easily snag a snack without anyone noticing."

        "Crates of fruits and vegetables are spread out along gray foldable tables."

        "People are shoulder to shoulder picking them out, smelling them, squeezing them, all before putting it down or in their bags. Is this worth it?"

        "Is this how everyone gets their food? If there is a better way for them then I don’t understand why’d they go through this."

        "I thought the mainlanders were more sanitary. Oh well,"

        "With all this business, I'm sure they wouldn’t miss one apple."

        play sound "audio/swipe.mp3" # make these sounds so chattering can continue
        with fade

        if persistent.apple_check == 0:

            $ persistent.apple_check = 1
            $ persistent.theft_count += 1
            #$ achievement.progress("Sticky Fingers", persistent.theft_count)

        if persistent.theft_count == 6:

            $ achievement.grant("Sticky Fingers")
            $ achievement.sync()

        mc "Like seperating a drunk from his money."

        play sound "audio/apple3.wav"
        $ food_check = 1

        "There’s a bench with nobody sitting there. Relaxing and eating while listening to other conversations could be a benefit to my understanding of these people."

        "Do other people do this? If it feels weird then I’ll stop immediately."

        cr "Have you played the new chapter yet?"

        cr "No! When did that come out?"

        cr "Yeah it came out yesterday for free if you can believe that."

        "Are they talking about a book coming out? Coming out per chapter?"

        "If it’s free I’ll have to check that out. Do they just go on forever, never ending? That sounds great."

        cr "Did Marcy not come to the party?"

        cr "Deryll was there but Marcy wasn’t. And guess who was all over him?"

        cr "Jenna?"

        cr "It was Jenna. She saw an opportunity and she took it."

        cr "No way!"

        "Political intrigue, very interesting."

        "Farewell to Deryll’s career. I should be wary if I hear Jenna is coming around."

        "A lot of people are walking around with friends and family. No one has looked my way yet, sitting on this bench alone doesn’t make me stand out too much."

        "A lot of people, presumably caregivers, are getting groceries by themselves or with friends. There are very few people that look my age walking around."

        "They’re probably in some type of school instead of being a pirate. Is nobody on land able to live freely as I have at sea?"

        cr "...with his feet over his head he split open both coconuts with his thighs."

        "What!?"
        play sound "audio/apple3.wav"

        "I should leave before I start asking questions I don’t want the answers to."

        "Where is this school anyway? Maybe there is a map around here somewhere?"

        "Breaking up a conversation to ask for directions doesn’t feel like something I could feasibly accomplish."

        mc "No, that’s dumb. You can do it matey."

        "Just need to walk up to someone who looks like a parent. They’ll know where it is."

        mc "Excuse ma’am."

        show mm with dissolve

        ma "Yes young lady."

        if player_identity == "m" or player_identity == "nb":

            "She thinks I’m a girl! Poseidon damn this luxurious hair!"
        else:

            "She doesn't sound annoyed that I'm bothering her, good start."

        mc "Do you know where the Seaborough high school is?"

        ma "Why aren’t you at school?"

        "Uh oh. Think fast!"

        menu:

            "I'm an alumni":

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "I just graduated. I need to pick something up from."

                $ quick_menu = True

                ma "You don't know where the school you just graduated from is?"

                "Damn this woman! That's obvious though, that bad call is on me."

                "Is this so hard to just tell me though?"

                $ ma = Character('Annoying Woman', color="#FF793B", callback=rot_voice)

            "I'm from another school":

                $ quick_menu = False
                $ renpy.block_rollback()
                $ lady_pts += 1

                mc "Because I graduated from another school. I need to pick something up from there."

                $ quick_menu = True

                ma "You need to pick up something from another school?"

                "Damn this woman! Why is she asking so many questions? Is this so hard to just tell me?"

                $ ma = Character('Annoying Woman', color="#FF793B", callback=rot_voice)

        mc "Yup, that’s weird I know but that’s where they sent them."

        ma "Them what?"

        "Poseidon drown this woman for me!"

        menu:

            "My school work":

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "I need to pick up some school work is all."

                $ quick_menu = True

                mc "Could you tell me which way it is from here please?"

                ma "But I thought you graduated already?"

                "What does it look like lady?!"

                $ ma = Character('Nightmare', color="#FF793B", callback=rot_voice)

            "My papers":

                $ quick_menu = False
                $ renpy.block_rollback()
                $ lady_pts += 1

                mc "Them my papers. Do you know where it is at all?"

                $ quick_menu = True

                ma "Which papers?"

                "Do I just not pass as a high school graduate?"

                mc "My uh, test scores. I need them for referening."

                ma "Why don't you have your test scores?"

                "None of your business, that's why!"

                $ ma = Character('Nightmare', color="#FF793B", callback=rot_voice)

            "My lunch":

                $ quick_menu = False
                $ renpy.block_rollback()
                $ lady_pts -= 1

                mc "I forgot my lunch."

                $ quick_menu = True

                ma "Your lunch?"

                mc "Yes ma'am."

                ma "So did you graduate or didn't you?"

                "What kind of answer was that?!"

                mc "I just need to get back to school."

                $ ma = Character('Nightmare', color="#FF793B", callback=rot_voice)

        mc "Could you please just tell me where to go?"

        ma "{cps=20}Uhhhhhhhh.{/cps}"

        ma "Okay."

        ma "But I'm not entirely sure. Let me ask that nice police officer over there if they know."

        "Oh no. Not the law. What would have Mom done to avoid them?"

        menu:

            "Flattery":

                $ quick_menu = False
                $ renpy.block_rollback()
                $ lady_pts += 1

                mc "Ma’am please, I’m sure someone like yourself knows the general direction from here."

                $ quick_menu = True

                mc "I’ve been told the woman of Seaborough knows the streets very well."

                ma "{cps=10}Hmmmmmmm.{/cps}"

                ma "Yes of course, you know my husband never thinks I’m good with directions."

                ma "He’s such a rude man you wouldn’t believe it."

                mc "You deserve someone who treats you like the smart independent woman you are."

                "If this was any other person I would believe that line."

            "Double Down":

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "Look lady. I'm just lost and I'm asking for directions."

                $ quick_menu = True

                mc "If you need the police to guide your every action, I can find someone else to tell me."

                "I really should have by now."

                ma "I don't think I like your tone very much, young lady."

                if player_identity == "m" or player_identity == "nb":

                    mc "Well I'm not a bloody woman!"

                    mc "Are you gonna tell me where to go or not?"

                else:

                    mc "Are you gonna tell me where to go or not?"

            "Run Away":

                $ quick_menu = False
                $ renpy.block_rollback()
                $ lady_pts -= 10

                "I can't risk dealing with the police right now."

                $ quick_menu = True

                "Nobody would know if I was in custody and I wouldn't get to go to school."

                "My whole day would be ruined. Better make a break for it."

                mc "You know what wench. I'm out of here."

                hide mm with dissolve
                jump street

        if lady_pts >= 2:

            if lady_pts == 3:

                $ achievement.grant("Karen Along") # Grant Achievement
                $ achievement.sync()

            ma "Exit the market that way, make a left, then the second. No the third right! Then go down the street, you can’t miss it."

            mc "Thank you ma’am! Have a nice day!"

            hide mm with dissolve

            "That was painful."

            "Unless it was the Captain's orders to keep quiet, pirates are easier to get important information from. It keeps duties efficient."

            "If I see a mom picking their kid up it’s best to avoid them. This will be useful information."

            "Let's focus on getting to that school. I have to see how many sails these kids are missing if they were expecting the Captain to just talk to them."

            hide crowd with dissolve
            stop effect fadeout 2.0

            jump act1_3

        else:

            ma "No, I don't think I will. You've been quite rude to me and I don't want you anywhere near my daughter."

            "What daughter?!"

            ma "Stay away from me or I'll call the police."

            mc "You have to be kidding me."

            hide mm with dissolve

            "What an obnoxious woman. It took all I had not to brandish my weapon."

            "Not that I have it on me."

            "I don't want anything like that to happen again. I'll just wander around until I find the school. I have the address at least."

            "Hopefully there aren't any people like that at the school or I'm doomed."

            hide crowd with dissolve
            stop effect fadeout 2.0

            jump street

    label arcade:

        define game_played = "" # for storing game played in arcade

        # for the Gamer Achievement
        define persistent.game_count = 0
        define persistent.game1_count = 0
        define persistent.game2_count = 0
        define persistent.game3_count = 0

        $ quick_menu = False
        $ renpy.block_rollback()

        mc "Oh! That place had those video games Merigold told me about. Checking those out is a must."

        $ quick_menu = True

        "She said arcades have old games so I suppose I can pick them up easily."

        show BG black with fade
        show BG harbor with fade

        "A dim neon sign lights up the doorway of the building."

        "\"Gaming Street\""

        "That seems weird because this was the only arcade on the street that I noticed."

        "It could be that people name their business like pirates name their ships."

        "The Red Plague isn't an actual disease, but the ship causes horror and pain as the sickness would."

        "If gaming happens here, then why not call it a street."

        play effect "audio/dooropen.ogg"
        show BG ar with fade

        play effect "audio/entrybeep.mp3"

        "The inside is illuminated by multicolored lights on the floors and ceiling. Layers of large machines with screens are backed up against the walls."

        "There’s a fancy bar in the center of it all. A tall slender man in black is cleaning glasses with pristine looking rags."

        show bartender with dissolve

        bt "Oh!"

        bt "Welcome!"

        bt "People don’t normally come this close to opening. You want anything to drink?"

        "I can’t exactly steal a drink from a bartender."

        "Nor could I sneak these huge games out the front door?"

        mc "Uh, no thank you."

        mc "I was just wandering around. I’ve never seen an arcade before. I didn’t know they had bars in them."

        bt "Well the good ones do at least."

        bt "Har ha ha!"

        bt "You want to try a game?"

        mc "I’d like to, I’ve never played."

        bt "You have any cash on you?"

        mc "I have nothing on me, sorry. Like I said I was just wandering around."

        bt "I see, well here. Since you're the first customer today, have a game on me."

        bt "You put one of these into the machine and follow the directions."

        play effect "audio/coin.mp3"

        "He flicks a coin in my direction from his thumb."

        "It flies past me on my left side and bounces off the wall onto the floor."

        "The bartender’s expression turns blank as he’s now staring at the floor."

        mc "Thanks sir."

        "He mumbles something close to \"No problem\" under his breath, still looking down."

        hide bartender with dissolve

        "A free game is more than I expected walking in here."

        "What machine looks like something I could handle?"
        $ renpy.block_rollback()

        menu:

            "{color=#F93A22}Fly Guy{/color}":

                $ quick_menu = False
                $ renpy.block_rollback()

                "The red wrapped machine has drawings of a little person with wings shooting strange creatures with a harpoon and then pumping them with air until they fall to their death."

                $ quick_menu = True

                "That's pretty gruesome."

                "My kind of game."

                "After the coin goes into the machine it says {color=#F93A22}\"Player One\"{/color} can start. Where my hands are suppose to go there's only a stick and one red button."

                "Seems simple enough, hopefully easy to play."

                play effect "audio/flyguy.mp3"

                "..."

                scene BG black with fade
                scene BG ar with fade
                $ game_played = "Fly Guy"

                play effect "audio/boom.ogg"

                if persistent.game1_count == 0:

                    $ persistent.game1_count = 1
                    $ persistent.game_count += 1
                    #$ achievement.progress("G A M E R", persistent.game_count)

                if persistent.game_count == 4:

                    $ achievement.grant("G A M E R")
                    $ achievement.sync()

                "That couldn’t have lasted longer than five minutes."

                "I was shooting the little creatures pretty consistently until they overwhelmed me."

                "They gave me three lives but the enemies didn’t reset at all and killed me the second I was back on the screen."

                "Turning back to the bartender it was obvious he was watching during my first life, but after my character was corner he returned to preparing for paying customers."

                jump ar_end

            "{color=#F9F222}Monkey 2{/color}":

                $ quick_menu = False
                $ renpy.block_rollback()

                "This machine appears as if it was painted over black recently."

                $ quick_menu = True

                "Different pictures of cartoon monkeys in distinct styles cover every inch of it. There are two sets of sticks and dozens of buttons as controls."

                "None of which are labeled."

                "The music coming from the screen is noticeably joyful. Compared to the other machines it sounds much higher quality."

                "If I lose then no big deal, the song is simply mesmerizing."

                "Plus monkeys are cool. I've seen much older pirates with ones as pets."

                "They always do little dances when songs are played."

                "I saw one throw a knife at a guy once."

                "The game takes my coin with no issues."

                "Let's see if digital monkeys hold up to my high expectations."

                play effect "audio/monkey.mp3"

                "..."

                scene BG black with fade
                scene BG ar with fade
                $ game_played = "Monkey 2"

                play effect "audio/monkeyded.ogg"

                if persistent.game2_count == 0:

                    $ persistent.game2_count = 1
                    $ persistent.game_count += 1
                    #$ achievement.progress("G A M E R", persistent.game_count)

                if persistent.game_count == 4:

                    $ achievement.grant("G A M E R")
                    $ achievement.sync()

                "That was amazingly ridiculous!"

                "No idea what was happening, but it was amazing. Monkeys kept falling down from the top of the screen and hitting buttons randomly seemingly did nothing."

                "Yet the music, coupled with the monkey’s faces triggered something in my brain that forced a smile onto my face. That was incredibly fun."

                "JoeJoe is always saying he wants a monkey on the ship."

                "If I think I could tell him about today without getting hit, I'll mention this game."

                "Turning back to the bartender I could tell he was watching me enjoying the game. He also has a big grin on his face."

                jump ar_end

            "{color=#232AFA}Dinosaur Mission IX: Kingdom Royale Finale{/color}":

                $ quick_menu = False
                $ renpy.block_rollback()

                "The only part of this machine’s instructions that are in English is the title. Everything else is in Japanese, including what the button inputs do."

                $ quick_menu = True

                "The character that keeps appearing on the screen sort of looks like me, so I sort of want to try it."

                "Paragraphs of text are scrolling by, none of which is understandable."

                "Who would wanna read this much while playing a game? Isn’t the point of video games the action?"

                "I don’t have any previous experience, but my preconceived notions are being challenged."

                "My character swings their sword in between enemies spousing meaty lines of dialogue at me."

                play effect "audio/dino.mp3"

                "..."

                scene BG black with fade
                scene BG ar with fade
                $ game_played = "Dino Mission"

                play effect "audio/dinoded.ogg"

                if persistent.game3_count == 0:

                    $ persistent.game3_count = 1
                    $ persistent.game_count += 1
                    #$ achievement.progress("G A M E R", persistent.game_count)

                if persistent.game_count == 4:

                    $ achievement.grant("G A M E R")
                    $ achievement.sync()

                "It feels as if an hour has flown by."

                "The game flashes {color=#D91400}\"Game Over\"{/color} in blood red English with an ominous sound playing."

                "The gameplay wasn’t the most captivating, but it sucked me in so well without me noticing."

                "People have started to wander into the arcade to play other games."

                "The bartender is serving someone a dull looking drink with a pleasant expression."

                jump ar_end

    label ar_end:

        "I should ask him how to get to the school. There was no sign of a map anywhere and all that was in the letter was the address."

        "If I finish at the school quickly then maybe I should come back here and try to play more games. There’s bound to be some loose change at the school that could get me on a couple more games."

        show bartender with dissolve

        bt "You have a good time on that one?"

        mc "Yeah it was great. Thanks for letting me play."

        mc "Do you know how to get to Seaborough high school from here?"

        bt "Sure kid. Make a left when you exit and then take the next left. Follow the signs for the school zone and you won’t be able to miss it."

        mc "Thank you sir. Have a nice day."

        bt "No problem."

        bt "Come back with money for a drink later to thank me properly."

        mc "Yeah, sure thing."

        hide bartender with dissolve

        "That guy was super nice. I do want to come back later."

        "But if I don’t find any money then I can’t. There’s nothing to steal in an arcade though."

        "This was an experience I would not have got at sea."

        "Better make my way to the school now."

        jump act1_3

    label street:

        if lady_pts == 2 or lady_pts == 3:

            $ quick_menu = False
            $ renpy.block_rollback()

            "I should go to the school while I’m thinking about it. There’s no need to waste a ton of time there."

            $ quick_menu = True

            "If things move quickly, I can check out the rest of town. Hopefully this club won’t eat up the entire day."

            show BG black with fade
            show BG st with fade

        else:

            "The school must be around somewhere."

            "I didn't see it wandering around the port, so it must be deeper into the town."

            hide crowd with dissolve
            stop effect fadeout 2.0
            show BG black with fade
            show BG st with fade

        "Wandering the town’s underbelly isn’t as exciting as I thought it would be."

        "Seaborough’s streets are mainly made up of housing and abandoned complexes once I made it past the harbor."

        "It’s super depressing seeing all the wrecked and abandoned buildings."

        "When we destroy ships at least the sea takes care of their final resting place. Here, they just sit there and bake in the sun."

        "The desolate poverty surrounding the area is dampening my mood. Trash is plentiful and the air is thick with discomfort."

        "Speaking of the air, it’s much drier away from the ocean. It's making me sweat more than usual and I’ve only been walking for a few hours, I think."

        "Looking for this school is taking too long, how much longer can I wander aimlessly?"

        "If I lose my way there’s no doubt the Captain will leave without me."

        "There’s nothing for me to swindle or survive off of here. I’d be dead in a week, max."

        if clothing_check == 0:

            "My shirt is starting to show sweat marks through the stains."

        else:

            "My nice shirt is starting to show sweat marks."

        "I'm sure everyone here is used to it being hot, but will the high school people make fun of me for it?"

        mc "Oh no."

        "It's starting to dawn on me."

        "This is going to be the first interaction with people my own age I’ve ever had."

        "They might be a few years younger than me, but what if high schoolers are super mature?"

        "I’ve got a lot of life experience. But they might not care what I say if I’m not the Captain."

        "Should I lie? Or come in as an aggressive hardy pirate to scare them stiff?"

        "What should I do? Oh, damn it!"

        mc "Poseidon, fuel my determination!"

        "I can do this. Screw the pressure."

        "I’m a bloody pirate no matter what."

        "No more worrying about how people view me. A pirate culture club wants to know what a pirate life is like. I’m going to show them what it’s really like."

        "Behaving on land is one thing, but I’ve cut the arms off of a man who called the Captain a dolphin breeder."

        "Torn threw ships like they were stale bread."

        "A third tough sounding thing that's happened to me!"

        "There’s no reason to worry. Once the way reveals itself to me, the Pirate Culture Club won’t know what hit them."

        show BG street_sign with dissolve

        mc "Oh! And look what we got here."

        "{b}SLOW STUDENT CROSSING{/b}"

        "Did I ever say I needed a map?"

        "Look out Seaborough, The Demonic Pirate [player_name] is coming in for a special lecture."

        jump act1_3
