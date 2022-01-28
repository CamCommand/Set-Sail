# Cameron Drummond 2021-2022
init python in myworld:

    def getText():

        mylines = renpy.file('MysteriousTome.txt').read().decode("utf-8")
        return mylines

    def getCount():

        mylines = renpy.file('MysteriousTome.txt').read().decode("utf-8")
        total = len(mylines)
        return total

    def getCurse():

        mylines = renpy.file('MysteriousTome.txt').read().decode("utf-8")
        cc = ''.join(mylines[43]+mylines[44]+mylines[45]+mylines[46]+mylines[47])
        return cc

label act1_0:

    define script = myworld.getText()
    define charcount = myworld.getCount()
    define match = myworld.getCurse()
    define i = 0

    # define line9 = ""
    # $ line9 = script[44]
    # n "[charcount]"
    # n "[line9]"
    #"[match]"

    if charcount == 1623 and match == "Curse":

        jump secretending

    else:

        "{i}[tome_title]{/i}."

        "I can't read any of this, it doesn't even look like a real language."

        "This tome must be cursed or something. I don't have the knowledge to decipher it."

        "This was a bad idea, this isn’t right and it's not going to help me."

        jump choice_emptystore

label secretending:

        stop music fadeout 10.0

        $ tome_title = "Curse: Beyond The Realm"
        show BG insidestore2 with dissolve

        "The inside has a legible header,"
        "[tome_title]."

        $ gui.nvl_height = None

        nvl show

        n "[script]"

        nvl clear

        show BG insidestore3 with dissolve
        mc "What is this tome? What is happening?"

        "Did this book just address me?"

        "The rest of the pages are unintelligible. What is Curse supposed to mean and how does it know I’m a pirate?"

        "Fiction like this couldn't have existed when this was made, it’s too old."

        "This tome can't exist."

        "Unless it’s not from here?"

        "Wait a second, is the woman still here?"

        mc "Hello?"

        "No response."

        mc "Hello? Is anyone still here?"

        "Silence."

        mc "I feel someone else is here. Where are you?"

        "I can’t see anyone, but yet, I still feel heard. Like there's an audience who isn’t responsive to my plight."

        "A weird feeling is running up and down my body. Beyond the silence, this feeling is like."

        "I don’t have the words for it."

        "Could it be the energy the tome described? Curse?"

        mc "Who are you? I can feel you right here!"

        mc "You can see me, can’t you? Answer me!"

        define input_C = ""
        $ input_C = renpy.input(" ", length=45)

        mc "I can’t understand you."

        $ input_C = renpy.input(" ", length=45)

        mc "What are you trying to say? Who are you and what’s going on?"

        show c at truecenter with dissolve
        play effect "audio/curse.ogg" loop

        "What the hell is that? Is that the Curse?"

        "This can’t be real, Poseidon, give me strength to overcome this trial."

        show c flip at truezoom with dissolve

        "This sound is, familiar. What does it mean to me, I can’t remember?"

        "It's nostalgic somehow, is it coming from this thing?"

        show c at truestzoom with dissolve

        mc "I know you. You’re me-"

        show c flip at truestzoom2 with dissolve
        pause 1.5

        mc "This isn’t real?"

        play effect "audio/end.ogg"

        show c with ease:
            ease 1.0 zoom 100

        pause 2.0

        return
