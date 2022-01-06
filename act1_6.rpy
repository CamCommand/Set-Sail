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

# transition to inside cafe
# play inside music

if mask == 1:

    w "Welcome to Corner Café, take a seat wherever and I’ll get right to you."

else:

    w "Excuse me, could you please put on a mask before entering the café?"

    mc "Do I have to?"

    w "No, we can’t make you, but it’s highly encouraged."

    mc "Okay thanks for nothing then."

    w "Uh!"

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

# slide tranition in the cafe

show g_d at right with ease
show b_d at centerright with ease
show fiona at center with ease

# excitable G

g "The Queen isn’t gonna make it I’m telling you, she’s done for this time next month."

b "She has access to the best healthcare in her entire country."

b "Women live on average longer than men. She is the most likely candidate to break the oldest age record."

# pissed Fiona

f "I don’t believe the shit you’re spewing G."

f "Why are you rooting for an old lady to die?"

a "Guys, you won’t believe what destiny swept in."

mc "Hey everyone."

# suprised Fiona

f "Well I’ll be damned."

# suprised Be

b "What are the odds you’d show up again?"

g "No freaking way man, and I almost didn’t show up today."

mc "It’s good to see you’re all as lively as I remembered you."


$ persistent.menuflag = 2
$ persistent.menuflag_count = 3 # testing
if persistent.menuflag_count == 3:

    $ persistent.menuflag_count += 1

return
