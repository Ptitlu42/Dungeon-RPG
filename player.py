import time
import random
import Constant
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, name, strength, life, speed, const, action_point, inventory, equiped_stuff, sprite, pos_x,
                 pos_y):
        super().__init__()
        self.name = name
        self.stuff_list = None
        self.id_list = None
        self.sprite_sheet = pygame.image.load(f'{Constant.PLAYER_PATH}basic.png')
        self.image = self.get_image(0, 0)
        self.rect = self.image.get_rect()
        self.image.set_colorkey(Constant.BLACK)

        # our data
        self.strength = strength
        self.strength_mod = strength
        self.life = life
        self.life_mod = life
        self.speed = speed
        self.speed_mod = speed
        self.const = const
        self.const_mod = const
        self.action_point = action_point
        self.action_point_mod = action_point
        self.inventory = inventory
        self.equiped_stuff = equiped_stuff
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

    def get_id_equiped_from_player(self, player) -> list:
        equiped_ids_stuff_list = []
        for ids in player.equiped_stuff.items():
            if ids[1] != "":
                equiped_ids_stuff_list.append(ids[1])
        return equiped_ids_stuff_list

    def get_items_from_ids_list(self, list, game) -> list:
        equiped_stuff_list = []
        for id_item in list:
            equiped_stuff_list.append(game.item.get_item_id(id_item, game.item_list))
        return equiped_stuff_list

    def stat_with_mods(self, equiped_stuff_list):
        for item in equiped_stuff_list:
            self.strength.mod += item.strength_mod
            self.speed.mod += item.speed_mod
            self.const_mod += item.const_mod
            self.life_mod += item.life_mod

    def get_mod_from_player(self, game):
        self.id_list = self.get_id_equiped_from_player(self)
        self.stuff_list = self.get_items_from_ids_list(self.id_list, game)
        self.stat_with_mods(self.stuff_list)

    # Coyotte move function
    def player_move(self, map, screen, interface, game):
        """
        print all accessible tiles around the player and move him on key press if able
        :param game:
        :param map:
        :param interface:
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
            footsteps = f"{Constant.FOOTSTEPS_SOUNDS}footsteps.mp3"
            footsteps_sound = pygame.mixer.Sound(footsteps)
            footsteps_sound.play(0)
            time.sleep(0.2)

    def player_melee(self, map, screen, interface, game):
        """
        Attack an entity in an orthogonal cell.
        :param map:
        :param screen:
        :param interface:
        :return:
        """

        self.last_action = "melee"
        player_has_attacked, target = False, False

        if self.actual_point > 0:
            if pygame.key.get_pressed()[pygame.K_LEFT] and self.player_can_go["left"]:
                target = (-1, 0)
                player_has_attacked = True
            if pygame.key.get_pressed()[pygame.K_RIGHT] and self.player_can_go["right"]:
                target = (1, 0)
                player_has_attacked = True
            if pygame.key.get_pressed()[pygame.K_UP] and self.player_can_go["up"]:
                target = (0, -1)
                player_has_attacked = True
            if pygame.key.get_pressed()[pygame.K_DOWN] and self.player_can_go["down"]:
                target = (0, 1)
                player_has_attacked = True

            if player_has_attacked:
                self.actual_point -= 1
                target_cell = map.get_cell_by_xy(self.pos_x + target[0], self.pos_y + target[1])
                target_caracter = target_cell.occuped_by
                if self.strength_mod > target_caracter.const_mod:
                    length = len(game.player_list)
                    for i in range(length):
                        if game.player_list[i].name == target_caracter.name:
                            game.player_list[i].life_mod -= self.strength_mod - game.player_list[i].const_mod
                interface.print_map(map, screen, self, game)
                paf = pygame.image.load(f"{Constant.MISC}paf.png")
                paf_redim = pygame.transform.scale(paf, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
                pos_x = ((2 * Constant.SCREEN_WIDTH / 3) + (
                        (Constant.SPRITE_WIDTH / 2) * (target_caracter.pos_x + 1))) - \
                        Constant.SPRITE_WIDTH / 2 * target_caracter.pos_y

                pos_y = ((Constant.SPRITE_CARACTER_HEIGHT / 2) + (
                        (Constant.SPRITE_CARACTER_HEIGHT / 2) * (target_caracter.pos_y + 1))) + \
                        Constant.SPRITE_CARACTER_HEIGHT / 2.5 * target_caracter.pos_x - target_caracter.pos_y * Constant.SPRITE_CARACTER_HEIGHT * 0.12 \
                        - Constant.SPRITE_HEIGHT / 3
                screen.blit(paf_redim, (pos_x, pos_y))
                pygame.display.flip()
                aleatoire = random.randint(1, 6)
                hit = f"{Constant.HIT_SOUNDS}hit{aleatoire}.mp3"
                hit_sound = pygame.mixer.Sound(hit)
                hit_sound.play(0)
                time.sleep(0.5)

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
        weapon = game.item.get_item_id(self.equiped_stuff["right hand"], game.item_list)
        keys = pygame.key.get_pressed()
        for i, target in enumerate(interface.ranged_target_list):
            # Vérifier si la touche correspondante est enfoncée
            if keys[pygame.K_0 + i] and target is not None:
                target.life_mod -= weapon.ranged_damage
                self.actual_point -= 1
                arrow = pygame.image.load(f"{Constant.MISC}arrow.png")
                paf_redim = pygame.transform.scale(arrow, (Constant.SPRITE_WIDTH, Constant.SPRITE_HEIGHT))
                pos_x = ((2 * Constant.SCREEN_WIDTH / 3) + (
                        (Constant.SPRITE_WIDTH / 2) * (interface.ranged_target_list[i].pos_x + 1))) - \
                        Constant.SPRITE_WIDTH / 2 * interface.ranged_target_list[i].pos_y

                pos_y = ((Constant.SPRITE_CARACTER_HEIGHT / 2) + (
                        (Constant.SPRITE_CARACTER_HEIGHT / 2) * (interface.ranged_target_list[i].pos_y + 1))) + \
                        Constant.SPRITE_CARACTER_HEIGHT / 2.5 * interface.ranged_target_list[i].pos_x - \
                        interface.ranged_target_list[i].pos_y * Constant.SPRITE_CARACTER_HEIGHT * 0.12 \
                        - Constant.SPRITE_HEIGHT / 3
                screen.blit(paf_redim, (pos_x, pos_y))
                pygame.display.flip()
                aleatoire = random.randint(1, 6)
                hit = f"{Constant.ARROW_SOUNDS}arrow{aleatoire}.mp3"
                hit_sound = pygame.mixer.Sound(hit)
                hit_sound.play(0)
                time.sleep(0.5)

        interface.print_map(map, screen, self, game)
