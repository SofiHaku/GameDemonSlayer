import pygame
from settings import *

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

        self.b_image = pygame.image.load('Img/Shop/Functional/Background_Shop.png')
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
        self.skills = []

        for num_hero in range(MAX_HERO):
            hero_shop_game = Hero_shop(screen)
            with open('buy_herous.txt', 'r') as f:
                hero_shop_game.buy = int((f.read())[num_hero])
            if not hero_shop_game.buy:
                hero_shop_game.image = pygame.image.load('Img/Shop/Hero/Hero' + str(num_hero) + '.png')
            else:
                hero_shop_game.image = pygame.image.load('Img/Shop/Hero/Hero_buy' + str(num_hero) + '.png')
            hero_shop_game.rect = hero_shop_game.image.get_rect()
            hero_shop_game.rect.x = ((WIDTH - SHOP_HERO_W * MAX_HERO)//(MAX_HERO+1)) * (num_hero + 1) + (num_hero) * SHOP_HERO_W
            hero_shop_game.rect.y = (HEIGHT - SHOP_HERO_H - 2 * SHOP_SKILL_H)//3 + 25
            self.herous.append(hero_shop_game)


        for num_skill in range(MAX_SKILLS):
            skill_game = Skills(screen)
            skill_game.image = pygame.image.load('Img/Shop/Skills/skill' + str(num_skill) + '.png')
            skill_game.rect = skill_game.image.get_rect()
            skill_game.rect.x = ((WIDTH - SHOP_SKILL_W * MAX_SKILLS_SET)//(MAX_SKILLS_SET+1)) * (num_skill % MAX_SKILLS_SET + 1) + (num_skill % MAX_SKILLS_SET) * SHOP_SKILL_W
            # 25 и 15 соответсвенно расстояния между (героями и скилами) и (скилами между собой)
            skill_game.rect.y = self.herous[0].rect.bottom + (SHOP_SKILL_H + 15) * (num_skill // MAX_SKILLS_SET) + 25
            self.skills.append(skill_game)


    def draw_now(self):
        self.screen.blit(self.now_image, self.now_image_rect)

    def draw_back(self):
        self.screen.blit(self.b_image, self.b_image_rect)

    def draw_exc(self):
        self.screen.blit(self.exc, self.exc_rect)





