import time

import Constant
import item
import player
import map
import pygame
import interface


class Battle_mode:
    def __init__(self, map_to_load, player_list):
        self.main_button_zone = None
        window_size = (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
        self.screen_map = pygame.display.set_mode(window_size)
        #self.screen_player = pygame.display.set_mode(window_size)
        self.interface = interface.Interface()
        self.player_list = player_list

        # map 3d iso instanciation
        self.loaded_map = map.Map(map_to_load)

        # Item creation
        self.item_list = []
        self.item = item.Item(1, True, "Axe", "right hand", 2, 0, 0, 0, 0, 0, 1, 0)
        self.item_list.append(self.item)
        self.item = item.Item(2, True, "Magic Sword", "right hand", 1, 0, 2, 0, 0, 0, 1, 0)
        self.item_list.append(self.item)
        self.item = item.Item(3, True, "Wooden Shield", "left hand", 0, 0, 0, 1, 0, 0, 0, 0)
        self.item_list.append(self.item)
        self.item = item.Item(4, True, "Bow", "right hand", 0, 0, 0, 0, 0, 0, 4, 1)
        self.item_list.append(self.item)

        for players in self.player_list:
            self.get_mod_from_player(players)
            player_s_cell = self.loaded_map.get_cell_by_xy(players.pos_x, players.pos_y)
            player_s_cell.occuped_by = players

    def victory(self):
        victory = pygame.image.load(f"{Constant.BUTTONS}victory.png")
        victory_redim = pygame.transform.scale(victory,
                                               (Constant.SCREEN_WIDTH - 2, Constant.SCREEN_HEIGHT / 4))
        self.screen_map.blit(victory_redim,
                             (Constant.SCREEN_WIDTH / 2 - victory_redim.get_width() / 2, Constant.SCREEN_HEIGHT / 4))

        for players in self.player_list:
            if players.is_active:
                police = pygame.font.Font(f"{Constant.FONT}IMMORTAL.ttf", 30)
                txt_name = police.render((players.name), True, Constant.BLACK)
                self.screen_map.blit(txt_name, (Constant.SCREEN_WIDTH / 2, Constant.SCREEN_HEIGHT / 2))

        main = pygame.image.load(f"{Constant.BUTTONS}main_menu.png")
        main_redim = pygame.transform.scale(main,
                                            (Constant.SCREEN_WIDTH / 3, Constant.SCREEN_HEIGHT / 4))
        self.screen_map.blit(main_redim,
                             (Constant.SCREEN_WIDTH / 2 - main_redim.get_width() / 2, 3 * Constant.SCREEN_HEIGHT / 4))
        self.main_button_zone = pygame.Rect(Constant.SCREEN_WIDTH / 2 - main_redim.get_width() / 2,
                                            3 * Constant.SCREEN_HEIGHT / 4, Constant.SCREEN_WIDTH / 3,
                                            Constant.SCREEN_HEIGHT / 4)

        pygame.display.flip()
        waiting = True

        time.sleep(5)
        """while waiting:
            mouse_x, mouse_y = (0, 0)
            left_click, center_click, right_click = (pygame.mouse.get_pressed())
            if left_click:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if self.main_button_zone.collidepoint(mouse_x, mouse_y):
                    print("in return")
                    waiting = False"""
        return None

    def turn(self):

        # game loop
        running = True
        while running:
            for player in self.player_list:

                if player.life_mod > 0:
                    player.is_active = True
                    turn_is_on = True
                    player.actual_point = player.action_point
                    self.interface.print_map(self.loaded_map, self.screen_map, player, self)

                    while turn_is_on:

                        # Get mouse position
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        # Get mouse click
                        left_click, center_click, right_click = (pygame.mouse.get_pressed())
                        # Attribute action
                        if left_click:
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
                                    self.interface.print_player(player_print, self.screen_map)
                        # self.handle_input()
                        if player.action_move:
                            player.player_move(self.loaded_map, self.screen_map, self.interface, self)
                        if player.action_melee:
                            player.player_melee(self.loaded_map, self.screen_map, self.interface, self)
                        if player.action_ranged:
                            player.player_ranged(self.loaded_map, self.screen_map, self.interface, self)

                        dead_player = []
                        for players in self.player_list:
                            if players.life_mod <= 0:
                                dead_player.append(players)
                        if len(dead_player) == (len(self.player_list) - 1):
                            #self.victory()
                            return None

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
            actual_item = self.item.get_item_id(list[id_item], self.item_list)
            equiped_stuff_list.append(actual_item)
        return equiped_stuff_list

    def stat_with_mods(self, equiped_stuff_list, player):
        n = len(equiped_stuff_list)
        for item in range(n):
            if equiped_stuff_list[item]:
                player.strength_mod += equiped_stuff_list[item].strength_mod
                player.speed_mod += equiped_stuff_list[item].speed_mod
                player.const_mod += equiped_stuff_list[item].const_mod
                player.life_mod += equiped_stuff_list[item].life_mod

    def get_mod_from_player(self, player):
        self.id_list = self.get_id_equiped_from_player(player)
        self.stuff_list = self.get_items_from_ids_list(self.id_list)
        self.stat_with_mods(self.stuff_list, player)

