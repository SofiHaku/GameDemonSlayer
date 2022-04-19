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

        # to copy
        self.name = None
        self.index = None

    def draw(self):
        self.screen.blit(self.image, self.rect)
    def draw_info(self):
        self.screen.blit(self.image_info, (50, 80))
    def copy(self, name, index):
        new_achiv = One_achiv(self.screen)
        new_achiv.image = self.image
        new_achiv.rect = self.rect
        new_achiv.achieved = True
        new_achiv.name = name
        new_achiv.index = index
        return new_achiv

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

        self.have_new_achiv = One_achiv(screen)


    def draw(self):
        self.func[0].draw()

    def control(self, shop_game, locations_game, demon_6_moon_start_game):

        # Контроль количества кликов за один раз
        points_in_click = shop_game.points_in_click()
        for i in range(4, -1, -1):
            if points_in_click >= i*25 + 5 and not self.forses[i].achieved:
                print("True")
                self.forses[i].achieved = True
                self.forses[i].image = pygame.image.load(
                    'Img/Achievements/Forse/forse' + str(i) + '.png')
                self.forses[i].image_info = pygame.image.load(
                    'Img/Achievements/Forse/forse_info' + str(i) + '.png')

                self.have_new_achiv = self.forses[i].copy("forse", i)

                with open('Save_data/forse.txt', 'r') as file:
                    new_forse = list(file.read())
                    new_forse[i] = "1"
                    with open('Save_data/forse.txt', 'w') as file_1:
                        file_1.write("".join(new_forse))
                break

        # Контроль количества убитых демонов
        for i in range(4, -1, -1):
            if self.count_achiv_demon >= i*5 + 1 and not self.count_demon[i].achieved:
                self.count_demon[i].achieved = True
                self.count_demon[i].image = pygame.image.load(
                    'Img/Achievements/Count_demon/count_demon' + str(i) + '.png')
                self.count_demon[i].image_info = pygame.image.load(
                    'Img/Achievements/Count_demon/count_demon_info' + str(i) + '.png')

                self.have_new_achiv = self.forses[i].copy("count_demon", i)

                with open('Save_data/ach_count_demon.txt', 'r') as file:
                    new_count = list(file.read())
                    new_count[i] = "1"
                    with open('Save_data/ach_count_demon.txt', 'w') as file_1:
                        file_1.write("".join(new_count))
                break


        # Контроль особых достижений количества убитых демонов
        #if self.count_click >= 1000:
            #pass
            #locations_game.demon_1_moon = True
            #locations_game.first_list = False
        #elif self.count_click >= 999:
            #pass
            #locations_game.demon_3_moon = True
            #locations_game.first_list = False
        if self.count_click >= 50 and not demon_6_moon_start_game.use():
            locations_game.demon_6_moon_start = True
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

    def control_exc_new_achiv(self, Mouse_x, Mouse_y):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Mouse_x >= 500 + 25 and Mouse_x <= 500 + 25 + 30 and Mouse_y >= 50 + 20 and Mouse_y <= 50 + 20 + 30:
                    self.have_new_achiv.achieved = False

    def draw_new_achiv(self, Mouse_x, Mouse_y, text_g):
        if self.have_new_achiv.achieved:
            serf = pygame.Surface((550, 300))
            serf.fill((255, 255, 255))
            x = 25
            y = 50
            img = pygame.image.load("Img/Achievements/State/new_state.png")
            img_rect = img.get_rect()
            img_rect.x = 0
            img_rect.y = 30

            exc_x = 500
            exc_y = 20

            serf.blit(img, img_rect)
            serf.blit(self.func[2].image, (exc_x, exc_y))
            self.screen.blit(serf, (x, y))
            if self.have_new_achiv.name == "forse":
                text_g.draw_many_lines(270, 55, text_g.mess_forse[self.have_new_achiv.index], 25)
            elif self.have_new_achiv.name == "count_demon":
                text_g.draw_many_lines(270, 85, text_g.mess_count_demons[self.have_new_achiv.index], 20)

            self.control_exc_new_achiv(Mouse_x, Mouse_y)
            pygame.display.update()

    def return_have_new_achiv(self):
        return self.have_new_achiv.achieved