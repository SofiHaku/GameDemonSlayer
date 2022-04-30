import pygame
from Globals import Globals
from Clicker_base.statistics import Stat
from locations import now_locations
from menu import menu
from text_message import text_message
from Mini_game_1.start_and_end_of_6_demon import demon_6_moon_start
from Mini_game_2.main_mini_game_2 import main_mini_game_2
from Mini_game_1.main_mini_game_1 import main_mini_game_1
from Clicker_base.main_clicker_base import main_clicker_base

class Game():
    '''Класс, собирающий все игры вместе'''
    def __init__(self):
        pygame.mixer.pre_init(44100, -16, 1, 512)
        pygame.init()
        self.globals = Globals()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((self.globals.WIDTH, self.globals.HEIGHT))
        self.text_g = text_message(self.screen)
        self.stat_game = Stat(self.screen)
        self.locations_game = now_locations()
        self.menu_game = menu(self.screen)
        self.demon_6_moon_start_game = demon_6_moon_start(self.screen)
        self.mini_game_2_n = main_mini_game_2(self.screen)
        self.main_mini_1_n = main_mini_game_1(self.screen)
        self.mini_clicker_b = main_clicker_base(self.screen, self.stat_game)

        pygame.mixer.music.load("Music/фон.mp3")

    def run(self):
        '''Бесконечный цикл игры'''
        pygame.mixer.music.play(-1, 0, 10)
        while True:
            self.clock.tick(60)
            if self.locations_game.menu:
                self.menu_game.run(self.locations_game)
            elif self.locations_game.demon_3_moon_start:
                self.mini_game_2_n.run_start(self.locations_game, self.text_g)
            elif self.locations_game.demon_3_moon:
                self.mini_game_2_n.run(self.locations_game)
            elif self.locations_game.demon_3_moon_end:
                self.mini_game_2_n.run_end(self.locations_game, self.text_g)
            elif self.locations_game.demon_6_moon_start:
                self.main_mini_1_n.run_start(self.locations_game, self.text_g)
            elif self.locations_game.demon_6_moon:
                self.main_mini_1_n.run(self.stat_game, self.locations_game)
            elif self.locations_game.demon_6_moon_end and not self.locations_game.demon_6_moon:
                self.main_mini_1_n.run_end(self.locations_game, self.text_g)
            else:
                self.mini_clicker_b.run(self.locations_game, self.demon_6_moon_start_game)
