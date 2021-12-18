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

    #define line9 = ""

    if charcount == 1622 and match == "Curse":

        jump fakeloop

    else:

        "[tome_title]."

        "I can't read any of this, it doesn't even look like a real language."

        "This isn't going to help me now."

        jump choice_emptystore

label fakeloop:

        $ line9 = script[44]

        $ gui.nvl_height = None
        nvl show
        #n "[charcount]"
        n "[script]"
        #n "[line9]"

        nvl clear
