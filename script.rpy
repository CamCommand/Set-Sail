# Cameron Drummond 2021-2022
# version 1.1.0
init python:

    player_identity_voice = "m"

    if renpy.windows:

        config.tts_voice = "Mark"

        if player_identity_voice == "m":

            config.tts_voice = "Mark"

        elif player_identity_voice == "f":

            config.tts_voice = "Zira"

        else:

            config.tts_voice = "David"

    elif renpy.macintosh:
        config.tts_voice = "Alex"
    elif renpy.linux:
        config.tts_voice = "english_rp"

    def music_loop():
        renpy.music.play("music/MainThemeEnd.ogg", channel="music")
        renpy.music.queue("music/BelowDeck.ogg", channel="music")
        renpy.music.queue("music/PirateTimes.ogg", channel="music")
        renpy.music.queue("music/SchoolSucks.ogg", channel="music")

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

    def Crashsound_test(event, **kwargs):# noise to play when everyone yells
        if event == "show":
            renpy.music.play("audio/crash.mp3 ", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def hobo_voice(event, **kwargs):# voice for Doll
        if event == "show":
            renpy.music.play("audio/blip13.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    def crowd_voice(event, **kwargs):# voice for a crowd
        if event == "show":
            renpy.music.play("audio/blip14.ogg", channel="sound", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.music.stop(channel="sound")

    # Use this for sound effects bc voices play over them
    renpy.music.register_channel("effect","voice", loop = False, tight = True)

    # Registering Achievements here
    achievement.register("Cheeky Name")
    achievement.register("They Know")
    achievement.register("Do They Know?")
    achievement.register("Set Sail")
    achievement.register("Fluid", stat_max = 3)
    achievement.register("Book Worm", stat_max = 3)
    achievement.register("Book Worm Deluxe", stat_max = 7)
    achievement.register("G A M E R", stat_max = 4)
    achievement.register("Sticky Fingers", stat_max = 6)
    achievement.register("Quiet Time")
    achievement.register("Woman Respecter")
    achievement.register("Breathtaking Behati")
    achievement.register("G The Great")
    achievement.register("Fab Fiona")
    achievement.register("#1 Astrid Fan")
    achievement.register("Master Sword")
    achievement.register("Jane Doe", stat_max = 5)
    achievement.register("Your Own Medicine")
    achievement.register("Karen Along")

transform wiggle: # To shake the characters a little bit, use at
    linear 0.1 xoffset -5 yoffset 0
    linear 0.1 xoffset 7 yoffset 0
    linear 0.1 xoffset 5 yoffset 0
    linear 0.1 xoffset -7 yoffset 0
    linear 0.1 xoffset 0 yoffset 0

transform zoom: # zoom into dingy specifically in act1_4
    xalign 0.05 yalign 0.3
    ease 1.0 zoom 1.5
    pause 2.0

transform redo: # return from any zoom
    xalign 0.5 yalign 0.5
    ease 1.0 zoom 1.0

transform redochar: # zooming out of May's oversteps
    ease 1.0 zoom 1.0 yalign 1.0

transform zoom_may: # zooming in for May getting flirty
    ease 1.0 zoom 1.3 yalign 0.3

transform zoomer_may:
    ease 0.6 zoom 3.0 yalign 0.5

define whiteflash = Fade(.95, 0.0, .55, color="#fff")        # for emerging topside
define flash = Fade(.15, 0.0, .25, color="#fff")             # for flashy sword effect
define flash_lighting = Fade(.15, 0.0, .25, color="#AFDBF2") # for flashy lighting effect
define deathflash = Fade(.15, 0.0, .25, color="#F25555")     # for when character dies
define slowfade = Dissolve(20)                               # for fading out in death
define delete = Fade(.11, 0.0, .25, color="#0E041F")

screen game_over_screen: # Game over screen

    vbox:

        xalign 0.5
        yalign 0.5
        textbutton _("\n\n\n\n   Return to Main Menu") action Return()

# Main characters
define mc = Character("[player_name]", dynamic=True, color="#990033", callback=voice)                   # Player Character
define f = Character('Fiona', color="#d1c1ff", callback=fiona_voice, who_outlines=[ (1, "#000000")])    # Fiona
define g = Character('Geraldine', color="#2ef2f4", callback=g_voice, who_outlines=[ (1, "#000000")])    # Geraldine
define a = Character('Astrid', color="#c83d32", callback=astrid_voice, who_outlines=[ (1, "#FFFFFF")])  # Astird
define b = Character('Behati', color="#ffcb00", callback=b_voice, who_outlines=[ (1, "#000000")])       # Behati
define m = Character('May', color="#ffc77f", callback=may_voice, who_outlines=[ (1, "#000000")])        # May
define n = nvl_narrator                                                                                 # Narrator
define ev = Character('Everyone', color="#000000", callback=Crashsound_test)                            # Everyone at once

# Main charcter images
image may = "may.png"
image may flip = im.Flip("images/may.png", horizontal="True")
image may smug = "may smug.png"
image may smug flip = im.Flip("images/may smug.png", horizontal = "True")
image may smile = "may smile.png"
image may smile flip = im.Flip("images/may smile.png", horizontal = "True")
image may sad = "may sad.png"
image may sad flip = im.Flip("images/may sad.png", horizontal = "True")
image may fl = "may fl.png"
image may fl flip = im.Flip("images/may fl.png", horizontal = "True")

image ge = "g.png"
image ge happy = "g happy.png"
image ge mad = "g mad.png"
image ge sad = "g sad.png"
image ge smug = "g smug.png"
image ge int = "g int.png"
image ge smile = "g smile.png"

image ge post = "g post.png"
image ge suppost = "g suppost.png"
image ge smugpost = "g smug post.png"
image ge madpost = "g mad post.png"
image ge smilepost = "g smile post.png"

image ast = "Astrid.png"
image ast conf = "Astrid conf.png"
image ast emb = "Astrid emb.png"
image ast happy = "Astrid happy.png"
image ast sad = "Astrid sad.png"
image ast smile = "Astrid smile.png"
image ast sup = "Astrid sup.png"

image ast post = "astrid post.png"
image ast sadpost = "astrid sad post.png"
image ast confpost = "astrid conf post.png"
image ast embpost = "astrid emb post.png"
image ast suppost = "astrid sup post.png"
image ast happypost = "astrid happy post.png"

image fiona = "Fiona.png"
image fiona angry = "Fiona angry.png"
image fiona laugh = "Fiona laugh.png"
image fiona sad = "Fiona sad.png"
image fiona frown = "Fiona frown.png"

image fi post = "fiona post.png"
image fi madpost = "fiona mad post.png"
image fi sadpost = "fi sad post.png"
image fi happypost = "fiona happy post.png"
image fi smilepost = "fiona smile post.png"

image be = "behati.png"
image be happy = "behati happy.png"
image be emb = "behati emb.png"
image be quiz = "behati quiz.png"
image be shocked= "behati shocked.png"
image be skeptical = "behati skeptical.png"

image be post = "be post.png"
image be confpost = "be conf post.png"
image be suppost = "be sup post.png"
image be happypost = "be happy post.png"
image be quizpost = "be quiz post.png"

# Minor characters
define th = Character('[pirate]', color="#000000", who_outlines=[ (1, "#FFFFFF") ], callback=twohands_voice)# ol' Two Hands
define Cap = Character('Captain', color="#000000", callback=caps_voice, who_outlines=[ (1, "#6d3536")])     # The Demonic Pirate Ricardo AKA Captain
define fla = Character('Flavio', color="#8957ba", callback=fl_voice)                                        # sir Flavio
define woman = Character('Woman', dynamic=True, color="#07BB01", callback=lib_voice)                        # bookstore clerk
define cr = Character('Passerbys', color="#000001", who_outlines=[ (1, "#FFFFFF") ], callback=crowd_voice)  # crowd of people
define ma = Character('Short Woman', color="#FF793B", callback=rot_voice)                                   # woman at market
define bt = Character('Bartender', color="#748DA3", callback=bar_voice)                                     # bartender at arcade
define jj = Character('JoeJoe', color = "#0015BC", callback=jj_voice)                                       # JoeJoe
define p = Character('Enemy Pirate', color = "#0015BC", callback=pirate_voice)                              # attacking Pirates
define dl = Character('Lady', color = "#740E86", callback=hobo_voice)                                       # Doll the hobo

# Affinity of main characters
define Fi_affinity = 0
define G_affinity = 0
define Astrid_affinity = 0
define Be_affinity = 0
define May_affinity = 0

# background images
image BG MC_room = "background/bedroom.png"
image BG gm = "background/gameover.png"
image BG deckview = "background/deckview.png"
image BG deckview2 = "background/deckview2.png"
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
image BG street_sign = "background/street_post.png"
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
image BG school2 = "background/school2.jpg"
image BG schoolpost = "background/schoolpost.png"
image BG dollcorner = "background/dollcorner.png"
image BG dollcorner2 = "background/dollcorner2.png"
image BG signcorner = "background/signcorner.png"
image BG nobook = "background/nobook.png"
image BG insidestore = "background/insidestore.png"
image BG insidestore2 = "background/insidestore2.png"
image BG insidestore3 = "background/insidestore3.png"
image BG marketpost = "background/marketpost.png"
image BG cafeoutside = "background/cafe.png"
image BG cafeoutside ast = "background/café ast.png"
image BG cafeoutside ast sup = "background/café ast sup.png"
image BG cafeinside = "background/cafeinside.png"

# Other characters images
image twohands = "ol_ two hands neutral.png"
image twohands angry = "ol_ two hands angry.png"
image twohands angry dark = "ol_ two hands angry dark.png"
image twohands angry flip = im.Flip("images/ol_ two hands angry.png", horizontal="True")  # flipped image to run out left
image twohands angry dark flip = im.Flip("images/ol_ two hands angry dark.png", horizontal="True")
image twohands scared = "ol_ two hands scared.png"
image twohands scared dark = "ol_ two hands scared dark.png"
image twohands scared flip = im.Flip("images/ol_ two hands scared.png", horizontal="True") # flipped image to run out left
image twohands sweaty = "ol_ two hands sweaty.png"
image twohands sweaty dark = "ol_ two hands sweaty dark.png"

image flavio = "flavio neutral.png"
image flavio flip = im.Flip("images/flavio neutral.png", horizontal = "True")
image flavio scared = "flavio horrified dark.png"

image lib = "Yoko.png"
image lib smile = "Yoko Giggly.png"

image cap = "Ricardo neutral.png"
image cap yelling = "Ricardo yelling.png"
image cap yelling bloody = "Ricardo yelling bloody.png"
image cap bloody = "Ricardo neutral bloody.png"

image bartender = "bartender.png"
image mm = "evil mom.png"
image ds = "3ds.png"
image shirt = "shirt.png"
image crowd = "crowd.png"

image doll = "doll.png"
image doll mad = "doll mad.png"

image sword = "sword1.png"
image sword swing = "sword2.png"
image tome = "tome.png"
image tome2 = "tomebig.png"

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

$ persistent.menuflag = 0       # for the changing main menu
$ persistent.menuflag_count = 0 # for knowing if the player has reached a menu before
$ persistent.flg = 0            # you know what this is for ;)


if persistent.menuflag == 1:

    $ gui.main_menu_background = "gui/main_menu_sword.png"

elif persistent.menuflag == 2:

    $ gui.main_menu_background = "gui/main_menu_end.png"

else:

    $ gui.main_menu_background = "gui/main_menu.png"

# colors used reference
# 50A23B a good choice
# f00 a bad choice

# The Start of Game
label start:

    define track0 = "music/MainThemeEnd.ogg"
    define track1 = "music/BelowDeck.ogg"
    define track2 = "music/PirateTimes.ogg"
    define track3 = "music/SchoolSucks.ogg"

    $ menuflag = False

    # change skip speed
    define config.skip_delay = 50

    # for the custom cursor
    define config.mouse = { }
    define config.mouse['default'] = [ ( "gui/arrow.png", 0, 0) ]
    define config.mouse['man'] = [ ( "gui/arrow1.png", 0, 0) ]
    define config.mouse['woman'] = [ ( "gui/arrow2.png", 0, 0) ]
    define config.mouse['nb'] = [ ( "gui/arrow3.png", 0, 0) ] 

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

    define sitting = Position(ypos = 1.25, yanchor = 'bottom')

    define lefter = Position(xpos= -0.1, xanchor = 'left')
    define righter = Position(xpos = 1.12, xanchor = 'right')
    define leftiem = Position(xpos= -0.06, xanchor = 'left')
    define leftist = Position(xpos= 0.11, xanchor = 'left')
    define rightwing = Position(xpos = 0.95, xanchor = 'right')

    jump act1_1
