import pygame
from Globals import Globals

class draw():
    def __init__(self, screen):
        self.globals  = Globals()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image_back = pygame.image.load("Img/Mini_game_2/back2.png")
        self.image_back_rect = self.image_back.get_rect()
        self.image_back_rect.centerx = 300

        self.image_road1 = pygame.image.load("Img/Mini_game_2/road.png")
        self.image_road1_rect = self.image_road1.get_rect()
        self.image_road1_rect.y = self.globals.HEIGHT - 30
        self.image_road1_rect.x = self.globals.WIDTH // 4.5

        self.image_road2 = pygame.image.load("Img/Mini_game_2/road.png")
        self.image_road2_rect = self.image_road2.get_rect()
        self.image_road2_rect.y = self.globals.HEIGHT - 30
        self.image_road2_rect.right = self.image_road1_rect.left

        self.image_tap = pygame.image.load("Img/Mini_game_2/tap_to_play.png")
        self.image_tap_rect = self.image_road1.get_rect()
        self.image_tap_rect.y = 185
        self.image_tap_rect.x = 250

    def anim(self):
        self.image_road1_rect.left += 1
        self.image_road2_rect.left += 1
        if self.image_road1_rect.left >= self.screen_rect.right - self.globals.WIDTH // 4.5:
            self.image_road1_rect.right = self.image_road2_rect.left
        elif self.image_road2_rect.left >= self.screen_rect.right - self.globals.WIDTH // 4.5:
            self.image_road2_rect.right = self.image_road1_rect.left

    def all(self, hero, many_belts):
        self.screen.blit(self.image_back, self.image_back_rect)
        many_belts.draw_belts()
        self.screen.blit(self.image_road1, self.image_road1_rect)
        self.screen.blit(self.image_road2, self.image_road2_rect)

        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen_rect.x, self.screen_rect.y, self.globals.WIDTH // 4.5, self.globals.HEIGHT))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen_rect.right - self.globals.WIDTH // 4.5, self.screen_rect.y,  self.globals.WIDTH // 4.5, self.globals.HEIGHT))

        hero.draw()

    def draw(self):
        self.screen.blit(self.image_tap, self.image_tap_rect)

    def flip(self):
        pygame.display.flip()

