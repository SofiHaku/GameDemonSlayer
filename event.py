import pygame
import sys

from settings import *

class Event():

    def __init__(self):
        pass

    def control(self, stat_game, shop_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN and not shop_game.draw_back_bool:
                if event.key == pygame.K_SPACE:
                    stat_game.point_now += 1
                    with open('points.txt', 'w') as f:
                        f.write(str(stat_game.point_now))
                    stat_game.image_score()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    if Mouse_x >= SHOP[0] and Mouse_x <= SHOP[0] + SHOP_WH \
                            and Mouse_y >= SHOP[1] and Mouse_y <= SHOP[1] + SHOP_WH:
                        shop_game.draw_back_bool = True

    def in_shop(self, shop_game, stat_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                if Mouse_x >= EXC[0]  and Mouse_x <= EXC[0] + EXC_WH \
                        and Mouse_y >= EXC[1] and Mouse_y <= EXC[1] + EXC_WH:
                    shop_game.draw_back_bool = False
                for i in range(MAX_HERO):
                    x = shop_game.herous[i].rect.x
                    y = shop_game.herous[i].rect.y
                    cost = shop_game.herous[i].cost
                    if Mouse_x >= x and Mouse_x <= x + SHOP_HERO_W and Mouse_y >= y and Mouse_y <= y + SHOP_HERO_H:
                        if stat_game.point_now >= cost and not shop_game.herous[i].buy:
                            shop_game.herous[i].buy = True
                            shop_game.herous[i].image = pygame.image.load('Img/Shop/Hero/Hero_buy' + str(i) + '.png')
                            stat_game.point_now -= cost
                            stat_game.image_score()
                            with open('buy_herous.txt', 'r') as file_1:
                                new_buy_herous = list(file_1.read())
                                new_buy_herous[i] = '1'
                                with open('buy_herous.txt', 'w') as file_2:
                                    file_2.write("".join(new_buy_herous))
                            with open('points.txt', 'w') as file:
                                file.write(str(stat_game.point_now))
                        break

                for i in range(MAX_SKILLS):
                    x = shop_game.skills[i].rect.x
                    y = shop_game.skills[i].rect.y
                    cost = shop_game.skills[i].cost
                    if Mouse_x >= x and Mouse_x <= x + SHOP_SKILL_W and Mouse_y >= y and Mouse_y <= y + SHOP_SKILL_H:
                        if stat_game.point_now >= cost and not shop_game.skills[i].buy:
                            shop_game.skills[i].buy = True
                            shop_game.skills[i].image = pygame.image.load('Img/Shop/Skills/skill_buy' + str(i) + '.png')
                            stat_game.point_now -= cost
                            stat_game.image_score()
                            with open('buy_skills.txt', 'r') as file_1:
                                new_buy_skills = list(file_1.read())
                                new_buy_skills[i] = '1'
                                with open('buy_skills.txt', 'w') as file_2:
                                    file_2.write("".join(new_buy_skills))
                            with open('points.txt', 'w') as file:
                                file.write(str(stat_game.point_now))
                        break




