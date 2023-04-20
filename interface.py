# imports
import Constant
import pygame


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

        # arrows
        arrow_up = pygame.image.load(f"{Constant.BUTTONS}arrow_up.png")
        arrow_up_redim = pygame.transform.scale(arrow_up, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
        screen.blit(arrow_up_redim, (Constant.SCREEN_WIDTH * .9, Constant.SCREEN_HEIGHT * 0.05))
        self.up_button_zone = pygame.Rect(Constant.SCREEN_WIDTH * .9, Constant.SCREEN_HEIGHT * 0.05, Constant.SPRITE_WIDTH,
                                             Constant.SPRITE_HEIGHT)

        arrow_left = pygame.image.load(f"{Constant.BUTTONS}arrow_left.png")
        arrow_left_redim = pygame.transform.scale(arrow_left, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
        screen.blit(arrow_left_redim, (Constant.SCREEN_WIDTH * .9 - Constant.SPRITE_WIDTH, Constant.SCREEN_HEIGHT * 0.05))
        self.left_button_zone = pygame.Rect(Constant.SCREEN_WIDTH * .9 - Constant.SPRITE_WIDTH, Constant.SCREEN_HEIGHT * 0.05,
                                          Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT)

        arrow_right = pygame.image.load(f"{Constant.BUTTONS}arrow_right.png")
        arrow_right_redim = pygame.transform.scale(arrow_right, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
        screen.blit(arrow_right_redim,
                    (Constant.SCREEN_WIDTH * .9, Constant.SCREEN_HEIGHT * 0.05 + Constant.SPRITE_HEIGHT))
        self.right_button_zone = pygame.Rect(Constant.SCREEN_WIDTH * .9,
                                            Constant.SCREEN_HEIGHT * 0.05 + Constant.SPRITE_HEIGHT,
                                            Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT + Constant.SPRITE_HEIGHT)

        arrow_down = pygame.image.load(f"{Constant.BUTTONS}arrow_down.png")
        arrow_down_redim = pygame.transform.scale(arrow_down, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
        screen.blit(arrow_down_redim,
                    (Constant.SCREEN_WIDTH * .9 - Constant.SPRITE_WIDTH,
                     Constant.SCREEN_HEIGHT * 0.05 + Constant.SPRITE_HEIGHT))
        self.down_button_zone = pygame.Rect(Constant.SCREEN_WIDTH * .9 - Constant.SPRITE_WIDTH, Constant.SCREEN_HEIGHT * 0.05 + Constant.SPRITE_HEIGHT,
                                            Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT + Constant.SPRITE_HEIGHT)

        for active_player in game.player_list:

            if active_player.is_active:
                self.player_active = active_player
                coord = (Constant.SCREEN_WIDTH * 0.9 - Constant.SPRITE_WIDTH / 2,
                                                   Constant.SCREEN_HEIGHT * 0.05 + Constant.SPRITE_HEIGHT / 2)
                sprite_player = pygame.image.load(active_player.sprite)
                sprite_player_redim = pygame.transform.scale(sprite_player,
                                                             (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))
                screen.blit(sprite_player_redim, coord)

        player.player_can_go = {"left": False, "right": False, "up": False, "down": False}
        self.print_action_menu(screen, player)
        self.print_stat(screen, player, game)

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
            screen.blit(sprite_player_redim, (coord[0], coord[1] - Constant.SPRITE_HEIGHT / 2))
        else:
            if player.life_mod > 0:
                coord = self.cell_xy_to_screen_xy((player.pos_x, player.pos_y), self.player_active)
                sprite_player = pygame.image.load(player.sprite)
                sprite_player_redim = pygame.transform.scale(sprite_player,
                                                             (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))

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
            screen.blit(sprite_player_redim, (coord[0], coord[1] - Constant.SPRITE_HEIGHT / 2))

    def cell_xy_to_screen_xy(self, coord, player):
        """
        Get a cell in the list of map cell
        :param coord:
        :return: cell
        """
        pos_x = (Constant.SCREEN_WIDTH / 2) + (((coord[0] - player.pos_x) * Constant.SPRITE_WIDTH / 2) - (coord[1] - player.pos_y) * Constant.SPRITE_WIDTH / 2 - Constant.SPRITE_WIDTH / 2)
        pos_y = (Constant.SCREEN_HEIGHT / 2) + (((coord[1] - player.pos_y) * Constant.SPRITE_HEIGHT / 2 + (coord[0] - player.pos_x) * Constant.SPRITE_HEIGHT / 2) - Constant.SPRITE_HEIGHT / 2) - ((coord[1] - player.pos_y) * Constant.SPRITE_HEIGHT * 0.12 + (coord[0] - player.pos_x) * Constant.SPRITE_HEIGHT * 0.12)

        screen_xy = (pos_x, pos_y)
        return screen_xy

    def print_stat(self, screen, player, game):
        """
        print the stats of the player on the screen
        :param player:
        :param screen:
        :return:
        """
        pos_x = Constant.SCREEN_WIDTH / 50
        pos_y = (2 * Constant.SCREEN_HEIGHT / 3)
        police = pygame.font.Font(f"{Constant.FONT}IMMORTAL.ttf", 30)
        i = 1
        length = len(game.player_list)
        for i in range(length):
            txt_name = police.render((game.player_list[i].name), True, Constant.BLACK)
            txt_pv = police.render("Life : ", True, Constant.BLACK)
            val_pv = police.render(str(game.player_list[i].life_mod), True, Constant.BLACK)
            txt_strength = police.render("Strenght : ", True, Constant.BLACK)
            val_strength = police.render(str(game.player_list[i].strength_mod), True, Constant.BLACK)
            txt_const = police.render("Const : ", True, Constant.BLACK)
            val_const = police.render(str(game.player_list[i].const_mod), True, Constant.BLACK)
            screen.blit(txt_name, (pos_x + (i) * (20 * Constant.SCREEN_WIDTH / 100), pos_y))
            screen.blit(txt_pv, (pos_x + (i) * (20 * Constant.SCREEN_WIDTH / 100), pos_y + 25))
            screen.blit(val_pv, (pos_x + (i) * (20 * Constant.SCREEN_WIDTH / 100) + 150, pos_y + 25))
            screen.blit(txt_strength, (pos_x + (i) * (20 * Constant.SCREEN_WIDTH / 100), pos_y + 50))
            screen.blit(val_strength, (pos_x + (i) * (20 * Constant.SCREEN_WIDTH / 100) + 150, pos_y + 50))
            screen.blit(txt_const, (pos_x + (i) * (20 * Constant.SCREEN_WIDTH / 100), pos_y + 75))
            screen.blit(val_const, (pos_x + (i) * (20 * Constant.SCREEN_WIDTH / 100) + 150, pos_y + 75))

            i += 1
        pos_y = Constant.SCREEN_HEIGHT / 30
        active_player = police.render("Active player : " + player.name, True, Constant.BLACK)
        txt_pa = police.render("Point d'action restants : " + str(player.actual_point), True, Constant.BLACK)
        screen.blit(active_player, (pos_x, pos_y))
        screen.blit(txt_pa, (pos_x, pos_y + 50))

    def print_action_menu(self, screen, player):
        """
        print the action menu on the screen
        :param screen:
        :param player:
        :return:
        """
        for i in range(0, 4, 1):
            pos_x_button = Constant.SPRITE_WIDTH / 20
            pos_y_button = ((Constant.SCREEN_HEIGHT / 20) + 30) * (i + 1) + 100

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
                                    if cell.deco == "" and (cell.occuped_by == "" or cell.occuped_by.life_mod <= 0):
                                        # print the accessible PNG on the tile
                                        sprite_bluecell = pygame.image.load(f"{Constant.MISC}accessible.png")
                                        sprite_bluecell_redim = pygame.transform.scale(sprite_bluecell,
                                                                                       (Constant.SPRITE_WIDTH,
                                                                                        Constant.SPRITE_CARACTER_HEIGHT))
                                        cell_pos = self.cell_xy_to_screen_xy((cell.pos_x, cell.pos_y), player)
                                        screen.blit(sprite_bluecell_redim, cell_pos)
                                        self.set_player_can_move(player, [player.pos_x + xvar, player.pos_y + yvar])

                                if player.action_melee:
                                    if cell.occuped_by != "" and cell.occuped_by.name != player.name:
                                        # print the fightable PNG on the tile
                                        sprite_redcell = pygame.image.load(f"{Constant.MISC}fightable.png")
                                        sprite_redcell_redim = pygame.transform.scale(sprite_redcell,
                                                                                      (Constant.SPRITE_WIDTH,
                                                                                       Constant.SPRITE_CARACTER_HEIGHT))
                                        cell_pos = self.cell_xy_to_screen_xy((cell.pos_x, cell.pos_y), player)
                                        screen.blit(sprite_redcell_redim, cell_pos)
                                        self.set_player_can_move(player, [player.pos_x + xvar, player.pos_y + yvar])

                                if player.action_ranged:
                                    if cell.occuped_by != "" and cell.occuped_by.name != player.name:
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


