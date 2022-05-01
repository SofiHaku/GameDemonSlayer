class now_locations():
    '''Класс управляющий (булевые функции, которые потом использует классы control) локациями игры'''
    def __init__(self):
        self.first_list = False
        self.shop = False
        self.achiv = False
        self.menu = True

        self.shop_lamp = 0
        self.shop_hero = False
        self.shop_skills = False
        self.shop_info_hero = [0, 0, 0]
        self.shop_info_skills = [0, 0, 0, 0, 0, 0, 0, 0]

        self.achiv_demons = 0
        self.achiv_count_demons = 0
        self.achiv_forse = 0
        self.achiv_info_demons = [0, 0, 0]
        self.achiv_info_count_demons = [0, 0, 0, 0, 0]
        self.achiv_info_forse = [0, 0, 0, 0, 0]

        self.demon_6_moon_start = False
        self.demon_6_moon = False
        self.demon_6_moon_end = False
        self.demon_3_moon_start = False
        self.demon_3_moon = False
        self.demon_3_moon_end = False

        with open('save_data/use_demon', 'r') as file:
            use = list(file.read())
            self.use_demon_6_moon = int(use[0])
            self.use_demon_3_moon = int(use[1])