import pygame
import pygame.font
from Globals import Globals
from text_message import text_message

class Draw():
    '''Класс, отвечающий за вывод всех изображений на экран'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.globals = Globals()

        self.state = pygame.image.load('Img/Achievements/State/state1.png')
        self.state_rect = self.state.get_rect()
        self.state_rect.y = self.globals.GENERAL_STATE_Y
        self.state_rect.centerx = self.globals.GENERAL_STATE_X
        self.text_g = text_message(self.screen)

        self.back = pygame.image.load('Img/Background.png')
        self.back_rect = self.back.get_rect()
        self.back_rect = self.back.get_rect()
        self.back_rect.centery = self.screen_rect.centery
        self.back_rect.left = self.globals.SETTING


    def shop(self, shop_game, stat_game, locations_game, ill_butt, achiv):
        '''Вывод изображений в магазине'''
        self.screen.fill(self.globals.B_COLOR_NEW_SURF)
        # Проверка перехода в страницы-описания
        if locations_game.shop_lamp:
            self.draw_lamp(shop_game)
        elif locations_game.shop_hero:
            self.draw_hero(locations_game, shop_game)
        elif locations_game.shop_skills:
            self.draw_skills(locations_game, shop_game)
        else:
            self.basic_shop(shop_game, stat_game)
            self.glow_shop(ill_butt, shop_game)
            self.new_achiv(achiv)
            self.not_many(shop_game)
        pygame.display.flip()

    def draw_lamp(self, shop_game):
        '''Описание лампы-подсказки'''
        self.text_g.draw_many_lines(self.globals.TEXT_LINES_XY[0], self.globals.TEXT_LINES_XY[1],
                                    self.text_g.shop_mess_lamp, self.globals.TEXT_SIZE)
        shop_game.func[4].draw()
        shop_game.func[5].draw()

    def draw_hero(self, locations_game, shop_game):
        '''Описание героев'''
        for i in range(len(locations_game.shop_info_hero)):
            if locations_game.shop_info_hero[i]:
                self.text_g.draw_many_lines(self.globals.TEXT_LINES_XY[0], self.globals.TEXT_LINES_XY[1],
                                            self.text_g.shop_mess_hero[i], self.globals.TEXT_SIZE)
                shop_game.herous_info[i].draw()
                break
        # Выводим "крестик"
        shop_game.func[4].draw()

    def draw_skills(self, locations_game, shop_game):
        '''Описание скиллов'''
        for i in range(len(locations_game.shop_info_skills)):
            if locations_game.shop_info_skills[i]:
                self.text_g.draw_many_lines(self.globals.TEXT_LINES_T2_XY[0], self.globals.TEXT_LINES_T2_XY[1],
                                            self.text_g.shop_mess_skills[i], self.globals.TEXT_SIZE)
                shop_game.skills_info[i].draw()
                break
        # Выводим "крестик"
        shop_game.func[4].draw()

    def basic_shop(self, shop_game, stat_game):
        '''Вывод основых атрибутов на экран'''
        # Выводим фон, "крестик", иконку лампочки
        shop_game.func[0].draw()
        shop_game.func[2].draw()
        shop_game.func[3].draw()

        # Вывод количества монеток на экран
        stat_game.score_rect.y = self.globals.MONEY_Y
        stat_game.score_rect.centerx = self.screen_rect.centerx
        stat_game.draw()

    def not_many(self, shop_game):
        ''' Вывод изображения об отсутствии денег'''
        if shop_game.return_dont_have_many():
            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            shop_game.draw_you_dont_have_many(Mouse_x, Mouse_y, self.text_g)

    def new_achiv(self, achiv):
        ''' Вывод информации о новом достижении'''
        if achiv.return_have_new_achiv():
            Mouse_x, Mouse_y = pygame.mouse.get_pos()
            achiv.draw_new_achiv(Mouse_x, Mouse_y, self.text_g)

    def glow_shop(self, ill_butt, shop_game):
        '''Вывод кнопок в магазине и их подстветка'''
        # Подсветка "крестика"
        if ill_butt.exc:
            ill_butt.button(self.globals.EXC[0], self.globals.EXC[1], self.globals.EXC_WH, self.globals.EXC_WH)
        # Подсветка "лампы"
        if ill_butt.lamp:
            ill_butt.button(self.globals.LAMP[0], self.globals.LAMP[1], self.globals.LAMP_WH, self.globals.LAMP_WH)
        # Подсветка "героев"
        for i in range(self.globals.MAX_HERO):
            shop_game.herous[i].draw()
            shop_game.draw_cost_hero(shop_game.herous[i].rect.right, shop_game.herous[i].rect.bottom, i)
            if ill_butt.hero[i]:
                ill_butt.button(shop_game.herous[i].rect.x, shop_game.herous[i].rect.y, self.globals.SHOP_HERO_W, self.globals.SHOP_HERO_H)
        # Подсветка "скиллов"
        for i in range(self.globals.MAX_SKILLS):
            shop_game.skills[i].draw()
            shop_game.image_count(shop_game.skills[i].buy)
            shop_game.draw_count(shop_game.max_skills_coord[i][0], shop_game.max_skills_coord[i][1], i)
            if ill_butt.skills[i]:
                ill_butt.button(shop_game.skills[i].rect.x, shop_game.skills[i].rect.y, self.globals.SHOP_SKILL_W, self.globals.SHOP_SKILL_H)


    def achiv (self, shop_game, locations_game, ill_butt, achiv):
        """Вывод достижений на экран"""
        self.screen.fill(self.globals.B_COLOR_NEW_SURF)

        if locations_game.achiv_demons:
            self.draw_achiv_demon(locations_game, shop_game, achiv)
        elif locations_game.achiv_count_demons:
            self.draw_achiv_count_demons(locations_game, achiv, shop_game)
        elif locations_game.achiv_forse:
            self.draw_schiv_forse(locations_game, achiv, shop_game)
        else:
           self.draw_list_achiv(achiv, ill_butt)

        pygame.display.flip()

    def draw_achiv_demon(self, locations_game, shop_game, achiv):
        '''Вывод информации о достижениях-победе над демонами-лунами'''
        for i in range(len(locations_game.achiv_info_demons)):
            if locations_game.achiv_info_demons[i]:
                if i == 0:
                    self.text_g.draw_many_lines(self.globals.TEXT_LINES_T3_XY[0], self.globals.TEXT_LINES_T3_XY[1],
                                                self.text_g.mess_demon[i][locations_game.use_demon_6_moon], self.globals.TEXT_SIZE)
                else:
                    self.text_g.draw_many_lines(self.globals.TEXT_LINES_T3_XY[0], self.globals.TEXT_LINES_T3_XY[1],
                                                self.text_g.mess_demon[i][locations_game.use_demon_3_moon], self.globals.TEXT_SIZE)
                achiv.demons_moon[i].draw_info(self.globals)
        shop_game.func[4].draw()

    def draw_achiv_count_demons(self, locations_game, achiv, shop_game):
        '''Вывод информации о достижениях, которые обозначают количество убитых демонов'''
        for i in range(len(locations_game.achiv_info_count_demons)):
            if locations_game.achiv_info_count_demons[i]:
                self.text_g.draw_many_lines(self.globals.TEXT_LINES_XY[0], self.globals.TEXT_LINES_XY[1],
                                            self.text_g.mess_count_demons[i], self.globals.TEXT_SIZE)
                achiv.count_demon[i].draw_info(self.globals)
        shop_game.func[4].draw()

    def draw_schiv_forse(self, locations_game, achiv, shop_game):
        '''Вывод информации о достижениях, которые обозначают силу персонажа'''
        for i in range(len(locations_game.achiv_info_forse)):
            if locations_game.achiv_info_forse[i]:
                self.text_g.draw_many_lines(self.globals.TEXT_LINES_XY[0], self.globals.TEXT_LINES_XY[1],
                                            self.text_g.mess_forse[i], self.globals.TEXT_SIZE)
                achiv.forses[i].draw_info(self.globals)
        shop_game.func[4].draw()

    def draw_list_achiv(self, achiv, ill_butt):
        '''Вывод основной страницы достижений'''
        achiv.func[1].draw()
        achiv.func[2].draw()

        if ill_butt.exc:
            ill_butt.button(self.globals.EXC[0], self.globals.EXC[1], self.globals.EXC_WH, self.globals.EXC_WH)

        for i in range(2):
            achiv.demons_moon[i].draw()
            if ill_butt.demon[i]:
                ill_butt.button(achiv.demons_moon[i].rect.x, achiv.demons_moon[i].rect.y, self.globals.ACHIV_HERO_HW, self.globals.ACHIV_HERO_HW)
        for i in range(self.globals.MAX_COUNT_DEMON):
            achiv.count_demon[i].draw()
            if ill_butt.count_demon[i]:
                ill_butt.button(achiv.count_demon[i].rect.x, achiv.count_demon[i].rect.y, self.globals.ACHIV_COUNT_DEMON_HW, self.globals.ACHIV_COUNT_DEMON_HW)
        for i in range(self.globals.MAX_FORSE):
            achiv.forses[i].draw()
            if ill_butt.forse[i]:
                ill_butt.button(achiv.forses[i].rect.x, achiv.forses[i].rect.y, self.globals.ACHIV_FORSE_HW, self.globals.ACHIV_FORSE_HW)

    def first_sl(self, shop_game, hero_game, stat_game, demon_classic, ill_butt, achiv):
        '''Вывод изображений в первой странице'''
        self.screen.blit(self.back, self.back_rect)
        self.draw_frame()

        stat_game.score_rect.x = self.globals.SCORE_RECT[0]
        stat_game.score_rect.y = self.globals.SCORE_RECT[1]
        hero_game.draw(shop_game.what_gero_buy())

        stat_game.draw()
        shop_game.func[1].draw()
        achiv.draw()

        self.draw_glow_fl(ill_butt)
        achiv.draw_general_state()
        self.draw_demon_in_fl(demon_classic)
        self.new_achiv(achiv)

        pygame.display.flip()

    def draw_frame(self):
        '''Вывод рамки'''
        pygame.draw.rect(self.screen, self.globals.B_COLOR_NEW_SURF,
                         (self.screen_rect.x, self.screen_rect.y, self.globals.WIDTH // 3, self.globals.HEIGHT))
        pygame.draw.rect(self.screen, self.globals.B_COLOR_NEW_SURF, (self.screen_rect.x, self.screen_rect.y, self.globals.WIDTH, self.globals.FRAME_S))
        pygame.draw.rect(self.screen, self.globals.B_COLOR_NEW_SURF,
                         (self.screen_rect.x, self.screen_rect.bottom - self.globals.FRAME_S, self.globals.WIDTH, self.globals.FRAME_S))
        pygame.draw.rect(self.screen, self.globals.B_COLOR_NEW_SURF,
                         (self.screen_rect.right - self.globals.FRAME_S, self.screen_rect.y, self.globals.FRAME_S, self.globals.HEIGHT))

    def draw_demon_in_fl(self, demon_classic):
        '''Изображение демона на главном экране'''
        if not demon_classic.die():
            demon_classic.draw()
            demon_classic.draw_streak_of_life()
        else:
            demon_classic.create()
            demon_classic.draw()
            demon_classic.draw_streak_of_life()

    def draw_glow_fl(self, ill_butt):
        '''Изображение свечения на главном экране'''
        if ill_butt.to_shop:
            ill_butt.button(self.globals.SHOP[0], self.globals.SHOP[1], self.globals.SHOP_WH, self.globals.SHOP_WH)

        elif ill_butt.to_achiv:
            ill_butt.button(self.globals.CUP[0], self.globals.CUP[1], self.globals.CUP_WH[0], self.globals.CUP_WH[1])