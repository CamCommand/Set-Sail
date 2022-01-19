label act1_1:

        transform pan:                       # panning and looping the BG
            xalign 1.0
            linear 200.0 xalign 0.0          # still does transition nicely
            repeat

        transform ds_slide:                  # slideing ds infront of screen
            xalign 0.5 yalign 10.0
            ease 1.5 truecenter

        $ player_identity = "nb"             # default identity if needed
        define player_name = ""
        scene BG map at pan
        play music "music/waves.ogg" fadein 2.0

        $ persistent.menuflag = 0

        if persistent.menuflag_count == 0:

            $ persistent.menuflag_count += 1

        nvl show

        n "\n{nw}"

        n "{cps=30}\nPirating is older than recorded human history. Supply chains interrupted and intercepted by those with the might to steal large portions of materials.{nw}"

        n "{cps=30}\nEvery stretch of water has seen one form or another of piracy. Normally, stealing large sums of profit is seen as immoral.{nw}"

        n "{cps=30}\nYet pirates are deified and revered throughout history. Its unique form of crime shook the world in a way nothing else could.{nw}"

        n "{cps=30}\nThus began a code between these pirates. An honor amongst thieves to be upheld keeping the practice ruly in unruly times."

        nvl clear

        n "\n{nw}"

        n "{cps=30}\nThe Pirate Code kept the good times alive throughout the centuries. There was seemingly no end in sight to the popularity of the lifestyle.{nw}"

        n "{cps=30}\nMarching into the modern age, piracy has taken many forms. Many melded with the times to seek out the most profitable whales of the sea while some kept the old fashion {i}Jolly Roger{/i} casted.{nw}"

        n "{cps=30}\nThousands are at sea breathing new life into pirating today by their own means.{nw}"

        n "{cps=30}\nYou are someone who has known nothing other than the life. Your own adventure is about to {b}Set Sail{/b}."

        pause 1.0
        nvl clear

        stop music fadeout 3.0

        pause 1.0
        window hide
        scene BG black
        scene BG MC_room with fade
        with fade
        with fade

        play music "music/BelowDeck.mp3" volume 1.0 fadein 1.5 fadeout 1.5

        "My eyes peak open to the sound of small waves and seagulls crying. We must be close to a port."

        "Rolling my neck around, it cracks in multiple places, feeling incredibly sore."

        "Morning to me..."

        label input:

            $ renpy.block_rollback()

            menu:

                "{color=FF4DA6}My name is Valerie{/color}":

                    $ player_identity = "f"
                    $ player_name = "Valerie"
                    $ MC = Character('Valerie', color="FF4DA6", callback=voice)
                    jump choice_name_V

                "{color=00AAFF}My name is Oscar{/color}":

                    $ player_identity = "m"
                    $ player_name = "Oscar"
                    $ MC = Character('Oscar', color="00AAFF", callback=voice)
                    jump choice_name_O

                "{color=116600}My name is Reed{/color}":

                    $ player_identity = "nb"
                    $ player_name = "Reed"
                    $ MC = Character('Reed', color="116600", callback=voice)
                    jump choice_name_R

                "What is my name?":

                    $ player_name = renpy.input("Choose your name", length=15)
                    $ player_name = player_name.strip() #strip unused spaces

                    if player_name == "":

                        $ player_name = "Reed"

                    if player_name == "Blackbeard" or player_name == "black beard" or player_name == "Black Beard":

                        "Really? No jokes today, I can't take any more floggin'."
                        jump input

                    # if player_name == "Cam":
                        # $ player_name = "Cam"
                        # Add cheat menu to add to affinity variables

        "How do I identify?"

        $ renpy.block_rollback()

        menu:

            "{color=FF4DA6}Female{/color}":

                $ player_identity = "f"
                $ MC = Character('[player_name]', color="FF4DA6", callback=voice)
                jump choice_name_User

            "{color=00AAFF}Male{/color}":

                $ MC = Character('[player_name]', color="00AAFF", callback=voice)
                $ player_identity = "m"
                jump choice_name_User

            "{color=116600}Non Binary{/color}":

                $ MC = Character('[player_name]', color="116600", callback=voice)
                $ player_identity = "nb"
                jump choice_name_User

        label choice_name_V:

            $ quick_menu = False
            $ renpy.block_rollback()

            MC "I'm feeling okay enough. Poseidon, please allow for pleasant skys today. I cannot sleep through something as brutal as last night."
            jump opening

        label choice_name_O:

            $ quick_menu = False
            $ renpy.block_rollback()

            MC "Feeling tighter than an anchor knot. Poseidon, please allow for pleasant skys today. I cannot sleep through something as brutal as last night."

            jump opening

        label choice_name_R:

            $ quick_menu = False
            $ renpy.block_rollback()

            MC "It's another salty morning. Poseidon, please allow for pleasant skys today. I cannot sleep through something as brutal as last night."

            jump opening

        label choice_name_User:

            $ quick_menu = False
            $ renpy.block_rollback()

            MC "Suffering is key to living. Poseidon, please allow for pleasant skys today. I cannot sleep through something as brutal as last night."

            jump opening

        label opening:

            $ pirate = "Pirate"

            "Sunlight pours into my eyes through the cracks in the old boards across the room."

            $ quick_menu = True

            "I get up from my cot and scan through my room. It’s a small storage space under the stairs to the top deck with barely enough room for anything extra beyond my necessities."

            "I am lucky to have it, one of the only perks I’ve gotten from being the Captain's child."

            "The privacy is amazing, and the smells of the common area don’t leak into my nose from here."

            "I’d like to think I earned this spot, but realistically, it was the only spot on the ship to keep a young person without anyone getting to them."

            "Either way I appreciated the forethought."

            "At the time..."

            "I was supposed to clean the cannons this morning, but did it last night so I could sleep in."

            "The Code says lights out after sun down, but I’ve cleaned them so many times I need only muscle memory for the job."

            "They get dirty in the exact same spots anyway."

            "Nobody has caught on yet, if they even care."

            MC "{cps=20}Arrrgh!{/cps}"

            MC "{cps=20}Ahhhh!{/cps}"

            "I bend in every direction possible, but the stretching doesn’t alleviate the pain in my shoulders."

            "If we are close to a port, maybe I can snag an extra pillow from a vendor or something."

            "I don’t remember having these pains before. Maybe I’m just getting old, I think eighteen is the appropriate age to start thinking that, right?"

            "I heard a new pirate say he hopes May has better weather. Safe to assume April has passed."

            "New guys always have a better sense of the date since they got onboard not too long ago."

            "Apparently it was my birthday at some point and all I got was new pains. That sucks."

            "Sometimes Captain says a passing mention of my birthday, but we’ve been out at sea for a while so I doubt he thought of it."

            $ th = Character('[pirate]', color="#000000", who_outlines=[ (1, "#FFFFFF") ], callback=twohands_voice)
            th "Wheres [player_name]! Why arrrgh’t they on deck?"

            "That sounds like my call to action. Quickly throwing myself out of bed shakes the boards beneath me."

            "My boots are at my feet, but how could I lose track of my shirt in here?"

            "Scanning my small abode, it evades my glance. It must be under something."

            "Checking behind my stack of books on the floor, the answer slaps the tired right off my face."

            "I was flattening it out after work last night. Attempting a technique to remove the wrinkles."

            "A side character in a book I just finished did the same and I wanted to see if it would work."

            "Pulling the dirty shirt out from under the heap of literature it’s apparent it failed. A stark reminder to stop reading young adult fiction at my age."

            th "[player_name] get yerr ass out from whatever gutter ye hiding under."

            $ pirate = "ol'Two Hands"
            "I think that’s [pirate] calling for me."

            "Last time I checked I outrank him, but when you’re younger than everyone else the more hardened pirates still treat you like shite."

            "I’ll grab my bristoles and brush my teeth and hair before gracing him."

            "A delayed head rush from springing up too fast numbs me momentarily."

            "Staring back at me, my cracked reflection shows a blank expression."

            "My salty hair won’t straighten no matter how much I brush and my skin is damaged beyond its original color."

            "I make note over my other features quite harshly to myself. My next thought flickers from the back of my mind."

            if player_identity == "f":

                MC "Could I ever be a woman of the land?"

            elif player_identity == "m":

                MC "Could I ever be a man of the land?"

            else:

                MC "Could I ever be someone of the land?"

            th "Damn ye [player_name]! I’ll flog ye later for this!"

            Cap "Why are ye threatening a mate so loudly in me presence Two Hands?"

            "Snapping back into action I head for the top deck. It’s time to start moving for real. I could use a peaceful type of day."

            "As peaceful as pirate's life could be."

            scene BG black with fade
            scene BG deckview with whiteflash
            pause 0.5
            show twohands angry at centerleft
            show cap at right
            with dissolve

            "Blinding heavenly light engulfs my face as I surface above deck."

            "Men and women working hard, or at least pretending to while The Demonic Pirate Ricardo is watching."

            "Presumably most were slacking off before Two Hands was shouting his head off. The deck is actually pretty clean."

            "The planks are looking pretty good in the bright morning light and they’re especially clear due to the lack of supplies available."

            th "Aye, there thee are Captain, right were I thought thee were."

            "Captain slowly turned around to look at me."

            "His dry expression told me nothing of his mood, but I assume he is annoyed at the unnecessary shrill yelling from ol’Two Hands."

            show cap yelling at centerright with moveinright
            show twohands scared with Dissolve(0.1)

            Cap "Two Hands, there isn't a pirate saltier than I. But yer a strong second ye seadog."

            Cap "So you know there ain't no reason for a pirate to be screaming for another unless ther be danger."

            th "Of course Captain."

            if player_identity == "f":

                Cap "When I asked ye to fetch me lass, I expected ye to do the searching and not be screaming."

            elif player_identity == "m" or player_identity == "nb":

                Cap "When I asked ye to fetch me lad, I expected ye to do the searching and not be screaming."

            Cap "Ye’ve heard me in battle, am I incapable of hollering?"

            th "No Captain. Ye have mighty powerful pipes."

            Cap "Aye, agreed."

            Cap "So if I hear ye flagging a false alarm on me ship again I’ll have Quartermaster Flavio give you [player_name]’s jobs for thee rest of ta week!"

            th "Aye Captain! Aye Captain!"

            Cap "Now get lost ye scurvy dog!"

            show twohands scared flip with Dissolve(0.1)
            hide twohands scared flip with moveoutleft
            show cap at center with move

            "Not many around has been on this ship as long as I have."

            "Of the Captain’s {i}Demon Moments{/i}, this wasn’t that bad, but I haven’t flinched during one of them since I was sixteen."

            "The intimidation tactics keep the crew in line and his reputation secured."

            "Two Hands needs to rip the pole from his ass and get the idea, you don't mess around when there's work to be done."

            MC "You requested me Captain?"

            if player_identity == "f":

                Cap "Aye [player_name]. Just wanted to talk to ye."

                Cap "The mainland considers ye a real adult now lass."

                show cap yelling with Dissolve(0.1)

                Cap "But I’ve been treating ye like that since ye could hold a scabbard. Hahaha!"

                MC "Aye Captain, but I didn’t get good with one until I beat Crookshaw."

                show cap with Dissolve(0.1)

                Cap "Aye lass, I remember. That scallywag fell flat on their arse and we prodded dem every night."

            elif player_identity == "m" or player_identity == "nb":

                Cap "Aye [player_name]. Just wanted to talk to ye."

                Cap "The mainland considers ye a real adult now lad."

                show cap yelling with Dissolve(0.1)

                Cap "But I’ve been treating ye like that since ye could hold a scabbard. Hahaha!"

                MC "Aye Captain, but I didn’t get good with one until I beat Crookshaw."

                show cap with Dissolve(0.1)

                Cap "Aye lad, I remember. That scallywag fell flat on their arse and we prodded dem every night."

            Cap "What happened to Crookshaw after that?"

            MC "He tried to flee his service from embarrassment and you obliged by marooning him."

            show cap yelling with Dissolve(0.2)

            Cap "Oh, that be right. Ha ha, ahhh."

            show cap with Dissolve(0.1)

            Cap "Nevertheless I wanted to give ye something. I got something made for ye, something I wish my."

            Cap "Captain"

            Cap "Gave me when I became a man."

            Cap "{cps=20}But it's, uh, I don’t have it yet.{/cps} It’sa, gonna be loaded up at while we're at port."

            Cap "I mainly wanted to say to ye is don’t worry about yer usual duties at port."

            Cap "I got Flavio to rearrange the grunt work so you could enjoy some of the fruits of land life."

            MC "Oh, thank you Captain. This is pleasantly unexpected."

            show cap yelling with Dissolve(0.1)

            Cap "Argh, what you expected nothing from me?"

            MC "No, it’s wonderful and thoughtful gift. I will use it wisely. Do you need me to get you anything?"

            Cap "No, no, nothing for me. There be nothing else I’ll ever need from this port ever again."

            Cap "Personally that is. We’re gonna need a lot more cannonballs of course."

            show cap yelling with Dissolve(0.1)

            Cap "Hahahaha ha!"

            MC "Ha ha."

            MC "Yes Captain I guess we always need more of those."

            show cap with Dissolve(0.1)

            Cap "Don’t be telling the crew where ye going. Don’t want dem thinking The Demonic Pirate Ricardo has gotten soft."

            MC "No, never Captain."

            if player_identity == "f":

                Cap "Get it out of yer system now lass. If not fer me, member yer mudder."

                Cap "She gave up da land life fer da free sea. And she never looked back."

                MC "Aye Captain. I’ll keep that fresh in my mind."

                Cap "Alright lass, dismissed. Put on something nicer and don’t get arrested."

            elif player_identity == "m" or player_identity == "nb":

                Cap "Get it out of yer system now lad. If not fer me, member yer mudder."

                Cap "She gave up da land life fer da free sea. And she never looked back."

                MC "Aye Captain. I’ll keep that fresh in my mind."

                Cap "Alright lad, dismissed. Put on something nicer and don’t get arrested."

            hide cap with moveoutleft

            pause 1.0
            scene BG deckview with fade
            show twohands angry with dissolve

            th "Yee got some fuck’en nerve doin’ that te me infront of thee Captain!"

            MC "Fuck off Two Hands I outrank you!"

            th "Aye, but a rank doesn’t stop me from order’n ye around."

            th "So when I say yer job is-"

            MC "My job was already done ye salty wet rag!"

            MC "I just didn’t do it when you wanted me to is all!"

            th "Which there lies thee problem."

            MC "Your problem, not mine!"

            show twohands angry at wiggle
            th "Yer dead wrong!"

            th "Tis yer problem if ye aren’t where ye supposed to be."

            MC "The job is done so why don’t you go boss around someone else with bleeding ears!"

            th "Why I outta throw ye overboard fer shark bait!"

            $ fla = Character('Flavio', color="#BB64F2", callback=fl_voice)
            show flavio at centerrighter with moveinright

            fla "Hey Two Hands why don’t yuh help me with the ropes, they need {cps=10}ummmmmm, knotting.{/cps}"

            show twohands sweaty with Dissolve(0.1)

            th "Not now Flavio!"

            fla "Knot now?"

            fla "Aye, let’s go then."

            fla "Bye [player_name], thanks for getting the canons clean so early."

            MC "Thanks Flavio."

            MC "Make sure you get’em nice and tight Mr. Two Whole Hands!"

            show twohands angry with Dissolve(0.1)
            pause 0.5
            hide twohands angry with moveoutright
            show flavio flip with dissolve
            hide flavio with moveoutright

            "That guy is unbelievable sometimes."

            "There isn’t a nicer, more studious pirate on this ship than I and he still has to give me a hard time."

            "Captain made me learn the hard way a long time ago, that if shite didn’t get done, we’d pay the price."

            "The easiest lesson to learn, and it’s still not good enough for some of these bastards."

            "At least the Captain recognizes my service."

            show BG black with dissolve
            pause 1.0
            scene BG MC_room with dissolve

            "I wonder how long Captain planned this? No way Flavio could have change the work schedule as quickly as yesterday, or even a week ago."

            "If someone gets my work and they know it’s mine, they’ll definitely give me a hard time about it."

            "This time off might be more of a double edged blade than Captain knows. However, he might expect me to hold my own at this point."

            "He’s right, but it’s best to reduce conflict with other pirates, if not to save my own skin, then for the morale of the crew."

            "We have to have each other's backs in a fire fight, no matter how one sided we might make them."

            "Another pirate ship hasn’t attacked The Red Plague in years thanks to our rep. Yet sometimes crews will fight back when we are raiding their hauls."

            "Numerous times I’ve had to cut the hand off a sailor who was looking to take a cheap shot at someone taking their valuables."

            "It'd be over for me if someone didn’t return the favor."

            "Captain said we were close to port. If I don’t have any work I guess I have some time to kill."

            define clothing_check = 0   # if you change clothes
            define daydream_check = 0   # if you've had a dozens
            define counter = 0          # count through fighting the painful memories

            $ re_list = ["No, I don’t want to think about it.", "No! I want to have a clear head if I’m gonna talk to anyone.", "Poseidon please let my mind be clear for the journey ahead of me.", "Poseidon, give me the strength of a thousand earthquakes to devour the thoughts of my mind.", "0"]
            # $ re_list[0]

        label waiting:

            define content_check = 0
            $ renpy.block_rollback()

            menu:

                "Change clothing" if clothing_check == 0:
                    jump clothes

                "Read a book":
                    jump book

                "Relax some more":
                    jump relax

                "Day dream" if daydream_check == 0:
                    jump dream

                "...Mom" if daydream_check == 1:
                    jump mom

        label clothes:

            $ clothing_check = 1
            $ renpy.block_rollback()

            MC  "Wait don’t I have a nicer set of clothes somewhere?"

            "I can’t walk through the streets looking like a dirty pirate. There has to be a clean shirt I kept somewhere in here."

            play effect "audio/rummaging_sound.wav"

            "It’s not under the books and it’s not on my bed so there aren’t a lot of other possibilities."

            MC "Wait wait wait."

            MC "Under my bed."

            "Getting under there is a crapshoot already because I can barely see that low to the floor."

            "If I angle my arm right and moves these book, some light should reach the back..."

            MC "Got it!"

            "Feeling the smooth finish of wood resin, I pull out a good sized cigar box I converted into an emergency provisions safe."

            "JoeJoe gave it to me after he finished his smokes and stole a better box of cubans from another Captain."

            "Anything perishable or fragile I steal that might be better to save goes in here. Sometimes fruits, candy, soap, and if memory serves."

            MC "That’s one soft shirt."

            "A folded black blouse barely fits in the recycled box. I stole it off a French Admiral’s son when he flipped me off as we were leaving their vessel."

            "With this shirt and a quick boot shine I should be looking moderately normal, or at least cleaner."

            play effect "audio/cloth_shine.wav"

            pause 3.5

            "That took maybe five minutes, now what?"

            jump waiting

        label book:

            define book_read = ""       # which book is picked if any

            $ quick_menu = False
            $ renpy.block_rollback()

            MC "I guess I could read without getting too invested."

            $ quick_menu = True

            "Most of these books aren’t actually stolen."

            "Obviously the first few were, but either at pirate ports or on the mainland, if there is ever a delay with the Plague leaving I go and find someone to do a swap with."

            "Most of those interactions go smoothly if you know who to approach."

            "Not to stereotype, but the muscle bound tattooed walls of meat don’t tend to be well read."

            "The more well dressed and young pirates normally have a novel or two they’d be willing to swap with me for one of mine."

            "My mate Merigold in the Virgin Islands has a really nice collection and swaps with me what she wants me to experience."

            "Sometimes out of a sense of urgency when she learns I haven't read any American classics."

            "I prefer reading stuff that came out this decade. Most of my social insight of the mainland comes from young adult fiction."

            "I believe I'm smart enough to know the dialogue isn't one-to-one from someone my age, but it set a good groundwork for me since all I understand of conversation comes from pirates."

            "Some of the least sociable people on Earth in my opinion. Very few pirates can have normal banter with me on something that isn't related to life at sea."

            "I could use this day off to swap some books, but I still have some to get through first."

            "As ample of an opportunity that this is, trying new things on the mainland could also be beneficial."

            MC "So what should I start?"

            $ renpy.block_rollback()

            menu:

                "Gamer Uno":
                    jump book1

                "The Afterlife is for Real":
                    jump book2

                "Stripes Are The New Black":
                    jump book3

        label book1:

            $ book_read = "gamer uno"

            $ quick_menu = False
            $ renpy.block_rollback()

            "Merigold had to explain to me what a video game was when she swapped with me."

            $ quick_menu = True

            "This book is supposedly about a dystopian world where people live in this virtual world instead of dealing with the hellscape they find themselves in."

            "The main character lives in Mexico and is so good at the virtual game they upstart a revolution inside the game. Merigold said it was selling really well in the US so I asked to read it."

            "Maybe I can pick up some mainland lingo. Although, I can’t tell which slang is real and which is made up for the book."

            play effect "audio/pages.wav"

            "..."

            show BG black with fade
            show BG MC_room with fade
            jump act1_2

        label book2:

            $ book_read = "afterlife"

            $ quick_menu = False
            $ renpy.block_rollback()

            "This is a nonfiction book?"

            $ quick_menu = True

            "It’s about a kid who died and was revived with a miraculous story of his culture's version of heaven. Funny how that works."

            "His accounts of the afterlife perfectly match what he was told by adults and with punjuncent details for a six year old."

            "Or that's what the back of it suggests."

            "I was taught the Greek myths. Knowing that they’re myths, but what happens to our souls seems so fair it gives me comfort in believing some of the stories for real."

            "The suffering described in Tartarus sounds like around the suffering someone who is sent there would deserve. Only the worst of the worst go there."

            "As nice as Elysium sounds, I’d be perfectly content with the Underworlds bleak nothingness for eternity."

            "Sounds more peaceful than worshiping forever in Cloud World for no reason."

            "But let's learn the wisdom from a not so dead kid. I'm sure it'll be insightful."

            play effect "audio/pages.wav"

            "..."

            show BG black with fade
            show BG MC_room with fade
            jump act1_2

        label book3:

            $ book_read = "stripes"

            $ quick_menu = False
            $ renpy.block_rollback()

            "A book about a normal woman getting sentenced to prison time for her past way of life."

            $ quick_menu = True

            "The juxtaposition sounds appealing. Pirates don’t get the luxury of sitting in a cell, but I always wondered what the lives are like of a bunch of criminals in the same building."

            "As opposed to a bunch of criminals on a boat."

            "Not enough to find out first hand, but that’s why books are so great. I can live a life that I could only sparsely imagine."

            play effect "audio/pages.wav"

            "..."

            show BG black with fade
            show BG MC_room with fade
            jump act1_2

        label relax:

            $ content_check = 1
            $ renpy.block_rollback()

            "Perhaps I should just relax some and enjoy the sway of the ocean."

            MC "Arrrghhhh, did I just start a sentence with \"Perhaps\"?"

            "I know I’m not as slimy as your average pirate, but I’ll be damned to Tatarus if I start acting like a British dandy royal."

            "I might be stressing out about this, it was just a thought, didn't actually say it."

            "I’ll just close my eyes and lie down."

            "A good snooze should whip my inner monologue into shape. Or, at the very least not make me sound like I live in a palace."

            "If the Captain heard me say something like that outloud he’d probably throw all my books overboard."

            "I’d rather him cut out my tongue, then I wouldn’t slip up."

            "Maybe it's stress? My first time roaming the mainland is a lot to consider."

            "Anything can happen, unlike at sea where you either die or don't."

            "I'm sure I'll be fine. Captain believes in me and that's enough."

            "..."

            show BG black with fade
            show BG MC_room with fade
            jump act1_2

        label dream:

            $ daydream_check = 1
            $ renpy.block_rollback()

            MC "I wonder what I can do at this port? Is the town around it big?"

            "Wait a second. Captain didn’t tell me where we were docking. After the storm last night I don’t know if we changed trajectory from our usual routes or not."

            "We were around Havana a couple of days ago. We might have turned north last night to avoid the worst of the storm."

            "If that’s right then we are headed to-"

            "Florida."

            "That’s why Captain said that thing about not needing anything from there anymore. Florida is where he picked up Mom all those years ago."

            "Imagining this place as sentimental to him at all is difficult."

            "The grizzled old pirate wouldn’t make special precautions for a port where zero people  give a shite that he's there."

            "He'd apperciate the lack of attention and interpret it as fear."

            "We haven’t been to that state since Mom died. We've been sailing around it for years."

            "I don’t want to think about it too much right now. But maybe I’ll walk the same ground she once did."

            "That would be nice."

            "..."

            jump waiting

        label mom:

            if counter != 4:

                $ lines = re_list[counter]
                MC "[lines]"
                $ counter += 1

            else:

                MC "Shite!"
                jump breakdown

            jump waiting

        label breakdown:

            $ content_check = 2
            $ renpy.block_rollback()

            "Mom,"

            "I miss you."

            "Being a pirate is so hard without you. You were there to balance out the lifestyle."

            "Telling me stories of your life to make me feel safer."

            "Getting the drunkards to stop yelling at me."

            "Raising me better than the water ever has."

            "I know the world of thieves more than anything else. More than myself."

            "Shite, I wish you were still here."

            "How different would I be if swashbuckling didn’t envelope me after you left? Would you recognize me?"

            "You were the only person that cared for me, that I cared about. Dad gives me a day off of work and it’s the nicest thing anyone has done for me in years."

            "I need more people like you in my or this life is gonna kill me slower than scurvy ever could."

            "You didn’t own a single thing when you stepped on The Red Plague."

            "All you left me were stories of your old life. And the scars you helped treat when you were here."

            "They’ve opened up without you."

            "Without you. I wouldn’t be anything. Or maybe I am nothing without your influence?"

            play effect "audio/crysniff.wav" volume .5

            "..."

            "But you aren't here anymore. So there's really only one thing I can do."

            MC "Keep on pirating."

            "It’s what you would've wanted. It’s what I was taught."

            "I believe you would have wanted me to find my answers without you anyway. Just as you did for yourself."

            "You dropped everything in your old life to start anew. It's crazy to think about."

            "It's like Dad said, you were the happiest on this ship."

            "That was clear as day when anyone looked into your eyes."

            "I wish you could reassure me, just one more time."

            show BG black with fade
            show BG MC_room with fade
            jump act1_2

return
