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

        self.image_info = None
        self.info_rect = None

    def draw(self):
        self.screen.blit(self.image, self.rect)
    def draw_info(self):
        self.screen.blit(self.image_info, (50, 80))

class Functional():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.name = None
        self.image = None
        self.image_rect = None

    def draw(self):
        self.screen.blit(self.image, self.image_rect)

class General_state():
    def __init__(self, screen, image, info):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.y = self.screen_rect.y + 10 + 20
        self.rect.centerx = 100
        self.achieved = False
        self.info = info
        self.font = pygame.font.SysFont("Verdana", 20)
        self.info_img = self.font.render(self.info, True, (0, 0, 0), (255, 255, 255))
        self.info_img_rect = self.info_img.get_rect()
        self.info_img_rect.top = self.rect.bottom
        self.info_img_rect.centerx = self.rect.centerx

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.info_img, self.info_img_rect)


class achievements():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.name_funcion = {'cup': CUP, 'Background_Shop': [0, 0], 'Exc': EXC}
        self.general_states_data = {0: 'Вы хлебушек!',
                                    1: 'Начинающий!',
                                    2: 'Опытный!',
                                    3: 'Столп воды!',
                                    4: 'Величайший!'}
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
        self.general_states = []

        for num_moon in range(MAX_MOON_DEMON):
            one_achiv_game = One_achiv(screen)
            with open('Save_data/moon_demon', 'r') as f:
                one_achiv_game.achieved = int((f.read())[num_moon])
            if not one_achiv_game.achieved:
                one_achiv_game.image = pygame.image.load('Img/Achievements/Demons/Hero' + str(num_moon) + '.png')
                one_achiv_game.image_info = pygame.image.load('Img/Achievements/Demons/Hero_info.png')
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
            if ach_count_demon.achieved:
                ach_count_demon.image = pygame.image.load('Img/Achievements/Count_demon/count_demon' + str(num_ach_count_demon) + '.png')
                ach_count_demon.image_info = pygame.image.load(
                    'Img/Achievements/Count_demon/count_demon_info' + str(num_ach_count_demon) + '.png')
            else:
                ach_count_demon.image = pygame.image.load(
                    'Img/Achievements/Count_demon/count_demon_b' + str(num_ach_count_demon) + '.png')
                ach_count_demon.image_info = pygame.image.load(
                    'Img/Achievements/Count_demon/count_demon_b_info' + str(num_ach_count_demon) + '.png')
            ach_count_demon.rect = ach_count_demon.image.get_rect()
            ach_count_demon.rect.x = ((WIDTH - 75 * MAX_COUNT_DEMON) // (MAX_COUNT_DEMON + 1)) * (
                        num_ach_count_demon + 1) + (
                                         num_ach_count_demon) * 75
            ach_count_demon.rect.y = self.demons_moon[0].rect.bottom + 75 + 20
            self.count_demon.append(ach_count_demon)

        for num_forse in range(MAX_FORSE):
            count_forse = One_achiv(screen)
            with open('Save_data/forse.txt', 'r') as f:
                count_forse.achieved = int((f.read())[num_forse])
            if not count_forse.achieved:
                count_forse.image = pygame.image.load('Img/Achievements/Forse/forse_b' + str(num_forse) + '.png')
                count_forse.image_info = pygame.image.load('Img/Achievements/Forse/forse_info_b' + str(num_forse) + '.png')
            else:
                count_forse.image = pygame.image.load('Img/Achievements/Forse/forse' + str(num_forse) + '.png')
                count_forse.image_info = pygame.image.load(
                    'Img/Achievements/Forse/forse_info' + str(num_forse) + '.png')
            count_forse.rect = count_forse.image.get_rect()
            count_forse.rect.x = ((WIDTH - 75 * MAX_FORSE) // (MAX_FORSE + 1)) * (num_forse + 1) + (
                num_forse) * 75
            count_forse.rect.y = self.demons_moon[0].rect.bottom + 10
            self.forses.append(count_forse)

        with open('Save_data/count_achiv_demon.txt', 'r') as f:
            self.count_achiv_demon = int(f.read())

        for num_state in range(MAX_STATE):
            one_state = General_state(screen, "Img/Achievements/State/state" + str(num_state + 1) + ".png", self.general_states_data[num_state])
            with open('Save_data/forse.txt', 'r') as f:
                one_state.achieved = int((f.read())[num_state])
            self.general_states.append(one_state)

        with open('Save_data/count_click.txt', 'r') as f:
            self.count_click = int(f.read())


    def draw(self):
        self.func[0].draw()

    def control(self, shop_game, locations_game):

        # Контроль количества кликов за один раз
        points_in_click = shop_game.points_in_click()
        if points_in_click >= 1000 and not self.forses[4].achieved:
            self.forses[4].achieved = True
            self.forses[4].image = pygame.image.load(
                'Img/Achievements/Forse/forse' + str(4) + '.png')
            self.forses[4].image_info = pygame.image.load(
                'Img/Achievements/Forse/forse_info' + str(4) + '.png')
        elif points_in_click >= 500 and not self.forses[3].achieved:
            self.forses[3].achieved = True
            self.forses[3].image = pygame.image.load(
                'Img/Achievements/Forse/forse' + str(3) + '.png')
            self.forses[3].image_info = pygame.image.load(
                'Img/Achievements/Forse/forse_info' + str(3) + '.png')
        elif points_in_click >= 250 and not self.forses[2].achieved:
            self.forses[2].achieved = True
            self.forses[2].image = pygame.image.load(
                'Img/Achievements/Forse/forse' + str(2) + '.png')
            self.forses[2].image_info = pygame.image.load(
                'Img/Achievements/Forse/forse_info' + str(2) + '.png')
        elif points_in_click >= 50 and not self.forses[1].achieved:
            self.forses[1].achieved = True
            self.forses[1].image = pygame.image.load(
                'Img/Achievements/Forse/forse' + str(1) + '.png')
            self.forses[1].image_info = pygame.image.load(
                'Img/Achievements/Forse/forse_info' + str(1) + '.png')
        elif points_in_click >= 5 and not self.forses[0].achieved:
            self.forses[0].achieved = True
            self.forses[0].image = pygame.image.load(
                'Img/Achievements/Forse/forse' + str(0) + '.png')
            self.forses[0].image_info = pygame.image.load(
                'Img/Achievements/Forse/forse_info' + str(0) + '.png')

        # Контроль количества убитых демонов
        if self.count_achiv_demon >= 50 and not self.count_demon[4].achieved:
            self.count_demon[4].achieved = True
            self.count_demon[4].image = pygame.image.load(
                'Img/Achievements/Count_demon/count_demon' + str(4) + '.png')
            self.count_demon[4].image_info = pygame.image.load(
                'Img/Achievements/Count_demon/count_demon_info' + str(4) + '.png')
        elif self.count_achiv_demon >= 25 and not self.count_demon[3].achieved:
            self.count_demon[3].achieved = True
            self.count_demon[3].image = pygame.image.load(
                'Img/Achievements/Count_demon/count_demon' + str(3) + '.png')
            self.count_demon[3].image_info = pygame.image.load(
                'Img/Achievements/Count_demon/count_demon_info' + str(3) + '.png')
        elif self.count_achiv_demon >= 10 and not self.count_demon[2].achieved:
            self.count_demon[2].achieved = True
            self.count_demon[2].image = pygame.image.load(
                'Img/Achievements/Count_demon/count_demon' + str(2) + '.png')
            self.count_demon[2].image_info = pygame.image.load(
                'Img/Achievements/Count_demon/count_demon_info' + str(2) + '.png')
        elif self.count_achiv_demon >= 5 and not self.count_demon[1].achieved:
            self.count_demon[1].achieved = True
            self.count_demon[1].image = pygame.image.load(
                'Img/Achievements/Count_demon/count_demon' + str(1) + '.png')
            self.count_demon[1].image_info = pygame.image.load(
                'Img/Achievements/Count_demon/count_demon_info' + str(1) + '.png')
        elif self.count_achiv_demon >= 1 and not self.count_demon[0].achieved:
            self.count_demon[0].achieved = True
            self.count_demon[0].image = pygame.image.load(
                'Img/Achievements/Count_demon/count_demon' + str(0) + '.png')
            self.count_demon[0].image_info = pygame.image.load(
                'Img/Achievements/Count_demon/count_demon_info' + str(0) + '.png')

        # Контроль особых достижений количества убитых демонов
        if self.count_click >= 1000:
            locations_game.demon_1_moon = True
            locations_game.first_list = False
        elif self.count_click >= 999:
            locations_game.demon_3_moon = True
            locations_game.first_list = False
        elif self.count_click >= 50:
            locations_game.demon_6_moon = True
            locations_game.first_list = False

    def draw_general_state(self):
        for i in range(len(self.general_states) - 1, -1, -1):
            if self.general_states[i].achieved:
                self.general_states[i].draw()
                break
            if i == 0:
                self.general_states[0].draw()

    def special_achiv(self, index_demon):
        if index_demon == 6:
            self.demons_moon[0].achieved = True
        elif index_demon == 3:
            self.demons_moon[1].achieved = True
        elif index_demon == 1:
            self.demons_moon[2].achieved = True

    def add_demon(self):
        self.count_achiv_demon += 1
        with open('Save_data/count_achiv_demon.txt', 'w') as file:
            file.write(str(self.count_achiv_demon))

    def add_click(self):
        self.count_click += 1
        with open('Save_data/count_click.txt', 'w') as file:
            file.write(str(self.count_click))

