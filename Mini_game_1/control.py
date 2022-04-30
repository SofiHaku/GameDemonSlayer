import pygame
import sys

class control():
    '''Контроль движения героя'''
    def __init__(self):
        pass

    def hero(self, in_lab_game, hero_mini, wall):
        '''Контроль движения героя'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.button_down(event, hero_mini)
            elif event.type == pygame.KEYUP:
                self.button_up(event, hero_mini)
        in_lab_game.corner_hero(hero_mini, wall)

    def button_down(self, event, hero_mini):
        '''Контроль движения героя при нажатии на кнопку'''
        if event.key == pygame.K_UP:
            hero_mini.move_to_up = True
        elif event.key == pygame.K_DOWN:
            hero_mini.move_to_down = True
        elif event.key == pygame.K_RIGHT:
            hero_mini.move_to_right = True
        elif event.key == pygame.K_LEFT:
            hero_mini.move_to_left = True

    def button_up(self, event, hero_mini):
        '''Контроль движения героя при отпускании кнопки'''
        if event.key == pygame.K_UP:
            hero_mini.move_to_up = False
        elif event.key == pygame.K_DOWN:
            hero_mini.move_to_down = False
        elif event.key == pygame.K_RIGHT:
            hero_mini.move_to_right = False
        elif event.key == pygame.K_LEFT:
            hero_mini.move_to_left = False