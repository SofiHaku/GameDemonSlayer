import pygame
import time

class meeting():
    def __init__(self):
        pass

    def eat_points(self, hero_game, points):
        if pygame.sprite.spritecollide(hero_game, points, True):
            pass
