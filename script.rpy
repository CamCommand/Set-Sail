# Cameron Drummond 2021

init python:

    def voice(event, **kwargs):# voice for MC
        if event == "show":
            renpy.music.play("audio/blip1.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def may_voice(event, **kwargs):# voice for May
        if event == "show":
            renpy.music.play("audio/blip15.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def astrid_voice(event, **kwargs):# voice for astrid
        if event == "show":
            renpy.music.play("audio/blip2.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def fiona_voice(event, **kwargs):# voice for Fiona
        if event == "show":
            renpy.music.play("audio/blip9.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def g_voice(event, **kwargs):# voice for G
        if event == "show":
            renpy.music.play("audio/blip10.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def b_voice(event, **kwargs):# voice for Behati
        if event == "show":
            renpy.music.play("audio/blip11.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def twohands_voice(event, **kwargs):# voice for TwoHands
        if event == "show":
            renpy.music.play("audio/blip3.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def caps_voice(event, **kwargs):# voice for Captain
        if event == "show":
            renpy.music.play("audio/blip4.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def fl_voice(event, **kwargs):# voice for Flavio
        if event == "show":
            renpy.music.play("audio/blip5.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def lib_voice(event, **kwargs):# voice for librarain
        if event == "show":
            renpy.music.play("audio/blip6.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def rot_voice(event, **kwargs):# voice for market woman
        if event == "show":
            renpy.music.play("audio/blip7.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def bar_voice(event, **kwargs):# voice for bartender
        if event == "show":
            renpy.music.play("audio/blip8.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def jj_voice(event, **kwargs):# voice for joejoe
        if event == "show":
            renpy.music.play("audio/blip12.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def pirate_voice(event, **kwargs):# voice for pirate man billy bob
        if event == "show":
            renpy.music.play("audio/blippirate.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def Crashsound_test(event, **kwargs):# noise to play when everone yells
        if event == "show":
            renpy.music.play("audio/crash.mp3 ", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def hobo_voice(event, **kwargs):# voice for hob lady
        if event == "show":
            renpy.music.play("audio/blip13.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")


    def crowd_voice(event, **kwargs):# voice for crowd
        if event == "show":
            renpy.music.play("audio/blip14.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")



    # USE this for sound effects bc voices play over them
    renpy.music.register_channel("effect","voice", loop = False, tight=True)

transform wiggle: # To shake the characters a little bit, use at
    linear 0.1 xoffset -4 yoffset 4
    linear 0.1 xoffset 6 yoffset -6
    linear 0.1 xoffset 4 yoffset -4
    linear 0.1 xoffset -6 yoffset 6
    linear 0.1 xoffset 0 yoffset 0

transform zoom: # zoom into dingy specifically
    xalign 0.05 yalign 0.3
    ease 1.0 zoom 1.5
    pause 2.0

transform redo: # return from any zoom
    xalign 0.5 yalign 0.5
    ease 1.0 zoom 1.0

transform redochar:
    xalign 0.5 yalign 1.0
    ease 1.0 zoom 1.0

transform zoom_may:
    ease 1.0 zoom 1.2

define flash = Fade(.15, 0.0, .25, color="#fff") # for making the sword cut sound working idk why
define flash_lighting = Fade(.15, 0.0, .25, color="#AFDBF2") # for making the sword cut sound working idk why
define deathflash = Fade(.15, 0.0, .25, color="#F25555") # for when character dies
define slowfade = Dissolve(20)

screen game_over_screen:
    vbox:
        xalign 0.5
        yalign 0.5
        text _("{size=156}Game Over{/size}")
        textbutton _("\n\n\n   Return to Main Menu") action Return()

# Main characters
define MC = Character("[player_name]", dynamic=True, color="#990033", callback=voice)# Player Character
define f = Character('Fiona', color="#E44D1A", callback=fiona_voice)                 # Fiona
define g = Character('Geraldine', color="#F0CD00", callback=g_voice)                 # Geraldine
define a = Character('Astrid', color="#FF79E6", callback=astrid_voice, dynamic=True) # Astird
define b = Character('Behati', color="#5E0F60", callback=b_voice)                    # Behati
define m = Character('May', color="#0A4AF6",  callback=may_voice)                    # May
define n = nvl_narrator                                                              # Narrator
define ev = Character('Everyone', color="#000000", callback=Crashsound_test)         # Everyone at once

# Main charcter resting images
image a_d = "Astrid.png"
image b_d = "behati.png"

image fiona = "Fiona.png"
image fiona angry = "Fiona angry.png"
image fiona laugh = "Fiona laugh.png"
image fiona sad = "Fiona sad.png"
image fiona frown = "Fiona frown.png"

image g_d = "G.png"
image m_d = "Palmer.png"

# Minor characters
define th = Character('[pirate]', color="#000000", who_outlines=[ (1, "#FFFFFF") ], callback=twohands_voice)# Ol' Two Hands
define Cap = Character('Captain', color="#7F0505", callback=caps_voice)                                     # The Demonic Pirate Ricardo AKA Captain
define fla = Character('Flavio', color="#BB64F2", who_outlines=[ (1, "#000000") ], callback=fl_voice)       # sir Flavio
define woman = Character('Woman', dynamic=True, color="#07BB01", callback=lib_voice)                        # Librarian
define cr = Character('Passerbys', color="#000001", who_outlines=[ (1, "#FFFFFF") ], callback=crowd_voice)  # crowd of people
define ma = Character('Short Woman', color="#F263E2", callback=rot_voice)                                   # woman at market
define bt = Character('Bartender', color="#748DA3", callback=bar_voice)                                     # bartender at arcade
define jj = Character('JoeJoe', color = "#0015BC", callback=jj_voice)                                       # JoeJoe
define p = Character('Enemy Pirate', color = "#0015BC", callback=pirate_voice)                              # attacking Pirates
define dl = Character('Lady', color = "#740E86", callback=hobo_voice)                                       # Doll the hobo

# Affinity of main characters
default Fi_affinity = 0
default G_affinity = 0
default Astrid_affinity = 0
default Be_affinity = 0
default May_affinity = 0

# background images
image BG MC_room ="background/bedroom.png"
image BG deckview = "background/deckview.png"
image BG topdeck = "background/topdeck.png"
image BG black = "background/black.png"
image BG harbor = "background/walk1.png"
image BG bogwalk = "background/bogwalk.png"
image BG map = "background/maplayered.png"
image BG bstore = "background/bstore.png"
image BG school = "background/school.png"
image BG market = "background/market.png"
image BG ar = "background/arcades.png"
image BG st = "background/street.png"
image BG hw = "background/hallway.png"
image BG cr = "background/classroom.png"
image BG wc1 = "background/wc.png"
image BG wc2 = "background/wc2.png"
image BG wc3 = "background/wc3.png"
image BG schoolan = "background/schoolafternoon.png"
image BG 4 = "background/4.png"
image BG walksunset = "background/walksunset.png"
image BG nightdeck1 = "background/nightdeck1.png"
image BG nightdeck2 = "background/nightdeck2.png"
image BG nightdeck3 = "background/nightdeck3.png"
image BG escape = "background/dingy.png"
image BG shore = "background/shore_after.png"
image BG shore_sword = "background/shore_after_sword.png"
image BG streetpost = "background/streetpost.png"
image BG schoolpost = "background/schoolpost.png"
image BG dollcorner = "background/dollcorner.png"
image BG signcorner = "background/signcorner.png"
image BG nobook = "background/nobook.png"
image BG insidestore = "background/insidestore.png"

# Other characters images
image twohands = "ol_ two hands neutral.png"
image twohands angry = "ol_ two hands angry.png"
image twohands angry dark = "ol_ two hands angry dark.png"
image twohands angry flip = im.Flip("images/ol_ two hands angry.png", horizontal="True") # flipped image to run out left
image twohands angry dark flip = im.Flip("images/ol_ two hands angry dark.png", horizontal="True")
image twohands scared = "ol_ two hands scared.png"
image twohands scared dark = "ol_ two hands scared dark.png"
image twohands scared flip = im.Flip("images/ol_ two hands scared.png", horizontal="True") # flipped image to run out left
image twohands sweaty = "ol_ two hands sweaty.png"
image twohands sweaty dark = "ol_ two hands sweaty dark.png"

image flavio = "flavio neutral.png"
image flavio scared = "flavio horrified dark.png"

image lib = "Yoko.png"
image lib smile = "Yoko Giggly.png"

image captain = "captain.png"
image bartender = "bt1.png"
image mm = "momlady.png"
image ds = "3ds.png"
image crowd = "crowd.png"
image doll = "doll.png"

image sword = "sword1.png"
image sword swing = "sword2.png"
image tome = "tome.png"

image c = "Untitled.png"
image c flip = im.Flip("images/Untitled.png", horizontal="True")

image pirate1 = "pirate 1.png"
image pirate1 slash = "pirate 11.png"
image pirate2 = "pirate 2.png"
image pirate2 slash = "pirate 22.png"
image pirate3 = "pirate 3.png"
image pirate3 slash = "pirate 33.png"
image pirate4 = "pirate 4.png"
image pirate4 slash = "pirate 44.png"
image pirate5 = "pirate 5.png"
image pirate5 slash = "pirate 55.png"
image pirate6 = "pirate 6.png"
image pirate6 slash = "pirate 66.png"
image pirate7 = "pirate 7.png"
image pirate7 slash = "pirate 77.png"
image pirate8 = "pirate 8.png"
image pirate8 slash = "pirate 88.png"

# Menu Music
define config.game_menu_music = "music/BelowDeck.mp3"
# define config.main_menu_music

# colors used reference
# #2150E7 when your previous choice comes back
# #50A23B a good choice
# #f00 a bad choice

# The game starts here baby!
label start:

    # for a cursor
    define config.mouse = { }
    define config.mouse['default'] = [ ( "gui/arrow.png", 0, 0) ]

    # position name of character speaking
    define gui.name_xpos = 0.1
    define gui.name_ypos = .15
    define gui.name_xalign = 0.2
    define gui.name_yalign = 0.5

    # center dialogue in center of box
    define gui.dialogue_xpos = 0.5
    define gui.dialogue_text_xalign = 0.5

    # size of namebox on the left side of screen
    define gui.namebox_width = 800
    define gui.namebox_height = 100
    #define gui.namebox_borders = Borders(5, 5, 5, 5)

    # use of namebox
    define gui.namebox_borders = Borders(15, 7, 15, 7)
    define gui.namebox_tile = True

    jump act1_1
