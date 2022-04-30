import pygame
import random
from src.globals import Globals

class belt():
    '''Класс движущих поясов, между которых будет пролетать персонаж'''
    def __init__(self, globals):
        self.image = pygame.image.load("assets/Mini_game_2/p.png")
        self.image_rect = self.image.get_rect()
        self.image_rect.x = globals.BELT_X

class many_belts():
    '''Рандомное создание многих поясов'''
    def __init__(self, screen):
        self.globals = Globals()
        self.screen = screen
        self.belt_list = []
        self.belt_height = self.globals.belt_height

    def create_belt(self):
        '''Создание пары поясов: снизу и сверху'''
        random_belt_pos = random.choice(self.belt_height)

        bottom_belt = belt(self.globals)
        bottom_belt.image_rect.y = random_belt_pos

        top_belt = belt(self.globals)
        top_belt.image_rect.bottom = random_belt_pos - self.globals.DIF_WITH_B
        self.belt_list.append(bottom_belt)
        self.belt_list.append(top_belt)

    def move_belts(self):
        '''Движение поясов'''
        for belt in self.belt_list:
            belt.image_rect.centerx -= 3

    def draw_belts(self):
        '''Вывод на экран'''
        for belt in self.belt_list:
            self.screen.blit(belt.image, belt.image_rect)

    def remove_belts(self, hero):
        '''Удаление поясов, вышедших за границы игрового экрана'''
        for belt in self.belt_list:
            if belt.image_rect.right <= self.globals.START_X:
                self.belt_list.remove(belt)
                hero.count_belt += 0.5

    def list_emply(self):
        '''Опустошение всего массива с поясами'''
        self.belt_list = []
