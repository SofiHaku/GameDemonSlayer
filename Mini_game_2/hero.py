import pygame

class hero():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image = pygame.image.load("Img/Mini_game_2/hero.png")
        self.image_rect = self.image.get_rect()
        self.image_rect.centery = self.screen_rect.centery

    def draw(self):
        self.screen.blit(self.image, self.image_rect)
