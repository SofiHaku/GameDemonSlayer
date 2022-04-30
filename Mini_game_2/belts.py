import pygame
import random
from Globals import Globals

class belt():
    def __init__(self):
        self.image = pygame.image.load("Img/Mini_game_2/p.png")
        self.image_rect = self.image.get_rect()
        self.image_rect.x = 500

class many_belts():
    def __init__(self, screen):
        self.globals = Globals()
        self.screen = screen
        self.belt_list = []
        self.belt_height = [200, 250, 300, 350]

    def create_belt(self):
        random_belt_pos = random.choice(self.belt_height)

        bottom_belt = belt()
        bottom_belt.image_rect.y = random_belt_pos

        top_belt = belt()
        top_belt.image_rect.bottom = random_belt_pos - 150
        self.belt_list.append(bottom_belt)
        self.belt_list.append(top_belt)

    def move_belts(self):
        for belt in self.belt_list:
            belt.image_rect.centerx -= 3

    def draw_belts(self):
        for belt in self.belt_list:
            self.screen.blit(belt.image, belt.image_rect)

    def remove_belts(self, hero):
        for belt in self.belt_list:
            if belt.image_rect.right <= self.globals.WIDTH // 4.5:
                self.belt_list.remove(belt)
                hero.count_belt += 0.5

    def list_emply(self):
        self.belt_list = []
