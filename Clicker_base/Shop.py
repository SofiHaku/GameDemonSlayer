import pygame
from Globals import Globals

class Improve():
    '''Класс улучшений (скилл)'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.image = None
        self.rect = None
        self.cost = None
        self.count = 0
        self.plus_points = None
        self.is_selected = False

    def draw(self):
        '''Вывод объекта на экран'''
        self.screen.blit(self.image, self.rect)

class Functional():
    '''Класс функциональных кнопок'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.name = None
        self.image = None
        self.image_rect = None

    def draw(self):
        '''Вывод объекта на экран'''
        self.screen.blit(self.image, self.image_rect)

class Shop():
    '''Класс всех объектов в магазине'''
    def __init__(self, screen):
        self.globals = Globals()
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.you_dont_have_many = False

        self.font = pygame.font.SysFont("Verdana", 15)
        self.max_skills_img = self.font.render('/5', True, (0, 0, 0), (255, 255, 255))
        self.max_skills_img_rect = self.max_skills_img.get_rect()

        self.name_funcion = {'Background_Shop': [0, 0], 'Shop': self.globals.SHOP, 'Exc': self.globals.EXC,
                             'lamp': self.globals.LAMP, 'Exc_info': self.globals.EXC_INFO, 'lamp_info': [15, 80]}
        cost_hero = [200, 500, 1000]
        cost_skills = [100, 150, 200, 250, 300, 350, 450, 500]
        plus_points_d = [1, 2, 4, 8, 16, 32, 64, 128]

        self.func = []
        self.herous = []
        self.herous_info = []
        self.skills = []
        self.skills_info = []
        self.max_skills_coord = []
        self.count_skills_to_draw = []
        self.herous_cost_img = []
        self.skills_cost_img = []

        self.make_func_in_shop()
        self.make_hero_in_shop(cost_hero)
        self.make_hero_info_in_shop()
        self.make_skills_in_shop(cost_skills, plus_points_d)
        self.make_skills_info_in_shop()
        self.make_cost_obj(cost_skills, cost_hero)

    def make_func_in_shop(self):
        '''Создание функицональных объектов на экране (переход между локациями)'''
        for key in self.name_funcion.keys():
            func_game = Functional(self.screen)
            func_game.image = pygame.image.load('Img/Shop/Functional/' + key + '.png')
            func_game.image_rect = func_game.image.get_rect()
            func_game.image_rect.x = (self.name_funcion[key])[0]
            func_game.image_rect.y = (self.name_funcion[key])[1]
            self.func.append(func_game)

    def make_hero_in_shop(self, cost_hero):
        '''Создание героев в магазине'''
        for num_hero in range(self.globals.MAX_HERO):
            hero_shop_game = Improve(self.screen)
            with open('Save_data/buy_herous.txt', 'r') as f:
                hero_shop_game.buy = int((f.read())[num_hero])
            hero_shop_game.image = pygame.image.load('Img/Shop/Hero/Hero' + str(num_hero) + '.png')
            hero_shop_game.rect = hero_shop_game.image.get_rect()
            hero_shop_game.rect.x = ((self.globals.WIDTH - self.globals.SHOP_HERO_W * self.globals.MAX_HERO)//(self.globals.MAX_HERO+ 1)) * (num_hero + 1) + (num_hero) * self.globals.SHOP_HERO_W
            hero_shop_game.rect.y = (self.globals.HEIGHT - self.globals.SHOP_HERO_H - 2 * self.globals.SHOP_SKILL_H)//3 + 25
            hero_shop_game.cost = cost_hero[num_hero]
            self.herous.append(hero_shop_game)

    def make_hero_info_in_shop(self):
        '''Создание информации о героях в магазине'''
        for num_hero in range(self.globals.MAX_HERO):
            hero_info_game = Improve(self.screen)
            hero_info_game.image = pygame.image.load('Img/Shop/Hero_info/Hero' + str(num_hero) + '.png')
            hero_info_game.rect = hero_info_game.image.get_rect()
            hero_info_game.rect.x = 25
            hero_info_game.rect.y = 75
            self.herous_info.append(hero_info_game)

    def make_skills_in_shop(self, cost_skills, plus_points_d):
        '''Создание скиллов в магазине'''
        for num_skill in range(self.globals.MAX_SKILLS):
            skill_game = Improve(self.screen)
            with open('Save_data/buy_skills.txt', 'r') as f:
                skill_game.buy = int((f.read())[num_skill])
            skill_game.image = pygame.image.load('Img/Shop/Skills/skill' + str(num_skill) + '.png')
            skill_game.rect = skill_game.image.get_rect()
            skill_game.rect.x = ((self.globals.WIDTH - self.globals.SHOP_SKILL_W * self.globals.MAX_SKILLS_SET)//(self.globals.MAX_SKILLS_SET+1)) * (num_skill % self.globals.MAX_SKILLS_SET + 1) + (num_skill % self.globals.MAX_SKILLS_SET) * self.globals.SHOP_SKILL_W + (self.globals.SHOP_SKILL_W + 52) * (num_skill // self.globals.MAX_SKILLS_SET)
            # 25 и 15 соответсвенно расстояния между (героями и скилами) и (скилами между собой)
            skill_game.rect.y = self.herous[0].rect.bottom + (self.globals.SHOP_SKILL_H + 15) * (num_skill // self.globals.MAX_SKILLS_SET) + 25
            skill_game.cost = cost_skills[num_skill]
            skill_game.plus_points = plus_points_d[num_skill]
            self.skills.append(skill_game)
            self.max_skills_coord.append([skill_game.rect.right, skill_game.rect.bottom])

    def make_skills_info_in_shop(self):
        '''Создание информации о скиллах в магазине'''
        for num_hero in range(6):
            skills_info_game = Improve(self.screen)
            skills_info_game.image = pygame.image.load('Img/Shop/Skills_info/skill' + str(num_hero) + '.png')
            skills_info_game.rect = skills_info_game.image.get_rect()
            skills_info_game.rect.x = 25
            skills_info_game.rect.y = 95
            self.skills_info.append(skills_info_game)

    def make_cost_obj(self, cost_skills, cost_hero):
        '''Создание стоимоcти объектов'''
        for cost in cost_skills:
            cost_img = self.font.render(str(cost), True, (0, 0, 0), (255, 255, 255))
            self.skills_cost_img.append([cost_img, cost_img.get_rect()])

        for cost in cost_hero:
            cost_img = self.font.render(str(cost), True, (0, 0, 0), (255, 255, 255))
            self.herous_cost_img.append([cost_img, cost_img.get_rect()])

    def points_in_click(self):
        '''Функция, возвращающая количество кликов за раз'''
        points = 1
        for i in range(self.globals.MAX_SKILLS):
            points += self.skills[i].buy * self.skills[i].plus_points
        for i in range(self.globals.MAX_HERO):
            points *= (self.herous[i].buy + 1)
        return points

    def image_count(self, count):
        '''Создание изображний количества объектов'''
        self.skills_img = self.font.render(str(count), True, (0, 0, 0), (255, 255, 255))
        self.skills_img_rect = self.skills_img.get_rect()

    def draw_count(self, x, y, number_skills):
        '''Вывод количества предметов на экран'''
        self.max_skills_img_rect.right = x
        self.max_skills_img_rect.bottom = y
        self.skills_img_rect.right = self.max_skills_img_rect.left
        self.skills_img_rect.bottom = y
        self.skills_cost_img[number_skills][1].bottom = y
        self.skills_cost_img[number_skills][1].left = x - self.globals.SHOP_SKILL_W
        self.screen.blit(self.max_skills_img, self.max_skills_img_rect)
        self.screen.blit(self.skills_img, self.skills_img_rect)
        self.screen.blit(self.skills_cost_img[number_skills][0], self.skills_cost_img[number_skills][1])

    def draw_cost_hero(self, x, y, number_hero):
        '''Вывод стоимости персонажей'''
        self.herous_cost_img[number_hero][1].bottom = y
        self.herous_cost_img[number_hero][1].right = x
        self.screen.blit(self.herous_cost_img[number_hero][0], self.herous_cost_img[number_hero][1])

    def you_have_many(self, stat_game, cost, shop_game, index, name):
        '''Проверка наличия нужно количества денег'''
        if name == "hero":
            if stat_game.point_now >= cost and not shop_game.herous[index].buy:
                return True
            if not shop_game.herous[index].buy:
                self.you_dont_have_many = True
            return False
        elif name == "skills":
            if stat_game.point_now >= cost and shop_game.skills[index].buy < 5:
                return True
            if shop_game.skills[index].buy < 5:
                self.you_dont_have_many = True
            return False

    def you_buy(self, index):
        '''Проверка купил ли герой объект ранее'''
        return self.herous[index].buy

    def control_you_dont_have_many(self, Mouse_x, Mouse_y):
        '''Контроль отсутсвия денег для перехода на другую локацию'''
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Mouse_x >= 500 and Mouse_x <= 530 and Mouse_y >= 70 and Mouse_y <= 110:
                    self.you_dont_have_many = False

    def draw_you_dont_have_many(self, Mouse_x, Mouse_y, text_g):
        '''Вывод окошка об осутсвии денег'''
        if self.you_dont_have_many:
            serf = pygame.Surface((500, 300))
            serf.fill((255, 255, 255))
            x, y = 50, 50
            img = pygame.image.load("Img/Shop/zenic.png")
            img_rect = img.get_rect()
            img_rect.x, img_rect.y = 20, 30
            exc_x, exc_y = 450, 20

            serf.blit(img, img_rect)
            serf.blit(self.func[2].image, (exc_x, exc_y))
            self.screen.blit(serf, (x, y))
            text_g.draw_many_lines(310, 150, text_g.mess_dont_many, 30)

            self.control_you_dont_have_many(Mouse_x, Mouse_y)

    def return_dont_have_many(self):
        '''Возвращение булевого значения об отсутвии денг'''
        return self.you_dont_have_many

    def what_gero_buy(self):
        '''Передача индекса персонажа, которого купил герой'''
        for i in range(len(self.herous) - 1, -1, -1):
            if self.herous[i].is_selected:
                return i + 1
        return 0













