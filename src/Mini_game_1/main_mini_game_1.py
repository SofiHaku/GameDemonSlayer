from src.Mini_game_1.lab import lab
from src.Mini_game_1.in_lab import in_lab
from src.Mini_game_1.control import control
from src.Mini_game_1.meetings import meeting
from src.Mini_game_1.make_many_point import make_many
from src.Mini_game_1.draw import draw
from src.Mini_game_1.Hero_m_1 import Hero
from src.Mini_game_1.Demon import Demon_6_moon
from pygame.sprite import Group
from src.Mini_game_1.start_and_end_of_6_demon import demon_6_moon_start, demon_6_moon_end
from src.Globals import Globals

class main_mini_game_1():
    '''Класс, полностью контролирующий 1 мини-игру'''
    def __init__(self, screen):
        self.screen = screen
        self.globals = Globals()
        self.lab_game = lab(screen)
        self.in_lab_game = in_lab()
        self.wall_mass = self.lab_game.return_wall()
        self.hero_mini = Hero(screen, self.globals)
        self.demon_6_moon = Demon_6_moon(screen, self.globals)
        self.meeting_game = meeting()
        self.make_many_game = make_many(screen)
        self.start = demon_6_moon_start(screen, self.globals)
        self.end = demon_6_moon_end(screen)

        self.points = Group()
        self.make_many_game.point(self.wall_mass, self.points, self.globals)

        self.control_game = control()
        self.lab_game = lab(screen)
        self.draw = draw(screen)

    def run(self, stat_game, locations_game):
        '''Запуск непосредственно самой мини-игры'''
        self.control_game.hero(self.in_lab_game, self.hero_mini, self.wall_mass, self.globals)
        self.hero_mini.update()
        self.in_lab_game.corner_demon(self.demon_6_moon, self.wall_mass, self.globals)
        self.meeting_game.eat_points(self.hero_mini, self.points, stat_game, locations_game, self.globals)
        self.meeting_game.with_demon(self.demon_6_moon, self.points, self.hero_mini, self.screen, self.wall_mass, self.make_many_game, stat_game, self.globals)
        self.demon_6_moon.update()
        self.draw.all(self.lab_game, self.points, self.hero_mini, self.demon_6_moon, self.globals)

    def run_start(self, locations_game, text_g):
        '''Запуск заставки'''
        self.start.draw(text_g, self.globals)
        self.start.control(locations_game)

    def run_end(self, locations_game, text_g):
        '''Запуск концовки'''
        self.end.draw(text_g, self.globals)
        self.end.control(locations_game)
