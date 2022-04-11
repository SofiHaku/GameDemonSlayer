import pygame
from settings import *
from event import Event
from Hero import Hero
def run():

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    control_game = Event()
    hero_game = Hero(screen)

    while True:
        screen.fill(B_COLOR)
        hero_game.draw()
        pygame.display.flip()

        control_game.control(screen)


run()

