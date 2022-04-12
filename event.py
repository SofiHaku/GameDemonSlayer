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
                    if Mouse_x >= 20 and Mouse_x < 200 and Mouse_y >= 200 and Mouse_y <= 350:
                        shop_game.draw_back_bool = True

    def in_shop(self, shop_game, stat_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                if Mouse_x >= 500 and Mouse_x < 530 and Mouse_y >= 20 and Mouse_y <= 50:
                    shop_game.draw_back_bool = False
                if Mouse_x >= 20 and Mouse_x < 300 and Mouse_y >= 20 and Mouse_y <= 300:
                    if stat_game.point_now >= 200 and not shop_game.herous[0].buy:
                        shop_game.herous[0].buy = True
                        shop_game.herous[0].image = pygame.image.load('Img/Shop/Hero/Hero_buy' + str(1) + '.png')
                        stat_game.point_now -= 200
                        stat_game.image_score()
                        with open('buy_herous.txt', 'w') as f:
                            f.write('100')
                        with open('points.txt', 'w') as f:
                            f.write('200')




