import pygame
import sys

class control():
    def __init__(self):
        self.count = 0
        self.play_now = False

    def start_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.play_now = True

    def events(self, hero, belt_many):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    hero.speed_down = 0
                    hero.image_rect.y -= 30

        if self.count % 80 == 0:
            belt_many.create_belt()
        self.count += 1

    def check_collision(self, hero, belt, draw):
        for blit in belt.belt_list:
            if hero.image_rect.colliderect(blit.image_rect) or hero.image_rect.y <= 0 or hero.image_rect.bottom >= draw.image_road2_rect.y:
                belt.list_emply()

                hero.count_belt = 0
                hero.speed_down = 0
                hero.image_rect.centery = hero.screen_rect.centery

                self.count = 0
                self.play_now = False

