import pygame
import sys

class mini_surface():
    def __init__(self):
        self.type = None
        self.x = None
        self.y = None
        self.img = None
        self.img_rect = None
        self.any_surface = None

class menu():
    def __init__(self, screen):
        self.hero = pygame.image.load("Img/menu/hero.png")
        self.hero_rect = self.hero.get_rect()
        self.hero_rect.y = 90
        self.hero_rect.x = 50

        self.tap_to_play = pygame.image.load("Img/menu/tap_to_play.png")
        self.tap_to_play_rect = self.tap_to_play.get_rect()
        self.tap_to_play_rect.y = 180
        self.tap_to_play_rect.x = 270

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.mini_surf = []
        for j in range(15):
            mini_surf_one = mini_surface()
            mini_surf_one.type = pygame.Surface((600, 29))
            mini_surf_one.type.fill((255, 255, 255))
            mini_surf_one.x = 0
            mini_surf_one.y = 0 + j*29
            mini_surf_one.any_surface = []
            mini_surf_one.type.set_alpha(120)
            for i in range(24):
                any_surf_one = mini_surface()
                any_surf_one.type = pygame.Surface((25, 25))
                any_surf_one.type.fill((255, 255, 255))
                if i * 30 + j*5 < 600:
                    any_surf_one.x = -25 + i * 30 + j*5
                else:
                    any_surf_one.x = (25 - i) * (-25) + j*5
                any_surf_one.y = 2
                if (i % 2) == 0:
                    any_surf_one.img = pygame.image.load("Img/menu/earring.png")
                else:
                    any_surf_one.img = pygame.image.load("Img/menu/mask.png")
                any_surf_one.type.set_alpha(120)
                any_surf_one.img_rect = any_surf_one.img.get_rect()
                mini_surf_one.any_surface.append(any_surf_one)
            self.mini_surf.append(mini_surf_one)

    def anim(self):
        self.screen.fill((255, 255, 255))
        for i in range(len(self.mini_surf)):
            for j in range(len(self.mini_surf[0].any_surface)):
                self.mini_surf[i].any_surface[j].type.blit(self.mini_surf[i].any_surface[j].img, self.mini_surf[i].any_surface[j].img_rect)
                self.mini_surf[i].type.blit(self.mini_surf[i].any_surface[j].type, (self.mini_surf[i].any_surface[j].x, self.mini_surf[i].any_surface[j].y))
                if self.mini_surf[i].any_surface[j].x < 600:
                    self.mini_surf[i].any_surface[j].x += 1
                else:
                    self.mini_surf[i].any_surface[j].x = (self.mini_surf[i].any_surface[(j - 23) % 24].x -25)
            if self.mini_surf[i].y < 406:
                self.mini_surf[i].y += 1
            else:
                self.mini_surf[i].y = -29

            self.screen.blit(self.mini_surf[i].type, (self.mini_surf[i].x, self.mini_surf[i].y))

        self.screen.blit(self.hero, self.hero_rect)
        self.screen.blit(self.tap_to_play, self.tap_to_play_rect)

        pygame.display.update()

    def control(self, locations_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                locations_game.menu = False

    def run(self, locations_game):
        self.control(locations_game)
        self.anim()

