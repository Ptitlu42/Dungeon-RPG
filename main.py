# Import
import pygame as pygame
import Constant
import map


# Initialisation map
loaded_map = map.load_map("maps/mapTest.xls", 10, 10)

# Pygame initialisation
pygame.init()

# Creating Window
window_size = (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("POEC Fantasy")



# Cleaning screen
screen.fill(Constant.WHITE)

#Affichage de la map
for case in loaded_map:
    print(f"Case sprite : {case.sprite} - Case deco : {case.deco}")
    sprite_floor = pygame.image.load(f"sprites/{case.sprite}")
    #sprite_redim = pygame.transform.scale(sprite_floor, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
    #screen.blit(sprite_redim, ((Constant.SPRITE_WIDTH / 2) * (case.pos_x + 1),
    #                           (Constant.SPRITE_HEIGHT / 2) * (case.pos_y + 1)))
    screen.blit(sprite_floor, (0, 0))
    if case.deco != "":
        sprite_deco = pygame.image.load(f"sprites/{case.deco}")
        sprite_redim = pygame.transform.scale(sprite_deco, (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT))
        screen.blit(sprite_redim, ((Constant.SPRITE_WIDTH / 2) * (case.pos_x + 1),
                                   (Constant.SPRITE_HEIGHT / 2) * (case.pos_y + 1) + 30))
        screen.blit(sprite_redim, (0, 0))



running = True
while running:
    sprite_floor = pygame.image.load(f"sprites/dirt1.png")
    screen.blit(sprite_floor, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            