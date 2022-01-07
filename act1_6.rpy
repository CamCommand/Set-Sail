label act1_6:

stop music fadeout 1.0
play music "music/PirateTimes.mp3" volume 0.5 fadein 1.5

scene BG black with fade
scene BG cafeoutside with fade

if may_talk == 0:

    "After some more aimless wandering finally, a strip where everything isn’t closed."

    "Actually, most of these businesses look closed, but just because of the time according to the open hours on their windows."

    "There’s what looks like a small café coming up on the right."

    "Even without the \"Open Café\" sign hanging from the canopy, the smell of brew bubbles up into my nostrils."

    "It’s about time something other than pollution or sea water tickled my sense of smell."

    "There are some people eating inside. This might be my best chance of getting some grub before I figure out where to go next."

    "I barely have energy to steal at this point. Begging them to take my earrings as payment is my only option."

    if earrings == 0:

        "That is, if I still had them."

        "That sly wench stole them right off my head and I didn’t even go after her."

        "How pathetic is that? Maybe if I’m fed my wrath will reawaken."

    "Getting closer to the windows, people are being served sandwiches and soups. Nobody but the server is wearing a mask."

    "Apparently this COVID thing spreads through air but not food."

    "My stomach is in control of my eyes, the soup’s holding onto my line of sight."

    # show astrid in the window

    mc "Is that…"

    mc "Astrid's soup?"

    # show a suprised astrid

    "It’s unbelievable, this is it!"

    "Astrid is who I was meant to find!"

    "Thank you Gods, you’re gracious and benevolent, I’m sorry for ever doubting you were looking out for me."



elif may_talk == 1:

    show m_d at left with dissolve

    "After some more small talk Hanna and I make it to the side of this small café."

    "Strolling down the side of a large strip of closed shops, the strong smell of brew bubbles up into my nose unexpectedly."

    "Finally, something to drown out the mix of sea water and trash."

    "There are a few people inside the café I can kind of see through the window."

    "Can’t tell if that’s a good or a bad thing at this point. They aren’t wearing masks while waiting for their food."

    m "You should put on your mask before we go in."

    m "It’s probably fine, but still, it’s better if you do, I've learned."

    if mask == 1:

        mc "Yeah I got one from Doll."

        mc "It was real nice of her, she didn’t even charge me."

        m "I wasn’t talking to her for long, but she seemed real nice for a homeless lady."

        mc "Are all homeless ladies not nice?"

        m "I don’t want to get into this."

    else:

        mc "I never got one."

        mc "People weren’t exactly being super nice to me about it."

        mc "Plus, nobody told me about this disease ruining everything cool."

        m "It’s worse than that, a whole ass pandemic has been going around."

        m "Although, at this point people seem to act like it’s over."

        mc "You mean they cured it?"

        m "No."

        mc "So how did they get over it? Did it die out?"

        m " No, they just stopped caring. Some people needed a haircut."

        mc "Oh… Well that’s one way to do it."

        mc "Couldn’t they just give themselves a haircut?"

        m "Haircuts are really important."

        m "Why couldn’t back in the day they just ignored the Black Plague, I mean like come on?"

        mc "Exactly, it could have been over so much easier if the peasants just prayed harder."

        m "You didn’t tell me you were a historian?"

        m "Our hindsight is too good nowadays, we’d never let history repeat itself."


    "Walking by the windows I start to make out some of the people in there."

    "Soup and coffee are being served to a table. My stomach has taken over my eyes, I can’t look away."

    "Perhaps these dishes are worth it to the type of people who’d brave this supposedly deadly disease?"

    # show astrid in the window

    mc "Is that?"

    # show suprised astrid

    m "Do you know that girl?"

    mc "Yeah, I do know her."

    m "You think she’d pay for the coffee?"

    mc "No, I don’t think so. Hanna, can we sit with her?"

    mc "She’s who I’ve been looking for."

    # flirty may

    m "Sure, I guess. What is she your little girlfriend?"

    if astrid_affinity >= 3:

        mc "{color=#2150E7}What?! No! I mean, like, I.{/color}"

        mc "Look I know her alright, she’s a good omen."

        mc "Are you coming in with me or not?"

        m "Okay dude, sure thing. I said I was, didn't I?"

    else:

        mc "{color=#2150E7}No, she’s a friend of mine.{/color}"

        mc "This is a good omen, are you gonna sit down with me?"

        m "I said I was going to, didn’t I?"

$ w = Character('Waitress', color="#FF793B", callback=rot_voice) # resuing the market woman for the waitress

transform caf: # align long cafe bg at the left

    xalign 0.0

transform cafe: # transition to other end of BG

    linear 2.0 xalign 1.0

scene BG cafeinside at caf with fade
show m_d at left with ease
# play inside music

if mask == 1:

    w "Welcome to Corner Café, take a seat wherever and I’ll get right to you."

else:

    w "Excuse me, could you please put on a mask before entering the café?"

    mc "Do I have to?"

    w "No, we can’t make you, but it’s highly encouraged."

    mc "Okay thanks for nothing then."

    w "Uh!"

show a_d at center with dissolve

mc "Astrid of Bellewood? Is that you?"

a "[player_name] oh my gosh it’s so good to see you."

# laughing astrid

a "Yeah, it’s me, Astrid. People keep dropping the \"of Bellewood\" part, haha."

a "Also I just changed my hair."

a "What are you doing back here?"

mc "That is such a long story, but I’m so glad to see you."

mc "I feel as if I was destined to find you here."

a "Don’t get all sappy on me now. You were destined to find me?"

mc "Well I mean, I think the Gods guided me here for some purpose."

a "You know I thought all that talk about the Poseidon and Greek Gods was you playing the pirate role up for us."

mc "No, I believe them to be as real as the waves that guide us."

a "That’s pretty dramatic, but I guess that fits."

# worried astrid

a "Are you dehydrated or what?"

if may_talk == 1:

    # smiling May

    m "Um hello?"

    mc "Oh my bad. Astrid, this is Hanna."

    mc "She is showing me around and was going to buy me some food."

    a "Nice to meet you Hanna."

    a "Any friend of [player_name] is a friend of ours."

a "We are all actually catching up right now."

if may_talk == 1:

    a "Do you both want to join us?"

else:

    a "You want to join us?"

mc "We? Like the eboard?"

a "Yup, we’re having a little get together."

mc "Of course, I’d love to hear what you’ve all been up to."

scene BG cafeinside at cafe
pause 1.0

show fiona at truecenter with dissolve
show b_d at centerrighter with dissolve
show g_d at right with dissolve

# excitable G

g "The Queen isn’t gonna make it I’m telling you, she’s done for this time next month."

b "She has access to the best healthcare in her entire country."

b "Women live on average longer than men. She is the most likely candidate to break the oldest age record."

# pissed Fiona

f "I don’t believe the shit you’re spewing G."

f "Why are you rooting for an old lady to die?"

show a_d at centerlefter

a "Guys, you won’t believe what destiny swept in."

mc "Hey everyone."

# suprised Fiona

f "Well I’ll be damned."

# suprised Be

b "What are the odds you’d show up again?"

g "No freaking way man, and I almost didn’t show up today."

mc "It’s good to see you’re all as lively as I remembered you."

if may_talk == 1:

    show m_d at left with dissolve

    mc "Everyone, this is my new friend Hanna."

    mc "She helped me find this place, is it alright if she sits with us?"

    f "No problem, welcome to the table."

    b "Nice to meet you."

    m "Hello hello, nice to meet you too."

    g "Sit down you two, don’t keep us waiting. I wanna know what’s happening."

g "What are you doing back here?"

f "Was Astrid joking or did destiny really guide your way?"

b "Don’t be silly Fiona, obviously the Red Plague is in port again."

f "Then why haven’t we heard about it?"

# quizzative Behati

b "Oh, that’s because…"

b "Well you can tell us [player_name]."

mc "That’s an, uncomfortable subject right now."

a "What’s wrong, I didn’t want to say anything but you don’t look so good."

if may_talk == 1:

    if player_identity == "f":

        m "I think she’s just hungry."

    elif player_identity == "m":

        m "I think he’s just hungry."

    else:

        m "I think they’re just hungry."

    m "Hey waitress, can we get two cups of black coffee and a chocolate chip muffin?"

    mc "Thanks Hanna, again that means a lot."

else:

    mc "Right now, I’m just really hungry."

    # smiling G

    g "What? Don’t they feed you on that ship?"

    # mad Fiona

    f "G!"

    if player_identity == "f":

        f "She just said they don’t want to talk about it."

    elif player_identity == "m":

        f "He just said they don’t want to talk about it."

    else:

        f "They just said they don’t want to talk about it."

    # apologetic G

    g "Oh duh, sorry."

    mc "It’s okay, we can talk, I just need something to eat."

    if earrings == 1:

        mc "You think they’d take my earrings as payment for some food?"

    else:

        mc "Would you guys be willing to share some food?"

        mc "I’d buy my own, but anything I had of value got stolen."

    a "Of course [player_name]. Anything for a fellow pirate."

    a "You can have my fries if you don’t mind that I ordered them spicy."

    b "My sandwich comes with soup, you can have that too."

    mc "That sounds great, I can’t thank you girls enough."

mc "It’s good to see you all still hang out together. Do you do this often?"

g "We try, if we can get Astrid out of her room."

f "G! Come on!"

g "What, stop snapping at me? It’s true."

g "How many of these has Behati tried setting up and we barely are all together once every other month."

f "Don’t know if you remembered but there’s been a stupid pandemic prancing around."

g "Yeah, but Corner has been back open for months."

# concered Behati

b "Can we not argue while we’re all here please?"

b "There’s a one hundred percent chance it will upset someone beyond what apologizing will fix."

pause 1.5

g "You’re right Be. Sorry Astrid."

a "It’s okay G. Sorry [player_name], things have been hard on all of us these past few months."

f "Astrid, this has been going on for over a year now."

f "I wish it was still March as much as the next person, but there's still no sign of this blowing over."

g "Two weeks my ass."

if may_talk == 1:

    mc "Hanna, did you know this was going on for so long?"

    m "Like I said, it’s been rough around here."

    m "Oh, here’s our coffee."

    w "Here’s your muffin and coffees, will there be anything else?"

    mc "No, thank you."

    "The first bite was like nothing had ever graced my mouth in years."

    "Hanna’s muffin is also gone, she’s started on her coffee now. I’m still feeling hungry though."

    "Maybe one of the girls will share some of their sandwiches with me later."

mc "So, everything hasn’t been great?"

f "Not like all our lives were on track for success after high school, but the pandemic really messed our shit up."

g "I almost had that consulting job and you know it Fiona!"

f "Why are you yelling at me now?"

f "But yeah G, then the company went under so drop it and move on."

g "[player_name] so get this. I was doing some odd jobs here and there after high school."

g "Delivering food, running some wafer cookie companies’ Twitter, when I get this call from a friend of a friend’s coworker about coming onto their studio as a consultant."

b "A video game studio opening in Florida felt like a bad idea from the start."

g "Well we were almost done with my contract when,"

play effect "audio/crash.mp3"

g "BAM!"

g "The rona ruined everything."

g "Now I’ve been stuck working for slave wages at my parent’s resturant to keep it open."

if may_talk == 1:

    mc "That’s awful G. You were so close."

    m "You almost had it kid."

    # mad G

    g "I know right! It blows."

else:

    mc "That’s terrible G, I’m sorry it wound up like that."

    g "I know right! It’s bullcrap."

g "Could’ve been worse, Fiona had to drop out of college."

f "It’s not my fault I can’t learn calculus from sloppily written notes sent to us every week if the professor remembered they had a job."

a "Fiona relax, you’ll try again when this is over with."

f "I was doing great until this country decided to get even grosser than usual."

f "Couldn’t even take the simple steps to make things go back to the way they liked it."

f "It had to be a grand conspiracy and not getting a shot ruined young people’s lives specifically. Like we weren’t being shafted enough."

b "Vaccination rates are up you know. It could get better."

f "Anything’s better than zero I suppose."

f "No wait, it isn’t because that’s not how vaccines work! Half our state alone doesn’t seem to get that!"

a "It’s bullshit, we know, but calm down girl."

f "Sorry, jeez, you’re right I don’t need to get riled up before eating."

mc "You made it to college Fiona?"

mc "How was it, was it everything you thought it was?"

# happy fiona

f "Oh, sweet sweet [player_name]. It was nice while it lasted."

f "I was learning actually cool stuff, there was a super large queer association on campus, living in the dorms was hard but fulfilling."

f "It was all just so…"

g "Epic?"

b "Satisfactory?"

if may_talk == 1:

    m "Sooooo much drinking."

f "It was perfect. Which makes what happened suck even more."

f "I’m lucky Behati knew what I was going through and I wasn’t just making it up."

b "It’s great and all, but I agree with Astrid."

b "Once this is over I’m sure some school will let you and me in so we can study together now."

mc "You got into college too Behati?"

# happy Be

b "Yes I did! I got a full ride to Florida State."

b "I was still undeclared but was having a great time. Living in a co-ed dorm and everyone was so pretty it was nuts!"

if may_talk == 1:

    m "So you went for the whole platter aye?"

g "It was annoying at first when she texted us pictures of every hot person she saw."

g "But you’d send me the pictures of the cute girls so it was cool with me."

a "And you sent me the guys so it was fair and balanced."

f "All I got were rocks."

b "The geological history by the school was so fascinating only you’d appreciate the layers Fiona."

mc "So if it was so great what happened?"

b "I can’t remember if we talked about it, but I was interested in old guns and one went off in my dorm room."

b "It went through every wall on my side of the floor."

b "Which was completely unpredictable because I was just starting to take it apart and the guy who sold it to me said it was decommissioned and hadn't been fired in years."

f "We looked him up after Be was expelled and he had been selling stolen goods he knew nothing about for years."

f "The state still can’t find him."

mc "Maybe he escaped out to sea."

b "The jerk ruined my future just when I decided my major would be history."

b "Or was it anthropology?"

a "You told me you were going to choose computer science?"

g "I thought it was linguistics?"

f "Same."

b "Well either way the school system shut down due to rona at the same time I was allowed to reapply."

b "Georgia schools are opening soon, Fiona, we could both try to get in up north?"

f "Just for them to be shut down again for the third or fourth time?"

f "No thank you, I’ll just suffer in silence until it’s done for good."

g "Silence?"

f "Oh quit it G! I don’t need your-"

g "Okay, okay, remember to relax."

a "[player_name] tell us what you’ve been up to please."

a "You can skip the bad parts right? You said being a pirate was very freeing."

a "You were still living free, right?"

mc "..."

mc "Yeah, I was doing great for a while."

mc "I got promoted to first mate for real this time and was taking on more responsibility on the ship and people were starting to respect me for it."

mc "There was even this one time where both the Captain and Flavio, our Quartermaster, both fell ill and I took charge for three whole days."

a "Wait, you weren’t the first mate when we met?"

mc "No, I wanted to sound important. At the time I was either assistant to the Captain's assistant or head deck hand."

a "Well that’s fine, not like you were a dockboy or anything."

g "So you got a real taste at being in charge, that’s awesome."

mc "I didn’t do too much while in charge though."

mc "We took them to this island off of the Bahamas to get treated. So the Plague was in port for most of the duration."

if may_talk == 0:

    $ m = Character("[may_name]", color="#0A4AF6", callback=may_voice)

    show m_d at left with moveinleft

    m "Excuse me, sorry to interrupt. But did you say \"The Plague\"?"

    m "As in the Red Plague?"

    mc "{cps=70}Ummm, no I meant the black plague.{/cps}"

    mc "In Europe."

    mc "We’re doing a history school thing about it."

    m "No, I’ve been listening."

    m "You all aren’t in school anymore and you look and have been talking about being a pirate."

    g "Yeah, they’re a pirate!"

    g "So don’t mess with us lady, mind your own business!"

    mc "Wait, I recognize you."

    mc "You’re that [may_position] from the [activity_choice]."

    if activity_choice == "market":

        mc "Or what was left of it."

    elif earrings != 1:

        mc "And you stole my earrings!"

    m "That's right first mate. I couldn’t help but overhear your entire, loud, conversation."

    m "Sorry about your sob stories girls."

    m "It’s pretty ballsy for a pirate of a feared pirate ship to be waiting for coffee in some rundown town."

    mc "Not really any of your concern though, is it?"

    "This would be an ample moment where I’d flash my weapon. If I still had one."

    m "I won’t cause a scene involving any feds under one condition."

    mc "And you’re calling me ballsy?"

    mc "You think your government will swarm my exact location off of some phone call?"

    f "Yeah, we don’t even know you and you’re just blackmailing the people at the table next to you?"

    f "Are you really that desperate or stupid?"

    m "I just don’t want to drag this out sweethearts."

    m "There are reasons for what I do and I won’t blab if you give me one thing."

    mc "What? What else could you possibly take from me?"

    m "Give me a job on your ship. Simple as that."

    mc "You’re joking with me aren’t you?"

    g "Hey that’s not fair! [player_name] wouldn’t let us come with them."

    g "Who do you think you are?"

    b "This is such a weird and barely qualifies as a hostage situation."

    mc "My thoughts exactly, why would you want to join a pirate crew anyway?"

    mc "Are you also a wayward soul?"

    m "Let’s just say I have my reasons."

    m "Not like I’m completely worthless, I’m an experienced doctor. Any ship could use another one of those."

    mc "Oh I’m sure you are."

    mc "An experienced doctor is roaming the streets running cons on random people."

    m "I’ll have you know I went to the Herbert Wertheim College of Medicine in this, the great state of Florida."

    m "And I've been a practicing sea vessel doctor for years now. I know my way around a ship and a scalpel."

    mc "Behati, is that a real place?"

    g "Dude, how do you not know you’re in Florida at this point?"

    mc "No G, the school-"

    b "\"Medical school is a transformative experience. It is an exciting and challenging journey.\""

    b "\"At HWCOM, your journey is enhanced by diversity, research and innovation, and community outreach.\""

    b "So it’s a big school that produces a lot of doctors."

    b "Or at least that’s what it says on their website."

    f "Well that may be lady, but how is [player_name] supposed to trust you?"

    if player_identity == "m":

        f "You haven’t even told him your real name?"

    elif player_identity == "f":

        f "You haven’t even told her your real name?"

    else:

        f "You haven’t even told them your real name?"

    m "It isn’t a matter of trust, it’s easy peasy, super appealing, blackmail."

    m "Or at the very least get you kicked out of one of the few remaining coffee shops left in town."

    if player_identity == "m":

        m "So, do we have a deal handsome?"

    else:

        m "So, do we have a deal gorgeous?"

    a "That’s outrageous!"

    a "We could just leave you know."

    f "Who do you think you are making these demands?"

    g "If anyone gets to be on the ship it’s me!"

    # zoom may

    m "Oh come on. I’m asking very nicely."

    m "Could you really turn down a woman who’s offering her services to you?"

    mc "I can’t let you on the ship lady."

    m "Oh please [player_name]. Don’t make me ask twice darling."

    mc "Because there isn’t a ship to go back to."

    # undo may zoom

else:

    m "Wait, I’m sorry. You’re a pirate?"

    m "I thought they were kidding? What happened to the rich brat story?"

    mc "Sorry for lying Hanna, I didn’t know if I could trust you."

    mc "The Red Plague is a notorious ship, I didn't know if you would change your opinion about me if you had known."

    m "So you’re a wanted pirate or whatever?"

    mc "Like I said, I didn’t know if I could trust you."

    mc "What if you’d turn me into the state?"

    mc "You aren’t going to do that, are you?"

    m "No, of course not. I’m not going to crawl to the cops or some dumb shit like that."

    m "I lied to you too, by the way."

    mc "Really?"

    m "Yup, Hanna’s not my name and my kid is a dog I met a couple of days ago."

    mc "Playing the sympathy card, not a bad trick."

    m "Between the deceit and the muffin we’re almost even."

    mc "Oh, is that right?"

    m "You could make us square if you let me on your ship after this."

    mc "That’s funny not Hanna."

    m "No seriously, let me work on your ship."

    g "Hey that’s not fair! [player_name] wouldn’t let us come with them."

    g "Why would a muffin change that?"

    mc "Why do you want to join a pirate crew anyway?"

    m "Let’s just say I have my reasons."

    m "I can make it worth your while, I’m an excellent doctor."

    mc "For sure, an excellent doctor is roaming the streets earning sympathy points from random pirates."

    m "I’ll have you know I went to the Herbert Wertheim College of Medicine and have been a practicing sea vessel doctor for years now."

    m "I’m not just some hobo, I know my way around a ship and a scalpel."

    mc "Behati, is that a real place?"

$ persistent.menuflag = 2

if persistent.menuflag_count == 3:

    $ persistent.menuflag_count += 1

return
