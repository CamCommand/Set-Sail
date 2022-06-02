# Cameron Drummond 2021-2022
# version 1.0.5
label act1_6:

stop music fadeout 2.0
play music track1 volume 0.5 fadein 1.5 fadeout 1.5

scene BG black with fade
pause 1.0
scene BG cafeoutside with fade

if may_talk == 0:

    "After some more aimless wandering, finally a strip where everything isn’t closed."

    "Actually, most of these businesses do look closed."

    "There’s what looks like a small café coming up on the right."

    "Even without the \"Open Café\" sign hanging from the canopy, the smell of brew bubbles up into my nostrils."

    "It’s about time something other than pollution or sea water tickled my sense of smell."

    "There are some people eating and drinking inside. This might be my best chance of getting some grub before I figure out where to go next."

    "I barely have energy to steal at this point. Begging them to take my earrings as payment is my only option."

    if earrings == 0:

        "That is, if I still had them."

        "That sly wench stole them right off my head and I didn’t even go after her."

        "How pathetic is that? Maybe if I’m fed my wrath will reawaken."

    if may_v == 2:

        "I could have had some money if that woman didn't take it all for herself."

        "If she only knew how desperate I am, maybe she would have spared me some change."

    "Getting closer to the windows, people are being served sandwiches and soups. Nobody but the server is wearing a mask though."

    "Apparently this covid thing spreads through air, but not food?"

    "Seems strange, but I've never suffered from anything worse than Ocean's Ear."

    "My stomach is in control of my eyes now, the soup’s holding onto my line of sight and not letting go."

    show BG cafeoutside ast with dissolve

    mc "Except that woman. Is that..."

    mc "Astrid?"

    show BG cafeoutside ast sup with dissolve

    "I hardly believe my eyes."

    "It’s unbelievable, this is where I had to go!"

    "Astrid is who I was meant to find!"

    "Thank you Gods, you’re all gracious and benevolent, I’m sorry for ever doubting you weren't looking out for me."

elif may_talk == 1:

    show may flip at left with dissolve

    "After some more small talk, Hann and I make it to the side of this small café."

    "Strolling down the side of the large strip of closed shops, the strong smell of brew bubbles up into my nose unexpectedly."

    "Finally, something to drown out the mix of sea water and dry trash."

    "There are a few people inside the café I can kind of see through the window."

    "Can’t tell if that’s a good or a bad thing at this point. They aren’t wearing masks while waiting for their food."

    m "You should put on your mask before we go in."

    m "It’s probably fine, but still, it’s better if you do, I've learned."

    if mask == 1:

        mc "Yeah I got one from a street lady I met."

        mc "It was real nice of her, she didn’t even charge me."

        show may flip at bounce

        m "You took a mask from a random person on the street?"

        mc "Yeah? So what? It was sealed when she handed it to me."

        m "Wait, was this lady kinda scraggly looking? Said \"somethin'\" a lot?"

        mc "Yeah, she said to call her Doll."

        show may smile flip with Dissolve(0.1)

        m "Oh Doll! I've talked to her before. She seems really cool for a homeless person."

        mc "Are all homeless people not nice?"

        show may sad flip with Dissolve(0.1)

        m "No, that's not what I meant."

        m "Nevermind that, I don’t want to get into this."

    else:

        mc "I never got one. People weren’t exactly being super nice to me about it."

        mc "Plus, nobody told me about this disease ruining everything cool."

        show may sad flip with Dissolve(0.1)

        m "It’s worse than just a disease, a whole ass pandemic has been going around."

        m "Although, at this point people seem to act like it’s over."

        mc "You mean they cured it?"

        show may flip

        m "No."

        mc "So how did they get over it? Did it die out?"

        if badwords == True:

            m "No, they just stopped caring. Some people needed haircuts and {b}silly stuff{/b} like that."

        else:
            m "No, they just stopped caring. Some people needed haircuts and stupid shit like that."

        mc "Oh...Well that’s one way to do it."

        mc "Couldn’t they just give themselves a haircut?"

        show may smile flip with Dissolve(0.1)

        m "Haircuts are really important [player_name]."

        mc "I wouldn't know, I just cut off my split ends once in a while."

        m "Rich kid like you didn't have a ton of professional barbers lying around?"

        mc "Ugh, you live and learn I guess."

        show may smug flip with Dissolve(0.1)

        m "Our hindsight is better every day isn't it?"

    "Walking by the windows I start to make out some of the people inside."

    "Soup and coffee are being served to a large table. My stomach has taken over my eyes, I can’t look away."

    "Perhaps these dishes are worth it to the type of people who’d brave this supposedly deadly disease?"

    show BG cafeoutside ast with dissolve

    mc "Is that?"

    show BG cafeoutside ast sup with dissolve

    show may flip with Dissolve(0.1)

    m "Do you know that girl?"

    mc "Hann, she looks so much like someone I used to know."

    m "You think she’d pay for the coffee?"

    mc "No, I don’t think so. Hann, can we sit with her?"

    mc "I think she's an old friend of mine. She’s who I’ve been looking for today, I hope."

    show may fl flip
    $ m = Character('[may_name]', color="#ffc77f", callback=may_voice, who_outlines=[ (1, "#000000")])

    m "Sure, I guess. What is she your little ex-girlfriend?"

    if Astrid_affinity > Fi_affinity and Astrid_affinity > Be_affinity and Astrid_affinity > G_affinity:

        mc "What?! No! I mean, like, I don't think."

        show may fl flip at wiggle

        mc "Look I just know her, alright? She’s a good omen."

        mc "Are you coming in with me or not?"

        show may flip with Dissolve(0.1)

        m "Okay relax, sure thing. I said I was, didn't I?"

    else:

        mc "No, quick teasing me. She’s just a friend of mine."

        mc "This is a good omen, are you going to come sit down with me or not?"

        show may flip with Dissolve(0.1)

        m "Chill okay, I said I was going to, didn’t I?"

$ w = Character('Waitress', color="#FF793B", callback=rot_voice) # resuing the market woman for the waitress

transform caf: # align long cafe bg at the left

    xalign 0.0

transform cafe: # transition to other end of BG

    linear 2.0 xalign 1.0

stop music fadeout 2.0
scene BG cafeinside at caf with fade
play music track3 volume 0.5 fadein 1.5 fadeout 1.5

if may_talk == 1:

    show may at lefter with dissolve

if mask == 1:

    w "Welcome to Corner Café, take a seat wherever and I’ll get right to you."

else:

    w "Excuse me, could you please put on a mask before entering the café?"

    mc "Do I have to?"

    w "No, we can’t make you, but it’s highly encouraged."

    mc "Okay thanks for nothing then."

    w "Uh!"

show ast suppost at center with dissolve

mc "Astrid of Bellewood? Is that you?"

a "[player_name] oh my gosh it’s so good to see you."

show ast happypost with Dissolve(0.1)

a "Yeah, it’s me, Astrid. People keep dropping the \"of Bellewood\" part, but not you."

a "Also I just changed my hair."

show ast confpost

a "What are you doing back here?"

mc "That is such a long story, but I’m so glad to see you."

mc "I feel as if I was destined to find you here."

show ast happypost with Dissolve(0.1)

a "Don’t get all sappy on me now. You were destined to find me?"

mc "Well I mean, I think the Gods guided me here for some purpose."

a "You know I thought all that talk about the Poseidon and Greek Gods was you playing the pirate role up for us."

mc "No, I believe them to be as real as the waves that guide us."

a "That’s pretty dramatic, but I guess that fits."

show ast sadpost with Dissolve(0.1)

a "Are you dehydrated or something? You don't look so good."

if may_talk == 1:

    show may smile with Dissolve(0.1)

    m "Um hello?"

    mc "Oh my bad. Astrid, this is Hann."

    mc "She was showing me around and was going to buy me some food."

    show ast post with Dissolve(0.1)

    a "Nice to meet you Hann."

    a "Any friend of [player_name] is a friend of ours."

show ast post with Dissolve(0.1)

a "We are all actually catching up right now."

if may_talk == 1:

    a "Do you both want to join us?"

else:

    a "You want to join us?"

mc "We? Like the E-board?"

show ast post at wiggle

a "Yup, we’re having a little get together."

mc "Of course, I’d love to hear what you’ve all been up to."

pause 0.3
scene BG cafeinside at cafe
pause 1.0

show fi madpost at leftist
show be quizpost at rightwing
show ge smugpost at righter
with dissolve

g "The Queen isn’t gonna make it I’m telling you, she’s done for this time next month."

b "She has access to the best healthcare in her entire country."

b "Women live on average longer than men. She is the most likely candidate to break the oldest age record."

show fi madpost

if badwords == True:
    f "I don’t believe the {b}stank{/b} you’re spewing G."

else:
    f "I don’t believe the shit you’re spewing G."

f "Why are you rooting for an old lady to die?"

show ast post at leftiem with moveinleft

a "Guys, you won’t believe what destiny swept in."

mc "Hey everyone."

show fi post with Dissolve(0.1)

f "Well I’ll be damned."

show be suppost with Dissolve(0.1)

b "What are the odds you’d show up again?"

show ge suppost with Dissolve(0.1)

g "No freaking way man, and I almost didn’t show up today."

mc "It’s good to see you’re all as lively as I remembered you."

if may_talk == 1:

    show may at center behind fi with dissolve

    mc "Everyone, this is my new friend Hann."

    mc "She helped me find this place, is it alright if she sits with us?"

    show fi happypost with Dissolve(0.1)

    f "No problem, welcome to the table."

    show be post
    show ge post
    with Dissolve(0.1)

    b "Nice to meet you."

    show may smile with Dissolve(0.1)

    m "Hello hello, nice to meet you too."

    show ge smilepost with Dissolve(0.1)

    g "Sit down you two, don’t keep us waiting. I wanna know what’s happening."

show ge smilepost

g "What are you doing back here?"

f "Was Astrid joking or did destiny really guide your way?"

show be happypost with Dissolve(0.1)

b "Don’t be silly Fiona, obviously the Red Plague is in port again."

show fi sadpost with Dissolve(0.1)

f "Then why haven’t we heard about it?"

show be confpost with Dissolve(0.1)

b "Oh, that’s because..."

show be quizpost with Dissolve(0.1)

b "Well you can tell us [player_name]."

mc "That’s an, uncomfortable subject right now."

show ast sadpost
show be suppost
with Dissolve(0.1)

a "What’s wrong, I didn’t want to pry but you don’t look so good."

if may_talk == 1:

    show may with Dissolve(0.1)

    if player_identity == "f":

        m "I think she’s just hungry."

    elif player_identity == "m":

        m "I think he’s just hungry."

    else:

        m "I think they’re just hungry."

    m "Hey waitress, can we get two cups of black coffee and a chocolate chip muffin?"

    mc "Thanks Hann, again that means a lot."

else:

    mc "Right now, I’m just really hungry."

    show ge smilepost with Dissolve(0.1)

    g "What? Don’t they feed you on that ship?"

    show fi madpost with Dissolve(0.1)

    f "G!"

    show ge madpost with Dissolve(0.1)

    g "What!"

    if player_identity == "f":

        f "She just said she doesn't want to talk about it."

    elif player_identity == "m":

        f "He just said he doesn't want to talk about it."

    else:

        f "They just said they don’t want to talk about it."

    show ge post with Dissolve(0.1)

    g "Oh duh, sorry dude."

    mc "It’s alright, we can talk all you like, I just need something to eat."

    if earrings == 1:

        mc "You think they’d take my earrings as payment for some food?"

        show be confpost with Dissolve(0.1)

        b "Yeah that's not how things work here."

        mc "Oh, damn."

        mc "Would anyone be willing to share?"

    else:

        mc "Would you guys be willing to share some food?"

        mc "I’d buy my own, but anything I had of value got stolen."

    show ast happypost with Dissolve(0.1)

    a "Of course [player_name]. Anything for a fellow pirate."

    a "You can have my fries if you don’t mind that I ordered them spicy."

    show be post with Dissolve(0.1)

    b "My sandwich comes with soup, you can have that too."

    mc "That sounds great, I can’t thank you girls enough."

if may_v == 2:

    mc "Alright, off topic for a second."

    show ast confpost

    mc "Has anyone seen an older woman with a lot of money in the past hour walking around?"

    show fi sadpost with Dissolve(0.1)

    f "What are you talking about?"

    show be confpost with Dissolve(0.1)

    b "Did you get robbed or are looking to rob someone?"

    mc "Yes and no."

    "Who am I kidding. I'm not a detective."

    mc "Nevermind me."

    show ast post
    show fi post
    show be post
    with Dissolve(0.1)

mc "It’s good to see you all still hang out together. Do you do this often?"

show ge smugpost with Dissolve(0.1)

g "We try, if we can get Astrid out of her room."

show fi madpost with Dissolve(0.1)
show be suppost at wiggle

f "G! Come on!"

show ge madpost

g "What, stop snapping at me? It’s true."

g "How many of these has Behati tried setting up and we barely are all together once every other month?"

f "Don’t know if you remembered but there’s been a stupid pandemic prancing around."

g "Yeah, but Corner has been back open for months."

show be suppost at bounce

b "Can we not argue while we’re all here please?"

b "There’s a one hundred percent chance it will upset someone beyond what apologizing will fix."

pause 1.5
show ge post with Dissolve(0.1)

g "You’re right Be. Sorry Astrid."

show ast sadpost at wiggle

a "It’s okay G. Sorry [player_name], things have been hard on all of us these past few months."

show fi sadpost
show be confpost
with Dissolve(0.1)

f "Astrid, this has been going on for over a year now."

f "I wish it was still March as much as the next person, but there's still no sign of this blowing over."

show ge madpost

g "Two weeks my ass."

if may_talk == 1:

    mc "Hann, did you know this was going on for so long?"

    m "Like I said, it’s been rough around here."

    show may smile with Dissolve(0.1)

    m "Oh, here’s our coffee."

    w "Here’s your muffin and coffees, will there be anything else?"

    mc "No, thank you."

    "Finally I can defeat the monster in my stomach."

    "The first bite was like nothing had ever graced my mouth in years."

    "Hann’s muffin already disappeared, she’s started on her coffee now. I’m still feeling hungry though."

    "Maybe one of the girls will share some of their sandwiches with me later."

mc "So, everything hasn’t been great?"
if badwords == True:

    f "Not like all our lives were on track for success after high school, but the pandemic really messed our {b}plans{/b} up."

else:
    f "Not like all our lives were on track for success after high school, but the pandemic really messed our shit up."

show ge madpost at wiggle

g "I almost had that consulting job and you know it Fiona!"

show fi madpost with Dissolve(0.1)

f "Why are you yelling at me?"

show fi post
show be post

f "But yeah G, you did almost have it. Then the company went under so drop it and move on."

show ge suppost with Dissolve(0.1)

g "[player_name] so get this. I was doing some odd jobs here and there after high school."

g "Delivering food, running some wafer cookie companies’ Twitter, when I get this call from a friend of a friend’s coworker about coming onto their studio as a consultant."

show be quizpost with Dissolve(0.1)

b "A video game studio opening in Florida felt like a bad idea from the start."

show ge smilepost with Dissolve(0.1)

g "Well we were almost done with my contract when-"

show ge madpost at wiggle

play effect "audio/crash.mp3"

g "BAM!"

g "The rona ruined everything."

show be post

g "Now I’ve been stuck working for slave wages at my parent’s resturant to keep it open."

if may_talk == 1:

    mc "That’s awful G. You were so close too."

    show may sad with Dissolve(0.1)

    m "You almost had it kid."

    g "I know right! It blows."

    show may

else:

    mc "That’s terrible G, I’m sorry it wound up like that."

    if badwords == True:
        g "I know right! It’s {b}cruddy{/b}!"
    else:
        g "I know right! It’s bullcrap!"

show ge post

g "Could’ve been worse, Fiona had to drop out of college."

show fi sadpost with Dissolve(0.1)

f "It’s not my fault I can’t learn calculus from sloppily written notes sent to us every week if the professor remembered they had a job."

show ast post with Dissolve(0.1)

a "Fiona relax, you’ll try again when this is over with."

f "I was doing great until this country decided to get even grosser than usual."

f "Couldn’t even take the simple steps to make things go back to the way they liked it."

show fi madpost with Dissolve(0.1)

f "It had to be a grand conspiracy and not getting a shot ruined young people’s lives specifically. Like we weren’t being shafted enough."

show be happypost with Dissolve(0.1)

b "Vaccination rates are up you know. It could get better."

show fi sadpost with Dissolve(0.1)

f "Anything’s better than zero I suppose."

show fi madpost
show ge post

f "No wait, it isn’t because that’s not how vaccines work! Half our state alone doesn’t seem to get that!"

show ast confpost with Dissolve(0.1)

if badwords == True:

    a "It’s {b}icky{/b}, we know, but calm down girl."

else:
    a "It’s bullshit, we know, but calm down girl."

show fi sadpost with Dissolve(0.1)

f "Sorry, jeez, you’re right I don’t need to get riled up before eating."

show ast post
show be post

mc "You made it to college Fiona?"

mc "How was it, was it everything you thought it was?"

show fi happypost with Dissolve(0.1)

f "Oh, sweet sweet [player_name]. It was nice while it lasted."

show fi smilepost

f "I was learning actually cool stuff, there was a super large queer association on campus, living in the dorms was hard but fulfilling."

f "It was all just so..."

show ge smugpost with Dissolve(0.1)

g "Epic?"

show be happypost with Dissolve(0.1)

b "Satisfactory?"

if may_talk == 1:

    show may smile with Dissolve(0.1)

    m "Sooooo much drinking."

show fi happypost with Dissolve(0.1)

f "It was perfect."

show fi sadpost with Dissolve(0.1)

f "Which makes what happened suck even more."

show ge post
show be post
with Dissolve(0.1)

f "I’m lucky Behati knew what I was going through and I wasn’t just making it up."

show be confpost with Dissolve(0.1)

b "It’s great and all, but I agree with Astrid."

show be post

b "Once this is over I’m sure some school will let you and me in so we can study together now."

mc "You got into college too Behati?"

show be happypost with Dissolve(0.1)

b "Yes I did! I got a full ride to Florida State."

b "I was still undeclared, but was having a great time. Living in a co-ed dorm and everyone was so pretty it was nuts."

if may_talk == 1:

    show may fl

    m "So you went for the whole platter huh?"

    m "Go gettem girl."

    b "Oh, it was so overwhelming."

    show may smile

g "It was annoying at first when she texted us pictures of every hot person she saw."

show ge smugpost with Dissolve(0.1)

g "But you’d send me the pictures of the cute girls so it was cool with me."

show ast happypost with Dissolve(0.1)

a "And you sent me the guys so it was fair and balanced."

show fi madpost with Dissolve(0.1)

f "All I got were rocks."

f "Fair and balanced my perfect ass."

show be happypost at wiggle

b "The geological history by the school was so fascinating only you’d appreciate the layers Fiona."

show ge smilepost
show fi post
show ast post
with Dissolve(0.1)

mc "So if it was so great what happened?"

show be confpost with Dissolve(0.1)

b "I can’t remember if we talked about it, but I was interested in old guns and ended up getting a bunch."

show be confpost at wiggle

b "Then one went off in my dorm room on accident."

b "It went through every wall on my side of the floor."

b "Which was completely unpredictable because I was just starting to take it apart and the guy who sold it to me said it was decommissioned and hadn't been fired in years."

f "We looked him up after Be was expelled and he had been selling stolen goods he knew nothing about for years."

show fi sadpost with Dissolve(0.1)

f "The state still can’t find him."

mc "Maybe he escaped out to sea."

show be suppost at bounce with Dissolve(0.1)

b "The jerk ruined my future just when I decided my major would be history."

show be confpost

b "Or was it anthropology?"

show ast confpost with Dissolve(0.1)

a "You told me you were going to choose computer science?"

show ge suppost with Dissolve(0.1)

g "I thought it was linguistics?"

show fi happypost with Dissolve(0.1)

f "That's the same thing you told me."

if may_talk == 1:

    show may with Dissolve(0.1)

    m "All sounds like a waste of time to me. College is a scam."

    mc "I wouldn't know."

show be post with Dissolve(0.1)

b "Well either way the school system shut down due to rona at the same time I was allowed to reapply."

show ast post
show fi post
show ge smilepost
with Dissolve(0.1)

b "Georgia schools are opening soon, Fiona, we could both try to get in up north?"

show fi sadpost with Dissolve(0.1)

f "Just for them to be shut down again for the third or fourth time?"

f "No thank you, I’ll just suffer in silence until it’s done for good."

show ge suppost with Dissolve(0.1)

g "Silence?"

show fi madpost with Dissolve(0.1)

f "Oh quit it G! I don’t need your-"

show ge post with Dissolve(0.1)

g "Okay, okay, remember to relax dude."

show ast happypost with Dissolve(0.1)

a "[player_name] tell us what you’ve been up to please."

a "You can skip the bad parts right? You said being a pirate was very freeing back then."

show ast happypost at wiggle

a "You were still living free, right?"

mc "..."

if may_talk == 0:

    "I guess I can't escape Hann knowing I'm a pirate now."

    "Maybe she won't ask for context. Or I could convince her later I lied to the girls and not her."

mc "Yeah, I was doing great for a while."

mc "I got promoted to first mate for real this time and was taking on more responsibility on the ship and people were starting to respect me for it."

mc "There was even this one time where both the Captain and Flavio, our Quartermaster, both fell ill and I took charge for three whole days."

show ast confpost with Dissolve(0.1)

a "Wait, you weren’t the first mate when we met?"

mc "No, I wanted to sound important. At the time I was either assistant to the Captain's assistant or head deck hand."

show ast happypost with Dissolve(0.1)

a "Well that’s fine, not like you were a dockboy or anything."

show ge smilepost with Dissolve(0.1)

g "So you got a real taste at being in charge, that’s awesome."

show be quizpost with Dissolve(0.1)

b "Does that mean you can give me the ship's stats now?"

mc "I didn’t do too much while in charge though."

mc "We took them to this island off of the Bahamas to get treated. So the Plague was in port for most of the duration."

if may_talk == 0:

    $ m = Character("[may_name]", color="#ffc77f", callback=may_voice, who_outlines=[ (1, "#000000")])

    show may at center behind fi with dissolve

    m "Excuse me, sorry to interrupt. But did you say \"The Plague\"?"

    m "As in the Red Plague?"

    if may_v == 2:

        mc "Wait your voice..."

        mc "It was you in the abandoned bookstore just now!"

        show may smile with Dissolve(0.1)
        $ may_name = "Woman"
        $ m = Character("[may_name]", color="#ffc77f", callback=may_voice, who_outlines=[ (1, "#000000")])

        m "I got no idea what you're talking about."

        show may

        m "But I heard you very clearly. You're a pirate on that famous ship."

    elif may_v == 1:

        mc "Wait, I know you."

        mc "You took my earrings!"

        show may smile with Dissolve(0.1)
        $ may_name = "Theif"
        $ m = Character("[may_name]", color="#ffc77f", callback=may_voice, who_outlines=[ (1, "#000000")])

        m "I got no idea what you're talking about, I've never seen you before."

        mc "You have to be kidding me? You can't be playing that card."

        m "Do I look like I have any earrings? Maybe someone else took them."

        mc "But you jumped on me, it was very clearly you."

        show may

        m "That's not important right now."

        m "What is important is that you said you are from that famous pirate ship."

    mc "{cps=70}Ummm, no I meant the black plague.{/cps}"

    mc "In Europe."

    mc "We’re doing a history. School. Thing. About Europe."

    show may smile with Dissolve(0.1)
    show ast post

    m "No, I’ve been listening."

    m "You all aren’t in school anymore, your lives suck, and you were talking about being a pirate."

    show ge madpost
    show fi madpost
    with Dissolve(0.1)

    g "Yeah, they’re a pirate!"

    g "So don’t mess with us lady, mind your own business!"

    if may_v != 2 or may_v != 1:

        mc "Wait, I recognize you."

        mc "You’re that [may_position] from the [activity_choice]."

        if activity_choice == "market":# this does not appear

            mc "Or what was left of it."

        elif earrings != 1:

            mc "And you stole my earrings!"

    m "That's right first mate. I couldn’t help but overhear your entire, loud, conversation."

    show ast sadpost
    show be confpost at wiggle
    with Dissolve(0.1)

    m "Sorry about your sob stories girls."

    m "It’s pretty ballsy for a pirate of a feared pirate ship to be waiting for coffee in some rundown town."

    mc "Not really any of your concern though, is it?"

    "This would be an ample moment where I’d flash my weapon. If I still had one."

    show may with Dissolve(0.1)

    m "I won’t cause a scene involving any feds under one condition."

    mc "And you’re calling me ballsy?"

    mc "You think your government will swarm my exact location off of some phone call?"

    f "Yeah, we don’t even know you and you’re just blackmailing the people at the table next to you?"

    f "Are you really that desperate or stupid?"

    m "I just don’t want to drag this out sweethearts."

    m "There are reasons for what I do and I won’t blab if you give me one thing."

    mc "What? What else could you possibly take from me?"

    show may smile with Dissolve(0.1)

    m "Give me a job on your ship. Simple as that."

    mc "You’re joking with me aren’t you?"

    show ge madpost at bounce

    g "Hey that’s not fair! [player_name] wouldn’t let us come with them."

    g "Who do you think you are?"

    b "This is so weird and barely qualifies as a hostage situation."

    mc "My thoughts exactly, why would you want to join a pirate crew anyway?"

    mc "Are you also a wayward soul?"

    show may with Dissolve(0.1)

    m "Let’s just say I have my reasons."

    show may smug

    m "Not like I’m completely worthless, I’m an experienced doctor. Any ship could use another one of those."

    mc "Oh I’m sure you are."

    mc "An experienced doctor is roaming the streets running cons on random people."

    show may with Dissolve(0.1)

    m "I’ll have you know I went to the Herbert Wertheim College of Medicine in this, the great state of Florida."

    m "And I've been a practicing sea vessel doctor for years now. I know my way around a ship and a scalpel."

    mc "Behati, is that a real place?"

    show ge suppost with Dissolve(0.1)

    g "Dude, how do you not know you’re in Florida at this point?"

    mc "No G, the school-"

    show be quizpost
    show ge post
    with Dissolve(0.1)

    b "\"Medical school is a transformative experience. It is an exciting and challenging journey.\""

    b "\"At HWCOM, your journey is enhanced by diversity, research and innovation, and community outreach.\""

    b "So it’s a big school that produces a lot of doctors."

    show be confpost

    b "Or at least that’s what it says on their website."

    show be post
    show fi madpost at wiggle

    f "Well that may be lady, but how is [player_name] supposed to trust you?"

    if player_identity == "m":

        f "You haven’t even told him your real name?"

    elif player_identity == "f":

        f "You haven’t even told her your real name?"

    else:

        f "You haven’t even told them your real name?"

    show may smug with Dissolve(0.1)

    m "It isn’t a matter of trust, it’s easy peasy, always in style, blackmail."

    show may

    m "At the very least get you kicked out of one of the few remaining coffee shops left in town. Put you on the lam."

    show may fl with Dissolve(0.1)

    if player_identity == "m":

        m "So, do we have a deal handsome?"

    else:

        m "So, do we have a deal gorgeous?"

    show ast suppost with Dissolve(0.1)

    a "That’s outrageous!"

    a "We could just leave you know."

    f "Who do you think you are making these demands?"

    show ge madpost with Dissolve(0.1)

    g "If anyone gets to be on the ship it’s me!"

    show fi behind may
    show be post behind may
    show ast embpost
    show may fl at zoom_may

    if player_identity == "m":

        m "Oh come on sugar. I’m asking very nicely."

        m "Could you really turn down a woman who’s offering her services to you?"

    elif player_identity == "f":

        m "Let me on girlfriend. Give me a chance."

        m "I promise you won't regret it."

    else:

        m "Come on. Two beautiful people walking aboard?"

        m "Nobody will notice me until it's too late."

    mc "I can’t let you on the ship lady."

    m "Oh please [player_name]. Don’t make me ask twice darling."

    mc "Because there isn’t a ship to go back to."

    show ast suppost
    show be quizpost
    show ge suppost
    show fi sadpost
    with Dissolve(0.1)
    show may behind fi at redochar

else:

    show fi madpost behind may
    show be quizpost behind may
    show may at zoom_may

    m "Wait, I’m sorry. You’re a pirate?"

    m "I thought they were just kidding? Seriously?"

    m "What happened to the rich brat story?"

    if badwords == True:
        "{b}Oh nuts{/b}. I was hoping she'd call me out later so i wouldn't have to explain in front of the girls."

    else:
        "Shite. I was hoping she'd call me out later so i wouldn't have to explain in front of the girls."

    show ge suppost

    g "You didn't tell her?"

    show ast sadpost

    a "Well they might not want everyone to know G. So really we blew it."

    mc "Girls it's alright. Sorry for lying Hann, I didn’t know if I could trust you."

    mc "The Red Plague is a notorious ship, I didn't know if you would change your opinion about me if you had known."

    show may fl with Dissolve(0.1)

    m "So you’re a wanted pirate?"

    mc "Like I said, I didn’t know if I could trust you."

    mc "What if you’d turn me into the state?"

    mc "..."

    mc "You aren’t going to do that, are you?"

    show may fl behind fi
    show ast post
    show may fl at redochar

    if badwords == True:
        m "No, of course not. I’m not going to go crawl to the cops or some dumb {b}meme{/b} like that."
    else:
        m "No, of course not. I’m not going to go crawl to the cops or some dumb shit like that."

    m "I lied to you too, by the way."

    mc "Really?"

    m "Yup, Hanna’s not my name and my kid is a dog I met a couple of days ago."

    mc "Playing the sympathy card, not a bad trick."

    show may smug with Dissolve(0.1)

    m "You weren't too bad yourself."

    m "Between the deceit and the muffin we’re almost even."

    mc "Oh, is that right?"

    m "You could make us square if you let me on your ship after this."

    show ast suppost
    show be suppost
    show fi madpost at bounce
    show ge suppost
    with Dissolve(0.1)

    mc "That’s not funny, not Hanna."

    show may with Dissolve(0.1)

    m "No seriously, let me work on your ship."

    show ge madpost with Dissolve(0.1)

    g "Hey that’s not fair! [player_name] wouldn’t let us come with them."

    g "Why would a muffin change that?"

    show ge smugpost with Dissolve(0.1)

    g "Dude let me get you a whole ass sandwich and make me the pirate queen."

    show be confpost with Dissolve(0.1)

    b "Yeah and I can't get you, uh, porkchop...If you want."

    mc "Stop, no bribes. But I'm confused though."

    mc "Why do you want to join a pirate crew anyway?"

    show may sad with Dissolve(0.1)

    m "Let’s just say I have my reasons."

    show may fl with Dissolve(0.1)

    m "I can make it worth your while, I’m an excellent doctor."

    show ast confpost
    show ge post
    with Dissolve(0.1)

    mc "I'm confident, an excellent doctor is roaming the streets earning sympathy points from random pirates."

    show may smug with Dissolve(0.1)

    m "I’ll have you know I went to the Herbert Wertheim College of Medicine and have been a practicing sea vessel doctor for years now."

    m "I’m not just some hobo, I know my way around a ship and a scalpel."

    mc "Behati, is that a real place?"

    show be quizpost with Dissolve(0.1)

    b "It’s a top school that produces the best doctors in the state."

    b "Or that’s what the recruiter is implying in forum posts about it."

    f "That may be lady, but how is [player_name] supposed to trust you?"

    f "You admitted to using a fake name and won’t even tell us your real name?"

    show may with Dissolve(0.1)

    m "It isn’t a matter of trust, it’s simply tit for tat."

    if player_identity == "m":

        m "That’s the way pirates operate, I’m sure he knows nothing comes for free in this world better then all of us."

    elif player_identity == "f":

        m "That’s the way pirates operate, I’m sure she knows nothing comes for free in this world better then all of us."

    else:

        m "That’s the way pirates operate, I’m sure they know nothing comes for free in this world better then all of us."

    show be confpost with Dissolve(0.1)

    b "That may be, but the odds of that working on [player_name] I put at about ten percent. It’s a tall order."

    show fi madpost at bounce

    f "It’s stupid of you to even try making this work. You don’t scream \"pirate material\" to me."

    show ge madpost with Dissolve(0.1)

    g "Yeah, that’s what we scream!"

    mc "I can’t let you on the ship."

    show ast sadpost
    show fi sadpost
    show ge suppost
    with Dissolve(0.1)

    m "Oh please [player_name]. Don’t make me ask twice darling."

    mc "Because there isn’t a ship to go back to."

    show ast suppost
    show be suppost
    show ge suppost
    with Dissolve(0.1)

a "What do you mean by that [player_name]?"

mc "I mean that The Red Plague burned a hole through the ocean last night. There were no survivors, other than me."

m "How’d something like that happen to the feared ship of the Demonic Pirate Ricardo?"

mc "Not sure yet. We were boarded during a storm."

mc "There was no telling by how many pirates, but it was enough to disarm and destroy the majority of our crew in a matter of minutes."

b "How’d you escape?"

mc "The Captain helped me. He begged me to leave and let him go down with the ship."

mc "I almost didn’t let him. But he was very persuasive."

show ast sadpost with Dissolve(0.1)

a "[player_name], I’m so sorry. That all sounds so terrible."

mc "It wasn’t fun for sure, I washed up on shore this morning, not really knowing what to do with myself."

mc "I thought leaving it up to the Gods would be a good idea, but that might have been wishful thinking."

mc "Seeing you in the window just now made me think I was right to think that way, but to learn that all your lives got as crippled as mine, makes me feel like there isn’t much hope."

a "You know, rock bottom isn’t always bad."

show ast embpost with Dissolve(0.1)

mc "How’s that so Astrid?"

show ast post with Dissolve(0.1)

a "There’s comradery to be found in misery. If everyone around you is doing bad, then it takes the edge off of yourself."

show ast sadpost with Dissolve(0.1)

a "It isn’t a personal failing when everything is down, and it’s easier to pull yourself back up with friends. That’s what you guys have been doing for me."

show ge smilepost with Dissolve(0.1)

g "You mean us?"

show ast happypost with Dissolve(0.1)

a "Yes, you idiots. Always trying to get me out of my house when I doomer post online."

a "Coming over with movies to watch, because even though the theater couldn’t stay open, you all know movies make me happy."

show fi happypost with Dissolve(0.1)

f "Well of course we did those things, you’re our friend."

show be happypost with Dissolve(0.1)

b "It’s like you just said, feeling down isn’t as bad when you’re with others. We wouldn’t let you feel down without us."

g "Celebrate the victories and the losses together I guess."

mc "That’s helpful to think about Astrid, thank you for the extra perspective."

w "Here’s your food, will there be anything else?"

show ast post
show ge post
show fi post
show be post
with Dissolve(0.1)

if may_talk == 0:

    show ast post at bounce

    a "Could we get another plate of fries please?"

    w "Absolutely. I’ll put them in now."

"The food came out looking so hot and delicious. I remember the first time I got to enjoy hot food."

"It was once I contributed to my first ship raid that I was allowed to eat before the ship hands and get the food before it cooled off."

"It was inconceivable to me that chef Geraldine’s porridge was better warm."

if may_talk == 0:

    show fi smilepost with Dissolve(0.1)

    f "Here’s my soup matey. It's all yours."

    mc "Thank you Fiona. What kind is it?"

    f "Tomato, you can have the crackers too."

    show ast happypost with Dissolve(0.1)

    a "Take these fries now, I’ll eat the next order."

    mc "You’re all great, this should do me some good."

    "Astrid slides the plate of food in front of me. Fiona also hands me her bowl, but the warm salty goodness envelops my senses."

    "The plate of crispy fries are ten folds better than anything I’ve ever had. Who knew potatoes could be prepared in such an immaculate fashion?"

    show fi sadpost with Dissolve(0.1)

    f "You doin' good?"

    mc "These are amazing, are they like, the greatest in the world here?"

    f "No, that’s just how they’re made everywhere here."

    show be happypost with Dissolve(0.1)

    b "Air fryers have come a long way. Much better than deep fryers, wouldn’t you agree?"

    mc "Whatever fried these fries are a gift from Ambrosia in my book."

    show ge smugpost with Dissolve(0.1)

    g "I don’t know Be, deep fryers still have their uses."

    show be confpost with Dissolve(0.1)

    b "I guess the whole hoagie won’t fit in the air fryer."

    g "Sometimes I need them crispier. You should try it."

    show be post
    show fi post

else:

    mc "Could I have some of those fries Astrid?"

    show ast happypost with Dissolve(0.1)

    a "Yeah, sure [player_name]. Have you ever had them before?"

    mc "Cooked potato strips, I’ve had before."

    mc "I didn’t know that’s what mainlanders called them until recently though."

    show ast confpost with Dissolve(0.1)

    a "Oh yeah? How’d you learn that?"

    mc "From some pirate friends with more experience with land folks than I."

    mc "I just heard it off hand from them."

    show ge smugpost with Dissolve(0.1)

    g "More experience than you? That’s impossible, you went to high school for a day."

    show ast happypost

    mc "Huh huh ha, yeah."

    mc "I’m very cultured as you all know."

    show be quizpost with Dissolve(0.1)

    b "You’ve seen more of the world than us."

    show fi happypost with Dissolve(0.1)

    f "Lots of culture to be found in the sea water."

    mc "Oh plenty of it and even more to find."

    mc "I bet \"Hanna\" over here knows what I mean by that."

show may smile with Dissolve(0.1)

m "Heh heh."

m "You all seem like real good friends."

show ast sadpost
show ge post
show fi madpost
show be post
with Dissolve(0.1)

f "Um, yeah, sure."

g "Are you still here?"

g "Why don’t you go find some happy people whose lives you can make worse?"

show may with Dissolve(0.1)

m "You all are really cramping the good mood you just fixed. You’ll get wrinkles before you’re twenty five that way."

if may_name != "Woman":

    f "You mean the mood you were trying to take advantage of [may_name]?"

    show may at bounce

    m "Okay I’m sick of being called that already, it’s May."

else:

    f "You mean the mood you were trying to take advantage of creep?"

    show may at bounce

    m "Okay that's uncalled for."

    m "I have a name you can use if you'll be kind enough. It's May."

show be confpost

b "No it’s not, it’s November."

$ m = Character('May', color="#ffc77f", callback=may_voice, who_outlines=[ (1, "#000000")])

if persistent.name5 == 0:

    $ persistent.name5 = 1
    $ persistent.may_name_count += 1
    #$ achievement.progress("Jane Doe", persistent.may_name_count)

if persistent.may_name_count == 5:

    $ achievement.grant("Jane Doe")
    $ achievement.sync()


m "No little Miss Sarcasm, that’s my name."

m "My real name is May Palmer, I’m a real ship doctor, I have been for a while."

show may sad with Dissolve(0.1)

m "But due to the pandemic I’ve been unable to work. Running around this port town for almost three days now trying to figure something out."

m "Felt as if there was no more time left to do anything rational. So that’s why I took my shot with [player_name]."

show ge madpost with Dissolve(0.1)

g "Yeah right, like we’d believe you now."

show be suppost with Dissolve(0.1)

b "[player_name] surely you aren’t taking her seriously at this point?"

b "You met her today and she admitted to her lies."

if earrings == 0:

    g "And she took your earrings!"

    a "Not cool."

define may_trust1 = 0
$ renpy.block_rollback()
$ quick_menu = False

menu:

    "Believe her":

        $ may_trust1 = 1

        jump mAYbe

    "Doubt her":

        $ may_trust1 = 2

        jump mAYbe

label mAYbe:

    $ quick_menu = False
    $ renpy.block_rollback()

    if may_trust1 == 1:

        show ge suppost
        show ast sadpost
        show be suppost at bounce
        with Dissolve(0.1)

        mc "I believe you May. You’ve lied to me before, but I see it in your eyes now."

        $ quick_menu = True

        mc "You aren’t out here lying for some temporary gain, you don’t know what you’re doing anymore either."

        if earrings == 0:

            mc "How desperate do you have to be to steal someone’s studs?"

            mc "Those aren’t the actions of someone who has a lot of options."

            show may sad with Dissolve(0.1)

            m "Yeah, sorry about that, I couldn’t get much for them anyway so I feel worse about it now."

        mc "I think we’re all feeling a little lost, let’s ease off her."

        mc "Astrid’s whole comrade speech can extend to someone else who needs it for just a little bit, right?"

        show fi sadpost with Dissolve(0.1)

        f "Sure, whatever."

        show be post with Dissolve(0.1)

        b "I’m sorry May, I was just trying to be protective."

        show ge post with Dissolve(0.1)

        g "We still got our eyes on you, but you’re cool. I like your hair."

        $ May_affinity += 3
        play effect "audio/good.mp3"
        show may smile with Dissolve(0.1)

        m "{color=#50A23B}Thank you girls. And [player_name], that means a lot.{/color}"

    else:

        mc "I don’t trust you as far as I’m concerned. Your story has some holes that can’t be overlooked."

        $ quick_menu = True

        mc "But you do seem to have it as rough as we do right now. Why else would you resort to blackmailing someone you just met?"

        if earrings == 0:

            mc "I would like my earrings back too."

            show may sad with Dissolve(0.1)

            m "Sorry, I sold them."

            mc "Really? Come on May."

            mc "They were all I had left except the shirt on my back."

            show may with Dissolve(0.1)

            m "I’m sorry, I didn't get that much anyway. I feel bad about it now I guess."

            mc "Disregarding that slight."

        mc "Whatever your real deal is, let’s ease off her."

        mc "Astrid’s whole comrade speech can extend to someone else who needs it for just a little bit, right?"

        show fi sadpost with Dissolve(0.1)

        f "Even if you don’t fully trust her?"

        mc "I’m not feeling particularly hostile today, if you could believe it."

        mc "So yes, even if you don't trust her. I have nothing to offer so she shouldn't be a problem now."

        show be post with Dissolve(0.1)

        b "I’m sorry May, I was just being protective."

        b "You have really pretty eyes."

        show ge post with Dissolve(0.1)

        g "I suppose your hair is cool too."

        g "But we got our sensors pointed at you."

        show be confpost with Dissolve(0.1)

        b "Did you mean radar?"

        show ge suppost with Dissolve(0.1)

        g "{cps=100}Maybe{/cps}"

        show may smile with Dissolve(0.1)

        m "That’s very nice of you girls."

        $ May_affinity = 0
        play effect "audio/bad.mp3"
        show may with Dissolve(0.1)

        m "{color=#f00}Well, I can’t say I trust you all either, I’d get nothing out of being crude to you now.{/color}"

    show fi sadpost
    show be post
    with Dissolve(0.1)

    f "So congratulations, we’re all sad girls now, but we’re together. What do we do about it Astrid?"

    show ast embpost with Dissolve(0.1)

    a "I don’t know, what do you think I would do right now?"

    f "Well, you already did your speech, so now you’d come up with some plan involving all of us that is risky and could get us in trouble if done poorly."

    a "Is that what I do?"

    show ge smugpost with Dissolve(0.1)

    g "Yes, without a doubt."

    show be happypost with Dissolve(0.1)

    b "Most of your plans involve precise movements and timing."

    show fi smilepost with Dissolve(0.1)

    f "Remember when you wanted to play the Pirates of Honduras theme song during graduation and somehow involved all of us?"

    show ast happypost with Dissolve(0.1)

    a "Oh yeah, I remember that."

    mc "What happened?"

    show be happypost at wiggle

    b "You had G distract Mike in the sound booth so I could get in and play the song when you walked on stage."

    f "The confusion on Vice Principal Rowan’s face was worth it to me."

    show ge smugpost at bounce

    g "That little creep thought I was making a move on him."

    g "Yeah, he was kinda fem and all but not on your life Mike."

    f "But you planned the entire scheme in like a day."

    mc "That sounds hilarious."

    show may fl
    show ast post
    with Dissolve(0.1)

    m "Sounds to me that went all according to plan."

    show may smile

    m "And she does that often?"

    show fi sadpost with Dissolve(0.1)

    f "Well, she used to a lot before covid."

    show ge smilepost with Dissolve(0.1)

    g "Like that time at the deli."

    "I wonder which pirates in Honduras have their own theme song? I had no idea they were so coordinated."

    "While the girls are reminiscing, Astrid’s eyes are focused thinking about something else."

    show ast happypost at bounce with Dissolve(0.1)

    a "[player_name]!"

    a "So you said you’re the only survivor of The Red Plague?"

    show fi madpost with Dissolve(0.1)

    f "Astrid! Too soon."

    mc "Not that I want to go into details, but everyone else was either slain or went down with the ship."

    show ge post
    show be post
    show fi post

    a "If your Captain told you to escape, why do you think that is?"

    mc "I’m still trying to figure out why he did. Where are you going with this?"

    a "[player_name], he wants you to continue the legacy!"

    mc "Excuse me?"

    show ast happypost at wiggle

    a "You were solely trusted to keep the dream alive, that must be it. You like being a pirate don’t you?"

    mc "I do, but why wouldn’t he have just said that?"

    show ast confpost with Dissolve(0.1)

    a "You tell me, I have a feeling it’s supposed to act like a cryptic way for you to come to that conclusion yourself."

    show ast happypost at wiggle with Dissolve(0.1)

    a "Pirates are always leaving clues to their treasure. But their legacy must be more important than that."

    show fi sadpost with Dissolve(0.1)

    f "Astrid, don’t you think that's all a little much for someone that close to death?"

    f "[player_name] just lost everyone they knew to the pirate equivalent of a sucker punch."

    a "Not everyone, that’s where we come in."

    show fi madpost with Dissolve(0.1)

    f "Oh no."

    show be confpost
    show ge suppost
    with Dissolve(0.1)

    b "You aren’t going where I think you’re going?"

    if player_identity == "m":

        a "He was lucky to find us, wasn’t he?"

        show ast happypost at wiggle

        a "We can become his new crew!"

    elif player_identity == "f":

        a "She was lucky to find us, wasn’t she?"

        show ast happypost at wiggle

        a "We can become her new crew!"

    else:

        a "They were lucky to find us, weren't they?"

        show ast happypost at wiggle

        a "We can become their new crew!"

    show ge smugpost with Dissolve(0.1)

    g "Now that’s the Astrid I remember!"

    g "Just like {i}The Great Budget Meeting of ‘16{/i}, we’re taking control of our own destiny!"

    show fi madpost at wiggle

    f "We can’t just drop everything and become pirates Astrid."

    a "Why not Fiona? What’s there left for us here?"

    f "You’re just using this as an opportunity to escape your own problems."

    a "Exactly! Were you not a member of the Pirate Culture Club?"

    m "Did y'all really have a \"Pirate Culture Club\"?"

    a "Yes we did, and it was the best thing ever."

    a "This is why people become pirates in the first place. For economic liberty, where stealing is their only option left."

    f "Yeah, during the start to the Golden Age of Piracy maybe when it was lucrative."

    f "Nowadays people only do it to roleplay or if they’re born into it."

    show be quizpost with Dissolve(0.1)

    b "Actually, recent surveys show more and more people are rejecting modernity and returning to a simpler time of sailing the high seas."

    show be confpost

    b "It’s almost a direct correlation to the growth in the gap in income inequality in America and other countries."

    show ge smugpost at bounce
    show be post
    with Dissolve(0.1)

    g "Yeah! What Behati said, this is a great idea."

    show be confpost with Dissolve(0.1)

    b "I didn’t say that. I’m not even on board, pun not intended."

    show be post with Dissolve(0.1)

    b "Even if I really want to, what can we do? We’ve never been to sea and have zero privateering experience."

    show ast happypost at bounce

    a "What are you talking about no experience?"

    a "Besides the fact we studied this stuff all the time in high school, we each have something valuable we can use. I bet [player_name] sees it too."

    m "And I've been on a ship for the past few years as well."

    a "Exactly!"

    show fi sadpost with Dissolve(0.1)

    f "[player_name], you can’t be on the same page Astrid is on?"

    mc "Well, considering what I know about you all."

    # to determine if their job was purposed by Astrid and Reed
    define f_job = 0
    define b_job = 0
    define g_job = 0
    define m_job = 0

    # to know when to stop looping back to label pirate_position
    define job_counter = 0

    jump pirate_position

label pirate_position:

    if job_counter < 4:

        $ renpy.block_rollback()

        menu:

            "Fiona" if f_job == 0:

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "Fiona, you said you were doing math in college?"

                $ quick_menu = True

                f "Yeah? What’s your point?"

                mc "An important role on a ship is the navigator. Most of which entails good maths and direction."

                f "You have to be kidding me, I have a terrible sense of direction anyway."

                show ge smilepost with Dissolve(0.1)

                g "That isn’t even kinda true."

                g "We all got lost in the city during the prom after party and Fiona, having never been to the city, not only got us to the party on time."

                g "But afterwards, found this amazing burger place and found the bus station from there."

                show fi sadpost

                f "But I was just reading signs, that isn’t proof-"

                show ast happypost with Dissolve(0.1)

                a "You also memorized the layout of high school in one day. You had to spin me around multiple times that first week."

                show fi sadpost at bounce

                f "But-"

                show be happypost with Dissolve(0.1)

                b "And you’re the only person better at remembering street names than I am."

                show fi madpost with Dissolve(0.1)

                f "That’s because I got my license before you."

                show fi sadpost

                f "You’re all just being nice, I couldn’t navigate a pirate ship!"

                a "Looks like you’re the minority here Fiona. Sounds to me like you're a navigator."

                show fi madpost with Dissolve(0.1)

                f "Don’t go there Astrid, this is supposed to be my choice."

                show ast post with Dissolve(0.1)

                a "You look me in the eyes and tell me you couldn’t do it."

                pause 1.5

                show fi sadpost with Dissolve(0.1)

                f "... ... ..."

                show fi madpost

                f "That’s not fair, you know that gets me to do whatever you want."

                show ast happypost with Dissolve(0.1)

                a "And?"

                show fi madpost with Dissolve(0.1)

                f "Fine, whatever. Maybe I could be a navigator. Hypothetically, in some other universe."

                a "We all know you could be."

                $ f_job += 1
                $ job_counter += 1
                jump pirate_position

            "Behati" if b_job == 0:

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "Behati, you know how to use guns other than the one that you didn’t know, right?"

                $ quick_menu = True

                show be happypost at wiggle with Dissolve(0.1)

                b "Pistols were all I could afford. If it was made in the last hundred years I can fire it, with pretty good accuracy I don’t mean to brag."

                mc "Anything else?"

                show be confpost with Dissolve(0.1)

                b "Functionally I know how cannons and mounted machine guns work, I’ve just never used them."

                mc "You would make a good gunner then."

                mc "Someone in charge of the ships fire power and the best marksmen."

                b "Okay, but I’m not so sure you should trust me with all that weaponry, what if I blow it?"

                mc "I would need someone else to teach the others to use a gun. I’d guide you and you’d help me help the ship."

                show fi smilepost with Dissolve(0.1)

                f "You’re more careful than you give yourself credit for Be."

                f "You got me to hold a gun properly, even after I swore I’d never touch one of those things."

                show ge smugpost  with Dissolve(0.1)

                g "And I watched you at the range. You smoke’em so hard the gang bangers on 5th street nod when you walk by."

                show be suppost at bounce with Dissolve(0.1)

                b "That's all taken out of context."

                show ast happypost with Dissolve(0.1)

                a "Behati, it’d be a perfect job for you."

                a "You also can be learning about pirate stuff first hand like you’ve always wanted to. And I know you still want to."

                show be quizpost with Dissolve(0.1)

                b "That’s {cps=90}ummmmmmm,{/cps} not at all. But I guess. It seems like a plausible idea."

                b "I’d give it maybe a sixty percent chance of happening."

                b "Under the right circumstances, obviously."

                a "I know you’d be great at it Be."

                $ b_job += 1
                $ job_counter += 1
                jump pirate_position

            "Geraldine" if g_job == 0:

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "G, you said you've been working at your family’s restaurant this whole time?"

                $ quick_menu = True

                show ge post with Dissolve(0.1)

                g "Other than my whole life, yes, even more recently. What are you getting at?"

                mc "Every ship needs a chef."

                show ge madpost with Dissolve(0.1)

                g "Oh no! You aren’t putting me behind some big ol pot of stew while everyone takes all the action away from me!"

                show ast confpost with Dissolve(0.1)

                a "G, the chef isn’t like the school cafeteria."

                show ast happypost with Dissolve(0.1)

                a "They are an important part of the crew and they get just as much action as others because you aren’t allowed to skip battles."

                show ast happypost at bounce

                a "Right [player_name]?"

                mc "That’s right, the chefs are the most beloved part of the crew too."

                mc "They make the saltiest of pirates happy with what they make and have to keep malnutrition on the low."

                show ge suppost with Dissolve(0.1)

                g "Most beloved you say? How are they feared though?"

                mc "You control the food, if someone gets on your bad side, they can kiss their taste buds goodbye."

                if player_name == "Seymour":

                    show ge smugpost with Dissolve(0.1)

                    g "How delightfully devilish [player_name]."

                show ge smugpost with Dissolve(0.1)

                g "I’d like to have that kind of power."

                show ge smilepost with Dissolve(0.1)

                g "Okay I’m in. Call me Master Chef G. Better start working on my pot belly."

                show fi sadpost with Dissolve(0.1)

                f "G you can’t be serious?"

                g "Even though I’m skinny I think spiritually I’ve always had one, so yeah."

                show fi madpost

                f "No, I meant about becoming a pirate."

                g "If Astrid thinks it’s what we should do, I’ll follow her."

                g "She’s never led us astray before. Have a little faith you guys."

                a "Exactly, thank you G."

                $ g_job += 1
                $ job_counter += 1
                jump pirate_position

            "May" if m_job == 0:

                $ quick_menu = False
                $ renpy.block_rollback()

                mc "May, this would be the time for some confidence building for us. Are you a doctor or not?"

                $ quick_menu = True

                show may fl with Dissolve(0.1)

                m "Would you care for a live demonstration?"

                show fi madpost behind may
                show be post behind may
                show may fl at zoom_may

                m "Lift up your shirt kindly, please and thank you."

                show may fl behind fi
                show may fl at redochar

                mc "Get off me May! Alright."

                mc "I believe you, we could use a ship doctor."

                mc "I have no experience with medical stuff, so you’d be taking full reign on that operation."

                show may with Dissolve(0.1)

                m "Only if your potential crew trusts me enough to dig a bullet out of their leg."

                show fi madpost
                show ge suppost
                show be suppost
                show ast sadpost
                with Dissolve(0.1)

                f "..."

                b "..."

                g "Maybe we start with a splitter?"

                show ast sadpost at wiggle

                a "Guys come on, it’d be too big of a gamble to claim to be a doctor and not be one."

                show ast post

                a "She knows if we went out at sea and caught onto her faking it we’d maroon her. So on that count, I trust you May Palmer."

                show may smile with Dissolve(0.1)

                m "Thank you Astrid of Bellewood. I promise to show you all the level of care I’d treat my own family with."

                show may smug with Dissolve(0.1)

                if player_identity == "m":

                    m "We can all be a big crew of sisters and a cute older brother."

                else:

                    m "We can all be a big crew of sisters. Doesn’t that sound nice?"

                show be confpost with Dissolve(0.1)

                b "I don’t know if I need another older sibling."

                show fi madpost

                f "Family isn’t always reliable either."

                show may with Dissolve(0.1)

                m "Oh come on, cut me some slack like [player_name] said."

                m "If I can’t convince you, I’m sure [player_name] knows how important my role is."

                show may fl

                if player_identity == "m":

                    m "I need the help of a big strong man to get the young ones to agree with me."

                    mc "Girls, I think you should give May a fair shake if we’re going to try this."

                else:

                    m "I need your help getting the kids to agree. If you do, I promise to help you out as well in any way I can."

                    mc "Ladies I think you should give May a fair shake if we’re going to try this."

                mc "Plenty members of a crew are freelanced right off the docks. Personal trust comes afterwards."

                show ast post at wiggle

                a "Please be cool for now."

                show ge post with Dissolve(0.1)

                g "If you can convince Fiona then I’m down."

                show be confpost with Dissolve(0.1)

                b "If we don’t all vibe, what’s the point?"

                f "Astrid, I just don’t think-"

                show ast post at wiggle

                a "{cps=100}Pleeeeeease{/cps} be cool Fiona. If you want, I could patch you up instead?"

                show fi sadpost with Dissolve(0.1)

                f "Fine fine fine, no need for that."

                show fi madpost

                f "Okay May, you can be on our hypothetical pirate crew."

                show may smile with Dissolve(0.1)

                m "I’m sure we’ll get along wonderfully Fiona. Might I add you have such a beautiful complexion."

                show fi post with Dissolve(0.1)

                f "Yeah, thanks. You too."

                $ m_job += 1
                $ job_counter += 1
                jump pirate_position

    else:

        jump act1_end

label act1_end:

    $ quick_menu = False
    $ renpy.block_rollback()

    show fi post
    show ge post
    show be post
    show may
    show ast happypost
    with Dissolve(0.1)

    a "See! You’re all so qualified it’s like you’re begging to be a pirate right now."

    $ quick_menu = True

    show fi sadpost with Dissolve(0.1)

    f "But we aren’t."

    mc "There is still your job Astrid."

    show ast embpost with Dissolve(0.1)

    a "Me? Oh, um, I guess I could swab the decks or something."

    a "Don’t think watching pirate movies and being depressed all day are useful skills."

    mc "No, that doesn’t sound like anything. But your friends trust you and you’ve convinced them this might be possible."

    mc "You were also the president of the pirate club. I think you’d make a good Quartermaster."

    show ast embpost at bounce

    a "Me! The Quartermaster!"

    a "I couldn’t, isn’t that like a ton of responsibility?"

    mc "If I was the Captain, you’d also be second in command."

    show ast suppost at wiggle

    a "If you’d be the Captain?"

    show ast happypost

    a "Does that mean you think this is a good idea? You’ll do it?"

    mc "While ignoring a ton of the smaller and finer details not mentioned, yes, I think I would do this."

    mc "You all showed interest in being pirates when I met you, but back then you had futures on land."

    mc "I didn’t want you to become pirates when you had opportunities to become something else."

    show be confpost with Dissolve(0.1)

    b "We don’t have much going on now."

    mc "I wouldn’t just ship you off on the first vessel that came into port. You all couldn’t pass for hardened pirates, but maybe"

    mc "With the proper guidance."

    show fi sadpost at wiggle

    f "You don’t really think that."

    mc "You could become amazing pirates."

    show ast happypost at bounce

    a "Proper guidance? Does that mean you’ll?"

    mc "I’ll only agree to this if everyone is okay with me being the Captain."

    mc "If a pirate isn’t happy with leadership, they’re allowed to challenge it at any time."

    show be quizpost with Dissolve(0.1)

    b "There’s so much historic evidence of pirates being brutally democratic. Is this what they meant?"

    a "I vote for [player_name] to lead as our pirate Captain. All in favor?"

    show ge smilepost with Dissolve(0.1)

    g "Aye aye!"

    show may fl with Dissolve(0.1)

    m "Yes Captain, you can order me around as much as you want."

    show be happypost with Dissolve(0.1)

    b "I’d have to go get my guns, but aye aye. Count me in."

    show fi post with Dissolve(0.1)

    f "{cps=100}... ... ...{/cps}"

    f "{cps=80}This is crazy.{/cps}"

    show ast suppost with Dissolve(0.1)

    a "Fiona, come on. Can you really say no at this point."

    show fi madpost with Dissolve(0.1)

    f "I could, with zero problems."

    show ast suppost at wiggle

    a "And leave us all out there without you? You want G anywhere near a cannon without your supervision?"

    f "You’re all adults, you don’t need me."

    g "Yeah we do."

    show be quizpost with Dissolve(0.1)

    b "This is a highly non-traditional career path. We’d rather all do it together."

    show fi madpost with Dissolve(0.1)

    f "When was that decided?"

    show ast happypost with Dissolve(0.1)

    a "Right now, come on Fiona. Don’t make us beg."

    show fi post with Dissolve(0.1)

    pause 2.0

    show fi sadpost

    f "Okay, fine, fine, fine, relax, I’m in. I’m just thinking about the logistics."

    a "Why don’t we let Captain [player_name] worry about that?"

    f "You want to tell my parents I’m going out to sea with some random sea dog to risk my life for Mexican exports? Go right ahead."

    mc "I can if you need me to."

    show fi happypost with Dissolve(0.1)

    f "{cps=20}Huh ha ha.{/cps}"

    show fi smilepost

    f "It’s funny to know you’d try. Don’t worry I’ll take care of them."

    a "So it’s settled? Red Plague part two electric boogaloo?"

    show be confpost with Dissolve(0.1)

    b "Maybe a name that won’t remind Captain of their dead comrades?"

    show ast sadpost at bounce

    a "Oh right, sorry. How about the..."

    mc "How about we worry about a name once we have a ship?"

    show ast happypost with Dissolve(0.1)

    a "That’s a good idea. We should first come up with cool pirate nicknames for each other instead."

    mc "How about we-"

    show ge smugpost with Dissolve(0.1)

    g "Oh oh oh! I call using \"the Terrible\" in mine."

    show be post with Dissolve(0.1)

    b "I want to be Behati the Beautiful."

    show fi madpost with Dissolve(0.1)

    f "You’re gonna be Behati the Blind if you are just gonna declare yourself the prettiest."

    show be suppost with Dissolve(0.1)

    b "But why can’t I be? The alliteration is so nice to say. You can be Fiona the Fearless."

    if badwords == True:

        f "I might as well be Fiona the Barely {b}Loveable{/b} if \"The Beautiful\" is already taken."

    else:

        f "I might as well be Fiona the Barely Fuckable if \"The Beautiful\" is already taken."

    show be suppost at bounce

    b "{cps=80}What! Noooooooo!{/cps} Fine, you can have \"beautiful\"."

    show fi smilepost with Dissolve(0.1)

    f "Nope, I’m sticking with that now."

    b "Astrid make her change her name."

    show ast suppost with Dissolve(0.1)

    a "Fiona why not pick something that will strike fear, not half chubs."

    show fi sadpost with Dissolve(0.1)

    f "You guys are no fun. If G made that joke you’d be all for it."

    show ge smilepost with Dissolve(0.1)

    g "I am for it. I wish I said it."

    show may
    show be post
    with Dissolve(0.1)

    m "Are you really going to make yourself that available? Those wild men at sea sometimes forget about consent after being at sea for so long."

    mc "That won’t be a problem on my ship. But we should really focus on getting one first before we come up with names."

    show may smile with Dissolve(0.1)

    m "Well aren’t you an honorable Captain so far? Here I thought it was going to be hard to tell."

    mc "My core comes from the Pirate Code first and then the Gods."

    show ge suppost with Dissolve(0.1)

    g "What’s the Pirate Code?"

    show ast suppost with Dissolve(0.1)

    a "It’s the rules pirates abide by, G there was a poster with them in the club room."

    a "For four years."

    g "Was it next to the word collage from the French class? Because my eyes steered clear of that mess."

    show be confpost with Dissolve(0.1)

    b "Um, guys."

    w "Excuse me. Here’s the check, take care of it when you can."

    show be post
    show fi post
    show ge smilepost
    with Dissolve(0.1)

    show ast happypost with Dissolve(0.1)
    a "I'll take care of that."

    f "You sure? I got some on me."

    a "I've never been more sure in my life. It's our curtain call girls. Let's get started, shall we?"

    mc "The sooner the better."

    show may fl with Dissolve(0.1)

    m "Whatever the Captain says."

    show be happypost with Dissolve(0.1)

    b "G would you help carry my guns from home?"

    show ge smugpost with Dissolve(0.1)

    g "Only if you help me steal the ladle from my mom’s kitchen."

    mc "You all get what you need and settle your affairs. Meet back here at the front in an hour?"

    show ast happypost at bounce

    a "Sounds perfect [player_name]. Lets move out ladies."

    a "It’s time to hit the waters and set sail!"

    $ persistent.menuflag = 2

    if persistent.menuflag_count == 3:

        $ persistent.menuflag_count += 1

    stop music fadeout 2.0
    pause 2.0

    hide ast post
    hide fi post
    hide may
    hide be
    hide ge
    with dissolve

    if persistent.flg == 1:

        "Wait, something is wrong."

        "Wasn’t I just in the abandoned store?"

        "No, that was hours ago. I’m with the girls now."

        "Things are going to change now."

        $ persistent.flg += 1

        $ achievement.grant("They Know")
        $ achievement.sync()

    elif persistent.flg == 2:

        "This is familiar…"

        "Haven’t I done this before? With the girls I mean."

        mc "Hey girls wait a second."

        "They’re already gone."

        "This feels weird, like something is changing."

        $ persistent.flg += 1

    elif persistent.flg == 3:

        with delete

        "What is this feeling? It hurts a little."

        mc "Astrid, Fiona, anyone do you feel it?"

        show ast confpost with dissolve

        a "Feel what [player_name]? Are you okay?"

        mc "No, something is wrong. There’s something else here."

        a "What do you mean? We’re the only one’s talking?"

        with delete

        mc "We are talking, but we aren’t speaking. These voices are not our own."

        mc "I want to say something else but can’t..."

        $ input_C = renpy.input(" ", length=45)

        with delete

        mc "This isn’t happening."

        $ input_C = renpy.input(" ", length=45)

        define wherex = 0

        hide ast post with dissolve

        while wherex < 9:

            mc "Poseidon expels this being!{nw}"
            with delete

            $ wherex += 1

        mc "Why are you doing this?"

        $ persistent.flg += 1

    elif persistent.flg > 3:

        mc "Can you stop making me do this?"

        with delete

        mc "It’s starting to hurt."

    show BG black with fade
    pause 2.5

    $ quick_menu = False
    $ renpy.block_rollback()

    $ achievement.grant("Set Sail")
    $ achievement.sync()

    jump credits

    label credits:

        $ renpy.movie_cutscene("video/creditsBG.webm")

        return

return
