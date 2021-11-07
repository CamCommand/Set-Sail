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
define woman = Character('Woman',dynamic=True, color="#07BB01")# Librarian
define cr = Character('Passerbys', color="#000001", who_outlines=[ (1, "#FFFFFF") ])# crowd of people
define m = Character('Short Woman', color="#F263E2")# woman at market
define bt = Character('Bartender', color="#748DA3")# bartender at arcade

# Affinity of main characters
default Fiona_affinity = 0
default G_affinity = 0
default Astrid_affinity = 0
default Behati_affinity = 0
default May_affinity = 0

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

# default player name and identity
$ player_name = "Default Pirate Person"
$ player_identity = "nb"

# The game starts here baby!

label start:
    jump act1_1
