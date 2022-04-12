import pygame.font
from settings import *

class Stat():
    def __init__(self, screen):
        """Инициализирует подсчет очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        with open('points.txt', 'r') as f:
            self.point_now = int(f.read())

        self.text_color = TEXT_COLOR
        self.font = pygame.font.SysFont("Verdana", 20)
        self.image_score()

    def image_score(self):
        """Преобразование текста счета в графическое изображение"""
        self.score_img = self.font.render(str(self.point_now), True, self.text_color, B_COLOR)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - WIDTH / 21
        self.score_rect.top = 5

    def draw(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)

