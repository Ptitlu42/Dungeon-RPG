import pygame
from pygame.locals import *
from Case import Tile

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load("sprites/player.png").convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
    # def Run():
    #     pass
    