import pygame
from settings import *

class draw():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image_back = pygame.image.load("Img/Mini_game_2/back2.png")
        self.image_back_rect = self.image_back.get_rect()
        self.image_back_rect.centerx = 300

        self.image_road1 = pygame.image.load("Img/Mini_game_2/road.png")
        self.image_road1_rect = self.image_road1.get_rect()
        self.image_road1_rect.y = HEIGHT - 40
        self.image_road1_rect.x = WIDTH // 4.5

        self.image_road2 = pygame.image.load("Img/Mini_game_2/road.png")
        self.image_road2_rect = self.image_road2.get_rect()
        self.image_road2_rect.y = HEIGHT - 40
        self.image_road2_rect.right = self.image_road1_rect.left

    def anim(self):
        self.image_road1_rect.left += 2
        self.image_road2_rect.left += 2
        if self.image_road1_rect.left >= self.screen_rect.right - WIDTH // 4.5:
            self.image_road1_rect.right = self.image_road2_rect.left
        elif self.image_road2_rect.left >= self.screen_rect.right - WIDTH // 4.5:
            self.image_road2_rect.right = self.image_road1_rect.left

    def all(self, hero):
        self.screen.blit(self.image_back, self.image_back_rect)
        self.screen.blit(self.image_road1, self.image_road1_rect)
        self.screen.blit(self.image_road2, self.image_road2_rect)

        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen_rect.x, self.screen_rect.y, WIDTH // 4.5, HEIGHT))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen_rect.right - WIDTH // 4.5, self.screen_rect.y,  WIDTH // 4.5, HEIGHT))

        hero.draw()
        pygame.display.flip()