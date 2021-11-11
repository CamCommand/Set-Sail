label act1_2:

    th "Land Ho!"

    if content_check == 0:
        play sound "audio/bookclose.wav"

        MC "The rest of this book is probably going to be barnacles. Maybe I do need new books."

    elif content_check == 1:
        MC  "Ahhh"

        MC "May have not been the cure my shoulders were looking for, but that still felt good."

    else:
        play sound "audio/crysniff2.wav" volume .5

        MC "Get it together, you're a pirate not a swabbie."


    "Time to find out what land life has to offer."

    "Would Captain get the hint if I asked to get him something unimportant so that I could escape without attracting any attention from the crew doing my work?"

    "It could be futile, Feno may have made the schedule change apparent and the pirates already know."

    "I might end up just having to bite the bullet on this if he doesn’t help."

    stop music fadeout 3.0
    scene BG topdeck with fade

    "Everyone is unloading from the ship onto a boardwalk."

    "The port is partially empty. Maybe the town warned everyone of our arrival?"

    "I can see people by the market. All sorts of types trying to avoid eye contact with {color=#f00}The Red Plague{/color}. It’s towering over the stands and buildings lining the end of the harbor."

    "As if a sea monster poked it’s gigantic head out of the water to eye it’s next meal and everyone ignored it thinking it would shield them. I could be overthinking this."

    "Plenty of pirate ships could come here, it might be commonplace. Let’s check if the Captain is on the quarterdeck."

    show flavio at right with dissolve

    fla "A postman handed me this upon our arrival Captain. It’s got your name on it. Well just your title actually."

    show captain at center with dissolve

    Cap "\"To The Demonic Pirate Ricardo of The Red Plague\",  I don’t see a seal on it. Mustn’t be important. Wasn’t the Mayor supposed to make sure nobody would disturb us?"

    fla "Well the landlubber was terrified just handing it to me. Mustn't be important Captain. Just a poor prank, sorry to bother ye."

    Cap "Aye, don’t worry bout mere paper. Get rid of it and get what we came here for damn it!."

    fla "Aye aye Captain!"

    hide flavio with moveoutleft
    scene BG deckview with fade
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
    # Im so sorry this nvl looks this way, I just wanted it to be formated a certain way and the spacing made no sense
    n "{font=Cursive_Option.ttf}Dear The Demonic Pirate Ricardo,{/font}"

    n "{font=Cursive_Option.ttf}Word around Seaborough is that The Red Plague is coming to port this week. We welcome you with open arms and are honored that you have chosen to use our amenities instead of pillaging them.{/font}"

    n "{font=Cursive_Option.ttf}It is the wish of ours at the Pirate Culture club at Seaborough High School that you would join us this afternoon to talk with our members about your life at sea. Your freedom and lifestyle has inspired many students here past{/font}"

    n "{font=Cursive_Option.ttf}the threat you could wreak. We can provide food and drink (non alcoholic unfortunately) to those that are willing to share your adventures with us. A club representative will be waiting for you outside the school main entrance located at:{/font}"

    n "{font=Cursive_Option.ttf}232 Sunkissed Drive \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ We eagerly await your arrival \ Captain. \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ Sincerely, \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ The Pirate Culture Club <3{/font}"

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

    scene BG harbor with fade
    #play sound "audio/chattering.mp3" fadeout 2.0

    "Just as I saw from the top deck. There are so many people minding their own business as if their lives depend on it."

    "Hopefully my cleaner outfit separates me from the seakissed pirates so that blending in isn’t a hurdle. Although, people seem to be wearing t-shirts and shorts so I might look a little odd."

    "Let’s find out, hopefully my fake mainlander dialect can pass me through any doubt."

    show lib with dissolve
    $ woman = Character('Woman',color="#07BB01", callback=lib_voice)# Librarian

    MC "Excuse me ma’am, could I bother you for today’s date?"

    woman "Umm yeah, it’s the 28th."

    hide lib with moveoutleft

    "Wow, she rushed away faster than what she was walking before. She didn’t scream or anything so I assume that counts as a win."

    MC "The 28th. Hmmmm."

    "I’ve been eighteen for a week without knowing. Sure, I’m not supposed to feel different, but I had a feeling it might've been yesterday. Don’t know where that came from, but nevermind."

    "The letter said this place was called Seaborough. Some of the signs on the eatteries confirm it."

    "Other than the more personal stuff Mom uses to tell me, I’ve heard some interesting things about Florida. Mainly how there’s a bunch of old and crazy people here who have given up on life."

    "So I got to keep an eye out for lunatics, but also not to hurt anyone. Leaving my pistol onboard was a good idea, even if it leaves me naked."

    "All the manual labor has me in good physical condition. In a fight I can take care of myself, but losing the ship’s annual arm wrestling contest keeps me humble."

    "I have to wonder how often some of these people even look at a hammar. I should keep my expectations low. Let’s dive in head first, walk around, see what I can do."

    scene BG black with fade
    scene BG harbor with fade

    "Wow."

    "I’ve now seen more people in the last few hours than I have had all year on the ship. Even large vessels we’ve ravaged, most of the crew stayed hidden while we stole their goods and harassed their leaders."

    "Some of the outfits out here look ridiculous. Is it because of brands or sales, I don’t know?"

    "There was that police car that went by before. I wasn't as wary of the law as I should have been because that was the first car I’ve seen!"

    "It was much smaller than I expected, books kinda assume you know what they look like already. They’ve been described to me by pirates with more land experience, but only enough to give me the general idea."

    "If retiring is ever an option for me, selling my ship and buying a car might be a fun idea. Travel the roads of the world now that the seas are conquered."

    "What a dumb dream."

    "The ocean’s vastly more free, plus I know it already. If my car breaks down, I wouldn’t know how to fix it and oars wouldn’t be an alternative."

    MC "Maybe instead of having pirates aboard I’ll hire a pit crew."

    MC "Ha ha ha ha hargh!"

    "Alright, that's enough walking. Where should I go?"

    menu:
        "Bookstore":

            jump bs

        "Market":

            jump market# take picture downtown

        "Arcade":

            jump arcade

        "School":

            jump street# take picture on weekend

    label bs:

        MC "Wonder if they have any region specific books? Better question, do they have any books they wouldn’t notice go missing?"

        stop sound fadeout 2.0

        scene BG bstore with fade
        pause 2.0

        "Books cover the aged wooden walls from top to bottom. A large logo with a black bird displays its name, the Raven’s Nest. For some reason it’s spelt \"Raven’s Nezt\"."

        "No need to ask anybody about that, it’s probably a trendy land custom."

        "Everything is so wonderfully neat and organized. It makes my collection look like a pirate's booze cabinet after a successful plunder."

        "Tolstoy, Shakespear, Orwell, Twain, there are so many great authors all collected in one spot."

        "Normally I’d just snag the first book I see that I haven’t read, but there are so many good looking ones. Which one would be best?"

        show lib with dissolve
        $ woman = Character('Librarian',color="#07BB01", callback=lib_voice)# Librarian
        woman "Excuse me, do you need help with something?"

        MC "Oh, um yeah I’m looking for a book."

        "It’s the woman who I asked the time from a few hours ago. Seems that she works here."

        "Or maybe she doesn’t and wants to help me? Let’s not over think this, I am going to steal a book from here anyway. Don’t want to look suspicious."

        $ lib = "Librarian"
        woman "What kind of book?"

        MC "What kind of book? I want something,"

        $ book_choice = "" # to determine type of book chosen for future reference at the school

        menu:
            "Exciting":
                $ book_choice = "Exciting"
                "What kind of action adventures do landlubbers think is good for a book? My life is already full of life threatening events, so I required vastly less escapism than someone in high school."

                "Yet there are so many frontiers I’ve never thought to explore that could provide me with more relatable desires. Like space or something, I don’t know?"

                "Of course one book isn’t going to transform me into a different person. I’m overthinking this easy question."

                MC "Do you have any exciting action books?"

                woman "Hehe."

                "She laughed at me!"

                woman "Yeah let me find something a triller seeker like you would enjoy."

                "I hope I didn’t say that too weirdly."

                hide lib with moveoutright
                "She flew behind the front counter quickly and started shuffling through books. Is she trying to get rid of me or is she looking for a specific book?"

                show lib with easeinright
                woman "Have you read anything from the Parry Baxton series?"

                MC "No I don’t think so. What’s it about?"

                woman "Why don’t you skim it and find out."

                MC "Yes, I guess I can do that, thank you."

                hide lib with easeoutright

                "She hands me the book and walks back to the counter. Clearly trying to look busy, so maybe she can’t talk to me."

                "I’m capable of reading a summary of a book, so why ask for someone to explain it to me."

                "{i}Parry Baxton{/i}, it’s part of a series."

                "I should stray away from young adult fiction at this point, it’s giving me bad ideas about young people. Plus bad ideas in general."

                MC "Hmmm?"

                "It’s about the Gods!"

                "The main character is the half blood daughter of Hades. They are trying to earn their place amongst the Gods."

                "That sounds interesting, although, if they get mythos wrong will that make me mad? I’ll read the first chapter, see how it makes me feel."

                play sound "audio/pages.wav"

                with fade

                "..."

                "This is pretty dumb."

                "The plot seems engaging enough, but the characters sound so stupid. Or incompitent?"

                "Maybe these authors are right, maybe at this age, people of the land are simply barnacle heads until adulthood."

                "I’ll keep it either way, no reason not to at this point. Where is that woman? I don’t want anyone to catch me."

                "Nobody sees me, the store is practically empty. The woman is reading behind the counter. An easy swipe for me."

                "I should ask them how to get to the school. I didn’t see it on my walk and I don’t want to wander aimlessly looking for it."

                jump bstore_end

            "Smart":
                $ book_choice = "Smart"

                "A science book could be enthralling. As long as it’s not a straight textbook."

                "I’ve read one of those and I retained zero facts from it. Even the title escapes to me."

                MC "Do you have any good science books?"

                woman "Hehe."

                "She laughed at me!"

                woman "Yeah let me find something a labcoat like you would enjoy."

                "I hope I didn’t say that too weirdly."

                hide lib with moveoutright
                "She flew behind the front counter quickly and started shuffling through books. Is she trying to get rid of me or is she looking for a specific book?"

                show lib with moveinright

                woman "Have you read The Night Sky yet?"

                MC "No I don’t think so. What’s it about?"

                woman "Why don’t you skim it and find out."

                MC "Yes, I guess I can do that, thank you."

                hide lib with moveoutright

                "She hands me the book and walks back to the counter. Clearly trying to look busy, so maybe she can’t talk to me."

                "I’m capable of reading a summary of a book, so why ask for someone to explain it to me."

                "{i}The Night Sky{/i}, by Gail Mcryson."

                "Written by an astrophysicist about deep space. It’s nonfiction and heavy with science garggin, but it has the author's personal touch to it."

                "So it isn’t just a boring textbook thankfully, I’ve not read something like this before."

                "The night sky stares back at me all the time, I should learn more about it. Even if it won’t help me talk to people, it could be another conversation starter."

                "I’ll read the first chapter, see what I think."

                play sound "audio/pages.wav"

                with fade

                "..."

                "This book is quite fascinating."

                "I thought all space stuff was astrology based off of mythos and what other pirates talk to me about. There’s so much more going on up there."

                "Other solar systems, antimatter, and I still don’t get what a quasar is but it sounds explosive."

                "I’ll nab it for later, no reason not to at this point. Where is that woman? I don’t want anyone to catch me."

                "Nobody sees me, the store is practically empty. The woman is reading behind the counter. An easy swipe for me."

                "I should ask them how to get to the school. I didn’t see it on my walk and I don’t want to wander aimlessly looking for it."

                jump bstore_end

            "Funny":
                $ book_choice = "Funny"

                "What if the kids start making fun of me? Even worse, what if they do and I don't know it?"

                "How could I be certain what I’ve read and experienced has prepared me for the subtle ridicule of others?"

                "If I was able to make my own jokes, then it’s possible to even the playing field."

                MC "Do you have any comedy books?"

                woman "Hehe."

                "She laughed at me!"

                woman "Yeah let me find something a jokester like you would enjoy."

                "I hope I didn’t say that too weirdly."

                hide lib with moveoutright
                "She flew behind the front counter quickly and started shuffling through books. Is she trying to get rid of me or is she looking for a specific book?"

                show lib with moveinright

                woman "Do you want like, a joke book?"

                MC "Yeah, why not? What’s your best joke book?"

                woman "Hmmmm."

                woman "I don’t know if any joke books are good? This one is pirate themed if you’re into that sort of thing."

                MC "I guess I’ll look at that one then."

                hide lib with moveoutright

                "She hands me the thick book of pirate jokes and returns to her seat at the counter. Clearly trying to look busy, so maybe she can’t talk to me."

                "I’m capable of finding my own book if this one sucks."

                "{i}1001 Pirate Jokes{/i}."

                "That’s a strange total."

                "\"How do pirates like to communicate?\""

                "\"Aye to aye!\""

                "I don’t get it."

                "\"What’s a pirate’s favorite fish?\""

                "Personally I like tuna the best."

                "\"A Swordfish!\""

                "Well that was just lame. That isn’t even pirate nomenclature?"

                "Wouldn’t other people call them Marlins? These are just so bad I can’t take it."

                play sound "audio/pages.wav"
                play sound "audio/pages.wav" # play mutliple times for comedy
                play sound "audio/pages.wav"

                with fade

                "..."

                "Dear Poseidon, how long have I been reading these?"

                "They kept getting worse but I couldn’t stop. What’s wrong with me?"

                "I would never repeat any of these out loud. Even if my life depended on it"

                "This would fit so well in my pocket though."

                "I’ll nab it for later, no reason not to at this point. Where is that woman? I don’t want anyone to catch me."

                "Nobody sees me, the store is practically empty. The woman is reading behind the counter. An easy swipe for me."

                "I should ask them how to get to the school. I didn’t see it on my walk and I don’t want to wander aimlessly looking for it."

                jump bstore_end

            "Nerdy":

                ""

                $ book_choice = "Nerdy"

                "The books back in my room don’t look like they’re going to be any pleasant entertainment at all."

                "I want something meaty and wondrous, those are the types of books that lead me to reread them."

                MC "Do you have any good fantasy books?"

                woman "Hehe."

                "She laughed at me!"

                woman "Yeah let me find something a nerd like you might enjoy."

                "I hope I didn’t say that too weirdly."

                hide lib with moveoutright
                "She flew behind the front counter quickly and started shuffling through books. Is she trying to get rid of me or is she looking for a specific book?"

                show lib with moveinright

                woman "Have you read Rune yet?"

                MC "No I don’t think so. What’s it about?"

                woman "Why don’t you skim it and find out."

                MC "Yes, I guess I can do that, thank you."

                hide lib with moveoutright

                "She hands me the book and walks back to the counter. Clearly trying to look busy, so maybe she can’t talk to me."

                "I’m capable of reading a summary of a book, so why ask for someone to explain it to me."

                "{i}Rune{/i}, by Ron John. That pen name is a dud."

                "It’s an apocalypse fantasy with wizards in the desert."

                "That’s what I gathered from the summary, but it’s like three hundred words of fantasy nonsense. Lots of words I don’t know nor understand."

                "I think I know what a rune is, but maybe not in this book’s context. It has an award sticker on it for copies sold."

                "Appears that it’ll have darker themes and it's popular, so this might be the upgrade in my reading I was looking for."

                "I’ll read the first chapter, see what I think."

                "The prologue is close to eighty pages. I feel an info dump coming up."

                play sound "audio/pages.wav"

                with fade

                "..."

                "I still have no clue what this book is about. Did it confuse me more or has it numbed my brain?"

                "Looks like this one could be a multiple reread type of book. I’ll take all the content a book can give me."

                "Hopefully it’ll sail with me better after the first read. It barely fits in my pants without being noticable, no reason not to take it at this point."

                "Nobody sees me, the store is practically empty. The woman is reading behind the counter. An easy swipe for me."

                "I should ask them how to get to the school. I didn’t see it on my walk and I don’t want to wander aimlessly looking for it."

                jump bstore_end

    label bstore_end:

                MC "Excuse miss?"

                show lib with dissolve

                woman "Yes, hello again. Did you decide on a book?"

                MC "Um, no. I liked what you recommended but I left my wallet at home."

                woman "Oh, well I can hold it on the side for you if you want."

                MC "No that’s fine, I’ll come back later for it."

                "Hopefully she forgets about this and doesn’t keep the store open for my blatant lie. Is it still appropriate to ask for directions?"

                "Oh!"

                "I didn't notice her nametage."

                $ woman = Character('Yoko',color="#07BB01")# Librarian
                MC "Yoko."

                MC "Could you give me directions to Seaborough high school? I need to meet a friend there, but I’ve never been."

                woman "Yeah sure. Don’t you have any kind of map app though?"

                "No, the letter didn’t come with a map unfortunately. Just tell me please."

                MC "Uh no, I don’t have one. Is it far away?"

                woman "Not really. Going left out of the store, take the first left and it’s a mile up the road. You can’t miss it."

                MC "Thank you Yoko. Have a nice afternoon."

                woman "You too. Please come again."

                "{i}Please come again?{/i}"

                "Was that a formality or a personal request?"

                "Did she want me to spend money? Now I feel kind of bad about stealing from her."

                "Let's just focus on getting to that school. I have to see how many sails these kids are missing if they were expecting the Captain to just talk to them."

                jump act1_3

    label market:

        # need crowd character and people sounds+crunch sounds
        $ food_check = 0 # This will be used later to determine if MC is hungry at school
        # $ crowd = ["Tall Man"]

        MC "Something to eat sounds nice. I’m sure nobody will miss one apple."

        scene BG market with fade
        pause 2.0

        "A few business buildings widen away from each other to reveal a brick path. There's a whole side street with tons of vendors lined up."

        "Mostly foods, but some of this stuff is weird to me to sell by fish and vegetables."

        "There’s multiple candle stands, one with soaps, and random crafts. Each of them have large banners with their website I presume."

        "Someone explained what \"dot com\" meant to me, but it has not been saved to memory."

        "I don’t understand how someone could make a living off of cartoon print earrings. Yet, being a pirate doesn’t give me the best business sense so can I really judge?"

        "People are gathering around fruit stands. I could easily snag a snack without anyone noticing."

        "Crates of fruits and vegetables are spread out along grey foldable tables."

        "People are shoulder to shoulder picking them out, smelling them, squeezing them, all before putting it down or in their bags. Is this worth it?"

        "Is this how everyone gets their food? If there is a better way for them then I don’t understand why’d they go through this."

        "I thought the mainlanders were more sanitary. With all this business, they wouldn’t miss one apple."

        with fade
        play sound "audio/swipe.mp3"

        MC "Like swiping gold from a drunk."

        play sound "audio/apple3.wav"
        $ food_check = 1

        "There’s a bench with nobody sitting there. Relaxing and eating while listening to other conversations could be a benefit."

        "Do other people do that? If it feels weird then I’ll stop immediately."

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

        "A lot of people, presumably moms, are getting groceries by themselves or with friends. There are very few people that look my age walking around."

        "They’re probably in some type of school instead of being a pirate. Is nobody on land able to live freely as I have at sea?"

        cr "...with his feet over his head he split open both coconuts with his thighs."

        "What!?"
        pause 1.5
        play sound "audio/apple3.wav"

        "I should leave before I start asking questions I don’t want the answers to."

        "Where is this school anyway? Maybe there is a map around here somewhere?"

        "Breaking up a conversation to ask for directions doesn’t feel like something I feasibly accomplish."

        MC "No, that’s dumb. You can do it sailor."

        "Just need to walk up to someone who looks like a mom. They’ll know where it is."

        MC "Excuse ma’am."

        show mm with dissolve

        m "Yes young lady."

        if player_identity == "m" or player_identity == "nb":

            "She thinks I’m a girl! Poseidon damn this luxurious hair!"
        else:

            "She doesn't sound annoyed, good start."

        MC "Do you know where the Seaborough high school is?"

        m "Why aren’t you at school?"

        MC "Because I graduated from another school. I need to pick something up from there."

        m "You need to pick up something from another school?"

        "Damn this woman! Why is she asking so many questions? Is this so hard to just tell me?"

        $ m = Character('Annoying Woman', color="#F263E2", callback=rot_voice)# woman at market

        MC "Yup, that’s weird I know but that’s where they sent them."

        m "Them what?"

        "Poseidon drown this woman for me!"

        MC "Them my papers. Do you know where it is at all?"

        m "Which papers?"

        "Do I just not pass as a high school graduate?"

        MC "My uh, test scores. They got sent to the wrong school by accident."

        m "The tests you took at your school got sent to another?"

        $ m = Character('Nightmare Woman', color="#F263E2", callback=rot_voice)# woman at market

        MC "No, the tests I took somewhere else got sent to Seaborough. Could you please just tell me where to go?"

        m "Hmmm."

        m "Okay."

        m "Exit the market that way, make a left, then the second. No the third right! Then go down the street, you can’t miss it."

        MC "Thank you ma’am! Have a nice day!"

        hide mm with dissolve

        "That was painful."

        "Unless it was the Captain's orders to keep quiet, pirates are easier to get important information from. It keeps duties efficient."

        "If I see a mom picking their kid up it’s best to avoid them. This will be useful information."

        "Let's focus on getting to that school. I have to see how many sails these kids are missing if they were expecting the Captain to just talk to them."

        jump act1_3

    label arcade:

        $ game_played = "" # for storing game played in arcade

        MC "Oh! That place had those video games Merigold told me about. Checking those out is a must."

        "They’re supposed to be old and fun and she said I could pick them up easily."

        scene BG ar with fade
        pause 1.5

        "A dim neon sign lights up the doorway of the building."

        "\"Gaming Street\""

        "That seems weird because this was the only arcade on the street that I noticed."

        "It could be that people name their business like pirates name their ships."

        "{color=#f00}The Red Plague{/color} is an actual disease, but the ship causes horror and pain as the sickness would."

        "If gaming happens here, then why not call it a street."

        play sound "audio/entrybeep.mp3"

        "The inside is illuminated by multicolored lights on the floors and ceiling. Layers of large machines with screens are backed up against the walls."

        "There’s a fancy bar in the center of it all. A tall slender man in black is cleaning glasses with pristine looking rags."

        show bartender with dissolve

        bt "Oh!"

        bt "Welcome!"

        bt "People don’t normally come this close to opening. You want anything to drink?"

        "I can’t exactly steal a drink from a bartender. How would one even play these games, nonetheless sneak them out the front door?"

        MC "Um, no thank you."

        MC "I was just wandering around. I’ve never seen an arcade before. I didn’t know they had bars in them."

        bt "Well the good ones do at least."

        bt "Har ha ha!"

        bt "You want to try a game?"

        MC "I’d like to, I’ve never played."

        bt "You have any cash on you?"

        MC "I have nothing on me, sorry. Like I said I was just wandering around."

        bt "I see, well here. Have a game on me. You put one of these into the machine and follow the directions."

        play sound "audio/coin.mp3"

        "He flicks a coin in my direction from his thumb."

        "It flies past me on my left side and bounces off the wall onto the floor."

        "The bartender’s expression turns blank as he’s now staring at the floor."

        MC "Thanks matey."

        "He mumbles something close to \"No problem\" under his breath staring at the floor."

        hide bartender with dissolve

        "A free game is more than I expected walking in here. What machine looks fun?"

        menu:

            "{color=#F93A22}Fly Guy{/color}":

                "The red wrapped machine has drawings of a little person with wings shooting strange creatures with a harpoon and then pumping them with air until they fall to their death."

                "After the coin goes into the machine it says {color=#F93A22}\"Player One\"{/color} can start. At hand level there is only a stick and one red button."

                "Seems simple enough, hopefully easy to play."

                play sound "audio/flyguy.mp3"
                "..."

                scene BG black
                scene ar with fade
                $ game_played = "Fly Guy"

                play sound "audio/boom.ogg"
                "That couldn’t have lasted longer than five minutes."

                "I was shooting the little creatures pretty consistently until they overwhelmed me. They gave me three lives but the enemies didn’t reset at all and killed me the second I was back on the screen."

                "Turning back to the bartender it was obvious he was watching during my first life, but after my character was corner he returned to preparing for paying customers."

                ""

                jump ar_end

            "{color=#F9F222}Monkey 2{/color}":

                "This machine appears as if it was painted over black recently."

                "Different pictures of cartoon monkeys in distinct styles cover every inch of it. There are two sets of sticks and dozens of buttons as controls."

                "None of which are labeled."

                "The music coming from the screen is noticeably joyful. Compared to the other machines it sounds much higher quality."

                "If I suck then no big deal, the song is simply mesmerizing. It takes the one coin given to me with no issues."

                "Let's see if it has more cool songs."

                play sound "audio/monkey.mp3"

                "..."

                scene BG black
                scene ar with fade
                $ game_played = "Monkey 2"

                play sound "audio/monkeyded.ogg"
                "That was amazingly ridiculous!"

                "No idea what was happening, but it was amazing. Monkeys kept falling down from the top of the screen and hitting buttons randomly seemingly did nothing."

                "Yet the music, coupled with the monkey’s faces triggered something in my brain that forced a smile onto my face. That was incredibly fun."

                "Ol’ Two Hands likes monkeys, I should tell him about it."

                "Turning back to the bartender I could tell he was watching me enjoying the game. He also has a big grin on his face."

                jump ar_end

            "{color=#232AFA}Dinosaur Mission IX: Kingdom Royale Finale{/color}":

                "The only part of this machine’s instructions that are in English is the title. Everything else is in Japanese, including what the button inputs do."

                "The character that keeps appearing on the screen sort of looks like me, so I sort of want to try it. Paragraphs of text are scrolling by, none of which is understandable."

                "Who would wanna read this much while playing a game? Isn’t the point of video games the action?"

                "I don’t have any previous experience, my preconceived notions are being challenged as my character swings their sword in between enemies spousing meaty dialogue at me."

                play sound "audio/dino.mp3"

                "..."

                scene BG black
                scene ar with fade
                $ game_played = "Dino Mission"

                play sound "audio/dinoded.ogg"
                "It feels as if an hour has flown by."

                "The game flashes {color=#D91400}\"Game Over\"{/color} in blood red English with an ominous sound playing. The gameplay wasn’t the most captivating, but it sucked me in so well without me noticing."

                "People have started to wander in to play other games. The bartender is serving someone a dull looking drink with a pleasant expression."

                jump ar_end

    label ar_end:

        "I should ask him how to get to the school. There was no sign of a map anywhere and all that was in the letter was the address."

        "If I finish at the school quickly then maybe I should come back here and try to play more games. There’s bound to be some loose change at the school that could get me on a couple more machines."

        show bartender with dissolve

        bt "You have a good time on that one?"

        MC "Yeah it was great. Thanks for letting me play."

        MC "Do you know how to get to Seaborough high school from here?"

        bt "Sure kid. Make a left when you exit and then take the next left. Follow the signs for the school zone and you won’t be able to miss it."

        MC "Thank you matey."

        bt "No problem."

        bt "Come back with money for a drink later to thank me properly."

        MC "Yeah, sure thing."

        hide bartender with dissolve

        "That guy was super nice. I do want to come back later."

        "But if I don’t find any money then I can’t. There’s nothing to steal in an arcade though."

        "This is good knowledge to hold onto. Better make my way to the school."

        jump act1_3

    label street:

        "I should go to the school while I’m thinking about it. There’s no need to waste a ton of time there."

        "If things move quickly, I can check out the rest of town. Hopefully this club won’t eat up the entire day."

        scene BG st with fade

        "Wandering the town’s underbelly isn’t as exciting as I thought it would be."

        "Seaborough’s streets are mainly made up of housing and abandoned complexes once I made it past the harbor. It’s super depressing seeing all the wrecked and abandoned buildings."

        "When we destroy ships at least the sea takes care of their final resting place. Here, they just sit here and bake in the sun."

        "The desolate poverty surrounding the area is dampening my mood. Trash is plentiful and the air is thick with discomfort."

        "Speaking of the air, it’s much drier away from the ocean. It's making me sweat more than usual and I’ve only been walking for a few hours, I think."

        "Looking for this school is taking too long, how much longer can I wander aimlessly? If I lose my way there’s no doubt the Captain will leave without me."

        "There’s nothing for me to swindle or survive off of here. I’d be dead in a week, max."

        "My shirt is starting to show sweat marks. Is it going to make the high schoolers make fun of me?"

        MC "Oh no."

        "This is going to be the first interaction with people my own age I’ve ever had. They might be a few years younger than me, but what if high schoolers are super mature?"

        "I’ve got a lot of life experience. But they might not care what I say if I’m not the Captain."

        "Should I lie? Or come in as an aggressive hardy pirate to scare them stiff?"

        MC "Poseidon, fuel my flame!"

        "I can do this."

        "I’m a bloody pirate for God’s sake!"

        "No more worrying about how people view me. A Pirate Culture Club wants to know what a pirate life is like. I’m going to show them what it’s really like."

        "Behaving on land is one thing, but I’ve cut the arms off of a man who called the Captain a dolphin breeder. Torn threw ships like it was stale bread."

        "A third tough sounding thing that's happened to me!"

        "There’s no reason to worry. Once the way reveals itself to me, the Pirate Culture Club won’t know what hit them."

        MC "Oh! And look what we got here."

        "{b}School Zone Ahead{/b}"

        "Did I ever say I needed a map?"

        "Look out Seaborough, The Demonic Pirate [player_name] is coming in for a special lecture."

        jump act1_3
