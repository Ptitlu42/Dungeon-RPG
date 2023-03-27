# Import
import pygame as pygame
import Constant
import map
import interface

# Initialisation map
loaded_map = map.load_map("maps/mapTest.xls", 10, 10)

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


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            