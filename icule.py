import pygame

pygame.init()

# Définir les dimensions de la fenêtre
size = (700, 500)
screen = pygame.display.set_mode(size)

# Définir les dimensions de l'objet Rect initial
rect_width = 100
rect_height = 50
rect_x = 200
rect_y = 200

# Créer une surface avec les dimensions de l'objet Rect initial
surface = pygame.Surface((rect_width, rect_height))

# Dessiner un rectangle sur la surface
rect = pygame.Rect(0, 0, rect_width, rect_height)
pygame.draw.rect(surface, (255, 255, 255), rect)

# Appliquer une rotation de 45 degrés à la surface
surface = pygame.transform.rotate(surface, 45)

# Récupérer les dimensions et les coordonnées de l'objet Rect après la rotation
new_rect = surface.get_rect()
new_rect.center = (rect_x, rect_y)

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Récupérer les coordonnées de la souris
            mouse_pos = pygame.mouse.get_pos()
            # Vérifier si les coordonnées de la souris se trouvent dans le rectangle tourné
            if new_rect.collidepoint(mouse_pos):
                print("Clic détecté dans le rectangle tourné !")

    # Dessiner le rectangle tourné sur l'écran
    screen.blit(surface, new_rect)

    pygame.display.flip()
