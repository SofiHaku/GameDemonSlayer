from src.globals import Globals
from src.Mini_game_2.belts import many_belts
from src.Mini_game_2.draw import draw
from src.Mini_game_2.events import control
from src.Mini_game_2.hero import hero
from src.Mini_game_2.start_and_end import demon_3_moon_start, demon_3_moon_end

class main_mini_game_2():
    '''Класс, полностью контролирующий 2 мини-игру'''
    def __init__(self, screen):
        self.globals = Globals()
        self.hero = hero(screen, self.globals)
        self.control = control()
        self.draw = draw(screen)
        self.belt = many_belts(screen)
        self.start = demon_3_moon_start(screen, self.globals)
        self.end = demon_3_moon_end(screen)

    def run(self, locations_game):
        '''Запуск непосредственно самой мини-игры'''
        if not self.control.play_now:
            self.control.start_events()
            self.draw.all(self.hero, self.belt)
            self.draw.draw()
            self.draw.flip()
        else:
            self.control.events(self.hero, self.belt, self.globals)
            self.control.check_collision(self.hero, self.belt, self.draw)
            self.hero.update()
            self.draw.all(self.hero, self.belt)
            self.draw.flip()
            self.belt.move_belts()
            self.belt.draw_belts()
            self.belt.remove_belts(self.hero)
            self.draw.anim()
            if self.hero.count_belt >= self.globals.MAX_BELT:
                locations_game.demon_3_moon, locations_game.use_demon_3_moon = False, True
                with open('save_data/use_demon', 'w') as file:
                    file.write("11")

    def run_start(self, locations_game, text_g):
        '''Запуск заставки'''
        self.start.draw(text_g, self.globals)
        self.start.control(locations_game)

    def run_end(self, locations_game, text_g):
        '''Запуск концовки'''
        self.end.draw(text_g, self.globals)
        self.end.control(locations_game)

