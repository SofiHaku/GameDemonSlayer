import pygame
from settings import *
from event import Event
from Hero import Hero
from statistics import Stat
from Shop import Shop
from draw import Draw

def run():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    control_game = Event()
    hero_game = Hero(screen)
    stat_game = Stat(screen)
    shop_game = Shop(screen)
    draw_game = Draw(screen)

    while True:
        draw_game.all(shop_game, hero_game, stat_game)
        control_game.control(screen, stat_game, shop_game)


run()

