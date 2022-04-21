import pygame
import sys

class control():
    def __init__(self):
        pass

    def events(self, hero):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hero.speed_down = 0
                    hero.image_rect.y -= 30

