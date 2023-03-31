# imports
import Constant
import pygame


class Interface():
    def __init__(self):
        self.move_button_zone = ""
        self.melee_button_zone = ""
        self.ranged_button_zone = ""

    def print_map(self, map, screen, player):
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
        self.print_action_menu(screen, player)
        self.print_stat(screen, player)
        for case in map.actual_map:
            cell_xy = (case.pos_x, case.pos_y)
            cell = self.cell_xy_to_screen_xy(cell_xy)

            sprite_floor = pygame.image.load(f"sprites/{case.sprite}")
            sprite_redim = pygame.transform.scale(sprite_floor, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
            screen.blit(sprite_redim, (cell[0], cell[1]))

            if case.deco != "":
                sprite_deco = pygame.image.load(f"{Constant.DECO}{case.deco}")
                sprite_redim = pygame.transform.scale(sprite_deco, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
                screen.blit(sprite_redim, (cell[0], cell[1] - 10))

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
        screen.blit(sprite_player_redim, (pos_x, pos_y - 10))
        pygame.display.flip()

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

    def print_stat(self, screen, player):
        """
        print the stats of the player on the screen
        :param player:
        :param screen:
        :return:
        """
        pos_x = Constant.SCREEN_WIDTH / 2
        pos_y = Constant.SCREEN_HEIGHT - Constant.SCREEN_HEIGHT / 5
        police = pygame.font.SysFont("arial", 30)
        txt_pa = police.render("Point d'action restants : " + str(player.actual_point), True, Constant.BLACK)
        screen.blit(txt_pa, (pos_x, pos_y))

    def print_action_menu(self, screen, player):
        for i in range(0, 3, 1):
            '''sprite_button = pygame.image.load(f"{Constant.BUTTONS}button_ready.png")
            sprite_button_redim = pygame.transform.scale(sprite_button,
                                                         (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
            pos_x_button = Constant.SPRITE_WIDTH / 20
            pos_y_button = ((Constant.SCREEN_HEIGHT / 20) + 50) * (i + 1)
            screen.blit(sprite_button_redim, (pos_x_button, pos_y_button))'''
            if i == 0:
                if player.action_move:
                    sprite_button = pygame.image.load(f"{Constant.BUTTONS}movebuttonactive.png")
                    sprite_button_redim = pygame.transform.scale(sprite_button,
                                                                 (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
                    pos_x_button = Constant.SPRITE_WIDTH / 20
                    pos_y_button = ((Constant.SCREEN_HEIGHT / 20) + 50) * (i + 1)

                else:
                    sprite_button = pygame.image.load(f"{Constant.BUTTONS}movebutton.png")
                    sprite_button_redim = pygame.transform.scale(sprite_button,
                                                                 (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
                    pos_x_button = Constant.SPRITE_WIDTH / 20
                    pos_y_button = ((Constant.SCREEN_HEIGHT / 20) + 50) * (i + 1)
                self.move_button_zone = pygame.Rect(pos_x_button, pos_y_button, Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT)
                screen.blit(sprite_button_redim, (pos_x_button, pos_y_button))
            if i == 1:
                if player.action_melee:
                    sprite_button = pygame.image.load(f"{Constant.BUTTONS}meleebuttonactive.png")
                    sprite_button_redim = pygame.transform.scale(sprite_button,
                                                                 (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
                    pos_x_button = Constant.SPRITE_WIDTH / 20
                    pos_y_button = ((Constant.SCREEN_HEIGHT / 20) + 50) * (i + 1)

                else:
                    sprite_button = pygame.image.load(f"{Constant.BUTTONS}meleebutton.png")
                    sprite_button_redim = pygame.transform.scale(sprite_button,
                                                                 (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
                    pos_x_button = Constant.SPRITE_WIDTH / 20
                    pos_y_button = ((Constant.SCREEN_HEIGHT / 20) + 50) * (i + 1)
                self.melee_button_zone = pygame.Rect(pos_x_button, pos_y_button, Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT)
                screen.blit(sprite_button_redim, (pos_x_button, pos_y_button))
            if i == 2:
                if player.action_ranged:
                    sprite_button = pygame.image.load(f"{Constant.BUTTONS}rangedbuttonactive.png")
                    sprite_button_redim = pygame.transform.scale(sprite_button,
                                                                 (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
                    pos_x_button = Constant.SPRITE_WIDTH / 20
                    pos_y_button = ((Constant.SCREEN_HEIGHT / 20) + 50) * (i + 1)

                else:
                    sprite_button = pygame.image.load(f"{Constant.BUTTONS}rangedbutton.png")
                    sprite_button_redim = pygame.transform.scale(sprite_button,
                                                                 (Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT))
                    pos_x_button = Constant.SPRITE_WIDTH / 20
                    pos_y_button = ((Constant.SCREEN_HEIGHT / 20) + 50) * (i + 1)
                self.ranged_button_zone = pygame.Rect(pos_x_button, pos_y_button, Constant.BUTTON_WIDTH, Constant.BUTTON_HEIGHT)
                screen.blit(sprite_button_redim, (pos_x_button, pos_y_button))
