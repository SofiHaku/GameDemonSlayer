import pygame

class Hero():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('Img/Hero/Tang.png')
        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

    def draw(self):
        self.screen.blit(self.image, self.rect)
