import pygame
import sys

from settings import *

class Event():

    def __init__(self):
        pass

    def control(self, screen, stat_game, shop_game):
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
                    if Mouse_x >= 500 and Mouse_x < 530 and Mouse_y >= 20 and Mouse_y <= 50:
                        shop_game.draw_back_bool = False




