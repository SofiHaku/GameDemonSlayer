import pygame

class Hero():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # Гланый герой будет в момент инициализации появляться из левого верхнего угла
        self.image = pygame.image.load('Img/Tang.png')
        self.rect = self.image.get_rect()
        self.rect.centery = self.screen_rect.centery
        self.rect.right = self.screen_rect.right

    def draw(self):
        self.screen.blit(self.image, self.rect)
