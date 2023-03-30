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
        self.screen = pygame.display.set_mode(window_size)
        pygame.display.set_caption("POEC Fantasy")

        # map 3d iso
        # Initialisation map
        self.loaded_map = map.load_map(f"{Constant.MAPS}mapTest.xls", 10, 10)


        '''# map top down
        # loading map
        tmx_data = pytmx.util_pygame.load_pygame(f'{Constant.MAPS}test_map_tiled.tmx')
        map_data = pyscroll.data.TiledMapData(tmx_data)
        map_layer = pyscroll.orthographic.BufferedRenderer(map_data, self.screen.get_size())
        map_layer.zoom = 1.5'''

        # Player initialisation
        self.player = player.Player(5, 5, 5, 5, 5, ("", "", "", "", "", "", "", "", "", "", ""),
                                    {"head": "", "chest": "", "legs": "", "left hand": "", "right hand": ""},
                                    f"{Constant.PLAYER_PATH}Owlet.png", 3, 3)

        '''#drawing map
        self.group = pyscroll.PyscrollGroup(map_layer=map_layer, default_layer=1)
        self.group.add(self.player)'''

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
        interface.print_map(self.loaded_map, self.screen)

        # game loop
        running = True
        while running:
            self.player.player_move(self.loaded_map, self.screen)
            # self.handle_input()
            '''self.group.update()
            self.group.center(self.player.rect.center) # center the view on the player
            self.group.draw(self.screen)'''
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()