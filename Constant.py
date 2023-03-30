from userinfo import screen_width
from userinfo import screen_height

# Screen Constants
SCREEN_HEIGHT = screen_height
SCREEN_WIDTH = screen_width
MAP_WIDTH = 800
MAP_HEIGHT = 600

# Sprites Constants
SPRITE_WIDTH = 64
SPRITE_HEIGHT = 64
SPRITE_CARACTER_HEIGHT = 64
SPRITE_CARACTER_WIDTH = 64

# Color Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSP = (0, 0, 0, 0)
# Path
PLAYER_PATH = "sprites/caracters/player/"
PLAYER_TILES_PATH = "sprites/caracters/misc/"
BG = "sprites/background/"
DECO = "sprites/deco/"
MAPS = "maps/"


# Prompts pnj

PR_AGGRESSIVE = "Context: 'Tu es un méchant dans un jeux vidéo et un joueur viens te parler, improvise en étant aggressif et distant avec lui, voici son message:'"
PR_FRIENDLY = "Context: 'Tu es un gentil dans un jeux vidéo, et un joueur viens te parler, improvise en étant amical avec lui, à la fin tu dois lui donner la quète, voici son message:'"
DEBUG = "Ne te met pas à la place du joueur voici la quetes et le context: \n"
