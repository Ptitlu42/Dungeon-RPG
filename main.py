# Import
import pygame as pygame
import Constant
import map
import interface
from map import find_object_case

# Initialisation map
loaded_map = map.load_map("maps/mapTest2.xls")

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
            
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        return_result = find_object_case("maps/mapTest2.xls", "viking.png")
        if return_result:
            print("YES")
        else:
            print("NO")
        
        print("Le joueur a appuyé sur la flèche gauche")
        
    if keys[pygame.K_RIGHT]:
        print("Le joueur a appuyé sur la flèche droite")
        
    if keys[pygame.K_UP]:
        print("Le joueur a appuyé sur la flèche haut")
        
    if keys[pygame.K_DOWN]:
        print("Le joueur a appuyé sur la flèche bas")
    