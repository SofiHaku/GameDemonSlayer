import pygame
from Mini_game_2.hero import hero
from Mini_game_2.events import control
from Mini_game_2.draw import draw

class main_mini_game_2():
    def __init__(self, screen):
        self.hero = hero(screen)
        self.control = control()
        self.draw = draw(screen)

    def run(self):
        self.control.events()
        self.draw.all(self.hero)
        self.draw.anim()
