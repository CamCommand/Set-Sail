label act1_3:

    pause 1.5
    scene BG school with fade
    define astrid_temp = "Girl"

    "Found it!"

    "This place is massive, are all schools like this?"

    "The large entrance doors are dwarfed by the humongous stone columns lining the front of the building. People are flooding out and filling the parking lot."

    play sound "audio/chattering.mp3"
    # add the crowd png when made

    "Other than narrowly avoiding leaving cars, nobody is staring at me."

    "The letter said someone would meet me outside the school, but there are so many people my rendezvous could be anyone. If everyone is leaving the school, I should wait to see who stays, they’ll be the club member."

    "All sorts of students are leaving. The array of people who go to this school seems vast."

    "One guy looked like a gorilla who’d fit well on the ship. This other kid might get blown under water by a small wave."

    "You’d think they’d be put into weight groups so the bigger ones don’t demolish the tiny children."

    with fade
    stop sound fadeout 2.0

    "Standing alone on the sidewalk, it takes about fifteen minutes for the clumps of students and faculty to disperse."

    "There are a few stranglers hanging around and talking. But this one girl has been standing on the stairs looking directly at me for a bit now."

    "She’s the only person standing alone. This couldn’t be who I was waiting for? If she was expecting the Captain, this is who they sent to greet him?"

    show a_d at center with dissolve

    MC "Uh, hello. You waiting for me lass?"

    # I redefine Astrid so much to change her name per the situation
    # I will also use the what_outline parameter to show feedback for positive choices
    $ a = Character('Girl', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])
    a "{cps=80}Ahhoooo{/cps}{cps=5}OOOOOOOOOOOO{/cps}{cps=50}oooooy Matey!{/cps}"

    #$ astrid_temp = "Astrid of Bellewood"
    $ a = Character('Astrid of Bellewood', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])
    a "{cps=75}I’m Officer Astrid of Bellewood at {color=#5FAFF6}Seaborough{/color} High School! Permission To Speak Easy Captain, Sir?!{/cps}"

    "Poseidon help me this girl is..."

    menu:# MC's different reactions to first meeting Astrid
        "She’s Enthusiastic":

            MC "Are you alright?"

            MC "No need to yell at me, Astrid of Bellewood."

            a "Thank you Captain. Bellewood is actually my last name, I just thought it would sound cooler in my introduction."

            MC "Can I just call you Astrid?"
            $ a = Character('Astrid', color="#FF79E6", callback=astrid_voice)

            a "Aye aye Captain!"

            MC "Fine Astrid, you can simply call me [player_name] no need to use titles like that on land."

            a "Aye aye [player_name]!"

            jump school_entry

        "She’s Amazing":

            MC "That’s incredible, at ease Astrid of Bellewood."

            $ Astrid_affinity += 1

            $ a = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (1, "#000000") ])
            a "{color=#50A23B}Thank you Captain. Bellewood is actually my last name, I just thought it would sound cooler.{/color}"
            #{color=#00ff00}{/color}
            #play good boy points sound effect

            MC "It sure did sailor."

            jump school_entry

        "She’s Beautiful":

            "She’s stunningly beautiful!"

            $ Astrid_affinity += 3
            MC "Umm, at ease Astrid of Bellewood."

            $ a = Character('Astrid', color="#FF79E6", callback=astrid_voice)
            a "{color=#50A23B}Thank you Captain. Bellewood is actually my last name, I just thought it would sound cooler said like that.{/color}"
            #play good boy points sound effect

            MC "I’d agree. You can just call me [player_name]."

            #$ a = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])# turn outline off
            a "Aye aye Captain [player_name]!"

            jump school_entry

        "{i}She has brain rot{/i}":

            MC "Have you acquired brian rot sailor?"

            $ Astrid_affinity -= 3
            a "{color=#f00}No Captain, Sir!{/color}"
            # play bad boy sound effect

            MC "Then why are you screaming bloody murder at me?"

            a "To show my respect Captain, Sir!"

            MC "You can just call me [player_name], stop yelling please."

            a "Aye aye Captain [player_name]!"

            $ a = Character('Astrid', color="#FF79E6", callback=astrid_voice)
            a "You can call me Astrid, Captain [player_name]."

            jump school_entry

    label school_entry:

        $ a = Character('Astrid', color="#FF79E6", callback=astrid_voice, what_outlines=[ (0, "#000000") ])
        a "Welcome to {color=#5FAFF6}Seaborough{/color} high school."

        a "I’m the current president of the Pirate Culture Club here. I’ll assume from your breezy shirt and filthy pants you’re a pirate of {color=#f00}The Red Plague{/color}."

        "Are my pants filthy?"

        "Covertly, I rub my thumb against the side of the leg. A black residue stains comes off on me. I thought these pants were a dark color."

        "What color are my pants?!"

        MC "Yes, that’s me. I’m the first mate."

        MC "The um, Captain sent me instead. We are here on important business and he was needed elsewhere."

        a "That makes sense. It was a longshot to try to get the big demon to show up at a high school anyway."

        "The big demon?"

        a "Well [player_name] you seem pretty cool."

        a "Come on inside and meet the rest of the club. They should be almost done setting up."

        "{cps=10}I seem cool!{/cps}"

        "{cps=20}A girl my age thinks I’m cool!{/cps}"

        "Cool is good, I'm almost certain of it."

        MC "That’s cool, lead the way."

        scene BG hw with fade

        "Astrid is guiding me through a labyrinth of dull hallways. Every corridor looks identical to the last, only a few pieces of colored paper lining the door frames give off any sense of divergency."

        "They’re so eerily empty, aif someone was meant to jump out and scare me. Our footsteps echo off the walls, enhanced by the silence. Astrid stops at a closed door on our left side."

        show a_d at center with dissolve
        a "This is it, our humble club appointed classroom. It isn't very flashy, so don't expect it to be overflowing with pirate stuff."

        a "Are you ready to meet everyone?"

        menu:
            "As ready as I can be":

                MC "Arrrrrgh, you bet Astrid."

                a "Definitely give them your best pirate \"arrrr\" right away. It’ll solidify you right away."

                jump classrooom_one

            "No wait":

                MC "Wait Astrid."

                a "Yeah? What’s up?"

                jump classroom_hesitation

        label classroom_hesitation:

            menu:
                "Anything I should know?":

                    MC "Anything I should know before going in?"

                    a "{cps=10}Hmmmmmmmmmm.{/cps}"

                    a "Don’t expect a big crowd. It’s like, just us on the e-board and a few straggling members who were in there before I went to get you."

                    a "We advertised that a real pirate would be coming but either nobody believed us or nobody cared. There’s some benefits to being a smaller club, but yeah, not too much."

                    MC "Oh, I’m sorry about that."

                    a "Don’t be. We aren’t a huge club for more than a few reasons. Most of the pirate stuff is just an excuse for us all to hangout."

                    MC "I understand."

                    a "But we do like pirate things. You’re gonna be great in there, I’m sure of it [player_name]."

                    MC "Thank you Astrid. I’ll put my best foot forward as they say."

                    a "Great, but I don’t think anyone says that anymore."

                    jump classrooom_one

                "Anything I should say?":

                    MC "Anything I should say to them?"

                    a "Give everyone a good story and a hardy \"arrrrrrgh\". Also they’re probably going to ask you a bunch of questions."

                    a "I’m holding all mine in right now by a thread. Why did I say that?"

                    "Her gaze swiftly averts to the lockers on the wall. No problem answering questions, but if they start getting repetitive I’ll cut her off."

                    MC "I’ll give it the ol’pirate try."

                    a "Is that a thing?"

                    MC "Not yet, pirates aren’t too keen on learning new lingo."

                    a "Well maybe you can pick up some new ones here."

                    jump classrooom_one

        label classrooom_one:

            #open door sounds
            scene BG cr with fade

            "The door opens to a barren classroom with no more than eight people in it. There are some skulls and hearts drawn on the whiteboard, yet the rest of the room has been thoroughly cleaned."

            "Or at least has been kept this clean intentionally. It reminds me of how the ship looked with none of the supplies on it when."

            show a_d at center

            a "{cps=80}Everyone! Attention!{/cps}"

            if player_identity == "f":
                a "This is [player_name]. She’s a member of {color=#f00}The Red Plague{/color} pirate ship that terrorizes the Gulf of Mexico and all the surrounding waters."
            elif player_identity == "m":
                a "This is [player_name]. He’s a member of {color=#f00}The Red Plague{/color} pirate ship that terrorizes the Gulf of Mexico and all the surrounding waters."
            else:
                a "This is [player_name]. They're a member of {color=#f00}The Red Plague{/color} pirate ship that terrorizes the Gulf of Mexico and all the surrounding waters."

            a "Why don’t you introduce yourself [player_name]? Say a little about yourself too."
            hide a_d with dissolve
            show b_d at right
            show g_d at center
            show f_d at left
            MC "Yeah, I’m capable of that."

            $ f_met = 0
            $ g_met = 0
            $ b_met = 0

            menu:
                "Be honest with them":

                    MC "Hello everybody. My name is [player_name], but you already knew that. I’ve been a pirate my whole life and served on {color=#f00}The Red Plague{/color} during that time."

                    MC "Most days at sea are treacherous and exhausting, but the life is free and can be very rewarding. I had to work my way towards  becoming the first mate in that time."

                    MC "However, ranks only come with more responsibility on pirate ships. It doesn’t automatically earn you respect."

                    "Someone is holding their hand above their head all of a sudden. Did I do something wrong? Is this a test?"

                    "If I pause Astrid should get the hint."

                    a "Oh!"

                    a "That’s a high school thing. We raise our hands when we have a question as to not blurt them out when someone is talking."

                    a "That’s Fiona, she’s our Vice President."

                    hide g_d
                    hide b_d
                    show f_d at center with dissolve

                    MC "What’s your question Fiona?"

                    $ f = Character('Fiona', color="#E44D1A", callback=fiona_voice)# Fiona
                    f "What earns you respect on pirate ships? Do you have to be a big strong man to get it?"

                    "Her tone makes it sound like she already knows the answer. Captain does a similar trick."

                    MC "What earns you respect?"

                    MC "From my experience, it’s feats and age. I feel as if I’ve done some pretty heroic things for the greater crew, but I’m treated like I was kidnapped yesterday."

                    MC "As for your second concern, our ship has had many prominent women figures throughout its voyage. And I’ve met a handful of retired female Captains in our travels."

                    MC "On the sea, when you’re fighting for everything you got, the only thing that matters is your merit."

                    f "{color=#50A23B}Well that’s a pleasant surprise.{/color}"

                    MC "Being a pirate is all about how good you are at the job. There have been some amazing pirates who are unbearable to talk to and be around."

                    MC "But when the going gets tough, a great pirate tightens their buckle and draws their sword."

                    "The room rings with a  small wave of applause. I’ve never been clapped at before."

                    $ Fi_affinity += 1
                    $ f_met += 1
                    jump classrooom_two

                "Exaggerate to sound cool":

                    MC "Ahoy everyone! I’m the Dreaded Pirate [player_name]."

                    MC "{color=#f00}The Red Plague{/color} and I have been ruling the southern seas for over fifty years. I’ve seen the coolest things the world has to offer and I haven’t paid for a single thing in my entire life."

                    MC "We steal exports, we swipe imports, we take minerals, products, people, and sink ships of anyone who offends our noses. Our brutal tactics made us a scourge of the Atalantic."

                    "Some girl in front is raising her arm above her head. Is she calling me out? Does Astrid know what she’s doing?"

                    a "Oh!"

                    a "That’s a high school thing. We raise our hands when we have a question as to not blurt them out when someone is talking."

                    a "That’s G, she’s our club’s Secretary."

                    hide f_d
                    hide b_d
                    show g_d at center with dissolve

                    MC "Aye lass, what’s yer question?"

                    $ g = Character('G', color="#F0CD00", callback=g_voice)# Geraldine
                    g "Hi [player_name], loving the accent by the way. Question."

                    g "What’s the coolest thing you’ve seen while stealing something? Like anything wackier than the average haul?"

                    "She called me out!"

                    MC "Well, let me think on that. Hmmmmmmm."

                    MC "It would have to be that time I saw Poseidon himself do his duty. We stole a Mexican vessel’s shipment full of beers and sodas."

                    MC "Their boss begged the Captain on his hands and knees to spare their lives. He offered to share his best whiskey with the Captain to convince him."

                    MC "The drink was so good that, according to the Demonic Pirate himself, he allowed them to pass his sea."

                    MC "As we sailed away from the ship a storm started to shake up the waves. I turned towards the ship and one sailor was loading a rocket propelled grenade and aimed it at our tail."

                    MC "Before I could brace for impact, an uncharacteristically powerful wave for that stage of the storm was knocked into the Mexican ship."

                    MC "The sailor must have been hit hard because his ship exploded right as they got hit. And our lives were saved by his divine decision."

                    g "{color=#50A23B}That sounds so cool. Did the ship sink?{/color}"

                    MC "Straight into Davy Jones."

                    g "I feel so much better now that I know Poseidon is real. Did you guys know this and not tell me?"

                    $ G_affinity += 1
                    $ g_met += 1
                    jump classrooom_two

                "Scare them away from piracy":

                    MC "Alright lassies here’s the dark truth from a subordinate of the Demonic Pirate Ricardo himself."

                    MC "Piracy is incredibly dangerous. Our lives are on the line everyday. We could be shot at, thrown overboard, or starved at sea."

                    MC "Constantly fighting for life and death just for a sliver of profits is a dreary way to live."

                    MC "Our living quarters are dank and grim. I had to burn through skin and bones to get a proper bed when I was fifteen."

                    MC "Pirates are the worst type of people. They’re remorseless thieves and you’re treated like dirt unless you’re in charge."

                    "Some girl in front is raising her arm up in the air. Is she trying to question me? Does Astrid know what she wants me to do?"

                    a "Oh! That’s a high school thing."

                    a "We raise our hands when we have a question as to not blurt them out when someone is talking. That’s Behati, our club's Treasurer."

                    hide g_d
                    hide f_d
                    show b_d at center with dissolve

                    $ b = Character('Behati', color="#5E0F60", callback=b_voice)# Behati
                    MC "Aye lass, what’s the problem?"

                    b "Y-yes hello, [player_name] isn’t it true that eight-six to ninety-nine percent of total goods stolen are raw material exports that the government plans to lose in their budgets?"

                    b "Ones that crews are instructed to not fight over and to protect themselves? Wouldn’t that make the act of piracy a part of the system as a whole and not an outlier?"

                    "What is she even talking about?"

                    MC "Do I look like someone who's familiar with your mainland statistics?"

                    b "Well y-you can account for your own ship’s actions, r-right?"

                    MC "Aye, well it’s true that American vessels tend to avoid us at all costs, others aren’t so cautious."

                    MC "We don’t steal from just governments. Other pirates and pleasure cruises are prime targets for loot of all kinds."

                    b "Are t-those unaccounted for in your main piracy focus?"

                    b "B-because how would you know where another pirate ship is going to be?"

                    b "Or if, if some oil millionaire’s kid is going on a joyride?"

                    MC "Behati was it?"

                    b "Yes that’s me."

                    MC "Pirates don’t have quotas or missions."

                    MC "We take advantage of opportunities and solve problems we come across with the tools at our disposal. The grand plan is wild riches and being free."

                    MC "No matter the costs."

                    b "{color=#50A23B}T-thank you for your honesty. That’s a lot to digest, I’ll adjust my data points accordingly.{/color}"

                    $ Be_affinity += 1
                    $ b_met += 1
                    jump classrooom_two

        label classrooom_two:
            # activity variables for menu
            $ activity_check = 0
            $ food_ate = 0
            $ b_check = 0

            hide g_d
            hide f_d
            hide b_d
            show a_d at center with dissolve

            a "That was a pretty good introduction. Thank you [player_name], I think we all learned a little more from that."

            a "Why don’t we eat some of the food that G brought and we can kinda just talk some more. You can spread the culture on us as thick as you want."

            hide a_d

            "The people not paying attention perked up for the food to rush the table. I expected to monologue more, guess it’s less pressure on me now."

            "Giving speeches is exhausting, no wonder Captain sounds as grizzled as he does. He’s had to speak over the ocean his entire life."

            "Well, his \"speeches\" are more like screaming matches, but still. What should I do now?"

            "Do they want me to socialize and answer more questions?"
            jump classroom_choice

        label classroom_choice:

        menu:
            "Socialize":
                jump social

            "Get some food" if food_ate == 0:
                jump food

            "Use the bathroom" if b_check == 0:
                jump washroom

            "Leave" if activity_check == 3:
                jump leave

        label social:

            # keeps track of conversation moments
            $ b_convo = 0
            $ f_convo = 0
            $ g_convo = 0
            $ a_convo = 0

            # Leaving menu list of respones
            $ leave["Maybe not right now.", "Wait a second.", "Not just yet."]
            $ rand1 = renpy.random.randint(0, 2)

            # just a check to do an intro line
            $ x = 0
            if x = 0:
                "This is what I wanted to do on land. Talk to people my own age, I should take advantage of this moment."
                $ x += 1
            "Who should I talk to?"

            menu:
                "Behati" if b_met == 1:
                    jump behati

                "Girl with large spectacles" if b_met == 0:
                    jump behati

                "Fiona" if f_met == 1:
                    jump fiona

                "Taller girl" if f_met == 0:
                    jump fiona

                "G" if g_met == 1:
                    jump g

                "The unassuming girl" if g_met == 0:
                    jump g

                "Astrid" if a_convo < 4:
                    jump astrid

                "No wait":
                    $ bye = leave[rand1]
                    "[bye]"
                    jump classroom_choice

        label behati:

            show b_d at center with dissolve

            if b_convo == 0:

                if b_met == 0:

                    MC "Hello, it’s nice to meet you young lady. Are you a valued member of the club or just came to see a pirate?"

                    b "Y-yes hi I am. I’m B-behati. T-thank you for c-coming t-today."

                    MC "Are you nervous about something Behati?"

                    b "Meeting a real p-pirate is overwhelming. I don’t, well I can’t. No, I-I d-don’t know what s-s-say, I-I mean."

                    MC "It’s alright, I’m not going to hurt you in any way."

                    MC "I was just trying to show everyone that being a pirate isn’t what you think it might be. Trying to be realistic, you know?"

                    b "It’s okay, I’m fine. I just need to breathe."

                    b "But, you’re not giving the Pirate Culture Club enough credit. We aren’t just a bunch of weebs, we appreciate the life you live. It’s admirable."

                    $ b_met += 1

                else:

                    MC "Well, what did you think of my opening Behati?"

                    MC "Maybe I said a little too much. It was to show everyone that being a pirate isn’t what you think it might be."

                    b "Hey [player_name]."

                    b "That was definitely a shock, but you shouldn’t underestimate us. We aren’t just a bunch of weebs, we appreciate the life you live. It’s admirable."

                MC "What do you mean?"

                b "I mean we all love something about being a pirate that we can’t fully enjoy in our own lives."

                MC "Like what?"

                b "I don’t want to speak for anyone else here other than myself. There’s a ninety percent chance they’ll tell you themselves."

                MC "That’s alright, but what about you Behati? What do you think about pirates?"

                b "{cps=15} M-me? I ummmmmmm. I am.{/cps}"

                b "I’m used to figuring out stuff I like pretty fast. When I was younger I saw one movie about Somlian pirates and was swept up by everything pirates are."

                b "The open seas, stealing to survive, all the interesting uses of old and new technology. It’s such a rich history, I’ve been wiki diving on new pirate stuff almost every month for the past two years."

                MC "What’s a \"wiki dive\"?"

                b "Oh my God, does your ship not get wi-fi? A generator for a mi-fi box even?"

                MC "Since those words mean nothing to me, I’ll say no."

                b "Do you know what the internet is at least?"

                MC "I have a vague understanding. It’s like videos and music right?"

                "Behait’s face shows some sign of relief. I should have had a better definition prepared, knowing that the internet is important to people our age."

                b "Well yes but there’s so much more. Movies, music, videos, games, the solar system of information!"

                b "But it also has something called a wiki. It’s like all the information we have on super easy to read pages all linked together."

                b "With pictures and citations and there’s a page for everything. They’re constantly updated so you’re never behind and it's and and the-"

                MC "So like a really long book?"

                "She exhales loudly into her hands. How long would she have kept going if I didn’t stop her?"

                b "Think the biggest encyclopedia ever."

                MC "That definitely sounds great for everyone."

                b "There’s even a page on {color=#f00}The Red Plague{/color}. It’s not well documented because a lot of historic pirating is told through legal documents after they’ve been hanged or died."

                b "However, your ship is often recorded as the reason for lost products publicly for some companies. I wonder why there’s only a few?"

                MC "Thats so great. It sounds wrong, but just true enough to keep the mythos alive."

                b "Yeah it’s pretty cool, I wish there was more info though."

                MC "Cool. Yes that's cool."

                b "Heh ha, very cool."

                b "And if you can prove who you are you can edit it yourself."

                MC "I could write a book?"

                b "Well you can edit your ship’s wiki page, sure. Help fill out the page but keep the details ambiguous so you’re still scary."

                MC "I’ll think of stuff to add and get back to you. Thanks Behati."

                b "No, I can't do anything unless you have public docu-"

                b "Nevermind, if you think of anything let me know."

                $ b_convo += 1
                hide b_d with dissolve
                jump social

            elif b_convo == 1:

                b "Hey [player_name], did you think of anything you wanted to add to your page?"

                MC "Yes! Something very cool."

                b "What is it?"

                MC "This great tale on how we ran over a blue whale from the bow of the ship."

                MC "The heroics of harvesting it’s resources against our own lives, the whole crew pitched in  this one and a lifetime-"

                b "{cps=15}Ummmmm. But, that’s n-not.{/cps}"

                MC "What you don’t think it’s true?"

                b "No it’s just that, this isn’t a book."

                b "Wikis are supposed to be informational. They aren’t the place for hearsay stories or non formative tales."

                MC "Alright, even though this is entirely a formative tale, I know what you mean."

                "That's really disappointing. I thought I could get a scribe to tell our tales for free. Most scribes aren’t worth the ink they charge us for."

                b "Something like, how many pirates are on the ship?"

                MC "I’d never reveal that information. But also I don’t know and it’s always changing anyway."

                b "Do you have any siblings onboard? Maybe like a special pirate task force for important battles?"

                MC "What are you talking about?"

                b "Okay so some of us are also weebs, don’t worry about it. Both my brothers left for college last year, so I’ve been able to use the big T.V. after school for anime."

                "What is she trying to say? I think the whale story may have made things weird."

                "I can still steer the conversation away from the awkward wiki misunderstanding."

                MC "Your brothers are seeking higher education? That’s interesting, do you want to do the same?"

                b "Yeah, I want to do the same."

                b "Jack and Tye both went to New York to study business, but I think I’ll stay in state. Try to become a teacher."

                b "Not sure what kind of teacher yet, so many subjects interest me. It’s not like I could choose the curriculum myself. That part sucks."

                MC "There are lots of illiterate pirates, if you want you could teach language on a pirate ship. Plenty of ships would pay for less stupid help."

                b "Oh my, being on a pirate ship sounds overwhelming. I’d want to do so much learning by myself. I’ve never even shot a gun before."

                MC "Do you want to?"

                b "Really badly yes. Is that weird?"

                b "I’ve read so much about older and new pistols. The mechanisms are so fascinating to me."

                MC "Is there a lot you gravitate towards about the pirate culture?"

                b "The club has been a big influence on me, but yeah, it all seems so cool."

                b "If I could teach a pirate class I would. But the school would have to let me bring in firearms."

                MC "Ha hahaha! Be sure they aren’t loaded at least."

                b "No way, I’m firing it. I read that old flintlocks make sounds louder than desert eagles. I have to know if that’s true."

                MC "I can confirm they are very loud."

                b "Something might be louder actually. I have to look this up."

                "Behati pulls out her device I’ve seen her look at before and begins tapping furiously. It seems like I’ve lost her to the wikis."

                $ b_convo += 1
                hide b_d with dissolve
                jump social

            elif b_convo == 2:

                "Behati is vigorously reading her device. I don’t know if she could hear me even if I tried."

                if book_choice == "smart":
                    # use this color when a previous choice has paid off
                    b "{color=#F0FF3F}Hey [player_name]. What’s sticking in your waistband? Is that a book or something?{/color}"

                    "How did she notice, she didn’t even glance at me, seemingly."

                    MC "Yes, it’s a book. I grabbed this book from a store after I got off the ship. Thought it could be an interesting read."

                    b "Oh! It’s a Gail Mcryson book!"

                    b "Her books are all super interesting. I have a bunch stacked up under my bed I got for my birthday. You’re interested in space?"

                    MC "Well, I’m not entirely sure yet. This could be the deciding factor."

                    b "Then I think you’re gonna become obsessed like me after reading it."

                    "Behati grows a big grin and then gets flushed after she holds it for too long. She’s clearly passionate about her interests but not the most prideful of them."

                    "All I learn out at sea is how to be a pirate. Here is where I think the most knowledge lies."

                    $ book_choice = "used"# just to know when the variable is used
                    $ b_convo += 1
                    jump social

                else:
                    b "I’m checking online if I could reasonably get an old timey gun."

                    MC "That’s cool. Need my advice?"

                    b "I mean. I don’t know what would work or be better if I could get one."

                    b "But it looks like they are all really expensive and I’m not sure yet how legal it would be for a minor to own one."

                    MC "That’s unfortunate."

                    MC "To make the process cheaper, you should look for a gun that takes bullets. Straight gunpowder guns are a pain and finding raw materials for them is borderline impossible."

                    b "Thanks, that’s good advice."

                    $ b_convo += 1
                    jump social

            else:
                "Behati is vigorously reading her device. I don’t know if she could hear me even if I tried. I should get one of those if they’re as cool as she says."
                jump social

        label fiona:
            "testfiona"
        label g:
            "testg"
        label astrid:
            "testastrid"
        label food:
            "testfood"
        label washroom:
            "testwashroom"
        label leave:
            "testleave"
    return
