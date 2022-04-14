import pygame
import random
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


class Demon_normal(Demon):

    def __init__(self, screen):
        super().__init__(screen)
        self.image = pygame.image.load('Img/Demons/demon_classic_1.png')
        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.left = SETTING
        self.speed = 3
        self.move_to_up = True
        self.move_to_down = False
        self.count_life = DEMON_W - 8
        self.image_set = ["demon_classic_1.png", "demon_classic_2.png", "demon_classic_3.png", "demon_classic_4.png"]

    def move(self):
        if self.move_to_up:
            if self.rect.top > 0:
                self.rect.centery -= self.speed
            else:
                self.move_to_up = False
        else:
            if self.rect.bottom < HEIGHT:
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
        self.image = pygame.image.load('Img/Demons/' + self.image_set[random.randint(0,3)])










