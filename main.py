# Import
import threading
import pygame as pygame
import game
import server

if __name__ == '__main__':
    # Pygame initialisation
    pygame.init()
    pygame.mixer.init()

    # Starting server
    server = server.Server()
    # Démarrez le serveur dans un thread séparé
    server_thread = threading.Thread(target=server.start_server)
    server_thread.start()

    game = game.Game()
    game.run()
