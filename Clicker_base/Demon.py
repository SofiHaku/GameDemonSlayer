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
        self.rect.left = self.globals.DEMON_CL_L
        self.count_life = self.globals.DEMON_LIFE

        # Массив изображений демона
        self.image_set = ["demon_classic_1.png", "demon_classic_2.png", "demon_classic_3.png"]

        # Атрибуты, отвечающие за движение демона
        self.speed = 2
        self.move_to_up = True
        self.move_to_down = False


    def move(self):
        """Движение демона"""
        if self.move_to_up:
            if (self.rect.top - self.globals.MOVE_DEMON_SIZE_TO_END) > 0:
                self.rect.centery -= self.speed
            else:
                self.move_to_up = False
        else:
            if (self.rect.bottom + self.globals.MOVE_DEMON_SIZE_TO_END) < self.globals.HEIGHT:
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
        self.count_life = self.globals.DEMON_LIFE
        self.move_to_up = True
        self.move_to_down = False

    def die(self):
        """Проверка, жив ли демон или нет"""
        if self.count_life > 0:
            return False
        return True

    def draw_streak_of_life(self):
        """Вывод полокски жизни на экран"""
        pygame.draw.rect(self.screen, self.globals.COLOR_STEAK_BL, (self.rect.x, self.rect.y - self.globals.DEMON_STEAK_LIFE_S,
                                                        self.globals.DEMON_W, self.globals.DEMON_STEAK_LIFE_S))
        pygame.draw.rect(self.screen, self.globals.COLOR_STEAK_SL, (self.rect.x + self.globals.DIFF_SMALL_AND_BIG_DEMON_STEAK_LIFE,
                                                     self.rect.y - self.globals.DEMON_STEAK_LIFE_S + self.globals.DIFF_SMALL_AND_BIG_DEMON_STEAK_LIFE,
                                                     self.count_life, self.globals.DEMON_STEAK_LIFE_S - 2 * self.globals.DIFF_SMALL_AND_BIG_DEMON_STEAK_LIFE))
