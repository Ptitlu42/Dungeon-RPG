# imports
import Constant
import pygame


def print_map(map, screen):
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
    for case in map.actual_map:
        cell_xy = (case.pos_x, case.pos_y)
        cell = cell_xy_to_screen_xy(cell_xy)

        sprite_floor = pygame.image.load(f"sprites/{case.sprite}")
        sprite_redim = pygame.transform.scale(sprite_floor, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
        screen.blit(sprite_redim, (cell[0], cell[1]))

        if case.deco != "":
            sprite_deco = pygame.image.load(f"{Constant.DECO}{case.deco}")
            sprite_redim = pygame.transform.scale(sprite_deco, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
            screen.blit(sprite_redim, (cell[0], cell[1] - 10))
    pygame.display.flip()


def print_player(player, screen):
    # player printing
    pos_x = ((2 * Constant.SCREEN_WIDTH / 3) + ((Constant.SPRITE_WIDTH / 2) * (player.pos_x + 1))) - \
            Constant.SPRITE_WIDTH / 2 * player.pos_y

    pos_y = ((Constant.SPRITE_CARACTER_HEIGHT / 2) + ((Constant.SPRITE_CARACTER_HEIGHT / 2) * (player.pos_y + 1))) + \
            Constant.SPRITE_CARACTER_HEIGHT / 2.5 * player.pos_x - player.pos_y * Constant.SPRITE_CARACTER_HEIGHT * 0.12\
            - Constant.SPRITE_HEIGHT / 3
    sprite_player = pygame.image.load(player.sprite)
    sprite_player_redim = pygame.transform.scale(sprite_player,
                                                 (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))
    screen.blit(sprite_player_redim, (pos_x, pos_y - 10))
    pygame.display.flip()

def cell_xy_to_screen_xy(coord):
    pos_x = ((2 * Constant.SCREEN_WIDTH / 3) + ((Constant.SPRITE_WIDTH / 2) * coord[0])) - \
            Constant.SPRITE_WIDTH / 2 * (coord[1] - 1)

    pos_y = ((Constant.SPRITE_HEIGHT / 2) + ((Constant.SPRITE_HEIGHT / 2) * (coord[1] + 1) )) + \
            Constant.SPRITE_HEIGHT / 2.5 * coord[0] - coord[1] * Constant.SPRITE_HEIGHT * 0.12
    screen_xy = (pos_x, pos_y)
    print(screen_xy)
    return screen_xy

def print_stat(pa, screen):
    pos_x = Constant.SCREEN_WIDTH / 2
    pos_y = Constant.SCREEN_HEIGHT - Constant.SCREEN_HEIGHT / 5
    police = pygame.font.SysFont("arial", 30)
    txt_pa = police.render("Point d'action restants : " + str(pa), True, Constant.BLACK)
    screen.blit(txt_pa, (pos_x, pos_y))