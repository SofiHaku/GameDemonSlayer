import pygame
from settings import *

class text_message():
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.SysFont("Verdana", 20)
        self.shop_mess_hero = ["Я Незука",
                               "Я Зеницу",
                               "Я Иноске"]
        self.shop_mess_skills = ['1',
                                 '2',
                                 '3',
                                 '4',
                                 '1',
                                 '2',
                                 '3',
                                 '4'
                                 ]
        self.shop_mess_lamp = "Привет! Я чудесная подсказка по управлению! \n" \
                              "Как меня зовут? \n" \
                              "Одуванчик!"

    def draw_many_lines(self, x, y, text, size):
        lines = text.split("\n")
        for i, l in enumerate(lines):
            self.screen.blit(self.font.render(l, True, TEXT_COLOR, (255, 255, 255)), (x, y + size * i))


