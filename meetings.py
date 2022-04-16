import pygame
import time

class meeting():
    def __init__(self):
        pass

    def eat_points(self, hero_game, points):
        if pygame.sprite.spritecollide(hero_game, points, True):
            pass

    '''def with_demon(self, demon, points, hero_game, screen, wall, make_many_object_game):

        if pygame.Rect.colliderect(hero_game.rect, demon.rect):
            points.empty()
            make_many_object_game.point(points, wall)
            print("Yes")'''
