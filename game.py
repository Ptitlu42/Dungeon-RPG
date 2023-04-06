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

        # map 3d iso instanciation
        self.loaded_map = map.Map(f"{Constant.MAPS}mapTest.xls")

        # Player initialisation
        self.player_list = []
        player_temp = None
        self.player = player.Player(5, 5, 5, 5, 5, ("", "", "", "", "", "", "", "", "", "", ""),
                                    {"head": "", "chest": "", "legs": "", "left hand": "", "right hand": ""},
                                    f"{Constant.PLAYER_PATH}Owlet.png", 3, 3)
        self.player_list.append(self.player)
        player_s_cell = self.loaded_map.get_cell_by_xy(self.player.pos_x, self.player.pos_y)
        player_s_cell.occuped_by = self.player
        self.player2 = player.Player(5, 5, 6, 4, 5, ("", "", "", "", "", "", "", "", "", "", ""),
                                    {"head": "", "chest": "", "legs": "", "left hand": "", "right hand": ""},
                                    f"{Constant.PLAYER_PATH}cat.png", 3, 4)
        self.player_list.append(self.player2)
        player2_s_cell = self.loaded_map.get_cell_by_xy(self.player2.pos_x, self.player2.pos_y)
        player2_s_cell.occuped_by = self.player2

        print(self.player_list[0])

        length = len(self.player_list)
        for j in range(length) :
            for i in range (0, length-j-1) :
                if self.player_list[i].speed < self.player_list[i+1].speed :
                    player_temp = self.player_list[i]
                    self.player_list[i] = self.player_list[i+1]
                    self.player_list[i + 1] = player_temp

        print(self.player_list[0])


    def turn(self):

        # game loop
        running = True
        while running:
            for player in self.player_list:
                turn_is_on = True
                player.actual_point = player.action_point
                print(player)
                self.interface.print_map(self.loaded_map, self.screen_map, player, self)

                while turn_is_on :

                    # Get mouse position
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    # Get mouse click
                    left_click, center_click, right_click = (pygame.mouse.get_pressed())
                    # Attribute action
                    if left_click:
                        print(self.interface.end_button_zone)
                        print(mouse_x,"+",mouse_y)
                        # if click on move button
                        if self.interface.move_button_zone.collidepoint(mouse_x, mouse_y):
                            player.action_move = True
                            player.action_melee = False
                            player.action_ranged = False
                        # if click on melee button
                        if self.interface.melee_button_zone.collidepoint(mouse_x, mouse_y):
                            player.action_move = False
                            player.action_melee = True
                            player.action_ranged = False
                        # if click on ranged button
                        if self.interface.ranged_button_zone.collidepoint(mouse_x, mouse_y):
                            player.action_move = False
                            player.action_melee = False
                            player.action_ranged = True
                        # if click on end button
                        if self.interface.end_button_zone.collidepoint(mouse_x, mouse_y):
                            player.action_move = False
                            player.action_melee = False
                            player.action_ranged = False
                            turn_is_on = False
                            time.sleep(0.2)
                            self.interface.print_map(self.loaded_map, self.screen_map, player, self)

                            for player_print in self.player_list:
                                self.interface.print_player(player_print, self.screen_map )
                    # self.handle_input()
                    if player.action_move:
                        player.player_move(self.loaded_map, self.screen_map, self.interface, self)
                    if player.action_melee:
                        player.player_melee(self.loaded_map, self.screen_map, self.interface, self)
                    if player.action_ranged:
                        player.player_ranged(self.loaded_map, self.screen_map, self.interface, self)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()



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
        self.interface.print_map(self.loaded_map, self.screen_map, self.player, self)
        self.turn()
