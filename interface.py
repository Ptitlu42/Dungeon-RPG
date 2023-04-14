# imports
import Constant
import pygame


class Interface():
    def __init__(self):
        self.move_button_zone = ""
        self.melee_button_zone = ""
        self.ranged_button_zone = ""
        self.end_button_zone = ""

    def print_map(self, map, screen, player, game):
        '''
        print the map in the window
        :param map:
        :param screen:
        :return:
        '''
        screen.fill(Constant.BLACK)
        background = pygame.image.load(f"{Constant.BG}scroll.png")
        bg_redim = pygame.transform.scale(background, (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT))
        screen.blit(bg_redim, (0, 0))
        player.player_can_go = {"left": False, "right": False, "up": False, "down": False}
        self.print_action_menu(screen, player)
        self.print_stat(screen, player, game)
        for case in map.actual_map:
            cell_xy = (case.pos_x, case.pos_y)
            cell = self.cell_xy_to_screen_xy(cell_xy)

            sprite_floor = pygame.image.load(f"{Constant.FLOOR}{case.sprite}")
            sprite_redim = pygame.transform.scale(sprite_floor, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
            screen.blit(sprite_redim, (cell[0], cell[1]))

            """if case.deco != "":
                sprite_deco = pygame.image.load(f"{Constant.DECO}{case.deco}")
                sprite_redim = pygame.transform.scale(sprite_deco, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
                screen.blit(sprite_redim, (cell[0], cell[1] - 10))"""

        if player.action_move:
            self.check_area(player.actual_point, player, map, screen)
        if player.action_melee:
            self.check_area(1, player, map, screen)
        """if player.action_ranged:
            if player.equiped_stuff[range] != "":
                self.check_area(player.equiped_stuff[range], player, map, screen)"""

        for case in map.actual_map:
            cell_xy = (case.pos_x, case.pos_y)
            cell = self.cell_xy_to_screen_xy(cell_xy)

            if case.deco != "":
                sprite_deco = pygame.image.load(f"{Constant.DECO}{case.deco}")
                sprite_redim = pygame.transform.scale(sprite_deco, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
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
        pos_x = ((2 * Constant.SCREEN_WIDTH / 3) + ((Constant.SPRITE_WIDTH / 2) * (player.pos_x + 1))) - \
                Constant.SPRITE_WIDTH / 2 * player.pos_y

        pos_y = ((Constant.SPRITE_CARACTER_HEIGHT / 2) + ((Constant.SPRITE_CARACTER_HEIGHT / 2) * (player.pos_y + 1))) + \
                Constant.SPRITE_CARACTER_HEIGHT / 2.5 * player.pos_x - player.pos_y * Constant.SPRITE_CARACTER_HEIGHT * 0.12 \
                - Constant.SPRITE_HEIGHT / 3
        sprite_player = pygame.image.load(player.sprite)
        sprite_player_redim = pygame.transform.scale(sprite_player,
                                                     (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))

        if player.is_active:
            halo_player = pygame.image.load(f"{Constant.MISC}activeplayer.png")
            halo_player_redim = pygame.transform.scale(halo_player,
                                                       (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))
            screen.blit(halo_player_redim, (pos_x, pos_y))
        screen.blit(sprite_player_redim, (pos_x, pos_y - 10))

    def cell_xy_to_screen_xy(self, coord):
        """
        Get a cell in the list of map cell
        :param coord:
        :return: cell
        """
        pos_x = ((2 * Constant.SCREEN_WIDTH / 3) + ((Constant.SPRITE_WIDTH / 2) * coord[0])) - \
                Constant.SPRITE_WIDTH / 2 * (coord[1] - 1)

        pos_y = ((Constant.SPRITE_HEIGHT / 2) + ((Constant.SPRITE_HEIGHT / 2) * (coord[1] + 1))) + \
                Constant.SPRITE_HEIGHT / 2.5 * coord[0] - coord[1] * Constant.SPRITE_HEIGHT * 0.12
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

    def check_case(self, player, map, screen, case_pos_x, case_pos_y):
        """
        verify if the cells are available
        :param player:
        :param map:
        :param screen:
        :param case_pos_x:
        :param case_pos_y:
        :return:
        """
        if player.actual_point > 0:

            for pos in [[player.pos_x + 1, player.pos_y], [player.pos_x, player.pos_y + 1],
                        [player.pos_x - 1, player.pos_y],
                        [player.pos_x, player.pos_y - 1]]:

                celltest = map.get_cell_by_xy(pos[0], pos[1])
                if pos[0] == case_pos_x and pos[1] == case_pos_y:
                    if player.action_move:
                        cell_xy = (celltest.pos_x, celltest.pos_y)
                        cell = self.cell_xy_to_screen_xy(cell_xy)

                        if celltest.deco == "" and celltest.occuped_by == "":
                            # print the accessible PNG on the tile
                            sprite_bluecell = pygame.image.load(f"{Constant.MISC}accessible.png")
                            sprite_bluecell_redim = pygame.transform.scale(sprite_bluecell,
                                                                           (Constant.SPRITE_WIDTH,
                                                                            Constant.SPRITE_CARACTER_HEIGHT))
                            screen.blit(sprite_bluecell_redim, (cell[0], cell[1]))
                            self.set_player_can_move(player, pos)

                    if player.action_melee:
                        cell_xy = (celltest.pos_x, celltest.pos_y)
                        cell = self.cell_xy_to_screen_xy(cell_xy)
                        if celltest.occuped_by != "":
                            # print the fightable PNG on the tile
                            sprite_redcell = pygame.image.load(f"{Constant.MISC}fightable.png")
                            sprite_redcell_redim = pygame.transform.scale(sprite_redcell,
                                                                          (Constant.SPRITE_WIDTH,
                                                                           Constant.SPRITE_CARACTER_HEIGHT))
                            screen.blit(sprite_redcell_redim, (cell[0], cell[1]))
                            self.set_player_can_move(player, pos)

                    if player.action_ranged:
                        pass

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
                                    if cell.deco == "" and cell.occuped_by == "":
                                        # print the accessible PNG on the tile
                                        sprite_bluecell = pygame.image.load(f"{Constant.MISC}accessible.png")
                                        sprite_bluecell_redim = pygame.transform.scale(sprite_bluecell,
                                                                                       (Constant.SPRITE_WIDTH,
                                                                                        Constant.SPRITE_CARACTER_HEIGHT))
                                        cell_pos = self.cell_xy_to_screen_xy((cell.pos_x, cell.pos_y))
                                        screen.blit(sprite_bluecell_redim, cell_pos)
                                        self.set_player_can_move(player, [player.pos_x + xvar, player.pos_y + yvar])

                                if player.action_melee or player.action_ranged:
                                    if cell.occuped_by != "" and cell.occuped_by.name != player.name:
                                        # print the fightable PNG on the tile
                                        sprite_redcell = pygame.image.load(f"{Constant.MISC}fightable.png")
                                        sprite_redcell_redim = pygame.transform.scale(sprite_redcell,
                                                                                      (Constant.SPRITE_WIDTH,
                                                                                       Constant.SPRITE_CARACTER_HEIGHT))
                                        cell_pos = self.cell_xy_to_screen_xy((cell.pos_x, cell.pos_y))
                                        screen.blit(sprite_redcell_redim, cell_pos)
                                        self.set_player_can_move(player, [player.pos_x + xvar, player.pos_y + yvar])
