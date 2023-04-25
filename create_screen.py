# imports
import threading
import server
import Constant
import pygame
import interface
import network


class CreateScreen:

    def __init__(self):
        window_size = (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
        self.screen_map = pygame.display.set_mode(window_size)
        self.interface = interface.Interface()

    def run_create_screen(self, player):
        # Starting server
        local_server = server.Server()
        # Démarrez le serveur dans un thread séparé
        server_thread = threading.Thread(target=local_server.start_server)
        server_thread.start()
        server_ip = local_server.send_address()

        local_client = network.Network(server_ip)

        start_button = pygame.image.load(f"{Constant.BUTTONS}start.png")
        start_button_redim = pygame.transform.scale(start_button,
                                                   (Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10))
        self.screen_map.blit(start_button_redim, (Constant.SCREEN_WIDTH / 2 - start_button_redim.get_width() / 2,
                                                 Constant.SCREEN_HEIGHT * 2 / 3 + 1 * start_button_redim.get_height()))
        self.start_button_zone = pygame.Rect(Constant.SCREEN_WIDTH / 2 - start_button_redim.get_width() / 2,
                                            Constant.SCREEN_HEIGHT * 2 / 3 + 1 * start_button_redim.get_height(),
                                            Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10)

        return_button = pygame.image.load(f"{Constant.BUTTONS}return.png")
        return_button_redim = pygame.transform.scale(return_button,
                                                   (Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10))
        self.screen_map.blit(return_button_redim, (Constant.SCREEN_WIDTH / 2 - return_button_redim.get_width() / 2,
                                                 Constant.SCREEN_HEIGHT * 2 / 3 + 2 * return_button_redim.get_height()))
        self.return_button_zone = pygame.Rect(Constant.SCREEN_WIDTH / 2 - return_button_redim.get_width() / 2,
                                            Constant.SCREEN_HEIGHT * 2 / 3 + 2 * return_button_redim.get_height(),
                                            Constant.SCREEN_WIDTH / 5, Constant.SCREEN_HEIGHT / 10)

        pygame.display.flip()
        local_server = None
        while True:

            mouse_x, mouse_y = pygame.mouse.get_pos()
            left_click, center_click, right_click = (pygame.mouse.get_pressed())

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()

                if self.start_button_zone.collidepoint(mouse_x, mouse_y) and left_click:
                    pass

