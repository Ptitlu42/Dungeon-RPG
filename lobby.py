# imports
import threading
#from pygame.examples.textinput import TextInput
import server
import Constant
import pygame
import interface
import network
import create_screen

class Lobby:

    def __init__(self):
        window_size = (Constant.SCREEN_WIDTH, Constant.SCREEN_HEIGHT)
        self.screen_map = pygame.display.set_mode(window_size)
        self.interface = interface.Interface()
        self.main = True
        self.create_screen = True
        self.join_screen = True
        self.police = pygame.font.Font(f"{Constant.FONT}IMMORTAL.ttf", 30)
        self.client_list = []

    def read_client_list(self, str):
        str = str.split(">,<")
        str_len = len(str)
        for element in range(0, str_len, 1):
            self.client_list.append(element)

    def run(self, player):

        # text input variables
        active = False
        text = '192.168.'
        color_inactive = Constant.WHITE
        color_active = Constant.BLUE
        color = color_inactive

        game_server = None
        while True:

            ##########################################################################################################
            # Interface
            self.screen_map.fill(Constant.BLACK)

            #---------------------------------------------------------------------------------------------------------
            # Btuttons
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

            #---------------------------------------------------------------------------------------------------------
            # Input field
            txt_serv = self.police.render(("Saisissez l'adresse du serveur :"), True, Constant.WHITE)
            self.screen_map.blit(txt_serv, (Constant.SCREEN_WIDTH / 2 - txt_serv.get_width() / 2,
                                                     Constant.SPRITE_HEIGHT * 2))

            # Input field variables :
            input_box = pygame.Rect(Constant.SCREEN_WIDTH / 2 - txt_serv.get_width() / 2,
                                    Constant.SPRITE_HEIGHT * 3, txt_serv.get_width(), Constant.SPRITE_HEIGHT)


            # Render the current text.
            txt_surface = self.police.render(text, True, Constant.WHITE)

            # Blit the text.
            self.screen_map.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
            # Blit the input_box rect.
            pygame.draw.rect(self.screen_map, color, input_box, 2)



            # ---------------------------------------------------------------------------------------------------------
            # If server is running
            if game_server:
                # Asking player_list
                player_in_lobby = client.send("Player_list")
                #print("lobby : ", player_in_lobby)

                conn_to = f"Connecté au serveur {server_ip}"
                txt_conn_to = self.police.render((conn_to), True, Constant.WHITE)
                self.screen_map.blit(txt_conn_to, (Constant.SCREEN_WIDTH / 2 - txt_conn_to.get_width() / 2,
                                                   Constant.SPRITE_HEIGHT * 4))
                txt_players_conn = self.police.render(("Joueurs connectés"), True, Constant.WHITE)
                self.screen_map.blit(txt_players_conn, (Constant.SCREEN_WIDTH / 2 - txt_conn_to.get_width() / 2,
                                                   Constant.SPRITE_HEIGHT * 5))
                player_in_lobby_len = len(player_in_lobby)
                for i in range(0, player_in_lobby_len,1):
                    # print(clients_list[i])
                    txt_client = self.police.render((str(player_in_lobby[i])), True, Constant.WHITE)
                    self.screen_map.blit(txt_client, (Constant.SCREEN_WIDTH / 2 - txt_conn_to.get_width() / 2,
                                                       Constant.SPRITE_HEIGHT * (i + 6)))


            ###########################################################################################################

            mouse_x, mouse_y = pygame.mouse.get_pos()
            left_click, center_click, right_click = (pygame.mouse.get_pressed())

            for event in pygame.event.get():
                if event.type == pygame.QUIT or (self.quit_button_zone.collidepoint(mouse_x, mouse_y) and left_click):
                    running = False
                    pygame.quit()

                if self.create_button_zone.collidepoint(mouse_x, mouse_y) and left_click:
                    if not game_server:
                        # Starting server
                        game_server = server.Server()
                        # Démarrez le serveur dans un thread séparé
                        server_thread = threading.Thread(target=game_server.start_server)
                        server_thread.start()
                        server_ip = game_server.send_address()

                        client = network.Network(server_ip)
                        client_thread = threading.Thread(target=client.receive)



                if self.join_button_zone.collidepoint(mouse_x, mouse_y) and left_click:
                    client = network.Network(text)
                    server_ip = text
                    game_server = True

                # If the user clicked on the input_box rect.
                if input_box.collidepoint(mouse_x, mouse_y) and left_click:
                    print("click on text zone")
                    # Toggle the active variable.
                    active = True
                elif left_click:
                    active = False
                    # Change the current color of the input box.
                color = color_active if active else color_inactive

                if event.type == pygame.KEYDOWN:
                    if active:
                        if event.key == pygame.K_RETURN:
                            print(text)
                            text = ''
                        elif event.key == pygame.K_BACKSPACE:
                            text = text[:-1]
                        else:
                            text += event.unicode

                if game_server:
                    # self.read_client_list()
                    pass


            # Refresh Screen
            pygame.display.flip()