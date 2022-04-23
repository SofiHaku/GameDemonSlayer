import pygame
import sys

from settings import *


class Event():

    def __init__(self):
        pass

    def control(self, stat_game, shop_game, hero_game, demon_game, locations_game, ill_butt, achiv):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stat_game.point_now += shop_game.points_in_click()
                    with open('Save_data/points.txt', 'w') as f:
                        f.write(str(stat_game.point_now))
                    stat_game.image_score(COUNT[0], COUNT[1])
                    damage = shop_game.points_in_click()
                    demon_game.update_count_life(damage)
                    achiv.add_click()
                    if demon_game.die():
                        achiv.add_demon()

            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            if Mouse_x >= SHOP[0] and Mouse_x <= SHOP[0] + SHOP_WH \
                    and Mouse_y >= SHOP[1] and Mouse_y <= SHOP[1] + SHOP_WH:
                ill_butt.to_shop = 1
            else:
                ill_butt.to_shop = 0

            if Mouse_x >= CUP[0] and Mouse_x <= CUP[0] + CUP_WH[0] \
                    and Mouse_y >= CUP[1] and Mouse_y <= CUP[1] + CUP_WH[1]:
                ill_butt.to_achiv = 1
            else:
                ill_butt.to_achiv = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    if Mouse_x >= SHOP[0] and Mouse_x <= SHOP[0] + SHOP_WH \
                            and Mouse_y >= SHOP[1] and Mouse_y <= SHOP[1] + SHOP_WH:
                        locations_game.shop = True
                        locations_game.first_list = False
                    elif Mouse_x >= CUP[0] and Mouse_x <= CUP[0] + CUP_WH[0] \
                    and Mouse_y >= CUP[1] and Mouse_y <= CUP[1] + CUP_WH[1]:
                        locations_game.achiv = True
                        locations_game.first_list = False

    def in_shop(self, shop_game, stat_game, locations_game, ill_butt):
        s_catch = pygame.mixer.Sound('Music/покупка.ogg')
        click = pygame.mixer.Sound('Music/меч.ogg')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            ill_butt.hero = ill_butt.hero_standart[-1]
            for i in range(MAX_HERO):
                x = shop_game.herous[i].rect.x
                y = shop_game.herous[i].rect.y
                if Mouse_x >= x and Mouse_x <= x + SHOP_HERO_W and Mouse_y >= y and Mouse_y <= y + SHOP_HERO_H:
                    ill_butt.hero = ill_butt.hero_standart[i]

            ill_butt.skills = ill_butt.skills_standart[-1]
            for i in range(MAX_SKILLS):
                x = shop_game.skills[i].rect.x
                y = shop_game.skills[i].rect.y
                if Mouse_x >= x and Mouse_x <= x + SHOP_SKILL_W and Mouse_y >= y and Mouse_y <= y + SHOP_SKILL_H:
                    ill_butt.skills = ill_butt.skills_standart[i]

            if Mouse_x >= EXC[0] and Mouse_x <= EXC[0] + EXC_WH \
                    and Mouse_y >= EXC[1] and Mouse_y <= EXC[1] + EXC_WH \
                    and locations_game.shop_hero and locations_game.shop_lamp and locations_game.shop_skills:
                ill_butt.exc = 1
            else:
                ill_butt.exc = 0


            if Mouse_x >= LAMP[0] and Mouse_x <= LAMP[0] + LAMP_WH \
                    and Mouse_y >= LAMP[1] and Mouse_y <= LAMP[1] + LAMP_WH:
                ill_butt.lamp = 1
            else:
                ill_butt.lamp = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                pressed = pygame.mouse.get_pressed()
                if pressed[0]:
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    if Mouse_x >= EXC[0] and Mouse_x <= EXC[0] + EXC_WH \
                            and Mouse_y >= EXC[1] and Mouse_y <= EXC[1] + EXC_WH \
                            and not locations_game.shop_skills and not locations_game.shop_hero and not locations_game.shop_lamp:
                        locations_game.shop = False
                        locations_game.first_list = True
                        click.play()

                    if Mouse_x >= LAMP[0] and Mouse_x <= LAMP[0] + LAMP_WH \
                            and Mouse_y >= LAMP[1] and Mouse_y <= LAMP[1] + LAMP_WH:
                        locations_game.shop_skills = 0
                        locations_game.shop_hero = 0
                        locations_game.shop_lamp = 1
                        click.play()

                    if Mouse_x >= EXC_INFO[0] and Mouse_x <= EXC_INFO[0] + EXC_INFO_WH \
                            and Mouse_y >= EXC_INFO[1] and Mouse_y <= EXC_INFO[1] + EXC_INFO_WH \
                            and (locations_game.shop_skills or locations_game.shop_hero or locations_game.shop_lamp):
                        locations_game.shop_skills = 0
                        locations_game.shop_hero = 0
                        locations_game.shop_lamp = 0
                        click.play()

                    for i in range(MAX_HERO):
                        x = shop_game.herous[i].rect.x
                        y = shop_game.herous[i].rect.y
                        cost = shop_game.herous[i].cost
                        if Mouse_x >= x and Mouse_x <= x + SHOP_HERO_W and Mouse_y >= y and Mouse_y <= y + SHOP_HERO_H:
                            if shop_game.you_have_many(stat_game, cost, shop_game, i, "hero"):
                                s_catch.play()
                                shop_game.herous[i].buy = True
                                shop_game.herous[i].image = pygame.image.load(
                                    'Img/Shop/Hero/Hero' + str(i) + '.png')
                                stat_game.point_now -= cost
                                stat_game.image_score(COUNT[0], COUNT[1])
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
                            elif shop_game.you_buy(i):
                                click.play()
                                shop_game.herous[i].is_selected = True
                                for j in range(2, i, -1):
                                    shop_game.herous[j].is_selected = False
                            else:
                                click.play()

                    for i in range(MAX_SKILLS):
                        x = shop_game.skills[i].rect.x
                        y = shop_game.skills[i].rect.y
                        cost = shop_game.skills[i].cost
                        if Mouse_x >= x and Mouse_x <= x + SHOP_SKILL_W and Mouse_y >= y and Mouse_y <= y + SHOP_SKILL_H:
                            if shop_game.you_have_many(stat_game, cost, shop_game, i, "skills"):
                                s_catch.play()
                                stat_game.point_now -= cost
                                stat_game.image_score(COUNT[0], COUNT[1])
                                shop_game.skills[i].buy += 1

                                with open('Save_data/buy_skills.txt', 'r') as file:
                                    new_buy = list(file.read())
                                    new_buy[i] = str(shop_game.skills[i].buy)
                                    with open('Save_data/buy_skills.txt', 'w') as file_1:
                                        file_1.write("".join(new_buy))
                                    '''with open('Save_data/buy_skills.txt', 'w') as file_2:
                                        file_2.write("".join(new_buy))'''
                                with open('Save_data/points.txt', 'w') as file:
                                    file.write(str(stat_game.point_now))
                            else:
                                click.play()

                elif pressed[2]:
                    for i in range(MAX_HERO):
                        x = shop_game.herous[i].rect.x
                        y = shop_game.herous[i].rect.y
                        if Mouse_x >= x and Mouse_x <= x + SHOP_HERO_W and Mouse_y >= y and Mouse_y <= y + SHOP_HERO_H:
                            locations_game.shop_skills = 0
                            locations_game.shop_hero = 1
                            locations_game.shop_lamp = 0
                            now_hero = [0, 0, 0]
                            now_hero[i] = 1
                            locations_game.shop_info_hero = now_hero.copy()
                            click.play()

                    for i in range(MAX_SKILLS):
                        x = shop_game.skills[i].rect.x
                        y = shop_game.skills[i].rect.y
                        if Mouse_x >= x and Mouse_x <= x + SHOP_SKILL_W and Mouse_y >= y and Mouse_y <= y + SHOP_SKILL_H:
                            locations_game.shop_skills = 1
                            locations_game.shop_hero = 0
                            locations_game.shop_lamp = 0
                            now_skills = [0, 0, 0, 0, 0, 0, 0, 0]
                            now_skills[i] = 1
                            locations_game.shop_info_skills = now_skills.copy()
                            click.play()

    def in_achiv(self, achiv, stat_game, locations_game, ill_butt):
        click = pygame.mixer.Sound('Music/меч.ogg')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            Mouse_x, Mouse_y = pygame.mouse.get_pos()

            if Mouse_x >= EXC[0] and Mouse_x <= EXC[0] + EXC_WH \
                    and Mouse_y >= EXC[1] and Mouse_y <= EXC[1] + EXC_WH:
                ill_butt.exc = 1
            else:
                ill_butt.exc = 0

            ill_butt.demon = ill_butt.demon_standart[-1]
            for i in range(2):
                x = achiv.demons_moon[i].rect.x
                y = achiv.demons_moon[i].rect.y
                if Mouse_x >= x and Mouse_x <= x + SHOP_HERO_W and Mouse_y >= y and Mouse_y <= y + SHOP_HERO_H:
                    ill_butt.demon = ill_butt.demon_standart[i]

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        locations_game.achiv_demons = 1
                        locations_game.achiv_info_demons = [0, 0, 0].copy()
                        locations_game.achiv_info_demons[i] = 1
                        click.play()


            ill_butt.count_demon = ill_butt.count_demon_standart[-1]
            for i in range(MAX_COUNT_DEMON):
                x = achiv.count_demon[i].rect.x
                y = achiv.count_demon[i].rect.y
                if Mouse_x >= x and Mouse_x <= x + SHOP_SKILL_W and Mouse_y >= y and Mouse_y <= y + SHOP_SKILL_H:
                    ill_butt.count_demon = ill_butt.count_demon_standart[i]

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        locations_game.achiv_count_demons = 1
                        locations_game.achiv_info_count_demons = [0, 0, 0, 0, 0].copy()
                        locations_game.achiv_info_count_demons[i] = 1
                        click.play()

            ill_butt.forse = ill_butt.forse_standart[-1]
            for i in range(MAX_FORSE):
                x = achiv.forses[i].rect.x
                y = achiv.forses[i].rect.y
                if Mouse_x >= x and Mouse_x <= x + SHOP_SKILL_W and Mouse_y >= y and Mouse_y <= y + SHOP_SKILL_H:
                    ill_butt.forse = ill_butt.forse_standart[i]

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        locations_game.achiv_forse = 1
                        locations_game.achiv_info_forse = [0, 0, 0, 0, 0].copy()
                        locations_game.achiv_info_forse[i] = 1
                        click.play()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Mouse_x >= EXC[0] and Mouse_x <= EXC[0] + EXC_WH \
                        and Mouse_y >= EXC[1] and Mouse_y <= EXC[1] + EXC_WH and \
                        not locations_game.achiv_demons and not locations_game.achiv_count_demons and not locations_game.achiv_forse:
                    locations_game.achiv = False
                    locations_game.first_list = True
                    click.play()

                if Mouse_x >= EXC_INFO[0] and Mouse_x <= EXC_INFO[0] + EXC_INFO_WH \
                        and Mouse_y >= EXC_INFO[1] and Mouse_y <= EXC_INFO[1] + EXC_INFO_WH \
                        and (locations_game.achiv_demons or locations_game.achiv_count_demons or locations_game.achiv_forse):
                    locations_game.achiv_demons = 0
                    locations_game.achiv_count_demons = 0
                    locations_game.achiv_forse = 0
                    click.play()

    def in_menu(self, locations_game, menu_game):
        menu_game.control(locations_game)


