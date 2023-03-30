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
    game.run()



'''# Cleaning screen
screen.fill(Constant.BLACK)

# Affichage de la map
interface.print_map(loaded_map, screen)
interface.print_player(player, screen)'''
