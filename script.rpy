# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Punk = Character('Punk', color="#E03B8B")
$ hex = "#000000"
define MC = Character('[player_name]', color="#380101")


# The game starts here.

label start:
        $ player_name = ""
        $ player_identity = ""
        scene bg dance
        "I do the same thing I do every morning and ask who I am."

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
                $ player_name = renpy.input("Choose your Identity", length=15)
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
            MC "I'm looking good."
            Punk "This is a test line."
            MC "Another line..."
            jump test
        label choice_name_O:
            MC "Feeling tight."
            jump test
        label choice_name_R:
            MC "It's every day."
            jump test
        label choice_name_User:
            MC "Suffering."
            jump test


label test:
    MC """
    This is the first line of dialogue. It's longer than the other two
    lines, so it has to wrap.

    This is the second line of dialogue.

    This is the third line of dialogue.
    """


    "During this tutorial I kick your ass..."
    scene bg aot
    "Punk" "Yo bitch it's ya girl."
    "Punk" "I've been \"kick your ass\" since you were a kid."


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
