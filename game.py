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


class Game():

    def __init__(self):

        # Creating Window
        window_size = (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
        self.screen_map = pygame.display.set_mode(window_size)
        self.screen_player = pygame.display.set_mode(window_size)
        self.interface = interface.Interface()
        self.battle_mode = battle_mode.Battle_mode()

        pygame.display.set_caption("POEC Fantasy")


    def run(self):

        while True:
            # Affichage de la map
            test_button = pygame.image.load(f"{Constant.BUTTONS}test.png")
            test_button_redim = pygame.transform.scale(test_button,
                                                         (Constant.SCREEN_WIDTH - 2, Constant.SCREEN_HEIGHT / 2 - 2))
            self.screen_map.blit(test_button_redim, (1, 1))
            self.test_button_zone = pygame.Rect(1, 1, Constant.SCREEN_WIDTH - 2,
                                                 Constant.SCREEN_HEIGHT / 2 - 2)

            quit_button = pygame.image.load(f"{Constant.BUTTONS}quit.png")
            quit_button_redim = pygame.transform.scale(quit_button,
                                                       (Constant.SCREEN_WIDTH - 2, Constant.SCREEN_HEIGHT / 2 - 2))
            self.screen_map.blit(quit_button_redim, (1, 1 + Constant.SCREEN_HEIGHT / 2))
            self.quit_button_zone = pygame.Rect(1, 1  + Constant.SCREEN_HEIGHT / 2, Constant.SCREEN_WIDTH - 2,
                                                Constant.SCREEN_HEIGHT / 2 - 2)

            mouse_x, mouse_y = pygame.mouse.get_pos()
            left_click, center_click, right_click = (pygame.mouse.get_pressed())


            pygame.display.flip()



            for event in pygame.event.get():
                if event.type == pygame.QUIT or (self.quit_button_zone.collidepoint(mouse_x, mouse_y) and left_click):
                    running = False
                    pygame.quit()

                if self.test_button_zone.collidepoint(mouse_x, mouse_y) and left_click:
                    self.battle_mode.turn()
