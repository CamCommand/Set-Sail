# Cameron Drummond 2021

# Main characters
define MC = Character("[player_name]", dynamic=True, color="#990033")# Player Character
define Fi = Character('Fiona', color="#E44D1A")
define G = Character('Geraldine', color="#DFDABB")# Geraldine
define As = Character('Astrid', color="#F236BD")
define Be = Character('Behati', color="#5E0F60")
define Ma = Character('May', color="#0A4AF6")
define n = nvl_narrator# Narrator

# Minor characters
define th = Character('[pirate]', color="#000000", who_outlines=[ (1, "#FFFFFF") ])# Ol' Two Hands
define Cap = Character('Captain', color="#7F0505")# The Demonic Pirate Ricardo AKA Captain
define fla = Character('Flavio', color="#BB64F2")# sir Flavio
define woman = Character("[lib]",dynamic=True, color="#45F574")# Librarian
define cr = Character('Passerbys', dynamic=True, color="#000001", who_outlines=[ (1, "#FFFFFF") ])# crowd of people
define m = Character('Short Woman', color="#F263E2")# woman at market

# Affinity of main characters
default Fiona_affinity = 0
default G_affinity = 0
default Astrid_affinity = 0
default Behati_affinity = 0
default May_affinity = 0

# background images
image BG MC_room ="bedroom.png"
image BG deckview = "deckview.png"
image BG topdeck = "topdeck.png"
image BG black = "black.png"
image BG harbor = "harbortemp.png"
image BG map = "map.png"
image BG bstore = "bstore.png"
image BG school = "school_temp.jpg"
image BG market = "market_temp.jpg"

# Other characters images
image twohands = "TwoHands.png"
image captain = "captain.png"
image fla = "flavio.png"
image woman = "lady.png"

# default player name and identity
$ player_name = "Default Pirate Person"
$ player_identity = "nb"

$ lib = "Woman"# Woman you talk to becomes librarian

# The game starts here baby!

label start:
    jump act1_1
