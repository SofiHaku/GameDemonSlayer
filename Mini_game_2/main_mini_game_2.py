import pygame
from Mini_game_2.hero import hero
from Mini_game_2.events import control

class main_mini_game_2():
    def __init__(self, screen):
        self.hero = hero(screen)
        self.control = control()

    def run(self):
        self.hero.draw()
        self.control.events()
        pygame.display.flip()
