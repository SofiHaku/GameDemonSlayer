import pygame
from settings import *
from event import Event
from Hero import Hero
from statistics import Stat
from Shop import Shop
from draw import Draw
from Demon import Demon_ordinary, Demon_6_moon
from lab import lab
from locations import now_locations
from in_lab import in_lab

def run():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    control_game = Event()
    hero_game = Hero(screen, "Img/Hero/Tang.png")
    stat_game = Stat(screen)
    shop_game = Shop(screen)
    draw_game = Draw(screen)
    demon_classic = Demon_ordinary(screen)
    lab_game = lab(screen)
    locations_game = now_locations()
    in_lab_game = in_lab()
    wall = lab_game.return_wall()
    demon_6_moon = Demon_6_moon(screen)

    while True:
        control_game.control_achiv(stat_game, shop_game, locations_game)
        if locations_game.shop:
            control_game.in_shop(shop_game, stat_game, locations_game)
        if locations_game.demon_6_moon:
            control_game.demon_6_moon(in_lab_game, hero_game, wall, lab_game, demon_6_moon)
            in_lab_game.corner_demon(demon_6_moon, wall)
            demon_6_moon.update()
        else:
            control_game.control(stat_game, shop_game, hero_game, demon_classic, locations_game)
        hero_game.update()
        draw_game.all(shop_game, hero_game, stat_game, demon_classic, lab_game, locations_game, demon_6_moon)
        demon_classic.move()
        clock.tick(60)
run()

