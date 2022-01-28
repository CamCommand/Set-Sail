# Cameron Drummond 2021-2022
screen pirate_fight1_0:

    imagebutton:
        xpos 0.55
        ypos 0.3
        auto "gui/button/x_%s.png"
        action Jump("pirate_fight1")# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.45
        ypos 0.4
        auto "gui/button/x_%s.png"
        action Jump("pirate_fight1_re")
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.5
        ypos 0.6
        auto "gui/button/x_%s.png"
        action Jump("pirate_fight1_re")
        hovered [Play("effect", "audio/swordclick.mp3")]

# 1st pirate alone in fight 2
screen pirate_fight2_0:

    imagebutton:
        xpos 0.52
        ypos 0.34
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate1_x", 1), Jump("pirate_fight2_1")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.42
        ypos 0.44
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate1_x", 3), Jump("pirate_fight2_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.48
        ypos 0.64
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate1_x", 3), Jump("pirate_fight2_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

# both pirates in alive fight 2
screen pirate_fight2_1:

# pirate 1

    imagebutton:
        xpos 0.52
        ypos 0.34
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate1_x", 1), Jump("pirate_fight2_1")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.42
        ypos 0.44
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate1_x", 3), Jump("pirate_fight2_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.48
        ypos 0.64
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate1_x", 3), Jump("pirate_fight2_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

# pirate 2

    imagebutton:
        xpos 0.14
        ypos 0.34
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate2_x", 3),Jump("pirate_fight2_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.02
        ypos 0.44
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate2_x", 3),Jump("pirate_fight2_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.10
        ypos 0.60
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate2_x", 1), Jump("pirate_fight2_2")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]


screen pirate_fight2_2:

# second pirate in 2nd fight

    imagebutton:
        xpos 0.51
        ypos 0.30
        auto "gui/button/x_%s.png"
        action Jump("pirate_fight2_re")
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.40
        ypos 0.40
        auto "gui/button/x_%s.png"
        action Jump("pirate_fight2_re")
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.45
        ypos 0.60
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate2_x", 1), Jump("pirate_fight2_2")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

screen pirate_fight3_0:

    imagebutton:
        xpos 0.51
        ypos 0.30
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate3_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.42
        ypos 0.40
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate3_x", 1), Jump("pirate_fight3_1")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.46
        ypos 0.58
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate3_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

screen pirate_fight3_1:

    # 1st pirate in 3rd fight
    imagebutton:
        xpos 0.51
        ypos 0.30
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate3_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.42
        ypos 0.40
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate3_x", 1), Jump("pirate_fight3_1")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.46
        ypos 0.58
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate3_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

# 2nd pirate in 3rd fight
    imagebutton:
        xpos 0.14
        ypos 0.34
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate4_x", 3),Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.04
        ypos 0.44
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate4_x", 3),Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.10
        ypos 0.65
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate4_x", 1), Jump("pirate_fight3_2")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

screen pirate_fight3_2:

# 1st pirate in 3rd fight
    imagebutton:
        xpos 0.51
        ypos 0.30
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate3_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.42
        ypos 0.40
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate3_x", 1), Jump("pirate_fight3_1")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.46
        ypos 0.58
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate3_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

# 2nd pirate in 3rd fight
    imagebutton:
        xpos 0.14
        ypos 0.34
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate4_x", 3),Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.04
        ypos 0.44
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate4_x", 3),Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.10
        ypos 0.65
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate4_x", 1), Jump("pirate_fight3_2")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

# 3rd pirate in 3rd fight
    imagebutton:
        xpos 0.72
        ypos 0.30
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate5_x", 1), Jump("pirate_fight3_3")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.60
        ypos 0.40
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate5_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.69
        ypos 0.58
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate5_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

screen pirate_fight3_3:

# 2nd pirate in 3rd fight
    imagebutton:
        xpos 0.14
        ypos 0.34
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate4_x", 3),Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.04
        ypos 0.44
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate4_x", 3),Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.10
        ypos 0.65
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate4_x", 1), Jump("pirate_fight3_2")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

# 3rd pirate in 3rd fight
    imagebutton:
        xpos 0.72
        ypos 0.30
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate5_x", 1), Jump("pirate_fight3_3")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.60
        ypos 0.40
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate5_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.69
        ypos 0.58
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate5_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

screen pirate_fight3_4:

# 2nd pirate in 3rd fight
    imagebutton:
        xpos 0.14
        ypos 0.34
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate4_x", 3),Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.04
        ypos 0.44
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate4_x", 3),Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.10
        ypos 0.65
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate4_x", 1), Jump("pirate_fight3_2")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

screen pirate_fight3_5:

# 3rd pirate in 3rd fight
    imagebutton:
        xpos 0.72
        ypos 0.30
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate5_x", 1), Jump("pirate_fight3_3")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.60
        ypos 0.40
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate5_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.69
        ypos 0.58
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate5_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

screen pirate_fight3_6:

    # 1st pirate in 3rd fight
    imagebutton:
        xpos 0.51
        ypos 0.30
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate3_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.42
        ypos 0.40
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate3_x", 1), Jump("pirate_fight3_1")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.46
        ypos 0.58
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate3_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

# 3rd pirate in 3rd fight
    imagebutton:
        xpos 0.72
        ypos 0.30
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate5_x", 1), Jump("pirate_fight3_3")]# correct
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.60
        ypos 0.40
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate5_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]

    imagebutton:
        xpos 0.69
        ypos 0.58
        auto "gui/button/x_%s.png"
        action [SetVariable("pirate5_x", 3), Jump("pirate_fight3_re")]
        hovered [Play("effect", "audio/swordclick.mp3")]
