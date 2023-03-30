# import pygame
# from pygame.locals import *
# from  settings import *
# from Case import Tile
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

    def get_image(self, x, y):
        image = pygame.Surface([Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT])
        image.blit(self.sprite_sheet, (0, 0), (x, y, Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
        return image

    def update(self):
        self.rect.topleft = [self.pos_x * Constant.SPRITE_WIDTH, self.pos_y * Constant.SPRITE_HEIGHT]

    #Coyotte move function
    def player_move(self, map, screen):
        """
        print all accessible tiles around the player and move him on key press if able
        :param loaded_map:
        :param screen:
        :return:
        """

        actual_point = self.action_point

        if self.last_x != self.pos_x or self.last_y != self.pos_y:

            # accessible cells printing
            if actual_point > 0:

                for case in map.actual_map:
                    # if the tile on the left of the player has no decoration
                    if case.pos_x == self.pos_x - 1 and case.pos_y == self.pos_y and case.deco == "":
                        pos_x = ((2 * Constant.SCREEN_WIDTH / 3) + ((Constant.SPRITE_WIDTH / 2) * (case.pos_x))) - \
                                Constant.SPRITE_WIDTH / 2 * (case.pos_y - 1)

                        pos_y = ((Constant.SPRITE_HEIGHT / 2) + ((Constant.SPRITE_HEIGHT / 2) * (case.pos_y + 1))) + \
                            Constant.SPRITE_HEIGHT / 2.5 * case.pos_x - case.pos_y * Constant.SPRITE_HEIGHT * 0.12

                        # print the accessible PNG on the tile
                        sprite_player = pygame.image.load(f"{Constant.PLAYER_TILES_PATH}accessible.png")
                        sprite_player_redim = pygame.transform.scale(sprite_player,
                                                                     (Constant.SPRITE_WIDTH,
                                                                      Constant.SPRITE_CARACTER_HEIGHT))
                        screen.blit(sprite_player_redim, (pos_x, pos_y))

                        # update the move option of the player
                        self.player_can_go["left"] = True

                    # if the tile on the right of the player has no decoration
                    if case.pos_x == self.pos_x + 1 and case.pos_y == self.pos_y and case.deco == "":
                        pos_x = ((2 * Constant.SCREEN_WIDTH / 3) + ((Constant.SPRITE_WIDTH / 2) * (case.pos_x))) - \
                                Constant.SPRITE_WIDTH / 2 * (case.pos_y - 1)

                        pos_y = ((Constant.SPRITE_HEIGHT / 2) + ((Constant.SPRITE_HEIGHT / 2) * (case.pos_y + 1))) + \
                                Constant.SPRITE_HEIGHT / 2.5 * case.pos_x - case.pos_y * Constant.SPRITE_HEIGHT * 0.12

                        # print the accessible PNG on the tile
                        sprite_player = pygame.image.load(f"{Constant.PLAYER_TILES_PATH}accessible.png")
                        sprite_player_redim = pygame.transform.scale(sprite_player,
                                                                     (Constant.SPRITE_WIDTH,
                                                                      Constant.SPRITE_CARACTER_HEIGHT))
                        screen.blit(sprite_player_redim, (pos_x, pos_y))

                        # update the move option of the player
                        self.player_can_go["right"] = True

                    # if the tile on the top of the player has no decoration
                    if case.pos_x == self.pos_x and case.pos_y == self.pos_y - 1 and case.deco == "":
                        pos_x = ((2 * Constant.SCREEN_WIDTH / 3) + ((Constant.SPRITE_WIDTH / 2) * (case.pos_x))) - \
                                Constant.SPRITE_WIDTH / 2 * (case.pos_y - 1)

                        pos_y = ((Constant.SPRITE_HEIGHT / 2) + ((Constant.SPRITE_HEIGHT / 2) * (case.pos_y + 1))) + \
                                Constant.SPRITE_HEIGHT / 2.5 * case.pos_x - case.pos_y * Constant.SPRITE_HEIGHT * 0.12

                        # print the accessible PNG on the tile
                        sprite_player = pygame.image.load(f"{Constant.PLAYER_TILES_PATH}accessible.png")
                        sprite_player_redim = pygame.transform.scale(sprite_player,
                                                                     (Constant.SPRITE_WIDTH,
                                                                      Constant.SPRITE_CARACTER_HEIGHT))
                        screen.blit(sprite_player_redim, (pos_x, pos_y))

                        # update the move option of the player
                        self.player_can_go["up"] = True

                    # if the tile on the top of the player has no decoration
                    if case.pos_x == self.pos_x and case.pos_y == self.pos_y + 1 and case.deco == "":
                        # accessible cells printing
                        pos_x = ((2 * Constant.SCREEN_WIDTH / 3) + ((Constant.SPRITE_WIDTH / 2) * (case.pos_x))) - \
                                Constant.SPRITE_WIDTH / 2 * (case.pos_y - 1)

                        pos_y = ((Constant.SPRITE_HEIGHT / 2) + ((Constant.SPRITE_HEIGHT / 2) * (case.pos_y + 1))) + \
                                Constant.SPRITE_HEIGHT / 2.5 * case.pos_x - case.pos_y * Constant.SPRITE_HEIGHT * 0.12

                        # print the accessible PNG on the tile
                        sprite_player = pygame.image.load(f"{Constant.PLAYER_TILES_PATH}accessible.png")
                        sprite_player_redim = pygame.transform.scale(sprite_player,
                                                                     (Constant.SPRITE_WIDTH,
                                                                      Constant.SPRITE_CARACTER_HEIGHT))
                        screen.blit(sprite_player_redim, (pos_x, pos_y))

                        # update the move option of the player
                        self.player_can_go["down"] = True


                    #screen.fill(Constant.TRANSP)
                    interface.print_player(self, screen)
                    #pygame.display.flip()
                    self.last_x = self.pos_x
                    self.last_y = self.pos_y

        # applying the movement to the player
        if pygame.key.get_pressed()[pygame.K_LEFT] and self.player_can_go["left"]:
            self.pos_x -= 1
            self.player_can_go = {"left": False, "right": False, "up": False, "down": False}

        if pygame.key.get_pressed()[pygame.K_RIGHT] and self.player_can_go["right"]:
            self.pos_x += 1
            self.player_can_go = {"left": False, "right": False, "up": False, "down": False}

        if pygame.key.get_pressed()[pygame.K_UP] and self.player_can_go["up"]:
            self.pos_y -= 1
            self.player_can_go = {"left": False, "right": False, "up": False, "down": False}

        if pygame.key.get_pressed()[pygame.K_DOWN] and self.player_can_go["down"]:
            self.pos_y += 1
            self.player_can_go = {"left": False, "right": False, "up": False, "down": False}

