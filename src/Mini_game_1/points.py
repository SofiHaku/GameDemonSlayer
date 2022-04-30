import pygame

class Point(pygame.sprite.Sprite):
    """Объекты, которые будет собирать герой"""
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load('assets/point.png')
        self.rect = self.image.get_rect()
        self.rect.bottomright = self.screen_rect.bottomright

    def draw(self):
        '''Вывод алмазиков на экран'''
        self.screen.blit(self.image, self.rect)
