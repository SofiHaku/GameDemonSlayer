import pygame
import random
import time
from src.demon_b import Demon

class Demon_6_moon(Demon):
    '''Класс демона, движущего по лабиринту'''
    def __init__(self, screen, globals):
        super().__init__(screen)

        self.screen = screen
        self.image = pygame.image.load('assets/Demon_6_moon/demon.png')
        self.rect = self.image.get_rect()
        self.rect.x = globals.RECT_DEMON[0]
        self.rect.y = globals.RECT_DEMON[1]
        self.x = globals.RECT_DEMON[0]
        self.y = globals.RECT_DEMON[1]

        self.speed = 3

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
        self.place_to_move = globals.PLACE_TO_MOVE


    '''def movement(self):
        """функция, которая переносит демона в контрольные точки"""
        self.time_now = time.time()
        if (self.time_now - self.time_before) > 10:
            random_ind = random.randint(0, 7)
            self.x = self.place_to_move[random_ind][0]
            self.y = self.place_to_move[random_ind][1]
            self.rect.x = self.place_to_move[random_ind][0]
            self.rect.y = self.place_to_move[random_ind][1]
            self.time_before = time.time()'''

    def update(self):
        """функция обновляет объект и изменяет его местоположение"""

        if not self.moving_straight():
            if not self.moving_in_3_angle():
                self.moving_in_2_angle()

    def moving_straight(self):
        '''Движение демона по прямой линии'''
        res = True
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
        else:
            res = False
        return res

    def moving_in_3_angle(self):
        '''Движение демона в угле, где есть 3 возможных пути'''
        res = True
        if self.can_move[0] and self.can_move[1] and self.can_move[3]:
            self.angle_013()
        elif self.can_move[1] and self.can_move[2] and self.can_move[3]:
            self.angle_123()
        elif self.can_move[0] and self.can_move[1] and self.can_move[2]:
            self.angle_012()
        elif self.can_move[0] and self.can_move[2] and self.can_move[3]:
            self.angle_023()
        else:
            res = False
        return res

    def angle_013(self):
        '''Движение демона в угле, где он может повернуть налево, направо и вниз'''
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

    def angle_123(self):
        '''Движение демона в угле, где он может повернуть направо, вверх и вниз'''
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

    def angle_012(self):
        '''Движение демона в угле, где он может повернуть направо, налево и вверх'''
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

    def angle_023(self):
        '''Движение демона в угле, где он может повернуть налево, вверх и вниз'''
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

    def moving_in_2_angle(self):
        '''Движение демона в угле, где есть 2 возможных пути'''
        if self.can_move[1] and self.can_move[3]:
            self.angle_13()
        elif self.can_move[1] and self.can_move[2]:
            self.angle_12()
        elif self.can_move[0] and self.can_move[2]:
            self.angle_02()
        elif self.can_move[0] and self.can_move[3]:
            self.angle_03()
        else:
            self.angle_23()

    def angle_13(self):
        '''Движение демона в угле, где он может повернуть направо и вниз'''
        if self.move_before[2]:
            self.move = self.mass_r.copy()
        else:
            self.move = self.mass_d.copy()

    def angle_12(self):
        '''Движение демона в угле, где он может повернуть направо и вверх'''
        if self.move_before[3]:
            self.move = self.mass_r.copy()
        else:
            self.move = self.mass_u.copy()

    def angle_02(self):
        '''Движение демона в угле, где он может повернуть налево и вверх'''
        if self.move_before[3]:
            self.move = self.mass_l.copy()
        else:
            self.move = self.mass_u.copy()

    def angle_03(self):
        '''Движение демона в угле, где он может повернуть налево и вниз'''
        if self.move_before[2]:
            self.move = self.mass_l.copy()
        else:
            self.move = self.mass_d.copy()

    def angle_23(self):
        '''Движение демона в угле, где он может повернуть вверх и вниз'''
        if self.move_before[0]:
            self.move = self.mass_r.copy()
        else:
            self.move = self.mass_l.copy()