import pygame
import pytmx
import pyscroll
import Constant
import player
import time
import map
import interface
import item

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

        # Item creation
        self.item_list = []
        self.item = item.Item(1, True, "Axe", "right hand", 2, 0, 0, 0, 0, 0)
        self.item_list.append(self.item)
        self.item = item.Item(2, True, "Magic Sword", "right hand", 1, 0, 2, 0, 0, 0)
        self.item_list.append(self.item)
        self.item = item.Item(3, True, "Wooden Shield", "left hand", 0, 0, 0, 1, 0, 0)
        self.item_list.append(self.item)

        self.item.get_item_id(2, self.item_list)

        # Player initialisation
        self.player_list = []
        player_temp = None
        self.player = player.Player("Owlet", 5, 50, 5, 5, 5, ("", "", "", "", "", "", "", "", "", "", ""),
                                    {"head": "", "chest": "", "legs": "", "left hand": 3, "right hand": 2},
                                    f"{Constant.PLAYER_PATH}Owlet.png", 3, 3)
        self.get_mod_from_player(self.player)
        self.player_list.append(self.player)
        player_s_cell = self.loaded_map.get_cell_by_xy(self.player.pos_x, self.player.pos_y)
        player_s_cell.occuped_by = self.player
        self.player2 = player.Player("Cat", 5, 40, 6, 4, 5, ("", "", "", "", "", "", "", "", "", "", ""),
                                    {"head": "", "chest": "", "legs": "", "left hand": "", "right hand": 1},
                                    f"{Constant.PLAYER_PATH}cat.png", 3, 4)
        self.get_mod_from_player(self.player2)
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
                player.is_active = True
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
                            player.is_active = False
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

    def get_id_equiped_from_player(self, player) -> list:
        equiped_ids_stuff_list = []
        for ids in player.equiped_stuff.items():
            if ids[1] != "":
                equiped_ids_stuff_list.append(ids[1])
        return equiped_ids_stuff_list

    def get_items_from_ids_list(self, list) -> list:
        equiped_stuff_list = []
        n = len(list)
        for id_item in range(n):
            equiped_stuff_list.append(self.item.get_item_id(list[id_item], self.item_list))
        return equiped_stuff_list

    def stat_with_mods(self, equiped_stuff_list, player):
        n = len(equiped_stuff_list)
        for item in range(n):
            print(equiped_stuff_list[item])
            player.strength_mod += equiped_stuff_list[item].strength_mod
            player.speed_mod += equiped_stuff_list[item].speed_mod
            player.const_mod += equiped_stuff_list[item].const_mod
            player.life_mod += equiped_stuff_list[item].life_mod

    def get_mod_from_player(self, player):
        self.id_list = self.get_id_equiped_from_player(player)
        self.stuff_list = self.get_items_from_ids_list(self.id_list)
        self.stat_with_mods(self.stuff_list, player)


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
