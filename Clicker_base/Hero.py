import pygame

class Hero():

    def __init__(self, screen, name_img):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.images = ["Img/Hero/Hero0.png", "Img/Hero/Hero1.png", "Img/Hero/Hero2.png", "Img/Hero/Hero3.png"]
        self.image = pygame.image.load(name_img)
        self.rect = self.image.get_rect()
        self.rect.y = 185
        self.rect.right = 550

    def draw(self, index):
        self.image = pygame.image.load(self.images[index])
        self.screen.blit(self.image, self.rect)

