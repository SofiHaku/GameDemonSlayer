from Clicker_base.event import Event
from Clicker_base.Hero import Hero
from Clicker_base.Shop import Shop
from Clicker_base.draw import Draw
from Clicker_base.Demon import Demon_ordinary
from Clicker_base.illumination import illumination
from Clicker_base.achievements import achievements

class main_clicker_base():
    '''Управление текущими событиями кликера'''
    def __init__(self, screen, stat_game):
        self.hero_game = Hero(screen, "Img/Hero/Hero0.png")
        self.stat_game = stat_game
        self.shop_game = Shop(screen)
        self.draw_game = Draw(screen)
        self.demon_classic = Demon_ordinary(screen)
        self.ill_butt = illumination(screen)
        self.achiv = achievements(screen)
        self.control_game = Event()

    def run(self, locations_game, demon_6_moon_start_game):
        '''Передача контроля функциям в зависимости от локации'''
        self.achiv.control(self.shop_game, locations_game, demon_6_moon_start_game)
        if locations_game.shop:
            self.control_game.in_shop(self.shop_game, self.stat_game, locations_game, self.ill_butt)
            self.draw_game.shop(self.shop_game, self.stat_game, locations_game, self.ill_butt, self.achiv)
        elif locations_game.achiv:
            self.control_game.in_achiv(self.achiv, self.stat_game, locations_game, self.ill_butt)
            self.draw_game.achiv(self.shop_game, locations_game, self.ill_butt, self.achiv)
        else:
            self.control_game.control(self.stat_game, self.shop_game, self.hero_game, self.demon_classic, locations_game, self.ill_butt, self.achiv)
            self.draw_game.first_sl(self.shop_game, self.hero_game, self.stat_game, self.demon_classic, self.ill_butt, self.achiv)
            self.demon_classic.move()

