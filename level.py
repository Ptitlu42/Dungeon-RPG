import pygame
from pygame.locals import *
from settings import *
from tile import Tile
from player import Player

class Level:
    def __init__(self):
        
        self.display_surface = pygame.display.get_surface()
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprite = pygame.sprite.Group()
        self.create_map()
        
    def create_map(self):
        for row_index, row in enumerate(WORLD_MAP):
            for col_index, col in enumerate(row):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if col == "x":
                    Tile((x,y), [self.visible_sprites])
                if col == "p":
                    key_pressed_is = pygame.key.get_pressed()
                    if key_pressed_is[K_LEFT]:
                        print("left")
                        x -= 64
                        Player((x,y), [self.visible_sprites])
                        pygame.display.update()
                        
                    if key_pressed_is[K_RIGHT]:
                        print("right")
                        x += 64
                        Player((x,y), [self.visible_sprites])
                        pygame.display.update()
                        
                    if key_pressed_is[K_UP]:
                        y -= 64
                        Player((x,y), [self.visible_sprites])
                        pygame.display.update()
                        print("up")
                        
                    if key_pressed_is[K_DOWN]:
                        y += 64
                        Player((x,y), [self.visible_sprites])
                        pygame.display.update()
                        print("down")
                        
                    else:                          
                        Player((x,y), [self.visible_sprites])
                    
    def run (self):
        
        self.visible_sprites.draw(self.display_surface)
                    