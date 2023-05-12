# imports
import time

import Constant
import pygame
import math


class Interface():
    def __init__(self):
        self.move_button_zone = ""
        self.melee_button_zone = ""
        self.ranged_button_zone = ""
        self.end_button_zone = ""
        self.ranged_target_list = []
        self.up_button_zone = ""
        self.down_button_zone = ""
        self.left_button_zone = ""
        self.right_button_zone = ""
        self.player_active = None

    def print_map(self, map, screen, player, game):
        '''
        print the map in the window
        :param map:
        :param screen:
        :return:
        '''
        # background
        screen.fill(Constant.BLACK)
        background = pygame.image.load(f"{Constant.BG}scroll.png")
        bg_redim = pygame.transform.scale(background, (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT))
        screen.blit(bg_redim, (0, 0))



        player.player_can_go = {"left": False, "right": False, "up": False, "down": False}
        self.print_action_menu(screen, player, game)
        self.print_stat(screen, game)

        for pos_x in range(player.pos_x - Constant.DISTANCE, player.pos_x + Constant.DISTANCE + 1, 1):
            if 0 <= pos_x < map.cols:
                for pos_y in range(player.pos_y - Constant.DISTANCE, player.pos_y + Constant.DISTANCE + 1, 1):
                    if 0 <= pos_y < map.rows:
                        case = map.get_cell_by_xy(pos_x, pos_y)
                        cell_xy = (case.pos_x, case.pos_y)
                        cell = self.cell_xy_to_screen_xy(cell_xy, player)

                        if case.sprite != "":
                            sprite_floor = pygame.image.load(f"{Constant.FLOOR}{case.sprite}")
                            sprite_redim = pygame.transform.scale(sprite_floor,
                                                                  (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
                            screen.blit(sprite_redim, (cell[0], cell[1]))

        self.ranged_target_list = []
        if player.action_move:
            self.check_area(player.actual_point, player, map, screen)
        if player.action_melee:
            self.check_area(1, player, map, screen)
        if player.action_ranged:
            for active_player in game.player_list:
                if active_player.is_active:
                    weapon = game.item.get_item_id(active_player.equiped_stuff["right hand"], game.item_list)
                    self.check_area(weapon.range, player, map, screen)
        self.mouse_on_grid(screen, player)

        for pos_x in range(player.pos_x - Constant.DISTANCE, player.pos_x + Constant.DISTANCE + 1, 1):
            if 0 <= pos_x < map.cols:
                for pos_y in range(player.pos_y - Constant.DISTANCE, player.pos_y + Constant.DISTANCE + 1, 1):
                    if 0 <= pos_y < map.rows:
                        case = map.get_cell_by_xy(pos_x, pos_y)
                        cell_xy = (case.pos_x, case.pos_y)
                        cell = self.cell_xy_to_screen_xy(cell_xy, player)

                        if case.deco != "":
                            sprite_deco = pygame.image.load(f"{Constant.DECO}{case.deco}")
                            sprite_redim = pygame.transform.scale(sprite_deco,
                                                                  (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
                            screen.blit(sprite_redim, (cell[0], cell[1] - 10))

                        if case.occuped_by != "":
                            self.print_player(case.occuped_by, screen)

        pygame.display.flip()

    def print_player(self, player, screen):
        '''
        print the player on the right cell
        :param player:
        :param screen:
        :return:
        '''

        if self.player_active.name == player.name:
            if player.life_mod > 0 :
                coord = self.cell_xy_to_screen_xy((player.pos_x, player.pos_y), player)
                sprite_player = pygame.image.load(player.sprite)
                sprite_player_redim = pygame.transform.scale(sprite_player,
                                                             (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))
                screen.blit(sprite_player_redim, (coord[0], coord[1] - Constant.SPRITE_HEIGHT / 2))

                if player.is_active:
                    halo_player = pygame.image.load(f"{Constant.MISC}activeplayer.png")
                    halo_player_redim = pygame.transform.scale(halo_player,
                                                               (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))
                    screen.blit(halo_player_redim, (coord[0] + 2, coord[1] - Constant.SPRITE_HEIGHT / 3))

            else:
                coord = self.cell_xy_to_screen_xy((player.pos_x, player.pos_y), player)
                print(player.name, player.pos_x, player.pos_y)
                sprite_player = pygame.image.load(player.tombstone)
                sprite_player_redim = pygame.transform.scale(sprite_player,
                                                             (Constant.SPRITE_WIDTH / 2, Constant.SPRITE_CARACTER_HEIGHT / 2))
                screen.blit(sprite_player_redim, (coord[0] + Constant.SPRITE_WIDTH / 4, coord[1]))
        else:
            if player.life_mod > 0:
                coord = self.cell_xy_to_screen_xy((player.pos_x, player.pos_y), self.player_active)
                sprite_player = pygame.image.load(player.sprite)
                sprite_player_redim = pygame.transform.scale(sprite_player,
                                                             (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))
                screen.blit(sprite_player_redim, (coord[0], coord[1] - Constant.SPRITE_HEIGHT / 2))

                if player.is_active:
                    halo_player = pygame.image.load(f"{Constant.MISC}activeplayer.png")
                    halo_player_redim = pygame.transform.scale(halo_player,
                                                               (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))
                    screen.blit(halo_player_redim, (coord[0] + 2, coord[1] - 20))

            else:
                coord = self.cell_xy_to_screen_xy((player.pos_x, player.pos_y), self.player_active)
                sprite_player = pygame.image.load(player.tombstone)
                sprite_player_redim = pygame.transform.scale(sprite_player,
                                                             (Constant.SPRITE_WIDTH / 2, Constant.SPRITE_CARACTER_HEIGHT / 2))
                screen.blit(sprite_player_redim, (coord[0] + Constant.SPRITE_WIDTH / 4, coord[1]))

    def cell_xy_to_screen_xy(self, coord, player):
        """
        transform coord of a cell to print it on screen
        :param coord:
        :return: cell
        """
        pos_x = (Constant.SPRITE_WIDTH * 8) + (((coord[0] - player.pos_x) * Constant.SPRITE_WIDTH / 2) - (coord[1] - player.pos_y) * Constant.SPRITE_WIDTH / 2 - Constant.SPRITE_WIDTH / 2)
        pos_y = (Constant.SPRITE_HEIGHT * 5.5) + (((coord[1] - player.pos_y) * Constant.SPRITE_HEIGHT / 2 + (coord[0] - player.pos_x) * Constant.SPRITE_HEIGHT / 2) - Constant.SPRITE_HEIGHT / 2) - ((coord[1] - player.pos_y) * Constant.SPRITE_HEIGHT * 0.12 + (coord[0] - player.pos_x) * Constant.SPRITE_HEIGHT * 0.12)

        screen_xy = (pos_x, pos_y)
        return screen_xy

    def print_stat(self, screen, game):
        """
        print the stats of the player on the screen
        :param player:
        :param screen:
        :return:
        """
        pos_x = Constant.SCREEN_WIDTH / 50  + Constant.SPRITE_WIDTH
        pos_y = (Constant.SCREEN_HEIGHT - Constant.SPRITE_HEIGHT * 2)
        police = pygame.font.Font(f"{Constant.FONT}IMMORTAL.ttf", 30)
        length = len(game.player_list)
        for i in range(length):
            sprite_player = pygame.image.load(game.player_list[i].sprite)
            sprite_player_redim = pygame.transform.scale(sprite_player,
                                                         (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))
            screen.blit(sprite_player_redim, (i * Constant.SCREEN_WIDTH / 4, pos_y))
            txt_name = police.render((game.player_list[i].name), True, Constant.BLACK)
            txt_pv = police.render("Life : ", True, Constant.BLACK)
            val_pv = police.render(str(game.player_list[i].life_mod), True, Constant.BLACK)
            txt_strength = police.render("Strenght : ", True, Constant.BLACK)
            val_strength = police.render(str(game.player_list[i].strength_mod), True, Constant.BLACK)
            txt_const = police.render("Const : ", True, Constant.BLACK)
            val_const = police.render(str(game.player_list[i].const_mod), True, Constant.BLACK)
            screen.blit(txt_name, (i * Constant.SCREEN_WIDTH / 4 + Constant.SPRITE_WIDTH, pos_y))
            screen.blit(txt_pv, (i * Constant.SCREEN_WIDTH / 4 + Constant.SPRITE_WIDTH, pos_y + 25))
            screen.blit(val_pv, (i * Constant.SCREEN_WIDTH / 4 + 150 + Constant.SPRITE_WIDTH, pos_y + 25))
            screen.blit(txt_strength, (i * Constant.SCREEN_WIDTH / 4 + Constant.SPRITE_WIDTH, pos_y + 50))
            screen.blit(val_strength, (i * Constant.SCREEN_WIDTH / 4 + 150 + Constant.SPRITE_WIDTH, pos_y + 50))
            screen.blit(txt_const, (i * Constant.SCREEN_WIDTH / 4 + Constant.SPRITE_WIDTH, pos_y + 75))
            screen.blit(val_const, (i * Constant.SCREEN_WIDTH / 4 + 150 + Constant.SPRITE_WIDTH, pos_y + 75))

            i += 1

    def print_action_menu(self, screen, player, game):
        """
        print the action menu on the screen
        :param screen:
        :param player:
        :return:
        """
        pos_x = Constant.SCREEN_WIDTH - Constant.BUTTON_WIDTH - Constant.SPRITE_WIDTH
        pos_y = Constant.SPRITE_HEIGHT
        police = pygame.font.Font(f"{Constant.FONT}IMMORTAL.ttf", 30)
        active_player = police.render("Active player : ", True, Constant.BLACK)
        screen.blit(active_player, (pos_x, pos_y))

        # arrows
        arrow_up = pygame.image.load(f"{Constant.BUTTONS}arrow_up.png")
        arrow_up_redim = pygame.transform.scale(arrow_up, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
        screen.blit(arrow_up_redim, (Constant.SCREEN_WIDTH - Constant.SPRITE_WIDTH * 2.5, Constant.SPRITE_HEIGHT * 2))
        self.up_button_zone = pygame.Rect(Constant.SCREEN_WIDTH - Constant.SPRITE_WIDTH * 2.5, Constant.SPRITE_HEIGHT * 2,
                                          Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT)

        arrow_left = pygame.image.load(f"{Constant.BUTTONS}arrow_left.png")
        arrow_left_redim = pygame.transform.scale(arrow_left, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
        screen.blit(arrow_left_redim,
                    (Constant.SCREEN_WIDTH  - Constant.SPRITE_WIDTH * 3.5, Constant.SPRITE_HEIGHT * 2))
        self.left_button_zone = pygame.Rect(Constant.SCREEN_WIDTH  - Constant.SPRITE_WIDTH * 3.5, Constant.SPRITE_HEIGHT * 2,
                                            Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT)

        for active_player in game.player_list:

            if active_player.is_active:
                self.player_active = active_player
                coord = (Constant.SCREEN_WIDTH - Constant.SPRITE_WIDTH * 3, Constant.SPRITE_HEIGHT * 2.5)
                sprite_player = pygame.image.load(active_player.sprite)
                sprite_player_redim = pygame.transform.scale(sprite_player,
                                                             (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))
                screen.blit(sprite_player_redim, coord)

        arrow_right = pygame.image.load(f"{Constant.BUTTONS}arrow_right.png")
        arrow_right_redim = pygame.transform.scale(arrow_right, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
        screen.blit(arrow_right_redim, (Constant.SCREEN_WIDTH - Constant.SPRITE_WIDTH * 2.5, Constant.SPRITE_HEIGHT * 3))
        self.right_button_zone = pygame.Rect(Constant.SCREEN_WIDTH - Constant.SPRITE_WIDTH * 2.5, Constant.SPRITE_HEIGHT * 3,
                                             Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT)

        arrow_down = pygame.image.load(f"{Constant.BUTTONS}arrow_down.png")
        arrow_down_redim = pygame.transform.scale(arrow_down, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
        screen.blit(arrow_down_redim, (Constant.SCREEN_WIDTH - Constant.SPRITE_WIDTH * 3.5, Constant.SPRITE_HEIGHT * 3))
        self.down_button_zone = pygame.Rect(Constant.SCREEN_WIDTH - Constant.SPRITE_WIDTH * 3.5, Constant.SPRITE_HEIGHT * 3,
                                            Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT)

        for i in range(0, 4, 1):
            pos_x_button = Constant.SCREEN_WIDTH - Constant.BUTTON_WIDTH - Constant.SPRITE_WIDTH
            pos_y_button = (Constant.BUTTON_HEIGHT * 4) + (Constant.BUTTON_HEIGHT * i) + Constant.SPRITE_HEIGHT / 2

            if i == 0:
                if player.action_move:
                    sprite_button = pygame.image.load(f"{Constant.BUTTONS}movebuttonactive.png")
                    sprite_button_redim = pygame.transform.scale(sprite_button,
                                                                 (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
                else:
                    sprite_button = pygame.image.load(f"{Constant.BUTTONS}movebutton.png")
                    sprite_button_redim = pygame.transform.scale(sprite_button,
                                                                 (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
                self.move_button_zone = pygame.Rect(pos_x_button, pos_y_button, Constant.BUTTON_WIDTH,
                                                    Constant.BUTTON_HEIGHT)
                screen.blit(sprite_button_redim, (pos_x_button, pos_y_button))

            if i == 1:
                if player.action_melee:
                    sprite_button = pygame.image.load(f"{Constant.BUTTONS}meleebuttonactive.png")
                    sprite_button_redim = pygame.transform.scale(sprite_button,
                                                                 (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
                else:
                    sprite_button = pygame.image.load(f"{Constant.BUTTONS}meleebutton.png")
                    sprite_button_redim = pygame.transform.scale(sprite_button,
                                                                 (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
                self.melee_button_zone = pygame.Rect(pos_x_button, pos_y_button, Constant.BUTTON_WIDTH,
                                                     Constant.BUTTON_HEIGHT)
                screen.blit(sprite_button_redim, (pos_x_button, pos_y_button))

            if i == 2:
                if player.action_ranged:
                    sprite_button = pygame.image.load(f"{Constant.BUTTONS}rangedbuttonactive.png")
                    sprite_button_redim = pygame.transform.scale(sprite_button,
                                                                 (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
                else:
                    sprite_button = pygame.image.load(f"{Constant.BUTTONS}rangedbutton.png")
                    sprite_button_redim = pygame.transform.scale(sprite_button,
                                                                 (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
                self.ranged_button_zone = pygame.Rect(pos_x_button, pos_y_button, Constant.BUTTON_WIDTH,
                                                      Constant.BUTTON_HEIGHT)
                screen.blit(sprite_button_redim, (pos_x_button, pos_y_button))

            if i == 3:
                sprite_button = pygame.image.load(f"{Constant.BUTTONS}endbutton.png")
                sprite_button_redim = pygame.transform.scale(sprite_button,
                                                             (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
                self.end_button_zone = pygame.Rect(pos_x_button, pos_y_button, Constant.BUTTON_WIDTH,
                                                   Constant.BUTTON_HEIGHT)
                screen.blit(sprite_button_redim, (pos_x_button, pos_y_button))

            txt_pa = police.render("Points d'action : " + str(player.actual_point), True, Constant.BLACK)
            screen.blit(txt_pa, (Constant.SCREEN_WIDTH - Constant.BUTTON_WIDTH - Constant.SPRITE_WIDTH * 1.5,
                                 (Constant.BUTTON_HEIGHT * 9)))

    def set_player_can_move(self, player, pos):
        """
        Update the "player_can_move" attibute
        :param player:
        :param pos:
        :return:
        """

        if pos == [player.pos_x + 1, player.pos_y]:
            player.player_can_go["right"] = True
        elif pos == [player.pos_x, player.pos_y + 1]:
            player.player_can_go["down"] = True
        elif pos == [player.pos_x - 1, player.pos_y]:
            player.player_can_go["left"] = True
        elif pos == [player.pos_x, player.pos_y - 1]:
            player.player_can_go["up"] = True

    def check_area(self, range_area, player, map, screen):
        """
        check cells in an area
        :param range_area:
        :param player:
        :param map:
        :param screen:
        :return:
        """
        checked_cell = []
        ranged_target_list = []
        for x in range(0, range_area + 1, 1):
            for y in range(0, (range_area + 1 - x), 1):
                for xvar in [x, -x]:
                    for yvar in [y, -y]:
                        # list the cell

                        cell_already_checked = False
                        length = len(checked_cell)
                        for i in range(0, length, 1):
                            if checked_cell[i] == (xvar, yvar):
                                cell_already_checked = True

                        if not cell_already_checked:
                            checked_cell.append((xvar, yvar))
                            if 0 <= player.pos_x + xvar < map.cols and 0 <= player.pos_y + yvar < map.rows:
                                cell = map.get_cell_by_xy(player.pos_x + xvar, player.pos_y + yvar)

                                if player.action_move:
                                    if cell.deco == "" and (cell.occuped_by == "" or cell.occuped_by.life_mod <= 0) and cell.sprite != "water.png":
                                        # print the accessible PNG on the tile
                                        sprite_bluecell = pygame.image.load(f"{Constant.MISC}accessible.png")
                                        sprite_bluecell_redim = pygame.transform.scale(sprite_bluecell,
                                                                                       (Constant.SPRITE_WIDTH,
                                                                                        Constant.SPRITE_CARACTER_HEIGHT))
                                        cell_pos = self.cell_xy_to_screen_xy((cell.pos_x, cell.pos_y), player)
                                        screen.blit(sprite_bluecell_redim, cell_pos)
                                        self.set_player_can_move(player, [player.pos_x + xvar, player.pos_y + yvar])

                                if player.action_melee:
                                    if cell.occuped_by != "" and cell.occuped_by.name != player.name and cell.occuped_by.life_mod >= 0:
                                        # print the fightable PNG on the tile
                                        sprite_redcell = pygame.image.load(f"{Constant.MISC}fightable.png")
                                        sprite_redcell_redim = pygame.transform.scale(sprite_redcell,
                                                                                      (Constant.SPRITE_WIDTH,
                                                                                       Constant.SPRITE_CARACTER_HEIGHT))
                                        cell_pos = self.cell_xy_to_screen_xy((cell.pos_x, cell.pos_y), player)
                                        screen.blit(sprite_redcell_redim, cell_pos)
                                        self.set_player_can_move(player, [player.pos_x + xvar, player.pos_y + yvar])

                                if player.action_ranged:
                                    if cell.occuped_by != "" and cell.occuped_by.name != player.name and cell.occuped_by.life_mod >= 0:
                                        # print the fightable PNG on the tile
                                        sprite_redcell = pygame.image.load(f"{Constant.MISC}fightable.png")
                                        sprite_redcell_redim = pygame.transform.scale(sprite_redcell,
                                                                                      (Constant.SPRITE_WIDTH,
                                                                                       Constant.SPRITE_CARACTER_HEIGHT))
                                        cell_pos = self.cell_xy_to_screen_xy((cell.pos_x, cell.pos_y), player)
                                        screen.blit(sprite_redcell_redim, cell_pos)
                                        self.set_player_can_move(player, [player.pos_x + xvar, player.pos_y + yvar])
                                        self.ranged_target_list.append(cell.occuped_by)
                                        police = pygame.font.Font(f"{Constant.FONT}IMMORTAL.ttf", 20)
                                        target_number = police.render(str(len(self.ranged_target_list) - 1), True, Constant.BLACK)
                                        screen.blit(target_number, (cell_pos[0] + Constant.SPRITE_WIDTH / 2, cell_pos[1] + Constant.SPRITE_HEIGHT / 2))

    def mouse_on_grid(self, screen, player):
        """
        Check if the mouse is on the grid and place a white tile on the cell if so
        """
        mouse_x, mouse_y = pygame.mouse.get_pos()
        orig_x = (Constant.SPRITE_WIDTH * 8)
        orig_y = (Constant.SPRITE_HEIGHT * 5.5)
        delta_mouse_x = mouse_x - orig_x
        delta_mouse_y = mouse_y - orig_y
        sprite_ratio = math.sqrt((Constant.SPRITE_WIDTH / 2) ** 2 + (Constant.SPRITE_HEIGHT / 2) ** 2)

        # Distance between orig and mouse using Pythagore
        distance_orig_mouse = math.sqrt(delta_mouse_x ** 2 + delta_mouse_y ** 2)

        # Angle between horizontal and (orig - mouse) using trigonometry
        acos_mouse_angle = math.acos(delta_mouse_x / distance_orig_mouse)
        mouse_angle = math.degrees(acos_mouse_angle)
        print(f"delta_mouse_x {delta_mouse_x} delta_mouse_y {delta_mouse_y} mouse_angle {mouse_angle}")
        # searching the quadrant the mouse is over
        if 0 < mouse_angle < 90:
            if delta_mouse_y < 0:
                if delta_mouse_x > delta_mouse_y:
                    # The angle using the isometric grid is 45° + mouse_angle
                    isometric_mouse_angle = mouse_angle + 45

                    # isometric_delta_x using trigonometry
                    rad_isometric_mouse_angle = math.radians(isometric_mouse_angle)
                    isometric_delta_x = (math.cos(rad_isometric_mouse_angle) * distance_orig_mouse)
                    int_isometric_delta_x = int((isometric_delta_x + Constant.SPRITE_HEIGHT / 2) / sprite_ratio)

                    # isometric_delta_y using Pythagore
                    isometric_delta_y = math.sqrt(distance_orig_mouse ** 2 - isometric_delta_x ** 2)
                    int_isometric_delta_y = - int((isometric_delta_y + Constant.SPRITE_HEIGHT / 2)/ sprite_ratio)

                    if -7 < int_isometric_delta_y < 7 and -7 < int_isometric_delta_x < 7:
                        mouse_cell = self.cell_xy_to_screen_xy((player.pos_x + int_isometric_delta_x, player.pos_y + int_isometric_delta_y), player)
                        sprite_deco = pygame.image.load(f"{Constant.MISC}highlight.png")
                        sprite_redim = pygame.transform.scale(sprite_deco,
                                                              (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
                        screen.blit(sprite_redim, (mouse_cell[0], mouse_cell[1]))
            if delta_mouse_y > 0:
                if delta_mouse_x > delta_mouse_y:
                    # The angle using the isometric grid is 45 - mouse_angle
                    isometric_mouse_angle = 45 - mouse_angle

                    # isometric_delta_x using trigonometry
                    rad_isometric_mouse_angle = math.radians(isometric_mouse_angle)
                    isometric_delta_x = (math.cos(rad_isometric_mouse_angle) * distance_orig_mouse)
                    int_isometric_delta_x = int((isometric_delta_x + Constant.SPRITE_HEIGHT / 2) / sprite_ratio)

                    # isometric_delta_y using Pythagore
                    isometric_delta_y = math.sqrt(distance_orig_mouse ** 2 - isometric_delta_x ** 2)
                    int_isometric_delta_y = - int((isometric_delta_y) / sprite_ratio)
                    # print(f"isometric_delta_x{int_isometric_delta_x} isometric_delta_y {int_isometric_delta_y}")

                    if -7 < int_isometric_delta_y < 7 and -7 < int_isometric_delta_x < 7:
                        mouse_cell = self.cell_xy_to_screen_xy(
                            (player.pos_x + int_isometric_delta_x, player.pos_y + int_isometric_delta_y), player)
                        sprite_deco = pygame.image.load(f"{Constant.MISC}highlight.png")
                        sprite_redim = pygame.transform.scale(sprite_deco,
                                                              (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
                        screen.blit(sprite_redim, (mouse_cell[0], mouse_cell[1]))
        # time.sleep(1)

