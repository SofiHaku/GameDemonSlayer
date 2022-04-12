import pygame
from settings import *

class Draw():

    def __init__(self, screen):
        self.screen = screen

    def all(self, shop_game, hero_game, stat_game):
        self.screen.fill(B_COLOR)

        if not shop_game.draw_back_bool:
            hero_game.draw()
            stat_game.draw()
            shop_game.func[1].draw()
        else:
            shop_game.func[0].draw()
            shop_game.func[2].draw()

            for i in range(MAX_HERO):
                shop_game.herous[i].draw()
            for i in range(MAX_SKILLS):
                shop_game.skills[i].draw()

        pygame.display.flip()