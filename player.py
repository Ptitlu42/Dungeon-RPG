# import pygame
# from pygame.locals import *
# from  settings import *
# from Case import Tile
import Constant
import pygame
import interface

class Player():
    def __init__(self, strength, life, speed, const, action_point, inventory, equiped_stuff, sprite, pos_x, pos_y):
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
        
    def player_move(self, loaded_map, screen):

        actual_point = self.action_point


        if self.last_x != self.pos_x or self.last_y != self.pos_y:
            print(f" last : {self.last_x} ; {self.last_y} - actual : {self.pos_x} ; {self.pos_y}")
            # accessible cells printing
            if actual_point > 0:

                for case in loaded_map:

                    if case.pos_x == self.pos_x - 1 and case.pos_y == self.pos_y and case.deco == "":
                        pos_x = ((Constant.SCREEN_WIDTH / 2) + ((Constant.SPRITE_WIDTH / 2) * (case.pos_x))) - \
                                Constant.SPRITE_WIDTH / 2 * (case.pos_y - 1)

                        pos_y = ((Constant.SPRITE_HEIGHT / 2) + ((Constant.SPRITE_HEIGHT / 2) * (case.pos_y + 1))) + \
                                Constant.SPRITE_HEIGHT / 2.5 * case.pos_x - case.pos_y * Constant.SPRITE_HEIGHT * 0.12
                        sprite_player = pygame.image.load(f"{Constant.PLAYER_TILES_PATH}accessible.png")
                        sprite_player_redim = pygame.transform.scale(sprite_player,
                                                                     (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))
                        screen.blit(sprite_player_redim, (pos_x, pos_y))
                        self.player_can_go["left"] = True

                    if case.pos_x == self.pos_x + 1 and case.pos_y == self.pos_y and case.deco == "":

                        pos_x = ((Constant.SCREEN_WIDTH / 2) + ((Constant.SPRITE_WIDTH / 2) * (case.pos_x))) - \
                                Constant.SPRITE_WIDTH / 2 * (case.pos_y - 1)

                        pos_y = ((Constant.SPRITE_HEIGHT / 2) + ((Constant.SPRITE_HEIGHT / 2) * (case.pos_y + 1))) + \
                                Constant.SPRITE_HEIGHT / 2.5 * case.pos_x - case.pos_y * Constant.SPRITE_HEIGHT * 0.12
                        sprite_player = pygame.image.load(f"{Constant.PLAYER_TILES_PATH}accessible.png")
                        sprite_player_redim = pygame.transform.scale(sprite_player,
                                                                     (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))
                        screen.blit(sprite_player_redim, (pos_x, pos_y))
                        self.player_can_go["right"] = True

                    if case.pos_x == self.pos_x and case.pos_y == self.pos_y - 1 and case.deco == "":

                        pos_x = ((Constant.SCREEN_WIDTH / 2) + ((Constant.SPRITE_WIDTH / 2) * (case.pos_x))) - \
                                Constant.SPRITE_WIDTH / 2 * (case.pos_y - 1)

                        pos_y = ((Constant.SPRITE_HEIGHT / 2) + ((Constant.SPRITE_HEIGHT / 2) * (case.pos_y + 1))) + \
                                Constant.SPRITE_HEIGHT / 2.5 * case.pos_x - case.pos_y * Constant.SPRITE_HEIGHT * 0.12
                        sprite_player = pygame.image.load(f"{Constant.PLAYER_TILES_PATH}accessible.png")
                        sprite_player_redim = pygame.transform.scale(sprite_player,
                                                                     (Constant.SPRITE_WIDTH,
                                                                      Constant.SPRITE_CARACTER_HEIGHT))
                        screen.blit(sprite_player_redim, (pos_x, pos_y))
                        self.player_can_go["up"] = True

                    if case.pos_x == self.pos_x and case.pos_y == self.pos_y + 1 and case.deco == "":

                        # accessible cells printing
                        pos_x = ((Constant.SCREEN_WIDTH / 2) + ((Constant.SPRITE_WIDTH / 2) * (case.pos_x))) - \
                                Constant.SPRITE_WIDTH / 2 * (case.pos_y - 1)

                        pos_y = ((Constant.SPRITE_HEIGHT / 2) + ((Constant.SPRITE_HEIGHT / 2) * (case.pos_y + 1))) + \
                                Constant.SPRITE_HEIGHT / 2.5 * case.pos_x - case.pos_y * Constant.SPRITE_HEIGHT * 0.12
                        sprite_player = pygame.image.load(f"{Constant.PLAYER_TILES_PATH}accessible.png")
                        sprite_player_redim = pygame.transform.scale(sprite_player,
                                                                     (Constant.SPRITE_WIDTH, Constant.SPRITE_CARACTER_HEIGHT))
                        screen.blit(sprite_player_redim, (pos_x, pos_y))
                        self.player_can_go["down"] = True

                    interface.print_player(self, screen)
                    pygame.display.flip()
                    self.last_x = self.pos_x
                    self.last_y = self.pos_y
        print(f"{self.player_can_go['down']} {self.player_can_go['up']} {self.player_can_go['left']}")
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.player_can_go["left"]:
            self.pos_x -= 1
            self.player_can_go = {"left": False, "right": False, "up": False, "down": False}
            interface.print_map(loaded_map, screen)
        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.player_can_go["right"]:
            self.pos_x += 1
            self.player_can_go = {"left": False, "right": False, "up": False, "down": False}
            interface.print_map(loaded_map, screen)
        if pygame.key.get_pressed()[pygame.K_UP] and self.player_can_go["up"]:
            self.pos_y -= 1
            self.player_can_go = {"left": False, "right": False, "up": False, "down": False}
            interface.print_map(loaded_map, screen)
        if pygame.key.get_pressed()[pygame.K_DOWN] and self.player_can_go["down"]:
            self.pos_y += 1
            self.player_can_go = {"left": False, "right": False, "up": False, "down": False}
            interface.print_map(loaded_map, screen)
