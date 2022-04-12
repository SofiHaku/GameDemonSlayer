import pygame
from settings import *

class Draw():

    def __init__(self, screen):
        self.screen = screen

    def all(self, shop_game, hero_game, stat_game):dir
        self.screen.fill(B_COLOR)

        if not shop_game.draw_back_bool:
            hero_game.draw()
            stat_game.draw()
            shop_game.draw_now()
        else:
            shop_game.draw_back()
            for i in range(3):
                shop_game.herous[i].draw()
            shop_game.draw_exc()

        pygame.display.flip()