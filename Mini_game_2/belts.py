import pygame
import random

class belt():
    def __init__(self):
        self.image = pygame.image.load("Img/Mini_game_2/p.png")
        self.image_rect = self.image.get_rect()
        self.image_rect.x = 500

class many_belts():
    def __init__(self, screen):
        self.screen = screen
        self.belt_list = []
        self.belt_height = [270, 260, 300]

    def create_belt(self):
        random_belt_pos = random.choice(self.belt_height)

        bottom_belt = belt()
        bottom_belt.image_rect.y = random_belt_pos

        top_belt = belt()
        top_belt.image_rect.y = 200 - random_belt_pos
        self.belt_list.append(bottom_belt)
        self.belt_list.append(top_belt)

    def move_belts(self):
        for belt in self.belt_list:
            belt.image_rect.centerx -= 3

    def draw_belts(self):
        self.screen.blit(self.belt_list[0].image, self.belt_list[0].image_rect)
        for belt in self.belt_list:
            self.screen.blit(belt.image, belt.image_rect)

    def remove_belts(self):
        for belt in self.belt_list:
            if belt.image_rect.x <= 40:
                self.belt_list.remove(belt)