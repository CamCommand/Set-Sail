# The script of the game goes in this file.

# Main characters in game definitions
define MC = Character("[player_name]", dynamic=True, color="#990033")# Player Character
define Fi = Character('Fiona', color="#E44D1A")
define G = Character('Geraldine', color="#DFDABB")# Geraldine
define As = Character('Astrid', color="#F236BD")
define Be = Character('Behati', color="#5E0F60")
define Ma = Character('May', color="#0A4AF6")
define n = nvl_narrator# Narrator

# Minor characters in game definitions
define th = Character('[pirate]', color="#000000", who_outlines=[ (1, "#FFFFFF") ])# Ol' Two Hands
define Cap = Character('Captain', color="#7F0505")# The Demonic Pirate Ricardo AKA Captain
define fla = Character('Flavio', color="#BB64F2")# sir Flavio

# Affinity of main characters
default Fiona_affinity = 0
default G_affinity = 0
default Astrid_affinity = 0
default Behati_affinity = 0
default May_affinity = 0

image BG MC_room ="Minecraft_MC_room.png"
image BG deckview = "deckview.png"
image BG topdeck = "topdeck.png"
image BG black = "black.png"
image twohands = "TwoHands.png"
image captain = "captain.png"
image fla = "flavio.png"

$ player_name = "Default Pirate Person"
$ player_identity = "nb"

# The game starts here baby ;)

label start:
    jump act1_1
