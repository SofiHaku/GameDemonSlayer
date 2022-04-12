import pygame

class Hero_shop():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #self.image = None
        self.rect = None

    def draw(self):
        self.screen.blit(self.image, self.rect)

class Shop():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.b_image = pygame.image.load('Img/Shop/Back.png')
        self.now_image = pygame.image.load('Img/Shop/Shop.png')
        self.exc = pygame.image.load('Img/Shop/Exc.png')

        self.b_image_rect = self.b_image.get_rect()
        self.now_image_rect = self.now_image.get_rect()
        self.exc_rect = self.exc.get_rect()

        self.b_image_rect.x = 0
        self.b_image_rect.y = 0

        self.now_image_rect.x = 20
        self.now_image_rect.y = 200

        self.exc_rect.x = 500
        self.exc_rect.y = 20

        self.draw_back_bool = False

        self.herous = []

        for i in range(1,4):
            hero_game = Hero_shop(screen)
            hero_game.image = pygame.image.load('Img/Shop/Hero/Hero'+ str(i)+'.png')
            hero_game.rect = hero_game.image.get_rect()
            hero_game.rect.x = 50 * i + (i - 1)* 150
            hero_game.rect.y = 30
            self.herous.append(hero_game)


    def draw_now(self):
        self.screen.blit(self.now_image, self.now_image_rect)

    def draw_back(self):
        self.screen.blit(self.b_image, self.b_image_rect)

    def draw_exc(self):
        self.screen.blit(self.exc, self.exc_rect)
