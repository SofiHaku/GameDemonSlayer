import pygame
import pygame.font
from settings import *
from text_message import text_message

class Draw():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.state = pygame.image.load('Img/Achievements/State/state1.png')
        self.state_rect = self.state.get_rect()
        self.state_rect.y = self.screen_rect.y + 10 + 20
        self.state_rect.centerx = 100
        self.text_g = text_message(self.screen)

        self.back = pygame.image.load('Img/Background.png')
        self.back_rect = self.back.get_rect()
        self.back_rect = self.back.get_rect()
        self.back_rect.centery = self.screen_rect.centery
        self.back_rect.left = SETTING


    def shop(self, shop_game, stat_game, locations_game, ill_butt, achiv):
        self.screen.fill((255, 255, 255))

        # Проверка перехода в страницы-описания
        if locations_game.shop_lamp:
            # Описание лампы-подсказки
            self.text_g.draw_many_lines(290, 75, self.text_g.shop_mess_lamp, 20)
            shop_game.func[4].draw()
            shop_game.func[5].draw()

        elif locations_game.shop_hero:
            # Описание героев
            for i in range(len(locations_game.shop_info_hero)):
                if locations_game.shop_info_hero[i]:
                    self.text_g.draw_many_lines(290, 75, self.text_g.shop_mess_hero[i], 20)
                    shop_game.herous_info[i].draw()
                    break
            # Выводим "крестик"
            shop_game.func[4].draw()

        elif locations_game.shop_skills:
            # Описание скиллов
            for i in range(len(locations_game.shop_info_skills)):
                if locations_game.shop_info_skills[i]:
                    self.text_g.draw_many_lines(300, 95, self.text_g.shop_mess_skills[i], 20)
                    shop_game.skills_info[i].draw()
                    break
            # Выводим "крестик"
            shop_game.func[4].draw()

        else:
            # Выводим фон, "крестик", иконку лампочки
            shop_game.func[0].draw()
            shop_game.func[2].draw()
            shop_game.func[3].draw()

            # Блок проверки подсветки кнопок
            # Подсветка "крестика"
            if ill_butt.exc:
                ill_butt.button(EXC[0], EXC[1], EXC_WH, EXC_WH)

            # Подсветка "лампы"
            if ill_butt.lamp:
                ill_butt.button(LAMP[0], LAMP[1], LAMP_WH, LAMP_WH)

            # Подсветка "героев"
            for i in range(MAX_HERO):
                shop_game.herous[i].draw()
                shop_game.draw_cost_hero(shop_game.herous[i].rect.right, shop_game.herous[i].rect.bottom, i)
                if ill_butt.hero[i]:
                    ill_butt.button(shop_game.herous[i].rect.x, shop_game.herous[i].rect.y, 125, 125)

            # Подсветка "скиллов"
            for i in range(MAX_SKILLS):
                shop_game.skills[i].draw()
                shop_game.image_count(shop_game.skills[i].buy)
                shop_game.draw_count(shop_game.max_skills_coord[i][0], shop_game.max_skills_coord[i][1], i)
                if ill_butt.skills[i]:
                    ill_butt.button(shop_game.skills[i].rect.x, shop_game.skills[i].rect.y, 85, 75)

            # Вывод количества монеток на экран
            stat_game.score_rect.y = 25
            stat_game.score_rect.centerx = self.screen_rect.centerx
            stat_game.draw()

            # Вывод изображения об отсутствии денег
            if shop_game.return_dont_have_many():
                Mouse_x, Mouse_y = pygame.mouse.get_pos()
                shop_game.draw_you_dont_have_many(Mouse_x, Mouse_y, self.text_g)

        if achiv.return_have_new_achiv():
            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            achiv.draw_new_achiv(Mouse_x, Mouse_y, self.text_g)

        pygame.display.flip()

        #elif locations_game.demon_6_moon_start:
            #demon_6_moon_start_game.draw(text_g)


    def achiv (self, shop_game, locations_game, ill_butt, achiv):
        """Вывод достижений на экран"""

        self.screen.fill((255, 255, 255))

        if locations_game.achiv_demons:
            for i in range(len(locations_game.achiv_info_demons)):
                if locations_game.achiv_info_demons[i]:
                    if i == 0:
                        self.text_g.draw_many_lines(330, 75, self.text_g.mess_demon[i][locations_game.use_demon_6_moon], 20)
                    else:
                        self.text_g.draw_many_lines(330, 75, self.text_g.mess_demon[i][locations_game.use_demon_3_moon],
                                                    20)
                    achiv.demons_moon[i].draw_info()
            shop_game.func[4].draw()
        elif locations_game.achiv_count_demons:
            for i in range(len(locations_game.achiv_info_count_demons)):
                if locations_game.achiv_info_count_demons[i]:
                    self.text_g.draw_many_lines(290, 75, self.text_g.mess_count_demons[i], 20)
                    achiv.count_demon[i].draw_info()
            shop_game.func[4].draw()
        elif locations_game.achiv_forse:
            for i in range(len(locations_game.achiv_info_forse)):
                if locations_game.achiv_info_forse[i]:
                    self.text_g.draw_many_lines(290, 75, self.text_g.mess_forse[i], 20)
                    achiv.forses[i].draw_info()
            shop_game.func[4].draw()
        else:
            achiv.func[1].draw()
            achiv.func[2].draw()

            if ill_butt.exc:
                ill_butt.button(EXC[0], EXC[1], EXC_WH, EXC_WH)

            for i in range(2):
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

        pygame.display.flip()

    def first_sl(self, shop_game, hero_game, stat_game, demon_classic, ill_butt, achiv):
        self.screen.blit(self.back, self.back_rect)

        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen_rect.x, self.screen_rect.y, WIDTH // 3, HEIGHT))
        pygame.draw.rect(self.screen, (255, 255, 255), (self.screen_rect.x, self.screen_rect.y, WIDTH, 10))
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (self.screen_rect.x, self.screen_rect.bottom - 10, WIDTH, 10))
        pygame.draw.rect(self.screen, (255, 255, 255),
                         (self.screen_rect.right - 10, self.screen_rect.y, 10, HEIGHT))

        hero_game.draw(shop_game.what_gero_buy())
        stat_game.score_rect.x = 100
        stat_game.score_rect.y = 160
        stat_game.draw()
        shop_game.func[1].draw()
        achiv.draw()

        if ill_butt.to_shop:
            ill_butt.button(SHOP[0], SHOP[1], SHOP_WH, SHOP_WH)

        elif ill_butt.to_achiv:
            ill_butt.button(CUP[0], CUP[1], CUP_WH[0], CUP_WH[1])

        achiv.draw_general_state()

        if not demon_classic.die():
            demon_classic.draw()
            demon_classic.draw_streak_of_life()
        else:
            demon_classic.create()
            demon_classic.draw()
            demon_classic.draw_streak_of_life()

        if achiv.return_have_new_achiv():
            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            achiv.draw_new_achiv(Mouse_x, Mouse_y, self.text_g)

        pygame.display.flip()