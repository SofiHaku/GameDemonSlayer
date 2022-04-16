import pygame
import sys

from settings import *


class Event():

    def __init__(self):
        pass

    def control_achiv(self, statistics_game, shop_game, locations_game):
        statistics_game.achievements(shop_game, locations_game)

    def control(self, stat_game, shop_game, hero_game, demon_game, locations_game, ill_butt):
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

            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            if Mouse_x >= SHOP[0] and Mouse_x <= SHOP[0] + SHOP_WH \
                    and Mouse_y >= SHOP[1] and Mouse_y <= SHOP[1] + SHOP_WH:
                ill_butt.to_shop = 1
            else:
                ill_butt.to_shop = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    if Mouse_x >= SHOP[0] and Mouse_x <= SHOP[0] + SHOP_WH \
                            and Mouse_y >= SHOP[1] and Mouse_y <= SHOP[1] + SHOP_WH:
                        locations_game.shop = True
                        locations_game.first_list = False

    def in_shop(self, shop_game, stat_game, locations_game, ill_butt):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            for i in range(MAX_HERO):
                x = shop_game.herous[i].rect.x
                y = shop_game.herous[i].rect.y
                if Mouse_x >= x and Mouse_x <= x + SHOP_HERO_W and Mouse_y >= y and Mouse_y <= y + SHOP_HERO_H:
                    ill_butt.hero = ill_butt.hero_standart[i]

            for i in range(MAX_SKILLS):
                x = shop_game.skills[i].rect.x
                y = shop_game.skills[i].rect.y
                if Mouse_x >= x and Mouse_x <= x + SHOP_SKILL_W and Mouse_y >= y and Mouse_y <= y + SHOP_SKILL_H:
                    ill_butt.skills = ill_butt.skills_standart[i]

            if Mouse_x >= EXC[0] and Mouse_x <= EXC[0] + EXC_WH \
                    and Mouse_y >= EXC[1] and Mouse_y <= EXC[1] + EXC_WH:
                ill_butt.exc = 1
            else:
                ill_butt.exc = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                if Mouse_x >= EXC[0] and Mouse_x <= EXC[0] + EXC_WH \
                        and Mouse_y >= EXC[1] and Mouse_y <= EXC[1] + EXC_WH:
                    locations_game.shop = False
                    locations_game.first_list = True
                for i in range(MAX_HERO):
                    x = shop_game.herous[i].rect.x
                    y = shop_game.herous[i].rect.y
                    cost = shop_game.herous[i].cost
                    if Mouse_x >= x and Mouse_x <= x + SHOP_HERO_W and Mouse_y >= y and Mouse_y <= y + SHOP_HERO_H:
                        if stat_game.point_now >= cost and not shop_game.herous[i].buy:
                            shop_game.herous[i].buy = True
                            shop_game.herous[i].image = pygame.image.load('Img/Shop/Hero/Hero_buy' + str(i) + '.png')
                            stat_game.point_now -= cost
                            stat_game.image_score(COUNT[0], COUNT[1])
                            with open('Save_data/buy_herous.txt', 'r') as file_1:
                                new_buy_herous = list(file_1.read())
                                new_buy_herous[i] = '1'
                                with open('Save_data/buy_herous.txt', 'w') as file_2:
                                    file_2.write("".join(new_buy_herous))
                            with open('Save_data/points.txt', 'w') as file:
                                file.write(str(stat_game.point_now))
                        break

                for i in range(MAX_SKILLS):
                    x = shop_game.skills[i].rect.x
                    y = shop_game.skills[i].rect.y
                    cost = shop_game.skills[i].cost
                    if Mouse_x >= x and Mouse_x <= x + SHOP_SKILL_W and Mouse_y >= y and Mouse_y <= y + SHOP_SKILL_H:
                        if stat_game.point_now >= cost and shop_game.skills[i].count < 5:
                            stat_game.point_now -= cost
                            stat_game.image_score(COUNT[0], COUNT[1])
                            shop_game.skills[i].count += 1

                            with open('Save_data/count_skills.txt', 'r') as file:
                                new_count = list(file.read())
                                new_count[i] = str(shop_game.skills[i].count)
                                with open('Save_data/buy_skills.txt', 'w') as file_1:
                                    file_1.write("".join(new_count))
                                with open('Save_data/count_skills.txt', 'w') as file_2:
                                    file_2.write("".join(new_count))

                            with open('Save_data/points.txt', 'w') as file:
                                file.write(str(stat_game.point_now))
                        break

    def demon_6_moon(self, in_lab_game, hero_mini, wall, lab_game, demon_6_moon):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    hero_mini.move_to_up = True
                elif event.key == pygame.K_DOWN:
                    hero_mini.move_to_down = True
                elif event.key == pygame.K_RIGHT:
                    hero_mini.move_to_right = True
                elif event.key == pygame.K_LEFT:
                    hero_mini.move_to_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    hero_mini.move_to_up = False
                elif event.key == pygame.K_DOWN:
                    hero_mini.move_to_down = False
                elif event.key == pygame.K_RIGHT:
                    hero_mini.move_to_right = False
                elif event.key == pygame.K_LEFT:
                    hero_mini.move_to_left = False

        in_lab_game.corner_hero(hero_mini, wall)
        demon_6_moon.movement()
        demon_6_moon.update()
