import pygame
import pygame.font
from illumination import illumination
from settings import *
from threading import Timer
from text_message import text_message

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
        self.tan = pygame.image.load('Img/Demon_6_moon/Tangiro.png')
        self.tan_rect = self.tan.get_rect()
        self.tan_rect.x = 0
        self.tan_rect.y = 0

    def all(self, shop_game, hero_game, stat_game, demon_classic, lab_game,
            locations_game, demon_6_moon, points, hero_mini, ill_butt, achiv, menu_game):

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

        if locations_game.shop:

            text_g = text_message(self.screen)

            text_g = text_message(self.screen)
            if locations_game.shop_lamp:
                text_g.draw_many_lines(290, 75, text_g.shop_mess_lamp, 20)
                shop_game.func[4].draw()
                shop_game.func[5].draw()
            elif locations_game.shop_hero:
                for i in range(len(locations_game.shop_info_hero)):
                    if locations_game.shop_info_hero[i]:
                        text_g.draw_many_lines(290, 75, text_g.shop_mess_hero[i], 20)
                        shop_game.herous_info[i].draw()
                        break
                shop_game.func[4].draw()

            elif locations_game.shop_skills:
                for i in range(len(locations_game.shop_info_skills)):
                    if locations_game.shop_info_skills[i]:
                        text_g.draw_many_lines(300, 95, text_g.shop_mess_skills[i], 20)
                        shop_game.skills_info[i].draw()
                        break
                shop_game.func[4].draw()
            else:
                shop_game.func[0].draw()
                #pygame.draw.rect(self.screen, (255, 255, 255),
                                 #(self.screen_rect.right // 3, self.screen_rect.y, self.screen_rect.right // 3, 70))
                shop_game.func[2].draw()
                shop_game.func[3].draw()

                if ill_butt.exc:
                    ill_butt.button(EXC[0], EXC[1], EXC_WH, EXC_WH)
                if ill_butt.lamp:
                    ill_butt.button(LAMP[0], LAMP[1], LAMP_WH, LAMP_WH)

                for i in range(MAX_HERO):
                    shop_game.herous[i].draw()
                    shop_game.draw_cost_hero(shop_game.herous[i].rect.right, shop_game.herous[i].rect.bottom, i)
                    if ill_butt.hero[i]:
                        ill_butt.button(shop_game.herous[i].rect.x, shop_game.herous[i].rect.y, 125, 125)
                for i in range(MAX_SKILLS):
                    shop_game.skills[i].draw()
                    shop_game.image_count(shop_game.skills[i].count)
                    shop_game.draw_count(shop_game.max_skills_coord[i][0], shop_game.max_skills_coord[i][1], i)
                    if ill_butt.skills[i]:
                        ill_butt.button(shop_game.skills[i].rect.x, shop_game.skills[i].rect.y, 85, 75)

                stat_game.score_rect.y = 25
                stat_game.score_rect.centerx = self.screen_rect.centerx
                stat_game.draw()
                if shop_game.return_dont_have_many:
                    Mouse_x, Mouse_y = pygame.mouse.get_pos()
                    shop_game.draw_you_dont_have_many(Mouse_x, Mouse_y, text_g)

        elif locations_game.menu:
            menu_game.anim()

        elif locations_game.demon_6_moon:
            self.screen.blit(self.tan, self.tan_rect)
            lab_game.walls_draw()
            for point in points:
                point.draw()
            hero_mini.draw()
            demon_6_moon.draw()

        elif locations_game.achiv:

            text_g = text_message(self.screen)
            if locations_game.achiv_demons:
                for i in range(len(locations_game.achiv_info_demons)):
                    if locations_game.achiv_info_demons[i]:
                        text_g.draw_many_lines(20, 0, text_g.mess_demon[i][0], 40)
                        #achiv.count_demon.
                shop_game.func[4].draw()
            elif locations_game.achiv_count_demons:
                for i in range(len(locations_game.achiv_info_count_demons)):
                    if locations_game.achiv_info_count_demons[i]:
                        text_g.draw_many_lines(20, 0, text_g.mess_count_demons[i], 40)
                shop_game.func[4].draw()
            elif locations_game.achiv_forse:
                for i in range(len(locations_game.achiv_info_forse)):
                    if locations_game.achiv_info_forse[i]:
                        text_g.draw_many_lines(20, 0, text_g.mess_forse[i], 40)
                shop_game.func[4].draw()
            else:
                achiv.func[1].draw()
                achiv.func[2].draw()

                if ill_butt.exc:
                    ill_butt.button(EXC[0], EXC[1], EXC_WH, EXC_WH)

                for i in range(MAX_MOON_DEMON):
                    achiv.demons_moon[i].draw()
                    if ill_butt.demon[i]:
                        ill_butt.button(achiv.demons_moon[i].rect.x, achiv.demons_moon[i].rect.y, 125, 125)

                for i in range(MAX_COUNT_DEMON):
                    achiv.count_demon[i].draw()
                    if ill_butt.count_demon[i]:
                        ill_butt.button(achiv.count_demon[i].rect.x, achiv.count_demon[i].rect.y, 75, 75)

                for i in range(MAX_FORSE):
                    achiv.forses[i].draw()
                    if ill_butt.forse[i]:
                        ill_butt.button(achiv.forses[i].rect.x, achiv.forses[i].rect.y, 75, 75)
        else:
            hero_game.draw()
            stat_game.score_rect.x = 100
            stat_game.score_rect.y = 160
            stat_game.draw()
            shop_game.func[1].draw()
            achiv.draw()

            if ill_butt.to_shop:
                ill_butt.button(SHOP[0], SHOP[1], SHOP_WH, SHOP_WH)

            elif ill_butt.to_achiv:
                ill_butt.button(CUP[0], CUP[1], CUP_WH[0], CUP_WH[1])



            self.screen.blit(self.state, self.state_rect)
            self.state_name = self.font.render("Вы хлебушек!", True, (0, 0, 0), (255, 255, 255))
            self.state_name_rect = self.state_name.get_rect()
            self.state_name_rect.top = self.state_rect.bottom
            self.state_name_rect.centerx = self.state_rect.centerx
            self.screen.blit(self.state_name, self.state_name_rect)

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