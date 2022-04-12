import pygame

class Hero_shop():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()


    def draw(self):
        self.screen.blit(self.image, self.rect)

class Skills():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

    def draw(self):
        self.screen.blit(self.image, self.rect)

class Shop():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.b_image = pygame.image.load('Img/Shop/Functional/Back.png')
        self.now_image = pygame.image.load('Img/Shop/Functional/Shop.png')
        self.exc = pygame.image.load('Img/Shop/Functional/Exc.png')

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
            with open('buy_herous.txt', 'r') as f:
                hero_game.buy = int((f.read())[i-1])
            if not hero_game.buy:
                hero_game.image = pygame.image.load('Img/Shop/Hero/Hero' + str(i) + '.png')
            else:
                hero_game.image = pygame.image.load('Img/Shop/Hero/Hero_buy' + str(i) + '.png')
            hero_game.rect = hero_game.image.get_rect()
            hero_game.rect.x = 50 * i + (i - 1) * 150
            hero_game.rect.y = 30

            self.herous.append(hero_game)

        self.skills = []

        for i in range(1, 7):
            skil_game = Skills(screen)
            skil_game.image = pygame.image.load('Img/Shop/Skills/skil' + str(i) + '.png')
            skil_game.rect = skil_game.image.get_rect()
            skil_game.rect.x = 30 * (i % 4) + ((i % 4) - 1) * 60
            skil_game.rect.y = 250
            self.skills.append(skil_game)


    def draw_now(self):
        self.screen.blit(self.now_image, self.now_image_rect)

    def draw_back(self):
        self.screen.blit(self.b_image, self.b_image_rect)

    def draw_exc(self):
        self.screen.blit(self.exc, self.exc_rect)

    #def buy(self):




