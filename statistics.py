import pygame.font
from settings import *

class Stat():
    def __init__(self, screen):
        """Инициализирует подсчет очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        with open('Save_data/points.txt', 'r') as f:
            self.point_now = int(f.read())

        self.font = pygame.font.SysFont("Verdana", 20)
        self.image_score(COUNT[0], COUNT[1])

    def image_score(self, width, height):
        """Преобразование текста счета в графическое изображение"""
        self.score_img = self.font.render(str(self.point_now), True, TEXT_COLOR, (255, 255, 255))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.x = 100
        self.score_rect.y = 160

    def draw(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)



