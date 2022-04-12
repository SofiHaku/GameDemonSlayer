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
                shop_game.draw_cost_hero(shop_game.herous[i].rect.right, shop_game.herous[i].rect.bottom, i)
            for i in range(MAX_SKILLS):
                shop_game.skills[i].draw()
                shop_game.image_count(shop_game.skills[i].count)
                shop_game.draw_count(shop_game.max_skills_coord[i][0], shop_game.max_skills_coord[i][1], i)
        pygame.display.flip()