# Import
import threading
import pygame as pygame
import game
import server

if __name__ == '__main__':
    # Pygame initialisation
    pygame.init()
    pygame.mixer.init()

    game = game.Game()
    game.run()
