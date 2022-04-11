import pygame
import sys

from settings import *

class Event():

    def __init__(self):
        pass

    def control(self, screen):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
