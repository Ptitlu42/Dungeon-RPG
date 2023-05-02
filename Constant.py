from userinfo import screen_width
from userinfo import screen_height
import math

# Screen Constants
SCREEN_HEIGHT = screen_height
SCREEN_WIDTH = screen_width
"""SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1440"""
MAP_WIDTH = 800
MAP_HEIGHT = 600

# Button Constants
BUTTON_WIDTH = 200 * SCREEN_HEIGHT / 900
BUTTON_HEIGHT = 64 * SCREEN_HEIGHT / 900

# Sprites Constants
SPRITE_WIDTH = 64 * SCREEN_HEIGHT / 900
SPRITE_HEIGHT = 64 * SCREEN_HEIGHT / 900
SPRITE_CARACTER_HEIGHT = 64 * SCREEN_HEIGHT / 900
SPRITE_CARACTER_WIDTH = 64 * SCREEN_HEIGHT / 900

# Color Constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
TRANSP = (0, 0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Interface Constants
DISTANCE = 6
CIRCLE_RADIUS = math.sqrt(pow(32 * SCREEN_HEIGHT / 900, 2) * 2) / 2
MAP_CENTER_X = SPRITE_WIDTH * 8 - SPRITE_WIDTH / 2
MAP_CENTER_Y = SPRITE_HEIGHT * 5.5 - SPRITE_HEIGHT / 2

# Path
PLAYER_PATH = "sprites/caracters/player/"
MISC = "sprites/caracters/misc/"
BG = "sprites/background/"
FLOOR = "sprites/floor/"
DECO = "sprites/deco/"
MAPS = "maps/"
BUTTONS =  "sprites/buttons/"
FONT = "font/"
HIT_SOUNDS = "sfx/hit sound/"
FOOTSTEPS_SOUNDS = "sfx/footsteps/"
ARROW_SOUNDS = "sfx/arrow/"
SWING_SOUNDS = "sfx/swing/"
TITLE = "sprites/title/"

#INTERFACE CONSTANT
