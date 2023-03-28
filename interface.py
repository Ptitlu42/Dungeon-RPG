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
    for case in map:
        pos_x = ((Constant.SCREEN_WIDTH / 2) + ((Constant.SPRITE_WIDTH / 2) * (case.pos_x + 1))) - \
                Constant.SPRITE_WIDTH / 2 * case.pos_y

        pos_y = ((Constant.SPRITE_HEIGHT / 2) + ((Constant.SPRITE_HEIGHT / 2) * (case.pos_y + 1))) + \
                Constant.SPRITE_HEIGHT / 2.5 * case.pos_x - case.pos_y * Constant.SPRITE_HEIGHT * 0.12

        sprite_floor = pygame.image.load(f"sprites/{case.sprite}")
        sprite_redim = pygame.transform.scale(sprite_floor, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
        screen.blit(sprite_redim, (pos_x, pos_y))
        # print(f"Case x : {pos_x} - Case y : {pos_y}")
        # screen.blit(sprite_floor, (0, 0))
        if case.deco != "":
            sprite_deco = pygame.image.load(f"sprites/{case.deco}")
            sprite_redim = pygame.transform.scale(sprite_deco, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
            screen.blit(sprite_redim, (pos_x, pos_y - 10))
    pygame.display.flip()


def print_player(player, screen):
    # player printing
    pos_x = ((Constant.SCREEN_WIDTH / 2) + ((Constant.SPRITE_WIDTH / 2) * (player.pos_x + 1))) - \
            Constant.SPRITE_WIDTH / 2 * player.pos_y

    pos_y = ((Constant.SPRITE_CARACTER_HEIGHT / 2) + ((Constant.SPRITE_CARACTER_HEIGHT / 2) * (player.pos_y + 1))) + \
            Constant.SPRITE_CARACTER_HEIGHT / 2.5 * player.pos_x - player.pos_y * Constant.SPRITE_CARACTER_HEIGHT * 0.12\
            - Constant.SPRITE_HEIGHT / 3
    sprite_player = pygame.image.load(player.sprite)
    sprite_player_redim = pygame.transform.scale(sprite_player,
                                                 (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))
    screen.blit(sprite_player_redim, (pos_x, pos_y - 10))
    pygame.display.flip()

