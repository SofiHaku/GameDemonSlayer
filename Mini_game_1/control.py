import pygame
import sys

class Demon_n():
    def __init__(self):
        pass

    def demon_6_moon(self, in_lab_game, hero_mini, wall):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    hero_mini.move_to_up = True
                elif event.key == pygame.K_DOWN:
                    hero_mini.move_to_down = True
                elif event.key == pygame.K_RIGHT:
                    hero_mini.move_to_right = True
                elif event.key == pygame.K_LEFT:
                    hero_mini.move_to_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    hero_mini.move_to_up = False
                elif event.key == pygame.K_DOWN:
                    hero_mini.move_to_down = False
                elif event.key == pygame.K_RIGHT:
                    hero_mini.move_to_right = False
                elif event.key == pygame.K_LEFT:
                    hero_mini.move_to_left = False

        in_lab_game.corner_hero(hero_mini, wall)