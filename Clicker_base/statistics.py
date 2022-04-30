import pygame.font
from Globals import Globals

class Stat():
    def __init__(self, screen):
        """Инициализирует подсчет очков"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        with open('Save_data/points.txt', 'r') as f:
            self.point_now = int(f.read())

        self.globals = Globals()

        self.font = pygame.font.SysFont("Verdana", self.globals.TEXT_SIZE)
        self.image_score(self.globals.COUNT[0], self.globals.COUNT[1])
        self.point_in_mini_game = 0

    def image_score(self, width, height):
        """Преобразование текста счета в графическое изображение"""
        self.score_img = self.font.render(str(self.point_now), True, self.globals.TEXT_COLOR, self.globals.COLOR_BACK_TEXT)
        self.score_rect = self.score_img.get_rect()
        self.score_rect.x = self.globals.TEXT_LINES_T5_XY[0]
        self.score_rect.y = self.globals.TEXT_LINES_T5_XY[1]

    def draw(self):
        """Вывод счета на экран"""
        self.screen.blit(self.score_img, self.score_rect)



