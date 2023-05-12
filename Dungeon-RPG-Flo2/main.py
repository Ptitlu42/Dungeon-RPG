# Import
import pygame as pygame
import Constant
import map
import interface
import player
import game

# import importlib
# battlefield = importlib.import_module('maps/battlefield_map.py')


if __name__ == '__main__':
    # Pygame initialisation
    pygame.init()

    game = game.Game()
    print(game.loaded_map.actual_map)
    game.run()
