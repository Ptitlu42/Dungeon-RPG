# imports
import threading
import server
import Constant
import pygame
import interface
import create_screen

class Lobby:

    def __init__(self):
        window_size = (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
        self.screen_map = pygame.display.set_mode(window_size)
        self.interface = interface.Interface()
        self.main = True
        self.create_screen = True
        self.join_screen = True



    def run(self, player):
        self.screen_map.fill(Constant.BLACK)
        create_button = pygame.image.load(f"{Constant.BUTTONS}create.png")
        create_button_redim = pygame.transform.scale(create_button,
                                                   (Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10))
        self.screen_map.blit(create_button_redim, (Constant.SCREEN_WIDTH / 2 - create_button_redim.get_width() / 2,
                                                 Constant.SCREEN_HEIGHT * 2 / 3))
        self.create_button_zone = pygame.Rect(Constant.SCREEN_WIDTH / 2 - create_button_redim.get_width() / 2,
                                            Constant.SCREEN_HEIGHT * 2 / 3,
                                            Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10)

        join_button = pygame.image.load(f"{Constant.BUTTONS}join.png")
        join_button_redim = pygame.transform.scale(join_button,
                                                   (Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10))
        self.screen_map.blit(join_button_redim, (Constant.SCREEN_WIDTH / 2 - create_button_redim.get_width() / 2,
                                                 Constant.SCREEN_HEIGHT * 2 / 3 + 1 * join_button_redim.get_height()))
        self.join_button_zone = pygame.Rect(Constant.SCREEN_WIDTH / 2 - create_button_redim.get_width() / 2,
                                            Constant.SCREEN_HEIGHT * 2 / 3 + 1 * join_button_redim.get_height(),
                                            Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10)

        quit_button = pygame.image.load(f"{Constant.BUTTONS}quit.png")
        quit_button_redim = pygame.transform.scale(quit_button,
                                                   (Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10))
        self.screen_map.blit(quit_button_redim, (Constant.SCREEN_WIDTH / 2 - create_button_redim.get_width() / 2,
                                                 Constant.SCREEN_HEIGHT * 2 / 3 + 2 * quit_button_redim.get_height()))
        self.quit_button_zone = pygame.Rect(Constant.SCREEN_WIDTH / 2 - create_button_redim.get_width() / 2,
                                            Constant.SCREEN_HEIGHT * 2 / 3 + 2 * quit_button_redim.get_height(),
                                            Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10)

        pygame.display.flip()
        local_server = None
        while True:

            mouse_x, mouse_y = pygame.mouse.get_pos()
            left_click, center_click, right_click = (pygame.mouse.get_pressed())

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (self.quit_button_zone.collidepoint(mouse_x, mouse_y) and left_click):
                    running = False
                    pygame.quit()

                if self.create_button_zone.collidepoint(mouse_x, mouse_y) and left_click:
                    self.create_serv = create_screen.CreateScreen(player)
                    self.create_serv.run_create_screen()

                if self.join_button_zone.collidepoint(mouse_x, mouse_y) and left_click:
                    pass
