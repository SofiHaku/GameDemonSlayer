import pygame
from settings import *
from event import Event
from Hero import Hero
from statistics import Stat
from Shop import Shop
from draw import Draw
from Demon import Demon_normal

def run():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    control_game = Event()
    hero_game = Hero(screen)
    stat_game = Stat(screen)
    shop_game = Shop(screen)
    draw_game = Draw(screen)
    demon_classic = Demon_normal(screen)

    while True:
        if not shop_game.draw_back_bool:
            control_game.control(stat_game, shop_game, hero_game, demon_classic)
        else:
            control_game.in_shop(shop_game, stat_game)
        hero_game.update()
        draw_game.all(shop_game, hero_game, stat_game, demon_classic)
        demon_classic.move()
        clock.tick(60)
run()

