import pygame
import pytmx
import pyscroll
import Constant
import player
import time
import map
import interface
import item
import battle_mode
import lobby


class Game():

    def __init__(self):

        # Creating Window
        self.battle_mode = None
        window_size = (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
        self.screen_map = pygame.display.set_mode(window_size)
        self.screen_player = pygame.display.set_mode(window_size)
        self.interface = interface.Interface()
        pygame.display.set_caption("POEC Fantasy")
        self.lobby = None

        # player's list
        # Player initialisation
        self.player_list = []
        player_temp = None
        self.player = player.Player("Owlet", 5, 1, 5, 5, 5, ("", "", "", "", "", "", "", "", "", "", ""),
                                    {"head": "", "chest": "", "legs": "", "left hand": 3, "right hand": 2},
                                    f"{Constant.PLAYER_PATH}Owlet.png", 10, 10)
        #self.get_mod_from_player(self.player)
        self.player_list.append(self.player)
        # player_s_cell = self.loaded_map.get_cell_by_xy(self.player.pos_x, self.player.pos_y)
        # player_s_cell.occuped_by = self.player
        self.player2 = player.Player("Cat", 5, 40, 6, 4, 5, ("", "", "", "", "", "", "", "", "", "", ""),
                                     {"head": "", "chest": "", "legs": "", "left hand": "", "right hand": 4},
                                     f"{Constant.PLAYER_PATH}cat.png", 10, 11)
        #self.get_mod_from_player(self.player2)
        self.player_list.append(self.player2)
        # player2_s_cell = self.loaded_map.get_cell_by_xy(self.player2.pos_x, self.player2.pos_y)
        # player2_s_cell.occuped_by = self.player2
        self.player3 = player.Player("Pingu", 5, 1, 6, 4, 5, ("", "", "", "", "", "", "", "", "", "", ""),
                                     {"head": "", "chest": "", "legs": "", "left hand": "", "right hand": 4},
                                     f"{Constant.PLAYER_PATH}pingu.png", 11, 11)
        #self.get_mod_from_player(self.player2)
        self.player_list.append(self.player3)
        # player2_s_cell = self.loaded_map.get_cell_by_xy(self.player2.pos_x, self.player2.pos_y)
        # player2_s_cell.occuped_by = self.player2

        length = len(self.player_list)
        for j in range(length):
            for i in range(0, length - j - 1):
                if self.player_list[i].speed < self.player_list[i + 1].speed:
                    player_temp = self.player_list[i]
                    self.player_list[i] = self.player_list[i + 1]
                    self.player_list[i + 1] = player_temp


    def run(self):

        while True:
            self.screen_map.fill(Constant.BLACK)
            title = pygame.image.load(f"{Constant.TITLE}title.png")
            title_redim = pygame.transform.scale(title,
                                                       (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT))
            self.screen_map.blit(title_redim, (0, 0))
            test_button = pygame.image.load(f"{Constant.BUTTONS}test.png")
            test_button_redim = pygame.transform.scale(test_button,
                                                         (Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10))
            self.screen_map.blit(test_button_redim, (Constant.SCREEN_WIDTH / 2 - test_button_redim.get_width() / 2,
                                                     Constant.SCREEN_HEIGHT * 2 / 3))
            self.test_button_zone = pygame.Rect(Constant.SCREEN_WIDTH / 2 - test_button_redim.get_width() / 2,
                                                Constant.SCREEN_HEIGHT * 2 / 3,
                                                Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10)

            tuto_button = pygame.image.load(f"{Constant.BUTTONS}tuto.png")
            tuto_button_redim = pygame.transform.scale(tuto_button,
                                                       (Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10))
            self.screen_map.blit(tuto_button_redim, (Constant.SCREEN_WIDTH / 2 - test_button_redim.get_width() / 2,
                                                     Constant.SCREEN_HEIGHT * 2 / 3 + 1 * tuto_button_redim.get_height()))
            self.tuto_button_zone = pygame.Rect(Constant.SCREEN_WIDTH / 2 - test_button_redim.get_width() / 2,
                                                     Constant.SCREEN_HEIGHT * 2 / 3 + 1 * tuto_button_redim.get_height(),
                                                Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10)

            quit_button = pygame.image.load(f"{Constant.BUTTONS}quit.png")
            quit_button_redim = pygame.transform.scale(quit_button,
                                                       (Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10))
            self.screen_map.blit(quit_button_redim, (Constant.SCREEN_WIDTH / 2 - test_button_redim.get_width() / 2,
                                                     Constant.SCREEN_HEIGHT * 2 / 3 + 2 * quit_button_redim.get_height()))
            self.quit_button_zone = pygame.Rect(Constant.SCREEN_WIDTH / 2 - test_button_redim.get_width() / 2,
                                                Constant.SCREEN_HEIGHT * 2 / 3 + 2 * quit_button_redim.get_height(),
                                                Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            left_click, center_click, right_click = (pygame.mouse.get_pressed())


            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.QUIT or (self.quit_button_zone.collidepoint(mouse_x, mouse_y) and left_click):
                    running = False
                    pygame.quit()

                if self.test_button_zone.collidepoint(mouse_x, mouse_y) and left_click:
                    self.lobby = lobby.Lobby()
                    self.lobby.run(self.player)
                    """self.battle_mode = battle_mode.Battle_mode(f"{Constant.MAPS}mapTest.xls", self.player_list)
                    self.battle_mode.turn()
                    self.battle_mode.victory()
                    # del self.battle_mode
                    print("del ok")"""

                if self.tuto_button_zone.collidepoint(mouse_x, mouse_y) and left_click:
                    self.battle_mode = battle_mode.Battle_mode(f"{Constant.MAPS}mapTuto1.xls", self.player_list)
                    self.battle_mode.turn()
                    self.battle_mode.victory()
                    # del self.battle_mode
                    print("del ok")
