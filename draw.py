import pygame
import pygame.font
from settings import *
from threading import Timer

class Draw():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        '''self.back = pygame.image.load('Img/Background.png')
        self.back_rect = self.back.get_rect()
        self.back_rect.centery = self.screen_rect.centery
        self.back_rect.left = SETTING'''

        self.state = pygame.image.load('Img/state1.png')
        self.state_rect = self.state.get_rect()
        self.state_rect.y = self.screen_rect.y + 10 + 20
        self.state_rect.centerx = 100

        self.font = pygame.font.SysFont("Verdana", 20)
        self.state_name = None
        self.state_name_rect = None

    def all(self, shop_game, hero_game, stat_game, demon_classic, lab_game, locations_game):

        self.screen.fill((255, 255, 255))
        if locations_game.first_list:
            self.back = pygame.image.load('Img/Background.png')
            self.back_rect = self.back.get_rect()
            self.back_rect = self.back.get_rect()
            self.back_rect.centery = self.screen_rect.centery
            self.back_rect.left = SETTING
            self.screen.blit(self.back, self.back_rect)

        # Рисуем коемочку главного экрана
        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen_rect.x, self.screen_rect.y, WIDTH // 3, HEIGHT))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen_rect.x, self.screen_rect.y, WIDTH, 10))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen_rect.x, self.screen_rect.bottom - 10, WIDTH, 10))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen_rect.right - 10, self.screen_rect.y, 10, HEIGHT))


        self.screen.blit(self.state, self.state_rect)
        self.state_name = self.font.render("Вы хлебушек!", True, (0, 0, 0), (255, 255, 255))
        self.state_name_rect = self.state_name.get_rect()
        self.state_name_rect.top = self.state_rect.bottom
        self.state_name_rect.centerx = self.state_rect.centerx
        self.screen.blit(self.state_name, self.state_name_rect)

        if locations_game.shop:

            shop_game.func[0].draw()
            shop_game.func[2].draw()

            for i in range(MAX_HERO):
                shop_game.herous[i].draw()
                shop_game.draw_cost_hero(shop_game.herous[i].rect.right, shop_game.herous[i].rect.bottom, i)
            for i in range(MAX_SKILLS):
                shop_game.skills[i].draw()
                shop_game.image_count(shop_game.skills[i].count)
                shop_game.draw_count(shop_game.max_skills_coord[i][0], shop_game.max_skills_coord[i][1], i)

        elif locations_game.demon_6_moon:
            stat_game.draw()
            shop_game.func[1].draw()
            lab_game.walls_draw()
            hero_game.draw_mini()

        else:
            hero_game.draw()
            stat_game.draw()
            shop_game.func[1].draw()
            if not demon_classic.die():
                demon_classic.draw()
                demon_classic.draw_streak_of_life()
            else:
                # Позволяет создать интересный эффект перебора персонажей
                # timer = Timer(1, demon_classic.create)
                # timer.start()
                demon_classic.create()
                demon_classic.draw()
                demon_classic.draw_streak_of_life()

        if lab_game.bool:
            lab_game.walls_draw(self.screen)
        pygame.display.flip()