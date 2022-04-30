import pygame
from src.Globals import Globals

class One_achiv():
    '''Класс одного достижения'''
    def __init__(self, screen):
        '''Задаем начальную информацию'''
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
        '''Вывод достижения на экран'''
        self.screen.blit(self.image, self.rect)
    def draw_info(self, globals):
        '''Вывод информации о достижении на экран'''
        self.screen.blit(self.image_info, globals.INFO_ACHIV_XY)
    def copy(self, name, index):
        '''Функция для замены недостигнутого достижения на полученное'''
        new_achiv = One_achiv(self.screen)
        new_achiv.image = self.image
        new_achiv.rect = self.rect
        new_achiv.achieved = True
        new_achiv.name = name
        new_achiv.index = index
        return new_achiv

class Functional():
    '''Класс, отвечаючий за кнопки перехода между локациями'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.name = None
        self.image = None
        self.image_rect = None

    def draw(self):
        '''Вывод кнопок на экран'''
        self.screen.blit(self.image, self.image_rect)

class General_state():
    '''Класс основного статуса (изображение и текст в левом верхнем углу на главном экране)'''
    def __init__(self, screen, image, info, globals):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()

        self.rect.y = globals.GENERAL_STATE_Y
        self.rect.centerx = globals.GENERAL_STATE_X
        self.achieved = False
        self.info = info
        self.font = pygame.font.SysFont("Verdana", globals.TEXT_SIZE)
        self.info_img = self.font.render(self.info, True, globals.TEXT_COLOR, globals.COLOR_BACK_TEXT)
        self.info_img_rect = self.info_img.get_rect()
        self.info_img_rect.top = self.rect.bottom
        self.info_img_rect.centerx = self.rect.centerx

    def draw(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.info_img, self.info_img_rect)


class achievements():
    '''Класс отвечающий за все связанное с достижениями
    Их создания, контроля, вывод на экран'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.globals = Globals()
        self.have_new_achiv = One_achiv(screen)

        self.count_achiv_demon = None
        self.count_click = None

        self.name_funcion = {'cup': self.globals.CUP, 'Background_Shop': [0, 0], 'Exc': self.globals.EXC}
        self.general_states_data = {0: 'Вы хлебушек!',
                                    1: 'Начинающий!',
                                    2: 'Опытный!',
                                    3: 'Столп воды!',
                                    4: 'Величайший!'}
        self.func = []
        self.demons_moon = []
        self.count_demon = []
        self.forses = []
        self.general_states = []

        self.make_func()
        self.make_achiv_moon()
        self.make_achiv_count_demon()
        self.make_achiv_forse()
        self.make_gen_state()
        self.read_state_from_file()

    def make_func(self):
        '''Создание кнопок для перехода между локациями (добавление объектов в массив) '''
        for key in self.name_funcion.keys():
            func_game = Functional(self.screen)
            func_game.image = pygame.image.load('assets/Achievements/' + key + '.png')
            func_game.image_rect = func_game.image.get_rect()
            func_game.image_rect.x = (self.name_funcion[key])[0]
            func_game.image_rect.y = (self.name_funcion[key])[1]
            self.func.append(func_game)

    def make_gen_state(self):
        '''Создание основных достижений (для вывода на главном экране)'''
        for num_state in range(self.globals.MAX_STATE):
            one_state = General_state(self.screen, "assets/Achievements/State/state" +
                                      str(num_state + 1) + ".png", self.general_states_data[num_state], self.globals)
            with open('Save_data/forse.txt', 'r') as f:
                one_state.achieved = int((f.read())[num_state])
            self.general_states.append(one_state)

    def make_achiv_moon(self):
        '''Создание достижений (добавление объектов в массив) за победу над демоном-луной'''
        for num_moon in range(self.globals.MAX_MOON_DEMON):
            one_achiv_game = One_achiv(self.screen)
            with open('Save_data/use_demon', 'r') as f:
                one_achiv_game.achieved = int((f.read())[num_moon])
            if not one_achiv_game.achieved:
                one_achiv_game.image = pygame.image.load('assets/Achievements/Demons/Hero' + str(num_moon) + '.png')
                one_achiv_game.image_info = pygame.image.load('assets/Achievements/Demons/Hero_info.png')
            else:
                one_achiv_game.image = pygame.image.load('assets/Achievements/Demons/Hero_a' + str(num_moon) + '.png')
                one_achiv_game.image_info = pygame.image.load('assets/Achievements/Demons/Hero_a_info' + str(num_moon) + '.png')
            one_achiv_game.rect = one_achiv_game.image.get_rect()
            one_achiv_game.rect.x = ((self.globals.WIDTH - self.globals.SHOP_HERO_W * 2) // (2 + 1)) * (num_moon + 1) + (
                num_moon) * self.globals.SHOP_HERO_W
            one_achiv_game.rect.y = (self.globals.HEIGHT - self.globals.SHOP_HERO_H - 2 * self.globals.SHOP_SKILL_H) // 3 + 25
            self.demons_moon.append(one_achiv_game)

    def make_achiv_count_demon(self):
        '''Создание достижений (добавление объектов в массив) за количество убитых демонов'''
        for num_ach_count_demon in range(self.globals.MAX_COUNT_DEMON):
            ach_count_demon = One_achiv(self.screen)
            with open('Save_data/ach_count_demon.txt', 'r') as f:
                ach_count_demon.achieved = int((f.read())[num_ach_count_demon])
            if ach_count_demon.achieved:
                ach_count_demon.image = pygame.image.load('assets/Achievements/Count_demon/count_demon' + str(num_ach_count_demon) + '.png')
                ach_count_demon.image_info = pygame.image.load(
                    'assets/Achievements/Count_demon/count_demon_info' + str(num_ach_count_demon) + '.png')
            else:
                ach_count_demon.image = pygame.image.load(
                    'assets/Achievements/Count_demon/count_demon_b' + str(num_ach_count_demon) + '.png')
                ach_count_demon.image_info = pygame.image.load(
                    'assets/Achievements/Count_demon/count_demon_b_info' + str(num_ach_count_demon) + '.png')
            ach_count_demon.rect = ach_count_demon.image.get_rect()
            ach_count_demon.rect.x = ((self.globals.WIDTH - self.globals.ACHIV_S  * self.globals.MAX_COUNT_DEMON) //
                                      (self.globals.MAX_COUNT_DEMON + 1)) * (num_ach_count_demon + 1) + (num_ach_count_demon) * self.globals.ACHIV_S
            ach_count_demon.rect.y = self.demons_moon[0].rect.bottom + self.globals.ACHIV_S  + self.globals.ACHIV_COUNT_DEMON_Y
            self.count_demon.append(ach_count_demon)

    def make_achiv_forse(self):
        '''Создание достижений (добавление объектов в массив) за силу клика'''
        for num_forse in range(self.globals.MAX_FORSE):
            count_forse = One_achiv(self.screen)
            with open('Save_data/forse.txt', 'r') as f:
                count_forse.achieved = int((f.read())[num_forse])
            if not count_forse.achieved:
                count_forse.image = pygame.image.load('assets/Achievements/Forse/forse_b' + str(num_forse) + '.png')
                count_forse.image_info = pygame.image.load('assets/Achievements/Forse/forse_info_b' + str(num_forse) + '.png')
            else:
                count_forse.image = pygame.image.load('assets/Achievements/Forse/forse' + str(num_forse) + '.png')
                count_forse.image_info = pygame.image.load(
                    'assets/Achievements/Forse/forse_info' + str(num_forse) + '.png')
            count_forse.rect = count_forse.image.get_rect()
            count_forse.rect.x = ((self.globals.WIDTH - self.globals.ACHIV_S * self.globals.MAX_FORSE) // (self.globals.MAX_FORSE + 1)) * (num_forse + 1) + (
                num_forse) * self.globals.ACHIV_S
            count_forse.rect.y = self.demons_moon[0].rect.bottom + self.globals.ACHIV_FORSE_Y
            self.forses.append(count_forse)

    def read_state_from_file(self):
        '''Обновление информации о достижении'''
        with open('Save_data/count_achiv_demon.txt', 'r') as f:
            self.count_achiv_demon = int(f.read())

        with open('Save_data/count_click.txt', 'r') as f:
            self.count_click = int(f.read())

    def draw(self):
        '''Вывод фона на экран'''
        self.func[0].draw()

    def control(self, shop_game, locations_game, demon_6_moon_start_game):
        '''Общий контроль над достижениями'''
        self.control_click(shop_game)
        self.control_die_demon()
        self.control_special(locations_game)

    def control_click(self, shop_game):
        '''Контроль количества кликов за один раз'''
        points_in_click = shop_game.points_in_click()
        for i in range(self.globals.MAX_FORSE - 1, -1, -1):
            if points_in_click >= i*self.globals.DIFF_ACHIV_POINTS_IN_CLICK + self.globals.FIRST_ACHIV_POINTS_IN_CLICK  and not self.forses[i].achieved:
                self.forses[i].achieved = True
                self.forses[i].image = pygame.image.load(
                    'assets/Achievements/Forse/forse' + str(i) + '.png')
                self.forses[i].image_info = pygame.image.load(
                    'assets/Achievements/Forse/forse_info' + str(i) + '.png')

                self.have_new_achiv = self.forses[i].copy("forse", i)

                with open('Save_data/forse.txt', 'r') as file:
                    new_forse = list(file.read())
                    new_forse[i] = "1"
                    with open('Save_data/forse.txt', 'w') as file_1:
                        file_1.write("".join(new_forse))
                break

    def control_die_demon(self):
        '''Контроль количества убитых демонов'''
        for i in range(self.globals.MAX_COUNT_DEMON - 1, -1, -1):
            if self.count_achiv_demon >= i * self.globals.DIFF_ACHIV_COUNT_DEMON + 1 and not self.count_demon[i].achieved:
                self.count_demon[i].achieved = True
                self.count_demon[i].image = pygame.image.load(
                    'assets/Achievements/Count_demon/count_demon' + str(i) + '.png')
                self.count_demon[i].image_info = pygame.image.load(
                    'assets/Achievements/Count_demon/count_demon_info' + str(i) + '.png')

                self.have_new_achiv = self.forses[i].copy("count_demon", i)

                with open('Save_data/ach_count_demon.txt', 'r') as file:
                    new_count = list(file.read())
                    new_count[i] = "1"
                    with open('Save_data/ach_count_demon.txt', 'w') as file_1:
                        file_1.write("".join(new_count))
                break

    def control_special(self, locations_game):
        '''Контроль особых достижений количества убитых демонов'''
        if self.count_click >= self.globals.SECOND_SPECIAL_ACHIV and not locations_game.use_demon_3_moon:
            locations_game.demon_3_moon_start = True
            locations_game.demon_3_moon = True
            locations_game.demon_3_moon_end = True
            locations_game.first_list = False
        if self.count_click >= self.globals.FIRST_SPECIAL_ACHIV and not locations_game.use_demon_6_moon:
            locations_game.demon_6_moon_start = True
            locations_game.demon_6_moon = True
            locations_game.demon_6_moon_end = True
            locations_game.first_list = False

    def draw_general_state(self):
        '''Вывод вашего статуса на главном экране (левый верхний угол)'''
        for i in range(len(self.general_states) - 1, -1, -1):
            if self.general_states[i].achieved:
                self.general_states[i].draw()
                break
            if i == 0:
                self.general_states[0].draw()

    def special_achiv(self, index_demon):
        '''Используется при победе над особыми демонами: замена их статуса на достигнутый'''
        if index_demon == self.globals.INDEX_DEMON_MOON_1_MG:
            self.demons_moon[0].achieved = True
        elif index_demon == self.globals.INDEX_DEMON_MOON_2_MG:
            self.demons_moon[1].achieved = True
        elif index_demon == self.globals.INDEX_DEMON_MOON_3_MG:
            self.demons_moon[2].achieved = True

    def add_demon(self):
        '''Контроль убитых демонов: подсчитываем и сохраняем информацию'''
        self.count_achiv_demon += 1
        with open('Save_data/count_achiv_demon.txt', 'w') as file:
            file.write(str(self.count_achiv_demon))

    def add_click(self):
        '''Контроль количества кликов за раз: подсчитываем и сохраняем информацию'''
        self.count_click += 1
        with open('Save_data/count_click.txt', 'w') as file:
            file.write(str(self.count_click))

    def control_exc_new_achiv(self, Mouse_x, Mouse_y):
        '''Контроль над игровым процессом во время вывод изображения нового достижения
        Отвечает за выход из вылезающего окошка'''
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Mouse_x >= self.globals.EXC_NEW_ACHIV_XY[0] and Mouse_x <= self.globals.EXC_NEW_ACHIV_XY[0] + self.globals.EXC_WH \
                        and Mouse_y >= self.globals.EXC_NEW_ACHIV_XY[1] and Mouse_y <= self.globals.EXC_NEW_ACHIV_XY[1] + self.globals.EXC_WH:
                    self.have_new_achiv.achieved = False

    def draw_new_achiv(self, Mouse_x, Mouse_y, text_g):
        '''Вывод окошка о новом достижении на экран'''
        if self.have_new_achiv.achieved:
            serf = pygame.Surface(self.globals.NEW_SURF_ACHIV_SIZE)
            serf.fill(self.globals.B_COLOR_NEW_SURF)
            x, y = self.globals.NEW_SURF_ACHIV_XY[0], self.globals.NEW_SURF_ACHIV_XY[1]
            img = pygame.image.load("assets/Achievements/State/new_state.png")
            img_rect = img.get_rect()
            img_rect.x, img_rect.y = self.globals.NEW_SURF_ACHIV_IMG_XY[0], self.globals.NEW_SURF_ACHIV_IMG_XY[1]
            exc_x, exc_y = self.globals.NEW_SURF_ACHIV_EXC_XY[0], self.globals.NEW_SURF_ACHIV_EXC_XY[1]
            serf.blit(img, img_rect)
            serf.blit(self.func[2].image, (exc_x, exc_y))
            self.screen.blit(serf, (x, y))
            if self.have_new_achiv.name == "forse":
                text_g.draw_many_lines(self.globals.NEW_SURF_ACHIV_TEXT_FORSE_XY[0], self.globals.NEW_SURF_ACHIV_TEXT_FORSE_XY[1],
                                       text_g.mess_forse[self.have_new_achiv.index],  self.globals.NEW_SURF_TEXT_S)
            elif self.have_new_achiv.name == "count_demon":
                text_g.draw_many_lines(self.globals.NEW_SURF_ACHIV_TEXT_C_D_XY[0], self.globals.NEW_SURF_ACHIV_TEXT_C_D_XY[1],
                                       text_g.mess_count_demons[self.have_new_achiv.index], self.globals.TEXT_SIZE, self.globals)
            self.control_exc_new_achiv(Mouse_x, Mouse_y)
            pygame.display.update()

    def return_have_new_achiv(self):
        '''Передаем в другие функции представителя нового достижения'''
        return self.have_new_achiv.achieved