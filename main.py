import pygame
from pygame.sprite import Group
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
from meetings import meeting
from make_many_point import make_many
from illumination import illumination
from achievements import achievements
from menu import menu
from start_and_end_of_6_demon import demon_6_moon_start
from Mini_game_2.main_mini_game_2 import main_mini_game_2

def run():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    control_game = Event()
    hero_game = Hero(screen, "Img/Hero/Hero0.png")
    hero_mini = Hero(screen, "Img/Demon_6_moon/Mini_t.png")

    hero_mini.rect.x = 180 + 21 * 18 + 2
    hero_mini.rect.y = 21 * 17 + 4

    stat_game = Stat(screen)
    shop_game = Shop(screen)
    draw_game = Draw(screen)
    demon_classic = Demon_ordinary(screen)
    lab_game = lab(screen)
    locations_game = now_locations()
    in_lab_game = in_lab()
    wall_mass = lab_game.return_wall()
    demon_6_moon = Demon_6_moon(screen)
    meeting_game = meeting()
    make_many_game = make_many(screen)
    ill_butt = illumination(screen)
    achiv = achievements(screen)
    menu_game = menu(screen)
    demon_6_moon_start_game = demon_6_moon_start(screen)
    mini_game_2_n = main_mini_game_2(screen)

    points = Group()
    make_many_game.point(wall_mass, points)

    while True:
        clock.tick(60)
        control_game.control_achiv(achiv, shop_game, locations_game, demon_6_moon_start_game)
        if locations_game.demon_3_moon:
            mini_game_2_n.run(locations_game)
        elif locations_game.menu:
            control_game.in_menu(locations_game, menu_game)
        elif locations_game.shop:
            control_game.in_shop(shop_game, stat_game, locations_game, ill_butt)
        elif locations_game.demon_6_moon_start:
            demon_6_moon_start_game.control(locations_game)
        elif locations_game.demon_6_moon:
            control_game.demon_6_moon(in_lab_game, hero_mini, wall_mass, lab_game, demon_6_moon, meeting_game, points, hero_game, screen, make_many_game)
            hero_mini.update()
            in_lab_game.corner_demon(demon_6_moon, wall_mass)
            meeting_game.eat_points(hero_mini, points, stat_game, locations_game)
            meeting_game.with_demon(demon_6_moon, points, hero_mini, screen, wall_mass, make_many_game, stat_game)
            demon_6_moon.update()
        elif locations_game.achiv:
            control_game.in_achiv(achiv, stat_game, locations_game, ill_butt)
        else:
            control_game.control(stat_game, shop_game, hero_game, demon_classic, locations_game, ill_butt, achiv)

        draw_game.all(shop_game, hero_game, stat_game, demon_classic, lab_game, locations_game, demon_6_moon, points,
                      hero_mini, ill_butt, achiv, menu_game, demon_6_moon_start_game)
        hero_game.update()
        demon_classic.move()
run()

