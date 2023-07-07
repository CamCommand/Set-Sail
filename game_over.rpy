# Cameron Drummond 2021-2022
# version 1.1.0
label game_over:

    show sword swing at sword with ease
    play effect "audio/sword_swing.mp3"
    show BG nightdeck2 with deathflash

    show sword at sword with ease
    mc "Uh no, I didn't get to save,"

    hide sword with dissolve

    mc "Father, forgive me..."

    $ quick_menu = False
    $ renpy.block_rollback()

    stop music fadeout 3.0
    play music "audio/shore.ogg" fadein 1.0

    scene BG black with fade
    scene BG gm with dissolve
    call screen game_over_screen
    return
