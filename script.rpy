# The script of the game goes in this file.

define Punk = Character('Punk', color="#E03B8B") #temp character
define MC = Character('[player_name]', color="#380101")
define Fiona = Character('Fiona', color="#E44D1A")
define G = Character('Geraldine', color="#DFDABB")
define Astrid = Character('Astrid', color="#F236BD")
define Behati = Character('Behati', color="#5E0F60")
define May = Character('May', color="#0A4AF6")

image BG bkgd = "map.png"

# The game starts here baby ;)

label start:
    play music "audio/waves.ogg"
    """
    {cps=50}Pirating is older than recorded human history. Supply chains interrupted and intercepted by those with the might to steal large portions of materials.

    {cps=50}Every stretch of water has seen one form or another of piracy. Normally, stealing large sums of profit is seen as immoral.

    {cps=50}Yet pirates are deified and revered throughout history. Its unique form of crime shook the world in a way nothing else could.

    {cps=50}Thus began a code between these pirates. An honor amongst thieves to be upheld keeping the practice ruly in unruly times.

    {cps=50}The Pirate Code kept the practice alive throughout the centuries. There was seemingly no end in sight to the popularity of the lifestyle.

    {cps=50}Marching into the modern age, piracy has taken many forms. Many melded with the times to seek out the most profitable whales of the sea while some kept the old fashion {i}Jolly Roger{/i} casted.

    {cps=50}Thousands are at sea breathing new life into pirating today.

    {cps=50}You are someone who has known nothing other than the life. Your own adventure is about to {b}Set Sail{/b}.
    {/cps}"""

    pause 3.0

label select:
        scene BG bkgd
        with fade
        $ player_name = ""
        $ player_identity = ""
        "{cps=50}My eyes flutter open to the sound of small waves and seagulls crying. We must be close to a port. I roll my neck around, it cracks in multiple places, I’m incredibly sore.{/cps}"

        menu:
            "My name is Valerie":
                $ player_name = "Valerie"
                $ player_identity = "f"
                jump choice_name_V
            "My name is Oscar":
                $ player_name = "Oscar"
                $ player_identity = "m"
                jump choice_name_O
            "My name is Reed":
                $ player_name = "Reed"
                $ player_identity = "nb"
                jump choice_name_R
            "What is my name?":
                $ player_name = renpy.input("Choose your name", length=15)
                $ player_name = player_name.strip() #strip unused spaces
                if player_name == "":
                    $ player_name = "Me"
        "How do I identify?"
        menu:
            "Female":
                $ player_identity = "f"
                jump choice_name_User
            "Male":
                $ player_identity = "m"
                jump choice_name_User
            "Non Binary":
                    $ player_identity = "nb"
                    jump choice_name_User


        label choice_name_V:
            MC "{cps=50}I'm looking OK enough. Poseidon, please allow for pleasant skys today. I cannot sleep through something as brutal as last night.{/cps}"
            jump opening
        label choice_name_O:
            MC "{cps=50}Feeling tight. Poseidon, please allow for pleasant skys today. I cannot sleep through something as brutal as last night.{/cps}"
            jump opening
        label choice_name_R:
            MC "{cps=50}It's another salty morning. Poseidon, please allow for pleasant skys today. I cannot sleep through something as brutal as last night.{/cps}"
            jump opening
        label choice_name_User:
            MC "{cps=50}Suffering is key to living. Poseidon, please allow for pleasant skys today. I cannot sleep through something as brutal as last night.{/cps}"
            jump opening

        label opening:
            MC "{cps=50}I get up from my cot and scan through my room. It’s a small closet under the stairs to the top deck with barely enough room for anything extra beyond my necessities.v{/cps}"
            MC "{cps=50}I am lucky to have it, one of the only perks I’ve gotten from being the captain's child. The privacy is amazing, and the smells of the common area don’t leak into my nose from here.{/cps}"
            MC "{cps=50}I’d like to think I earned this spot, but realistically, it was the only spot on the ship to keep a young person without anyone getting to them. Either way I appreciated the forethought.{/cps}"

            jump girltest

label girltest:
    scene BG bkgd
    show astrid at center
    Astrid "How's your day going so far?"
    show g at right
    G "What's up losers?"
    show fiona at left
    Fiona "I'm in the middle of something, one second."
    hide astrid
    hide g
    hide fiona
    show behati at right
    Behati "I estimate a fifty percent chance if this working out."
    show palmer at left
    May "You need any help with those boxes sweatheart?"
    jump sprites
'''
label sprites:
    scene bg aot11
    show img_1506
    Punk "But you're looking good today."
    with fade
    show img_1506
    Punk "Have you been working out?"

    Punk "Or are you just toughing up finally?"
    stop music fadeout 1.0
    show img951489 at right
    "New Girl" "Or maybe he's on steroids!"
    #queue music "some new song.mp3
    #play sound "audio/somesound" for sound effect
    menu:
            "I'm juicing":
                jump choice1_a
            "what?!":
                jump choice1_b

    label choice1_a:
        Punk "Really?"
        jump nextline

    label choice1_b:
        "New Girl" "Come on..."
        jump nextline

    label nextline:
        Punk "Goddamn."

    return
'''
