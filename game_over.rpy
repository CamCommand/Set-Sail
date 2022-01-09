label game_over:

    show sword swing at sword with ease
    play effect "audio/sword_swing.mp3"
    show BG nightdeck2 with deathflash

    show sword at sword with ease
    mc "Uh no, I didn't get to save,"

    mc "Father, forgive me..."

    scene BG bogwalk
    with fade
    call screen game_over_screen
    return
