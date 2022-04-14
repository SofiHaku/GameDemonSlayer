import pygame
from settings import *

class Hero():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('Img/Hero/Tang.png')
        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right
        self.x = 0

        self.speed = 1

        # Логические переменные для управления движением игрока
        # Движение в данный момент и потенциально возможное

        self.move_to_up = False
        self.move_to_down = False

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.move_to_up:
            self.rect.centery -= self.speed
        elif self.move_to_down:
            self.rect.centery += self.speed
