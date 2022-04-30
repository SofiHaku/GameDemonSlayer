class Globals:
    '''Класс со всеми глобальными переменными'''
    def __init__(self):
        # Экран
        self.WIDTH = 600
        self.HEIGHT = 400

        # Фон поверхностей
        self.B_COLOR = (60, 170, 113)
        self.B_COLOR_NEW_SURF = (255, 255, 255)

        # Размеры в магазине
        self.SHOP_HERO_W = 125
        self.SHOP_HERO_H = 125
        self.SHOP_SKILL_W = 85
        self.SHOP_SKILL_H = 75
        self.EXC_WH = 30
        self.EXC_INFO_WH = 30
        self.LAMP_WH = 60
        self.DONT_MONET_SURF_S = (500, 300)
        self.DIFF_SKILL_X = 52
        self.DIFF_SKILL_Y = 15

        # Координаты в магазине
        self.SHOP = [25, 200]
        self.EXC = [550, 20]
        self.EXC_INFO = [550, 20]
        self.EXC_DONT_MONEY = [450, 20]
        self.IMG_DONT_MONEY = [20, 30]
        self.SURF_DONT_MONEY = [50, 50]
        self.LAMP = [0, 0]
        self.LAMP_INFO_XY = [15, 80]
        self.HERO_INFO_XY = [25, 75]
        self.SKILL_INFO_XY = [25, 95]

        # Стоимость объектов
        self.cost_hero = [200, 500, 1000]
        self.cost_skills = [100, 150, 200, 250, 300, 350, 450, 500]
        self.plus_points_d = [1, 2, 4, 8, 16, 32, 64, 128]

        # Главный экран
        # Размеры на главном экране
        self.SHOP_WH = 150
        self.SETTING = 200
        self.DEMON_W = 120
        self.DEMON_H = 225
        self.CUP_WH = [36, 46]

        # Координаты на главном экране
        self.COUNT = [100, 150]
        self.CUP = [50, 140]
        self.GENERAL_STATE_Y = 30
        self.GENERAL_STATE_X = 100

        # Иные размеры на главном экране
        self.DEMON_LIFE = self.DEMON_W - 8
        self.DEMON_CL_L = self.SETTING + 30

        # Достижения
        # Размеры в достижениях
        self.ACHIV_S = 75
        self.NEW_SURF_ACHIV_SIZE = (550, 300)
        self.NEW_SURF_TEXT_S = 25
        self.ACHIV_HERO_HW = 125
        self.ACHIV_COUNT_DEMON_HW = 75
        self.ACHIV_FORSE_HW = 75

        # Координаты в достижениях
        self.ACHIV_COUNT_DEMON_Y = 20
        self.ACHIV_FORSE_Y = 10
        self.EXC_NEW_ACHIV_XY = [525, 70]
        self.NEW_SURF_ACHIV_XY = [25, 50]
        self.NEW_SURF_ACHIV_IMG_XY = [0, 30]
        self.NEW_SURF_ACHIV_EXC_XY = [500, 20]
        self.NEW_SURF_ACHIV_TEXT_FORSE_XY = [270, 55]
        self.NEW_SURF_ACHIV_TEXT_C_D_XY = [270, 85]

        self.MOVE_DEMON_SIZE_TO_END = 30
        self.DEMON_STEAK_LIFE_S = 20
        self.DIFF_SMALL_AND_BIG_DEMON_STEAK_LIFE = 4
        self.COLOR_STEAK_BL = (255, 255, 255)
        self.COLOR_STEAK_SL = (221, 44, 0)

        # "Стоимость" достижений
        self.DIFF_ACHIV_COUNT_DEMON = 5
        self.DIFF_ACHIV_POINTS_IN_CLICK = 25
        self.FIRST_ACHIV_POINTS_IN_CLICK = 5
        self.FIRST_SPECIAL_ACHIV = 250
        self.SECOND_SPECIAL_ACHIV = 500

        self.INDEX_DEMON_MOON_1_MG = 6
        self.INDEX_DEMON_MOON_2_MG = 3
        self.INDEX_DEMON_MOON_3_MG = 1

        # Количество объектов
        self.MAX_HERO = 3
        self.MAX_MOON_DEMON = 2
        self.MAX_COUNT_DEMON = 5
        self.MAX_SKILLS_SET = 4
        self.MAX_SKILLS = 6
        self.MAX_FORSE = 5
        self.MAX_STATE = 5

        self.INFO_ACHIV_XY = (50, 80)

        # Текст
        # Размер текста
        self.TEXT_SIZE = 20
        self.TEXT_SIZE_2 = 15
        self.TEXT_SIZE_3 = 30
        self.TEXT_SIZE_4 = 40

        # Цвет текста
        self.TEXT_COLOR = (0, 0, 0)
        self.COLOR_BACK_TEXT = (255, 255, 255)

        # Координаты текста
        self.TEXT_LINES_XY = [290, 75]
        self.TEXT_LINES_T2_XY = [300, 95]
        self.TEXT_LINES_T3_XY = [330, 75]
        self.TEXT_LINES_T4_XY = [310, 150]
        self.TEXT_LINES_T5_XY = [100, 160]
        self.TEXT_LINES_T5_XY = [30, 150]
        self.TEXT_LINES_T6_X_DIFF = [30, 90]
        self.TEXT_LINES_T7_XY = [150, 280]

        self.MONEY_Y = 25
        self.SCORE_RECT = [100, 160]
        self.FRAME_S = 10
        self.HERO_XY_FL = [185, 550]
        self.GLOW_F = 50


        # Первая мини-игра

        # Координаты
        self.RECT_DEMON = [200, 19]
        self.PLACE_TO_MOVE = [[180 + 5 * 20, 3 * 19], [180 + 15 * 20, 3 * 19], [180 + 5 * 20, 13 * 19],
                              [180 + 15 * 20, 13 * 19],
                              [180 + 7 * 20, 7 * 19], [180 + 13 * 20, 7 * 19], [180 + 7 * 20, 11 * 19],
                              [180 + 13 * 20, 11 * 19]]
        self.HERO_RECT = [180 + 21 * 18 + 2, 21 * 17 + 4]
        self.WIN_X = 360

        # Размеры
        self.WALL_X_LEFT = 180
        self.MAX_WALL = 20
        self.MAX_WALL_H = 19
        self.WALL_CENTER_DEL = 15

        # Цвет
        self.BACK_C = (0, 121, 107)
        self.IDEX_SPEC = [[5, 15], [3, 13], [7, 13], [7, 11]]

        self.MAX_ALM = 180
