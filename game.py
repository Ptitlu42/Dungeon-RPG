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
        self.interface = interface.Interface()


        pygame.display.set_caption("POEC Fantasy")

        # Player initialisation
        self.player = player.Player(5, 5, 5, 5, 5, ("", "", "", "", "", "", "", "", "", "", ""),
                                    {"head": "", "chest": "", "legs": "", "left hand": "", "right hand": ""},
                                    f"{Constant.PLAYER_PATH}Owlet.png", 3, 3)
        # map 3d iso
        # Initialisation
        self.loaded_map = map.Map(f"{Constant.MAPS}mapTest.xls")



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
        self.interface.print_map(self.loaded_map, self.screen_map, self.player)
        self.interface.print_player(self.player, self.screen_map)

        # game loop
        running = True
        while running:

            # Get mouse position
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # Get mouse click
            left_click, center_click, right_click = (pygame.mouse.get_pressed())
            # Attribute action
            if left_click:
                # if click on move button
                if self.interface.move_button_zone.collidepoint(mouse_x, mouse_y):
                    self.player.action_move = True
                    self.player.action_melee = False
                    self.player.action_ranged = False
                # if click on melee button
                if self.interface.melee_button_zone.collidepoint(mouse_x, mouse_y):
                    self.player.player_melee(self.loaded_map, self.screen_map, self.interface)
                # if click on ranged button
                if self.interface.ranged_button_zone.collidepoint(mouse_x, mouse_y):
                    self.player.player_ranged(self.loaded_map, self.screen_map, self.interface)
            # self.handle_input()
            if self.player.action_move:
                self.player.player_move(self.loaded_map, self.screen_map, self.interface)



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()