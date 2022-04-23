from Mini_game_1.lab import lab
from Mini_game_1.in_lab import in_lab
from Mini_game_1.control import Demon_n
from Mini_game_1.meetings import meeting
from Mini_game_1.make_many_point import make_many
from Mini_game_1.draw import draw
from Mini_game_1.Hero_m_1 import Hero
from Demon import Demon_6_moon
from pygame.sprite import Group

class main_mini_game_1():
    def __init__(self, screen):
        self.screen = screen
        self.lab_game = lab(screen)
        self.in_lab_game = in_lab()
        self.wall_mass = self.lab_game.return_wall()
        self.hero_mini = Hero(screen, "Img/Demon_6_moon/Mini_t.png")
        self.hero_mini.rect.x = 180 + 21 * 18 + 2
        self.hero_mini.rect.y = 21 * 17 + 4
        self.demon_6_moon = Demon_6_moon(screen)
        self.meeting_game = meeting()
        self.make_many_game = make_many(screen)
        self.hero_game = Hero(screen, "Img/Hero/Hero0.png")

        self.points = Group()
        self.make_many_game.point(self.wall_mass, self.points)

        self.control_game = Demon_n()
        self.lab_game = lab(screen)
        self.draw = draw(screen)

    def run(self, stat_game, locations_game):
        self.control_game.demon_6_moon(self.in_lab_game, self.hero_mini, self.wall_mass, self.lab_game, self.demon_6_moon, self.meeting_game, self.points,
                                  self.hero_game, self.screen, self.make_many_game)
        self.hero_mini.update()
        self.in_lab_game.corner_demon(self.demon_6_moon, self.wall_mass)
        self.meeting_game.eat_points(self.hero_mini, self.points, stat_game, locations_game)
        self.meeting_game.with_demon(self.demon_6_moon, self.points, self.hero_mini, self.screen, self.wall_mass, self.make_many_game, stat_game)
        self.demon_6_moon.update()
        self.draw.all(self.lab_game, self.points, self.hero_mini, self.demon_6_moon)