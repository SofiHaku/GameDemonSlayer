import pygame

class Hero():
    '''Класс, главного героя, изображенного на главном экране'''
    def __init__(self, screen, name_img, globals):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.images = ["assets/Hero/Hero0.png", "assets/Hero/Hero1.png", "assets/Hero/Hero2.png", "assets/Hero/Hero3.png"]
        self.image = pygame.image.load(name_img)
        self.rect = self.image.get_rect()
        self.rect.y = globals.HERO_XY_FL[0]
        self.rect.right = globals.HERO_XY_FL[1]

    def draw(self, index):
        '''Вывод главного героя на экран'''
        self.image = pygame.image.load(self.images[index])
        self.screen.blit(self.image, self.rect)

