import pygame
from settings import *

class One_achiv():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = None
        self.rect = None
        self.cost = None
        self.achieved = False

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

class achievements():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.name_funcion = {'cup': CUP, 'Background_Shop': [0, 0], 'Exc': EXC}
        self.func = []

        for key in self.name_funcion.keys():
            func_game = Functional(screen)
            func_game.image = pygame.image.load('Img/Achievements/' + key + '.png')
            func_game.image_rect = func_game.image.get_rect()
            func_game.image_rect.x = (self.name_funcion[key])[0]
            func_game.image_rect.y = (self.name_funcion[key])[1]
            self.func.append(func_game)

        self.demons_moon = []
        self.count_demon = []
        self.forses = []

        for num_moon in range(MAX_MOON_DEMON):
            one_achiv_game = One_achiv(screen)
            with open('Save_data/moon_demon', 'r') as f:
                one_achiv_game.achieved = int((f.read())[num_moon])
            if not one_achiv_game.achieved:
                one_achiv_game.image = pygame.image.load('Img/Achievements/Demons/Hero' + str(num_moon) + '.png')
            else:
                one_achiv_game.image = pygame.image.load('mg/Achievements/Demons/Hero_die' + str(num_moon) + '.png')
            one_achiv_game.rect = one_achiv_game.image.get_rect()
            one_achiv_game.rect.x = ((WIDTH - SHOP_HERO_W * MAX_HERO) // (MAX_HERO + 1)) * (num_moon + 1) + (
                num_moon) * SHOP_HERO_W
            one_achiv_game.rect.y = (HEIGHT - SHOP_HERO_H - 2 * SHOP_SKILL_H) // 3 + 25
            self.demons_moon.append(one_achiv_game)

        for num_ach_count_demon in range(MAX_COUNT_DEMON):
            ach_count_demon = One_achiv(screen)
            with open('Save_data/ach_count_demon.txt', 'r') as f:
                ach_count_demon.achieved = int((f.read())[num_ach_count_demon])
            ach_count_demon.image = pygame.image.load(
                'Img/Achievements/Count_demon/count_demon' + str(num_ach_count_demon) + '.png')
            ach_count_demon.rect = ach_count_demon.image.get_rect()
            ach_count_demon.rect.x = ((WIDTH - 75 * MAX_COUNT_DEMON) // (MAX_COUNT_DEMON + 1)) * (
                        num_ach_count_demon + 1) + (
                                         num_ach_count_demon) * 75
            ach_count_demon.rect.y = self.demons_moon[0].rect.bottom + 10
            self.count_demon.append(ach_count_demon)

        for num_forse in range(MAX_FORSE):
            count_forse = One_achiv(screen)
            with open('Save_data/forse.txt', 'r') as f:
                count_forse.achieved = int((f.read())[num_forse])
            count_forse.image = pygame.image.load('Img/Achievements/Forse/count_demon' + str(num_forse) + '.png')
            count_forse.rect = count_forse.image.get_rect()
            count_forse.rect.x = ((WIDTH - 75 * MAX_FORSE) // (MAX_FORSE + 1)) * (num_forse + 1) + (
                num_forse) * 75
            count_forse.rect.y = self.count_demon[0].rect.bottom + 10
            self.forses.append(count_forse)


    def draw(self):
        self.func[0].draw()
