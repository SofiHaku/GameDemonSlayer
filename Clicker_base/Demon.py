import pygame
import random
from Globals import Globals
from Demon_b import Demon

class Demon_ordinary(Demon):
    '''Класс демонов, летающих на главном экране'''
    def __init__(self, screen):
        '''Класс-ребенок'''
        super().__init__(screen)
        self.globals = Globals()

        # Атрибуты изображения демона
        self.image = pygame.image.load('Img/Demons/demon_classic_1.png')
        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.left = self.globals.SETTING + 30
        self.count_life = self.globals.DEMON_W - 8

        # Массив изображений демона
        self.image_set = ["demon_classic_1.png", "demon_classic_2.png", "demon_classic_3.png"]

        # Атрибуты, отвечающие за движение демона
        self.speed = 2
        self.move_to_up = True
        self.move_to_down = False


    def move(self):
        """Движение демона"""
        if self.move_to_up:
            if (self.rect.top - 20) > 10:
                self.rect.centery -= self.speed
            else:
                self.move_to_up = False
        else:
            if (self.rect.bottom + 20) < self.globals.HEIGHT - 10 :
                self.rect.centery += self.speed
            else:
                 self.move_to_up = True

    def update_count_life(self, damage):
        """Урон, наносимый демону"""
        self.count_life -= damage

    def create(self):
        """Создание нового демона"""
        self.image = pygame.image.load('Img/Demons/' + self.image_set[random.randint(0,2)])
        self.rect.centery = self.screen_rect.centery
        self.count_life = self.globals.DEMON_W - 8
        self.move_to_up = True
        self.move_to_down = False

    def die(self):
        """Проверка, жив ли демон или нет"""
        if self.count_life > 0:
            return False
        return True

    def draw_streak_of_life(self):
        """Вывод полокски жизни на экран"""
        pygame.draw.rect(self.screen, (255, 255, 255), (self.rect.x, self.rect.y - 20, self.globals.DEMON_W, 20))
        pygame.draw.rect(self.screen, (221, 44, 0), (self.rect.x + 4, self.rect.y - 20 + 4, self.count_life, 12))
