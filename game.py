import pygame
import pytmx
import pyscroll
import Constant
import player
import time
import map
import interface

class Game():

    def __init__(self):

        # Creating Window
        window_size = (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
        self.screen_map = pygame.display.set_mode(window_size)
        self.screen_player = pygame.display.set_mode(window_size)
        pygame.display.set_caption("POEC Fantasy")

        # Player initialisation
        self.player = player.Player(5, 5, 5, 5, 5, ("", "", "", "", "", "", "", "", "", "", ""),
                                    {"head": "", "chest": "", "legs": "", "left hand": "", "right hand": ""},
                                    f"{Constant.PLAYER_PATH}Owlet.png", 3, 3)
        # map 3d iso
        # Initialisation
        self.loaded_map = map.Map(f"{Constant.MAPS}mapTest.xls", 10, 10)



    def handle_input(self): # get the pressed key
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_UP]:
            self.player.pos_y -= 1
        elif pressed[pygame.K_DOWN]:
            self.player.pos_y += 1
        elif pressed[pygame.K_LEFT]:
            self.player.pos_x -= 1
        elif pressed[pygame.K_RIGHT]:
            self.player.pos_x += 1


    def run(self):

        # Affichage de la map
        interface.print_map(self.loaded_map, self.screen_map)

        # game loop
        running = True
        while running:

            self.player.player_move(self.loaded_map, self.screen_map)
            # self.handle_input()
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()