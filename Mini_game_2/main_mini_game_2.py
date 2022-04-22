import pygame
from Mini_game_2.hero import hero
from Mini_game_2.events import control
from Mini_game_2.draw import draw
from Mini_game_2.belts import many_belts

class main_mini_game_2():
    def __init__(self, screen):
        self.hero = hero(screen)
        self.control = control()
        self.draw = draw(screen)
        self.belt = many_belts(screen)

    def run(self, locations_game):
        if not self.control.play_now:
            self.control.start_events()
            self.draw.all(self.hero, self.belt)
        else:
            self.control.events(self.hero, self.belt)
            self.control.check_collision(self.hero, self.belt, self.draw)
            self.hero.update()
            self.draw.all(self.hero, self.belt)
            self.belt.move_belts()
            self.belt.draw_belts()
            self.belt.remove_belts(self.hero)
            self.draw.anim()
            if self.hero.count_belt >= 10:
                locations_game.demon_3_moon = False

