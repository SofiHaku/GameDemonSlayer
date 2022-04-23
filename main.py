import pygame
from settings import *
from Clicker_base.statistics import Stat
from locations import now_locations
from menu import menu
from text_message import text_message
from Mini_game_1.start_and_end_of_6_demon import demon_6_moon_start
from Mini_game_2.main_mini_game_2 import main_mini_game_2
from Mini_game_1.main_mini_game_1 import main_mini_game_1
from Clicker_base.main_clicker_base import main_clicker_base

def run():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    pygame.mixer.music.load("Music/фон.mp3")
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    text_g = text_message(screen)

    stat_game = Stat(screen)
    locations_game = now_locations()

    menu_game = menu(screen)
    demon_6_moon_start_game = demon_6_moon_start(screen)
    mini_game_2_n = main_mini_game_2(screen)
    main_mini_1_n = main_mini_game_1(screen)
    mini_clicker_b = main_clicker_base(screen, stat_game)
    pygame.mixer.music.play(-1, 0, 10)

    while True:
        clock.tick(60)
        if locations_game.menu:
            menu_game.run(locations_game)
        elif locations_game.demon_3_moon_start:
            pygame.mixer.music.pause()
            mini_game_2_n.run_start(locations_game, text_g)
        elif locations_game.demon_3_moon:
            pygame.mixer.music.pause()
            mini_game_2_n.run(locations_game)
        elif locations_game.demon_3_moon_end:
            mini_game_2_n.run_end(locations_game, text_g)
            pygame.mixer.music.unpause()
        elif locations_game.demon_6_moon_start:
            main_mini_1_n.run_start(locations_game, text_g)
        elif locations_game.demon_6_moon:
            main_mini_1_n.run(stat_game, locations_game)
        elif locations_game.demon_6_moon_end and not locations_game.demon_6_moon:
            main_mini_1_n.run_end(locations_game, text_g)
        else:
            mini_clicker_b.run(locations_game, demon_6_moon_start_game)


run()

