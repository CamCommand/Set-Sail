# The script of the game goes in this file.

# Main characters in game definitions
define MC = Character('[player_name]', dynamic=True, color="#990033")# Player Character
define Fi = Character('Fiona', color="#E44D1A")
define G = Character('Geraldine', color="#DFDABB")# Geraldine
define As = Character('Astrid', color="#F236BD")
define Be = Character('Behati', color="#5E0F60")
define Ma = Character('May', color="#0A4AF6")
define n = nvl_narrator# Narrator
# Minor characters in game definitions
define th = Character('[pirate]', color="#000000", who_outlines=[ (1, "#FFFFFF") ])# Ol' Two Hands
define Cap = Character('Captain', dynamic=True, color="#7F0505", who_outlines=[ (1, "#FFFFFF") ])# The Demonic Pirate Ricardo AKA Captain
# Affinity of main characters
default Fiona_affinity = 0
default G_affinity = 0
default Astrid_affinity = 0
default Behati_affinity = 0
default May_affinity = 0

image BG bkgd = "map.png"
image BG MC_room ="Minecraft_MC_room.png"

# The game starts here baby ;)

label start:
    play music "audio/waves.ogg"
    nvl show dissolve
    n "\nPirating is older than recorded human history. Supply chains interrupted and intercepted by those with the might to steal large portions of materials."

    n "\n Every stretch of water has seen one form or another of piracy. Normally, stealing large sums of profit is seen as immoral."

    n "\n Yet pirates are deified and revered throughout history. Its unique form of crime shook the world in a way nothing else could."

    n "\n Thus began a code between these pirates. An honor amongst thieves to be upheld keeping the practice ruly in unruly times."

    nvl clear

    n "\n The Pirate Code kept the practice alive throughout the centuries. There was seemingly no end in sight to the popularity of the lifestyle."

    n "\n Marching into the modern age, piracy has taken many forms. Many melded with the times to seek out the most profitable whales of the sea while some kept the old fashion {i}Jolly Roger{/i} casted."

    n "\n Thousands are at sea breathing new life into pirating today."

    n "\n You are someone who has known nothing other than the life. Your own adventure is about to {b}Set Sail{/b}."

    pause 1.5
    nvl clear

label select:
        with fade
        scene BG MC_room
        with fade
        with fade
        $ player_name = "Default Pirate Person"
        $ player_identity = "nb"
        "My eyes flutter open to the sound of small waves and seagulls crying. We must be close to a port. I roll my neck around, it cracks in multiple places, I’m incredibly sore."

        menu:
            "{color=FF4DA6}My name is Valerie{/color}":
                $ player_identity = "f"
                $ player_name = "Valerie"
                $ MC = Character('Valerie', color="FF4DA6")
                jump choice_name_V
            "{color=00AAFF}My name is Oscar{/color}":
                $ player_identity = "m"
                $ player_name = "Oscar"
                $ MC = Character('Oscar', color="00AAFF")
                jump choice_name_O
            "{color=116600}My name is Reed{/color}":
                $ player_identity = "nb"
                $ player_name = "Reed"
                $ MC = Character('Reed', color="116600")
                jump choice_name_R
            "What is my name?":
                $ player_name = renpy.input("Choose your name", length=15)
                $ player_name = player_name.strip() #strip unused spaces
                if player_name == "":
                    $ player_name = "Me"
        "How do I identify?"
        menu:
            "{color=FF4DA6}Female{/color}":
                $ player_identity = "f"
                $ MC = Character('[player_name]', color="FF4DA6")
                jump choice_name_User
            "{color=00AAFF}Male{/color}":
                $ MC = Character('[player_name]', color="00AAFF")
                $ player_identity = "m"
                jump choice_name_User
            "{color=116600}Non Binary{/color}":
                $ MC = Character('[player_name]', color="116600")
                $ player_identity = "nb"
                jump choice_name_User


        label choice_name_V:
            MC "I'm feeling OK enough. Poseidon, please allow for pleasant skys today. I cannot sleep through something as brutal as last night."
            jump opening
        label choice_name_O:
            MC "Feeling tighter than an anchor knot. Poseidon, please allow for pleasant skys today. I cannot sleep through something as brutal as last night."
            jump opening
        label choice_name_R:
            MC "It's another salty morning. Poseidon, please allow for pleasant skys today. I cannot sleep through something as brutal as last night."
            jump opening
        label choice_name_User:
            MC "Suffering is key to living. Poseidon, please allow for pleasant skys today. I cannot sleep through something as brutal as last night."
            jump opening

        label opening:
            $ pirate = "Pirate"
            "Sunlight pours into my eyes through the cracks in the old boards."
            "I get up from my cot and scan through my room. It’s a small closet under the stairs to the top deck with barely enough room for anything extra beyond my necessities."

            "I am lucky to have it, one of the only perks I’ve gotten from being the captain's child. The privacy is amazing, and the smells of the common area don’t leak into my nose from here."

            "I’d like to think I earned this spot, but realistically, it was the only spot on the ship to keep a young person without anyone getting to them. Either way I appreciated the forethought."

            "I was supposed to clean the cannons this morning, but I did it last night so I could sleep in. The Code says lights out after sun down, but I’ve cleaned them so many times I need only muscle memory for the job."

            "Nobody has brought it up yet, if they even noticed."

            MC "Arrrgh!"

            MC "Ahhhh!"

            MC "Poseidon, please allow for pleasant skys today. I cannot sleep through something as brutal as last night."

            "I bend in every direction I can, but the stretching doesn’t alleviate the pain in my shoulders. If we are close to a port, maybe I can snag an extra pillow from a cafe or something."

            "I don’t remember having these pains before. Maybe I’m just getting old, I think eighteen is the appropriate age to start thinking that, right?"

            "I heard a new pirate say he hopes May has better weather so I assume April has passed. New guys always have a better sense of the date since they got on not too long ago."

            "So it was my birthday at some point and all I got was new pains. Sometimes Captain says a passing mention of it, but we’ve been out for a while so I doubt he knew."

            th "Wheres [player_name]!? Why arrrgh’t they on deck?"
            "That sounds like my call to action. I quickly throw myself out of bed. My shoes are at my feet, but how could I lose track of my shirt in here?"

            "Scanning my small abode, it evades my glance. It must be under something."

            "Checking behind my stack of books on the floor, the answer slaps the tired right off my face. I was flattening it out after work last night."

            "I was attempting this technique to remove the wrinkles. A side character in a book I just finished did the same and I wanted to see if it would work."

            "Pulling the dirty shirt out from under the heap of literature it’s apparent it failed. A stark reminder to stop reading young adult fiction."

            th "[player_name] get yerr ass out from whatever gutter ye hiding under."

            $ pirate = "Ol' Two Hands"
            "I think that’s [pirate] calling for me. I’m pretty sure I outrank him, but when you’re younger than everyone else the more hardened pirates still treat you like shit."

            "I’ll grab my bristoles and brush my teeth and hair. A delayed head rush from springing up too fast numbs me momentarily."

            "Staring back at me, my cracked reflection shows a blank expression. My salty hair won’t straighten no matter how much I brush and my skin is damaged beyond its original color."

            "I make note over my other features quite harshly to myself. My next thought flickers from the back of my mind."

            if player_identity = "f":
                MC "Could I ever be a woman of the land?"

            elif player_identity = "m":
                MC "Could I ever be a man of the land?"
                
            else:
                MC "Could I ever be someone of the land?"

            th "Damn ye [player_name]. I’ll flog ye later for this."

            Cap "Why are ye threatening a mate so loudly in me presence Two Hands?"

            "Snapping back into action I head for the top deck. It’s time to start moving for real. I could use a peaceful type of day. As peaceful as pirate life can be."

            #fade to new scene

            "Blinding heavenly light engulfs my face as I surface above deck. Men and women working hard, or at least pretending to while The Demonic Pirate Ricardo is watching."

            "Presumably most were slacking off before Two Hands was shouting his head off. The deck is actually pretty clean."

            "The planks are looking pretty good in the bright morning light and they’re especially clear due to the lack of supplies available."

            th "Aye, there thee are Captain, right were I thought thee were."

            "Captain slowly turned around to look at me. His dry expression told me nothing of his mood, but I assume he is annoyed at the unnecessary shrill yelling from Ol’ Two Hands. He takes a step closer to Two Hands getting right in his face."

            Cap "Two Hands, there isn't a pirate saltier than I. But yer a strong second ye seadog. So you know there ain't no reason for a pirate to be screaming for another unless ther be danger."

            th "Of course Captain."

            if player_identity = "f":
                Cap "When I asked you to fetch me lass, I expected ye to do the searching and not be screaming. Ye’ve heard me in battle, am I incapable of hollering?"

            elif player_identity = "m" or player_identity = "nb":
                Cap "When I asked you to fetch me lad, I expected ye to do the searching and not be screaming. Ye’ve heard me in battle, am I incapable of hollering?"

            th "No Captain. Ye have mighty powerful pipes."

            Cap "Aye agree. So if I hear ye flagging a false alarm on me ship again I’ll have Quartermaster Feno give you [player_name]’s jobs for thee rest of thee week!"

            th "Aye Aye Captain"

            Cap "Now get lost ye scurvy dog!"

            # quickly remove th

            Cap "Nobody in line of sight has been on this ship as long as I have. Of the Captain’s {i}Demon Moments{/i}, this wasn’t that bad, but I haven’t flinched during one of them since I was sixteen."

            Cap "The intimidation tactics keep the crew in line and his reputation secured."

            MC "You requested me Captain?"

            if player_identity = "f":
                Cap "Aye [player_name]. Just wanted to talk to ye. The mainland considers ye a real adult now lass. But I’ve been treating ye like that since ye could hold a scabbard. Hahaha!"

                MC "Aye Captain, but I didn’t get good with one until I beat Crookshaw."

                Cap "Aye lass, I remember. That scallywag fell flat on their arse and we prodded dem every night. Haha ha! What happened to Crookshaw after that?"

            elif player_identity = "m" or player_identity = "nb":
                MC "Aye Captain, but I didn’t get good with one until I beat Crookshaw."

                Cap "Aye [player_name]. Just wanted to talk to ye. The mainland considers ye a real adult now lad. But I’ve been treating ye like that since ye could hold a scabbard. Hahaha!"

                Cap "Aye lad, I remember. That scallywag fell flat on their arse and we prodded dem every night. Haha ha! What happened to Crookshaw after that?"

            MC "He tried to flee his service from embarrassment and you obliged by marooning him."

            Cap "Oh, that be right. Ha ha, ahhh. Nevertheless I wanted to give ye something. I got something made for ye, something I wish my."

            Cap "Captain"

            Cap "Gave me when I became a man. But aye, aye don’t have it yet. It’sa gonna be loaded up at the port. I mainly wanted to say to ye is don’t worry about yer usual duties at port."

            Cap "I got Feno to rearrange the grunt work so you could enjoy some of the fruits of land life."

            MC "Oh, thank you Captain. This is pleasantly unexpected."

            Cap "Argh, what you expected nothing from me?"

            MC "No, it’s wonderful and thoughtful gift. I will use it wisely. Do you need me to get you anything?"

            Cap "No, no, nothing for me. There be nothing else I’ll ever need from this port ever again. Personally that is. We’re gonna need a lot more cannonballs of course."

            Cap "Hahahaha ha!"

            MC "Ha ha."

            MC "Yes Captain I guess we always need more of those."

            Cap "Don’t be telling the crew where ye going. Don’t want dem thinking The Demonic Pirate Ricardo has gotten soft."

            MC "No, never Captain."

            if player_identity = "f":
                Cap "Get it out of yer system now lass. If not fer me, member yer mudder. She gave up da land life fer da free sea. And she never looked back."

                MC "Aye Captain. I’ll keep that fresh in my mind."

                Cap "Alright lass, dismissed. Put on something nicer and don’t get arrested."

            elif player_identity = "m" or player_identity = "nb":
                Cap "Get it out of yer system now lad. If not fer me, member yer mudder. She gave up da land life fer da free sea. And she never looked back."

                MC "Aye Captain. I’ll keep that fresh in my mind."

                Cap "Alright lad, dismissed. Put on something nicer and don’t get arrested."

return
