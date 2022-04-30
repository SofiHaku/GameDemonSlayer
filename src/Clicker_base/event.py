import pygame
import sys
from src.Globals import Globals

class Event():

    def __init__(self):
        self.globals = Globals()

    def control(self, stat_game, shop_game, hero_game, demon_game, locations_game, ill_butt, achiv):
        '''Контроль событий на главном экране'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self.down_space_in_fl(event, shop_game, stat_game, demon_game, achiv)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.down_mouse(event, locations_game)
            self.control_glow(ill_butt)


    def down_space_in_fl(self, event, shop_game, stat_game, demon_game, achiv):
        '''Обработка нажатия пробела'''
        if event.key == pygame.K_SPACE:
            stat_game.point_now += shop_game.points_in_click()
            with open('Save_data/points.txt', 'w') as f:
                f.write(str(stat_game.point_now))
            stat_game.image_score(self.globals.COUNT[0], self.globals.COUNT[1])
            damage = shop_game.points_in_click()
            demon_game.update_count_life(damage)
            achiv.add_click()
            if demon_game.die():
                achiv.add_demon()

    def control_glow(self, ill_butt):
        '''Контроль подстветки кнопок'''
        Mouse_x, Mouse_y = pygame.mouse.get_pos()
        if Mouse_x >= self.globals.SHOP[0] and Mouse_x <= self.globals.SHOP[0] + self.globals.SHOP_WH \
                and Mouse_y >= self.globals.SHOP[1] and Mouse_y <= self.globals.SHOP[1] + self.globals.SHOP_WH:
            ill_butt.to_shop = 1
        else:
            ill_butt.to_shop = 0

        if Mouse_x >= self.globals.CUP[0] and Mouse_x <= self.globals.CUP[0] + self.globals.CUP_WH[0] \
                and Mouse_y >= self.globals.CUP[1] and Mouse_y <= self.globals.CUP[1] + self.globals.CUP_WH[1]:
            ill_butt.to_achiv = 1
        else:
            ill_butt.to_achiv = 0

    def down_mouse(self, event, locations_game):
        '''Обработка событий с мышки'''
        if event.button == 1:
            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            if Mouse_x >= self.globals.SHOP[0] and Mouse_x <= self.globals.SHOP[0] + self.globals.SHOP_WH \
                    and Mouse_y >= self.globals.SHOP[1] and Mouse_y <= self.globals.SHOP[1] + self.globals.SHOP_WH:
                locations_game.shop = True
                locations_game.first_list = False
            elif Mouse_x >= self.globals.CUP[0] and Mouse_x <= self.globals.CUP[0] + self.globals.CUP_WH[0] \
                    and Mouse_y >= self.globals.CUP[1] and Mouse_y <= self.globals.CUP[1] + self.globals.CUP_WH[1]:
                locations_game.achiv = True
                locations_game.first_list = False

    def in_shop(self, shop_game, stat_game, locations_game, ill_butt):
        '''Контроль событий в магазине'''
        s_catch = pygame.mixer.Sound('Music/shopping_sound.ogg')
        click = pygame.mixer.Sound('Music/sound_of_sword.ogg')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            self.control_glow_in_shop(ill_butt, shop_game, Mouse_x, Mouse_y, locations_game)
            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = pygame.mouse.get_pressed()
                if pressed[0]:
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    self.go_to_fl_from_shop(Mouse_x, Mouse_y, locations_game, click)
                    self.go_to_info_lamp(Mouse_x, Mouse_y, locations_game, click)
                    self.go_to_shop_from_info(Mouse_x, Mouse_y, locations_game, click)
                    self.buy_hero(shop_game, Mouse_x, Mouse_y, s_catch, stat_game, click)
                    self.buy_skills(shop_game, Mouse_x, Mouse_y, stat_game, s_catch, click)
                elif pressed[2]:
                    self.go_to_info_hero(shop_game, Mouse_x, Mouse_y, locations_game, click)
                    self.go_to_info_skills(shop_game, Mouse_x, Mouse_y, locations_game, click)

    def control_glow_in_shop(self, ill_butt, shop_game, Mouse_x, Mouse_y, locations_game):
        '''Контроль подсвестки в магазине'''
        ill_butt.hero = ill_butt.hero_standart[-1]
        for i in range(self.globals.MAX_HERO):
            x = shop_game.herous[i].rect.x
            y = shop_game.herous[i].rect.y
            if Mouse_x >= x and Mouse_x <= x + self.globals.SHOP_HERO_W and Mouse_y >= y and Mouse_y <= y + self.globals.SHOP_HERO_H:
                ill_butt.hero = ill_butt.hero_standart[i]
        ill_butt.skills = ill_butt.skills_standart[-1]
        for i in range(self.globals.MAX_SKILLS):
            x = shop_game.skills[i].rect.x
            y = shop_game.skills[i].rect.y
            if Mouse_x >= x and Mouse_x <= x + self.globals.SHOP_SKILL_W and Mouse_y >= y and Mouse_y <= y + self.globals.SHOP_SKILL_H:
                ill_butt.skills = ill_butt.skills_standart[i]
        if Mouse_x >= self.globals.EXC[0] and Mouse_x <= self.globals.EXC[0] + self.globals.EXC_WH \
                and Mouse_y >= self.globals.EXC[1] and Mouse_y <= self.globals.EXC[1] + self.globals.EXC_WH \
                and locations_game.shop_hero and locations_game.shop_lamp and locations_game.shop_skills:
            ill_butt.exc = 1
        else:
            ill_butt.exc = 0
        if Mouse_x >= self.globals.LAMP[0] and Mouse_x <= self.globals.LAMP[0] + self.globals.LAMP_WH \
                and Mouse_y >= self.globals.LAMP[1] and Mouse_y <= self.globals.LAMP[1] + self.globals.LAMP_WH:
            ill_butt.lamp = 1
        else:
            ill_butt.lamp = 0

    def go_to_fl_from_shop(self, Mouse_x, Mouse_y, locations_game, click):
        '''Контроль перехода на главный экран'''
        if Mouse_x >= self.globals.EXC[0] and Mouse_x <= self.globals.EXC[0] + self.globals.EXC_WH \
                and Mouse_y >= self.globals.EXC[1] and Mouse_y <= self.globals.EXC[1] + self.globals.EXC_WH \
                and not locations_game.shop_skills and not locations_game.shop_hero and not locations_game.shop_lamp:
            locations_game.shop = False
            locations_game.first_list = True
            click.play()

    def go_to_info_lamp(self, Mouse_x, Mouse_y, locations_game, click):
        '''Контроль перехода в локацию лампочки'''
        if Mouse_x >= self.globals.LAMP[0] and Mouse_x <= self.globals.LAMP[0] + self.globals.LAMP_WH \
                and Mouse_y >= self.globals.LAMP[1] and Mouse_y <= self.globals.LAMP[1] + self.globals.LAMP_WH:
            locations_game.shop_skills = 0
            locations_game.shop_hero = 0
            locations_game.shop_lamp = 1
            click.play()

    def go_to_shop_from_info(self, Mouse_x, Mouse_y, locations_game, click):
        '''Контроль перехода из локаций, описывающих объекты, на гланую страницу магазина'''
        if Mouse_x >= self.globals.EXC_INFO[0] and Mouse_x <= self.globals.EXC_INFO[0] + self.globals.EXC_INFO_WH \
                and Mouse_y >= self.globals.EXC_INFO[1] and Mouse_y <= self.globals.EXC_INFO[
            1] + self.globals.EXC_INFO_WH \
                and (locations_game.shop_skills or locations_game.shop_hero or locations_game.shop_lamp):
            locations_game.shop_skills = 0
            locations_game.shop_hero = 0
            locations_game.shop_lamp = 0
            click.play()

    def buy_hero(self, shop_game, Mouse_x, Mouse_y, s_catch, stat_game, click):
        '''Покупка персонажа'''
        for i in range(self.globals.MAX_HERO):
            x = shop_game.herous[i].rect.x
            y = shop_game.herous[i].rect.y
            cost = shop_game.herous[i].cost
            if Mouse_x >= x and Mouse_x <= x + self.globals.SHOP_HERO_W and Mouse_y >= y and Mouse_y <= y + self.globals.SHOP_HERO_H:
                if shop_game.you_have_many(stat_game, cost, shop_game, i, "hero"):
                    self.buy_hero_pos(s_catch, shop_game, stat_game, i, cost)
                elif shop_game.you_buy(i):
                    self.buy_hero_neg(click, shop_game, i)
                else:
                    click.play()

    def buy_skills(self, shop_game, Mouse_x, Mouse_y, stat_game, s_catch, click):
        '''Покупка скиллов'''
        for i in range(self.globals.MAX_SKILLS):
            x = shop_game.skills[i].rect.x
            y = shop_game.skills[i].rect.y
            cost = shop_game.skills[i].cost
            if Mouse_x >= x and Mouse_x <= x + self.globals.SHOP_SKILL_W and Mouse_y >= y and Mouse_y <= y + self.globals.SHOP_SKILL_H:
                if shop_game.you_have_many(stat_game, cost, shop_game, i, "skills"):
                    s_catch.play()
                    stat_game.point_now -= cost
                    stat_game.image_score(self.globals.COUNT[0], self.globals.COUNT[1])
                    shop_game.skills[i].buy += 1
                    with open('Save_data/buy_skills.txt', 'r') as file:
                        new_buy = list(file.read())
                        new_buy[i] = str(shop_game.skills[i].buy)
                        with open('Save_data/buy_skills.txt', 'w') as file_1:
                            file_1.write("".join(new_buy))
                    with open('Save_data/points.txt', 'w') as file:
                        file.write(str(stat_game.point_now))
                else:
                    click.play()

    def buy_hero_pos(self, s_catch, shop_game, stat_game, i, cost):
        '''События при возможности покупки персонажа'''
        s_catch.play()
        shop_game.herous[i].buy = True
        shop_game.herous[i].image = pygame.image.load(
            'assets/Shop/Hero/Hero' + str(i) + '.png')
        stat_game.point_now -= cost
        stat_game.image_score(self.globals.COUNT[0], self.globals.COUNT[1])
        shop_game.herous[i].is_selected = True
        for j in range(2, i, -1):
            shop_game.herous[j].is_selected = False
        with open('Save_data/buy_herous.txt', 'r') as file_1:
            new_buy_herous = list(file_1.read())
            new_buy_herous[i] = '1'
            with open('Save_data/buy_herous.txt', 'w') as file_2:
                file_2.write("".join(new_buy_herous))
        with open('Save_data/points.txt', 'w') as file:
            file.write(str(stat_game.point_now))

    def buy_hero_neg(self, click, shop_game, i):
        '''События при отсутствии возможности покупки персонажа'''
        click.play()
        shop_game.herous[i].is_selected = True
        for j in range(2, i, -1):
            shop_game.herous[j].is_selected = False

    def go_to_info_hero(self, shop_game, Mouse_x, Mouse_y, locations_game, click):
        '''Переход в локацию, описывающую информацию о персонаже'''
        for i in range(self.globals.MAX_HERO):
            x = shop_game.herous[i].rect.x
            y = shop_game.herous[i].rect.y
            if Mouse_x >= x and Mouse_x <= x + self.globals.SHOP_HERO_W and Mouse_y >= y and Mouse_y <= y + self.globals.SHOP_HERO_H:
                locations_game.shop_skills = 0
                locations_game.shop_hero = 1
                locations_game.shop_lamp = 0
                now_hero = [0, 0, 0]
                now_hero[i] = 1
                locations_game.shop_info_hero = now_hero.copy()
                click.play()

    def go_to_info_skills(self, shop_game, Mouse_x, Mouse_y, locations_game, click):
        '''Переход в локацию, описывающую информацию о скиллах'''
        for i in range(self.globals.MAX_SKILLS):
            x = shop_game.skills[i].rect.x
            y = shop_game.skills[i].rect.y
            if Mouse_x >= x and Mouse_x <= x + self.globals.SHOP_SKILL_W and Mouse_y >= y and Mouse_y <= y + self.globals.SHOP_SKILL_H:
                locations_game.shop_skills = 1
                locations_game.shop_hero = 0
                locations_game.shop_lamp = 0
                now_skills = [0, 0, 0, 0, 0, 0, 0, 0]
                now_skills[i] = 1
                locations_game.shop_info_skills = now_skills.copy()
                click.play()

    def in_achiv(self, achiv, stat_game, locations_game, ill_butt):
        '''Контроль событий на странице достижений'''
        click = pygame.mixer.Sound('Music/sound_of_sword.ogg')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            Mouse_x, Mouse_y = pygame.mouse.get_pos()

            self.glow_exc(Mouse_x, Mouse_y, ill_butt)
            self.achiv_button_demon_moon(ill_butt, achiv, Mouse_x, Mouse_y, event, locations_game, click)
            self.achiv_button_count_demon(ill_butt, achiv, Mouse_x, Mouse_y, event, locations_game, click)
            self.achiv_button_forse(ill_butt, achiv, Mouse_x, Mouse_y, event, locations_game, click)
            self.achiv_exc_from_info_and_general(event, Mouse_x, Mouse_y, locations_game, click)

    def glow_exc(self, Mouse_x, Mouse_y, ill_butt):
        '''Подстветка кнопки выхода'''
        if Mouse_x >= self.globals.EXC[0] and Mouse_x <= self.globals.EXC[0] + self.globals.EXC_WH \
                and Mouse_y >= self.globals.EXC[1] and Mouse_y <= self.globals.EXC[1] + self.globals.EXC_WH:
            ill_butt.exc = 1
        else:
            ill_butt.exc = 0

    def achiv_button_demon_moon(self, ill_butt, achiv, Mouse_x, Mouse_y, event, locations_game, click):
        '''Обработка событий, связанных с кнопками-достижениями демонов высших лун
        Подстветка и нажатие'''
        ill_butt.demon = ill_butt.demon_standart[-1]
        for i in range(2):
            x = achiv.demons_moon[i].rect.x
            y = achiv.demons_moon[i].rect.y
            if Mouse_x >= x and Mouse_x <= x + self.globals.SHOP_HERO_W and Mouse_y >= y and Mouse_y <= y + self.globals.SHOP_HERO_H:
                ill_butt.demon = ill_butt.demon_standart[i]

                if event.type == pygame.MOUSEBUTTONDOWN:
                    locations_game.achiv_demons = 1
                    locations_game.achiv_info_demons = [0, 0, 0].copy()
                    locations_game.achiv_info_demons[i] = 1
                    click.play()

    def achiv_button_count_demon(self, ill_butt, achiv, Mouse_x, Mouse_y, event, locations_game, click):
        '''Обработка событий, связанных с кнопками-достижениями количества убитых демонов'''
        ill_butt.count_demon = ill_butt.count_demon_standart[-1]
        for i in range(self.globals.MAX_COUNT_DEMON):
            x = achiv.count_demon[i].rect.x
            y = achiv.count_demon[i].rect.y
            if Mouse_x >= x and Mouse_x <= x + self.globals.SHOP_SKILL_W and Mouse_y >= y and Mouse_y <= y + self.globals.SHOP_SKILL_H:
                ill_butt.count_demon = ill_butt.count_demon_standart[i]

                if event.type == pygame.MOUSEBUTTONDOWN:
                    locations_game.achiv_count_demons = 1
                    locations_game.achiv_info_count_demons = [0, 0, 0, 0, 0].copy()
                    locations_game.achiv_info_count_demons[i] = 1
                    click.play()

    def achiv_button_forse(self, ill_butt, achiv, Mouse_x, Mouse_y, event, locations_game, click):
        '''Обработка событий, связанных с кнопками-достижениями силы героя'''
        ill_butt.forse = ill_butt.forse_standart[-1]
        for i in range(self.globals.MAX_FORSE):
            x = achiv.forses[i].rect.x
            y = achiv.forses[i].rect.y
            if Mouse_x >= x and Mouse_x <= x + self.globals.SHOP_SKILL_W and Mouse_y >= y and Mouse_y <= y + self.globals.SHOP_SKILL_H:
                ill_butt.forse = ill_butt.forse_standart[i]

                if event.type == pygame.MOUSEBUTTONDOWN:
                    locations_game.achiv_forse = 1
                    locations_game.achiv_info_forse = [0, 0, 0, 0, 0].copy()
                    locations_game.achiv_info_forse[i] = 1
                    click.play()

    def achiv_exc_from_info_and_general(self, event, Mouse_x, Mouse_y, locations_game, click):
        '''Выход из локаций, описывающих информацию о достижениях, и из главной страницы достижений'''
        if event.type == pygame.MOUSEBUTTONDOWN:
            if Mouse_x >= self.globals.EXC[0] and Mouse_x <= self.globals.EXC[0] + self.globals.EXC_WH \
                    and Mouse_y >= self.globals.EXC[1] and Mouse_y <= self.globals.EXC[1] + self.globals.EXC_WH and \
                    not locations_game.achiv_demons and not locations_game.achiv_count_demons and not locations_game.achiv_forse:
                locations_game.achiv = False
                locations_game.first_list = True
                click.play()

            if Mouse_x >= self.globals.EXC_INFO[0] and Mouse_x <= self.globals.EXC_INFO[0] + self.globals.EXC_INFO_WH \
                    and Mouse_y >= self.globals.EXC_INFO[1] and Mouse_y <= self.globals.EXC_INFO[
                1] + self.globals.EXC_INFO_WH \
                    and (
                    locations_game.achiv_demons or locations_game.achiv_count_demons or locations_game.achiv_forse):
                locations_game.achiv_demons = 0
                locations_game.achiv_count_demons = 0
                locations_game.achiv_forse = 0
                click.play()

    def in_menu(self, locations_game, menu_game):
        '''Обработка событий в меню'''
        menu_game.control(locations_game)


