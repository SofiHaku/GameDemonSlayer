import pygame
from settings import *

class Improve():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = None
        self.rect = None

    def draw(self):
        self.screen.blit(self.image, self.rect)

class Functional():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.name = None
        self.image = None
        self.image_rect = None

    def draw(self):
        self.screen.blit(self.image, self.image_rect)

class Shop():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.name_funcion = {'Background_Shop': [0, 0], 'Shop': [20, 200], 'Exc': [500, 20]}
        self.func = []

        for key in self.name_funcion.keys():
            func_game = Functional(screen)
            func_game.image = pygame.image.load('Img/Shop/Functional/' + key + '.png')
            func_game.image_rect = func_game.image.get_rect()
            func_game.image_rect.x = (self.name_funcion[key])[0]
            func_game.image_rect.y = (self.name_funcion[key])[1]
            self.func.append(func_game)

        self.draw_back_bool = False

        self.herous = []
        self.skills = []

        for num_hero in range(MAX_HERO):
            hero_shop_game = Improve(screen)
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
            skill_game = Improve(screen)
            skill_game.image = pygame.image.load('Img/Shop/Skills/skill' + str(num_skill) + '.png')
            skill_game.rect = skill_game.image.get_rect()
            skill_game.rect.x = ((WIDTH - SHOP_SKILL_W * MAX_SKILLS_SET)//(MAX_SKILLS_SET+1)) * (num_skill % MAX_SKILLS_SET + 1) + (num_skill % MAX_SKILLS_SET) * SHOP_SKILL_W
            # 25 и 15 соответсвенно расстояния между (героями и скилами) и (скилами между собой)
            skill_game.rect.y = self.herous[0].rect.bottom + (SHOP_SKILL_H + 15) * (num_skill // MAX_SKILLS_SET) + 25
            self.skills.append(skill_game)





