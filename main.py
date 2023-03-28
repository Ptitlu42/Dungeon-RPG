# Import
import pygame as pygame
import Constant
import map
import interface
import player
# import importlib
# battlefield = importlib.import_module('maps/battlefield_map.py')

# Initialisation map
loaded_map = map.load_map("maps/mapTest.xls", 10, 10)
# map_loaded = battlefield.Battlefield()
# loaded_map = map.load_map2(map_loaded)

# Player initialisation
player = player.Player(5, 5, 5, 5, 5, ("", "", "", "", "", "", "", "", "", "", ""),
                       {"head": "", "chest": "", "legs": "", "left hand": "", "right hand": ""},
                       f"{Constant.PLAYER_PATH}Owlet.png", 1, 1)

# Pygame initialisation
pygame.init()

# Creating Window
window_size = (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("POEC Fantasy")


# Cleaning screen
screen.fill(Constant.BLACK)

# Affichage de la map
interface.print_map(loaded_map, screen)
interface.print_player(player, screen)


running = True
while running:
    player.player_move(loaded_map, screen)
    pygame.event.wait()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

            