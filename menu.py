import pygame
import sys

class mini_surface():
    '''Поверхности, используемые для создания анимации на заднем фоне'''
    def __init__(self):
        self.type = None
        self.x = None
        self.y = None
        self.img = None
        self.img_rect = None
        self.any_surface = None

class menu():
    '''Локация заставки перед основной игрой'''
    def __init__(self, screen, globals):
        self.hero = pygame.image.load("Img/menu/hero.png")
        self.hero_rect = self.hero.get_rect()
        self.hero_rect.y = globals.HERO_XY_MENU[1]
        self.hero_rect.x = globals.HERO_XY_MENU[0]

        self.tap_to_play = pygame.image.load("Img/menu/tap_to_play.png")
        self.tap_to_play_rect = self.tap_to_play.get_rect()
        self.tap_to_play_rect.y = globals.TAP_TO_PLAY_XY_MENU[0]
        self.tap_to_play_rect.x = globals.TAP_TO_PLAY_XY_MENU[1]

        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.mini_surf = []
        self.make_big_surface(globals)


    def make_big_surface(self, globals):
        '''Создание больших поверхностей, движущихся вниз'''
        for j in range(globals.MAX_BIG_SURF):
            mini_surf_one = mini_surface()
            mini_surf_one.type = pygame.Surface((globals.WIDTH, globals.BIG_SURF_H))
            mini_surf_one.type.fill(globals.B_COLOR_NEW_SURF)
            mini_surf_one.x = 0
            mini_surf_one.y = 0 + j*globals.BIG_SURF_H
            mini_surf_one.any_surface = []
            mini_surf_one.type.set_alpha(globals.ALPHA)
            for i in range(globals.MAX_SMALL_SURF):
                self.make_small_surface(i, j, mini_surf_one, globals)
            self.mini_surf.append(mini_surf_one)


    def make_small_surface(self, i, j, mini_surf_one, globals):
        '''Создание маленьких поверхностей, движущихся вправо'''
        any_surf_one = mini_surface()
        any_surf_one.type = pygame.Surface((globals.SURF_SMALL_SIZE, globals.SURF_SMALL_SIZE))
        any_surf_one.type.fill(globals.B_COLOR_NEW_SURF)
        if (i * globals.SURF_SMALL_SIZE_W + j * (globals.SURF_SMALL_SIZE_W - globals.SURF_SMALL_SIZE)) < globals.WIDTH:
            any_surf_one.x = -globals.SURF_SMALL_SIZE + i * globals.SURF_SMALL_SIZE_W + j * (globals.SURF_SMALL_SIZE_W - globals.SURF_SMALL_SIZE)
        else:
            any_surf_one.x = (globals.SURF_SMALL_SIZE - i) * (-globals.SURF_SMALL_SIZE) + j * (globals.SURF_SMALL_SIZE_W - globals.SURF_SMALL_SIZE)
        any_surf_one.y = 2
        if (i % 2) == 0:
            any_surf_one.img = pygame.image.load("Img/menu/earring.png")
        else:
            any_surf_one.img = pygame.image.load("Img/menu/mask.png")
        any_surf_one.type.set_alpha(globals.ALPHA)
        any_surf_one.img_rect = any_surf_one.img.get_rect()
        mini_surf_one.any_surface.append(any_surf_one)

    def anim(self, globals):
        '''Анимация заставки и вывод главной картинки и текста'''
        self.screen.fill(globals.B_COLOR_NEW_SURF)
        for i in range(len(self.mini_surf)):
            for j in range(len(self.mini_surf[0].any_surface)):
                self.mini_surf[i].any_surface[j].type.blit(self.mini_surf[i].any_surface[j].img, self.mini_surf[i].any_surface[j].img_rect)
                self.mini_surf[i].type.blit(self.mini_surf[i].any_surface[j].type, (self.mini_surf[i].any_surface[j].x, self.mini_surf[i].any_surface[j].y))
                if self.mini_surf[i].any_surface[j].x < globals.WIDTH:
                    self.mini_surf[i].any_surface[j].x += 1
                else:
                    self.mini_surf[i].any_surface[j].x = (self.mini_surf[i].any_surface[(j - globals.MAX_SMALL_SURF + 1) % globals.MAX_SMALL_SURF].x -globals.SURF_SMALL_SIZE_W)
            if self.mini_surf[i].y < globals.SURF_BIG_MAX_Y:
                self.mini_surf[i].y += 1
            else:
                self.mini_surf[i].y = -globals.BIG_SURF_H
            self.screen.blit(self.mini_surf[i].type, (self.mini_surf[i].x, self.mini_surf[i].y))
        self.screen.blit(self.hero, self.hero_rect)
        self.screen.blit(self.tap_to_play, self.tap_to_play_rect)
        pygame.display.update()

    def control(self, locations_game):
        '''Контроль действий игрока во время заставки'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                locations_game.menu = False

    def run(self, locations_game, globals):
        '''Запуск заставки'''
        self.control(locations_game)
        self.anim(globals)

