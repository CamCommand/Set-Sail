# Cameron Drummond 2021


init python:# define sound bleeps here
    def voice(event, **kwargs):# voice for MC
        if event == "show":
            renpy.music.play("audio/blip1.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def astrid_voice(event, **kwargs):# voice for astrid
        if event == "show":
            renpy.music.play("audio/blip2.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def twohands_voice(event, **kwargs):# voice for TwoHands
        if event == "show":
            renpy.music.play("audio/blip3.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def caps_voice(event, **kwargs):# voice for TwoHands
        if event == "show":
            renpy.music.play("audio/blip4.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def fl_voice(event, **kwargs):# voice for TwoHands
        if event == "show":
            renpy.music.play("audio/blip5.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def lib_voice(event, **kwargs):# voice for TwoHands
        if event == "show":
            renpy.music.play("audio/blip6.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def rot_voice(event, **kwargs):# voice for TwoHands
        if event == "show":
            renpy.music.play("audio/blip7.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def bar_voice(event, **kwargs):# voice for TwoHands
        if event == "show":
            renpy.music.play("audio/blip8.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    if renpy.windows:
        config.tts_voice = "Mark"
    elif renpy.macintosh:
        config.tts_voice = "Alex"
    elif renpy.linux:
        config.tts_voice = "english_rp"

# Main characters
define MC = Character("[player_name]", dynamic=True, color="#990033", callback=voice)# Player Character
define Fi = Character('Fiona', color="#E44D1A")
define G = Character('Geraldine', color="#DFDABB")# Geraldine
define As = Character('Astrid', color="#FF79E6", callback=astrid_voice, dynamic=True)
define Be = Character('Behati', color="#5E0F60")
define Ma = Character('May', color="#0A4AF6")
define n = nvl_narrator# Narrator

# Main charcter images
image astrid_default = "Astrid.png"

# Minor characters
define th = Character('[pirate]', color="#000000", who_outlines=[ (1, "#FFFFFF") ], callback=twohands_voice)# Ol' Two Hands
define Cap = Character('Captain', color="#7F0505", callback=caps_voice)# The Demonic Pirate Ricardo AKA Captain
define fla = Character('Flavio', color="#BB64F2", who_outlines=[ (1, "#000000") ], callback=fl_voice)# sir Flavio
define woman = Character('Woman', dynamic=True, color="#07BB01", callback=lib_voice)# Librarian
define cr = Character('Passerbys', color="#000001", who_outlines=[ (1, "#FFFFFF") ])# crowd of people
define m = Character('Short Woman', color="#F263E2", callback=rot_voice)# woman at market
define bt = Character('Bartender', color="#748DA3", callback=bar_voice)# bartender at arcade

# Affinity of main characters
default Fi_affinity = 0
default G_affinity = 0
default Astrid_affinity = 0
default Be_affinity = 0
default May_affinity = 0

# voice tags

# background images
image BG MC_room ="background/bedroom.png"
image BG deckview = "background/deckview.png"
image BG topdeck = "background/topdeck.png"
image BG black = "background/black.png"
image BG harbor = "background/harbortemp.png"
image BG map = "background/maplayered.png"
image BG bstore = "background/bstore.png"
image BG school = "background/school.png"
image BG market = "background/market_temp.jpg"
image BG ar = "background/arcades.png"
image BG st = "background/street.png"

# Other characters images
image twohands = "TwoHands.png"
image captain = "captain.png"
image fla = "flavio.png"
image lib = "lady.png"
image bartender = "bt1.png"
image mm = "momlady.png"

# Menu Music
define config.game_menu_music = "music/BelowDeck.mp3"
# define config.main_menu_music

# The game starts here baby!
label start:

    # position name of character speaking
    define gui.name_xpos = 0.1
    define gui.name_ypos = .15
    define gui.name_xalign = 0.2
    define gui.name_yalign = 0.5

    # center dialogue in center of box
    define gui.dialogue_xpos = 0.54
    define gui.dialogue_text_xalign = 0.5

    # size of namebox on the left side of screen
    define gui.namebox_width = 800
    define gui.namebox_height = 100

    # use of namebox
    define gui.namebox_borders = Borders(15, 7, 15, 7)
    define gui.namebox_tile = True

    jump act1_1
