import pygame
import random
import time
from settings import *

class Demon():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.name = None
        self.count_life = None

        self.image = None
        self.rect = None
        self.wight = None
        self.height = None


    def draw(self):
        self.screen.blit(self.image, self.rect)

    def die(self):
        if self.count_life > 0:
            return False
        return True

    def draw_streak_of_life(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.rect.x, self.rect.y - 20, DEMON_W, 20))
        pygame.draw.rect(self.screen, (221, 44, 0), (self.rect.x + 4, self.rect.y - 20 + 4, self.count_life, 12))


class Demon_ordinary(Demon):

    def __init__(self, screen):
        super().__init__(screen)
        self.image = pygame.image.load('Img/Demons/demon_classic_1.png')
        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.left = SETTING + 30
        self.speed = 2
        self.move_to_up = True
        self.move_to_down = False
        self.count_life = DEMON_W - 8
        self.image_set = ["demon_classic_1.png", "demon_classic_2.png", "demon_classic_3.png"]

    def move(self):
        if self.move_to_up:
            if (self.rect.top - 20) > 10:
                self.rect.centery -= self.speed
            else:
                self.move_to_up = False
        else:
            if (self.rect.bottom + 20) < HEIGHT - 10 :
                self.rect.centery += self.speed
            else:
                 self.move_to_up = True

    def update_count_life(self, damage):
        self.count_life -= damage

    def create(self):
        self.count_life = DEMON_W - 8
        self.rect.centery = self.screen_rect.centery
        self.move_to_up = True
        self.move_to_down = False
        self.image = pygame.image.load('Img/Demons/' + self.image_set[random.randint(0,2)])


class Demon_6_moon(Demon):

    def __init__(self, screen):
        super().__init__(screen)

        self.screen = screen
        self.image = pygame.image.load('Img/Demon_6_moon/Mini_t.png')
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 19
        self.x = 200
        self.y = 19

        self.speed = 1

        # Логические переменные для управления движением:
        # Массивы: движение в данный момент, прежде, потенциально возможное
        # [0] = влево, [1] = вправо, [2] = вверх, [3] = вниз
        self.move = [0, 0, 0, 0]
        self.move_before = [0, 0, 1, 0]
        self.can_move = [0, 0, 0, 0]

        # Логические константы
        self.mass_l = [1, 0, 0, 0]
        self.mass_r = [0, 1, 0, 0]
        self.mass_u = [0, 0, 1, 0]
        self.mass_d = [0, 0, 0, 1]

        self.time_before = time.time()
        self.time_now = time.time()
        self.place_to_move = [[180 + 5*20, 3*19], [180 + 15*20, 3*19], [180 + 5*20, 13*19], [180 + 15*20, 13*19],
                              [180 + 7*20, 7*19], [180 + 13*20, 7*19], [180 + 7*20, 11*19], [180 + 13*20, 11*19]]


    def movement(self):
        self.time_now = time.time()
        if (self.time_now - self.time_before) > 10:
            random_ind = random.randint(0, 7)
            self.x = self.place_to_move[random_ind][0]
            self.y = self.place_to_move[random_ind][1]
            self.rect.x = self.place_to_move[random_ind][0]
            self.rect.y = self.place_to_move[random_ind][1]
            self.time_before = time.time()

    def update(self):
        """функция обновляет объект и изменяет его местоположение"""
        #Движение по прямой линии

        if self.move[0]:
            self.x -= self.speed
            self.rect.x = self.x
            self.move_before = self.mass_l.copy()
        elif self.move[1]:
            self.x += self.speed
            self.rect.x = self.x
            self.move_before = self.mass_r.copy()
        elif self.move[2]:
            self.y -= self.speed
            self.rect.y = self.y
            self.move_before = self.mass_u.copy()
        elif self.move[3]:
            self.y += self.speed
            self.rect.y = self.y
            self.move_before = self.mass_d.copy()

        #В углах
        elif self.can_move[0] and self.can_move[1] and self.can_move[3]:
            if self.move_before[0]:
                if random.randint(0, 1):
                    self.move = self.mass_d.copy()
            elif self.move_before[1]:
                if random.randint(0, 1):
                    self.move = self.mass_d.copy()
            else:
                if random.randint(0, 1):
                    self.move = self.mass_l.copy()
                else:
                    self.move = self.mass_r.copy()
        elif self.can_move[1] and self.can_move[2] and self.can_move[3]:
            if self.move_before[2]:
                if random.randint(0, 1):
                    self.move = self.mass_r.copy()
            elif self.move_before[3]:
                if random.randint(0, 1):
                    self.move = self.mass_r.copy()
            else:
                if random.randint(0, 1):
                    self.move = self.mass_u.copy()
                else:
                    self.move = self.mass_d.copy()
        elif self.can_move[0] and self.can_move[1] and self.can_move[2]:
            if self.move_before[0]:
                if random.randint(0, 1):
                    self.move = self.mass_u.copy()
            elif self.move_before[1]:
                if random.randint(0, 1):
                    self.move = self.mass_u.copy()
            else:
                if random.randint(0, 1):
                    self.move = self.mass_l.copy()
                else:
                    self.move = self.mass_r.copy()
        elif self.can_move[0] and self.can_move[2] and self.can_move[3]:
            if self.move_before[2]:
                if random.randint(0, 1):
                    self.move = self.mass_l.copy()
            elif self.move_before[3]:
                if random.randint(0, 1):
                    self.move = self.mass_l.copy()
            else:
                if random.randint(0, 1):
                    self.move = self.mass_u.copy()
                else:
                    self.move = self.mass_d.copy()

        elif self.can_move[1] and self.can_move[3]:
            if self.move_before[2]:
                self.move = self.mass_r.copy()
            else:
                self.move = self.mass_d.copy()
        elif self.can_move[1] and self.can_move[2]:
            if self.move_before[3]:
                self.move = self.mass_r.copy()
            else:
                self.move = self.mass_u.copy()
        elif self.can_move[0] and self.can_move[2]:
            if self.move_before[3]:
                self.move = self.mass_l.copy()
            else:
                self.move = self.mass_u.copy()
        elif self.can_move[0] and self.can_move[3]:
            if self.move_before[2]:
                self.move = self.mass_l.copy()
            else:
                self.move = self.mass_d.copy()
        else:
            if self.move_before[0]:
                self.move = self.mass_r.copy()
            else:
                self.move = self.mass_l.copy()










