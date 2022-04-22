import pygame
import sys

class control():
    def __init__(self):
        self.count = 0

    def events(self, hero, belt_many):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hero.speed_down = 0
                    hero.image_rect.y -= 30

        if self.count % 40 == 0:
            belt_many.create_belt()
        self.count += 1

