﻿## This file contains options that can be changed to customize your game.
##
## Lines beginning with two '#' marks are comments, and you shouldn't uncomment
## them. Lines beginning with a single '#' mark are commented-out code, and you
## may want to uncomment them when appropriate.


## Basics ######################################################################

## A human-readable name of the game. This is used to set the default window
## title, and shows up in the interface and error reports.
##
## The _() surrounding the string marks it as eligible for translation.

define config.name = _("Set Sail")

## The version of the game.

define config.version = ".83"

## Determines if the title given above is shown on the main menu screen. Set
## this to False to hide the title.

define gui.show_name = True

## Text that is placed on the game's about screen. Place the text between the
## triple-quotes, and leave a blank line between paragraphs.

define gui.about = _p("""
In 2017, pirating hasn’t lost it’s vigor. You play through the eyes of the protagonist who’s the child of the scourge of Cuba’s northern water, {i}The Demonic Pirate Ricardo{/i}.  \n
Quickly docked in Florida for supplies, your ship receives a letter from the local high school asking if a representative (preferably the Captain) of the Red Plague could give a talk about being a pirate to the Pirate Culture Club.  \n
The bitter old Captain throws the letter away in disgust. You, the player, have never been to a high school, only ever knowing the seas as your teacher.  \n
Wanting to teach the naive students why being a pirate is nothing to glorify, you decide to go and give a talk, prepping some of the worst stories imaginable to share.  \n
Once you arrive, you are greeted by the pleasantly hospitable e-board of the club. Their questions are more humbling and inquisitive than you anticipate.  \n
You end up having the most pleasant social experience of your life with the girls of the club, retailing fun pirating stories and inspiring some young pirates.  \n
A four year time skip occurs and you are at sea in a losing battle against a new pirate ship. Your father, who has never lost a battle and seemingly never cared about you that much, sends you off in the last escape dingy.  \n
You presume that your father and crew are all lost in battle. Washing up on a familiar shore line, you wander the mainland pondering your next move in between mourning your comrades.  \n
You then lock eyes through a cafe window with a group of familiar girls. The old members of the Pirate Culture Club are meeting for drinks and invite you to join them.  \n
The 2020 pandemic ruined each of their plans for the future and they have fallen on hard times. They ask of your adventures to inspire them, but you can only recall the recent bad news.  \n
One from the group recommends that you start from scratch and start your own crew. They could be your first recruits! Elated by the idea to have a new crew around the same age as them, you humbly ask them to join his pirate crew.  \n
Without anything else promising the girls a better future, they enthusiastically accept. Along with a strange but seemingly trustworthy woman who was eavesdropping, you'll get your affairs in order for a long journey ahead of you. Adventure, riches, and true friendship await when you set sail!
""")

# These extra centers are for showing four characters on screen at once

transform centerleft: # for girls
    xalign 0.35 yalign 1.0

transform centerright: # for girls
    xalign 0.65 yalign 1.0

transform leftbottom:
    xalign 0.001 yalign 1.5

transform bottom: # to show the tome
    xalign 0.68 yalign .55

transform ground:
    xalign 0.5 yalign 0.2

transform centerlefter:
    xalign 0.20 yalign 1.0

transform centerrighter:
    xalign 0.80 yalign 1.0

# This is for the bloody sword
transform sword:
    xalign 1.0 yalign 1.0

transform truecenter:
    xalign 0.5 yalign 0.5

transform truezoom:
    xalign 0.5 yalign 0.5
    ease 1.0 zoom 2.0

transform truestzoom:
    xalign 0.5 yalign 0.5
    ease 1.0 zoom 3.0

transform truestzoom2:
    xalign 0.5 yalign 0.5
    ease 1.0 zoom 4.0

define config.layers = [ 'master', 'transient', 'screens', 'overlay']

## A short name for the game used for executables and directories in the built
## distribution. This must be ASCII-only, and must not contain spaces, colons,
## or semicolons.

define build.name = "SetSail"


## Sounds and music ############################################################

## These three variables control which mixers are shown to the player by
## default. Setting one of these to False will hide the appropriate mixer.

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound to play.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Uncomment the following line to set an audio file that will be played while
## the player is at the main menu. This file will continue playing into the
## game, until it is stopped or another file is played.

define config.main_menu_music = "music/waves.ogg"

## Transitions #################################################################
##
## These variables set transitions that are used when certain events occur.
## Each variable should be set to a transition, or None to indicate that no
## transition should be used.

## Entering or exiting the game menu.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Between screens of the game menu.

define config.intra_transition = dissolve


## A transition that is used after a game has been loaded.

define config.after_load_transition = None


## Used when entering the main menu after the game has ended.

define config.end_game_transition = None


## A variable to set the transition used when the game starts does not exist.
## Instead, use a with statement after showing the initial scene.


## Window management ###########################################################
##
## This controls when the dialogue window is displayed. If "show", it is always
## displayed. If "hide", it is only displayed when dialogue is present. If
## "auto", the window is hidden before scene statements and shown again once
## dialogue is displayed.
##
## After the game has started, this can be changed with the "window show",
## "window hide", and "window auto" statements.

define config.window = "auto"


## Transitions used to show and hide the dialogue window

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Preference defaults #########################################################

## Controls the default text speed. The default, 0, is infinite, while any other
## number is the number of characters per second to type out.

default preferences.text_cps = 50


## The default auto-forward delay. Larger numbers lead to longer waits, with 0
## to 30 being the valid range.

default preferences.afm_time = 15


## Save directory ##############################################################
##
## Controls the platform-specific place Ren'Py will place the save files for
## this game. The save files will be placed in:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## This generally should not be changed, and if it is, should always be a
## literal string, not an expression.

define config.save_directory = "SetSail_save_directory"


## Icon ########################################################################
##
## The icon displayed on the taskbar or dock.

define config.window_icon = "gui/setSailTemp.png"


## Build configuration #########################################################
##
## This section controls how Ren'Py turns your project into distribution files.

init python:

    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base directory,
    ## with and without a leading /. If multiple patterns match, the first is
    ## used.
    ##
    ## In a pattern:
    ##
    ## / is the directory separator.
    ##
    ## * matches all characters, except the directory separator.
    ##
    ## ** matches all characters, including the directory separator.
    ##
    ## For example, "*.txt" matches txt files in the base directory, "game/
    ## **.ogg" matches ogg files in the game directory or any of its
    ## subdirectories, and "**.psd" matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app build,
    ## so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')


## A Google Play license key is required to download expansion files and perform
## in-app purchases. It can be found on the "Services & APIs" page of the Google
## Play developer console.

# define build.google_play_key = "..."


## The username and project name associated with an itch.io project, separated
## by a slash.

# define build.itch_project = "renpytom/test-project"
