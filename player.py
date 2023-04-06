# import pygame
# from pygame.locals import *
# from  settings import *
# from Case import Tile
import time

import Constant
import pygame
import interface
import map


class Player(pygame.sprite.Sprite):
    def __init__(self, strength, life, speed, const, action_point, inventory, equiped_stuff, sprite, pos_x, pos_y):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'{Constant.PLAYER_PATH}basic.png')
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(Constant.BLACK)

        # our data
        self.strength = strength
        self.life = life
        self.speed = speed
        self.const = const
        self.action_point = action_point
        self.inventory = inventory
        self.equiped_stuff = equiped_stuff,
        self.sprite = sprite
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.last_x = 0
        self.last_y = 0
        self.player_can_go = {"left": False, "right": False, "up": False, "down": False}
        self.actual_point = self.action_point
        self.action_move = False
        self.action_melee = False
        self.action_ranged = False
        self.end_turn = False
        self.last_action = ""
        self.is_active = False


    def __str__(self):
        return str(self.speed)

    def get_image(self, x, y):
        image = pygame.Surface([Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT])
        image.blit(self.sprite_sheet, (0, 0), (x, y, Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
        return image

    def update(self):
        self.rect.topleft = [self.pos_x * Constant.SPRITE_WIDTH, self.pos_y * Constant.SPRITE_HEIGHT]

    # Coyotte move function
    def player_move(self, map, screen, interface, game):
        """
        print all accessible tiles around the player and move him on key press if able
        :param interface:
        :param loaded_map:
        :param screen:
        :return:
        """

        if self.last_x != self.pos_x or self.last_y != self.pos_y or self.last_action != "move":

            self.last_action = "move"
            interface.print_map(map, screen, self, game)

            # accessible cells printing
            if self.actual_point > 0:

                self.last_x = self.pos_x
                self.last_y = self.pos_y

        for player in game.player_list:
            interface.print_player(player, screen)
        # applying the movement to the player
        player_has_moved = False
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.player_can_go["left"]:
            self.pos_x -= 1
            player_has_moved = True
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.player_can_go["right"]:
            self.pos_x += 1
            player_has_moved = True
        if pygame.key.get_pressed()[pygame.K_UP] and self.player_can_go["up"]:
            self.pos_y -= 1
            player_has_moved = True
        if pygame.key.get_pressed()[pygame.K_DOWN] and self.player_can_go["down"]:
            self.pos_y += 1
            player_has_moved = True

        if player_has_moved:
            player_s_cell = map.get_cell_by_xy(self.last_x, self.last_y)
            player_s_cell.occuped_by = ""
            player_s_cell = map.get_cell_by_xy(self.pos_x, self.pos_y)
            player_s_cell.occuped_by = self
            self.player_can_go = {"left": False, "right": False, "up": False, "down": False}
            self.actual_point -= 1
            time.sleep(0.2)

    def player_melee(self, map, screen, interface, game):
        """
        Attack an entity in an orthogonal cell.
        :param map:
        :param screen:
        :param interface:
        :return:
        """
        self.player_can_go = {"left": False, "right": False, "up": False, "down": False}

        if self.last_x != self.pos_x or self.last_y != self.pos_y or self.last_action != "melee":

            self.last_action = "melee"
            # interface.print_action_menu(screen, self)
            # interface.print_map(map, screen, self)

            # accessible cells printing
            if self.actual_point > 0:
                interface.print_map(map, screen, self, game)

    def player_ranged(self, map, screen, interface, game):
        """
        player make a ranged attack
        :param map:
        :param screen:
        :param interface:
        :return:
        """
        self.player_can_go = {"left": False, "right": False, "up": False, "down": False}
        self.action_move = False
        self.action_melee = False
        self.action_ranged = True
        """interface.print_action_menu(screen, self)
        interface.print_map(map, screen, self)
        interface.print_player(self, screen)"""
        interface.print_map(map, screen, self, game)

        self.last_action = "ranged"