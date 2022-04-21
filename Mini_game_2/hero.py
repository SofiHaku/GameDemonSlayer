import pygame

class hero():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("Img/Mini_game_2/hero.png")
        self.image_rect = self.image.get_rect()
        self.image_rect.centery = self.screen_rect.centery
        self.image_rect.x = 200
        self.gravity = 0.2
        self.speed_down = 0

    def draw(self):
        self.screen.blit(self.image, self.image_rect)

    def update(self):
        self.speed_down += self.gravity
        self.image_rect.y += self.speed_down



