import pygame

class illumination():
    '''Класс, отвечающий за подстветку кнопок'''
    def __init__(self, screen, globals):
        self.hero = [0, 0, 0]
        self.hero_standart = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
        self.skills = [0, 0, 0, 0, 0, 0, 0, 0]
        self.skills_standart = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0]]
        self.exc = 0
        self.lamp = 0
        self.to_shop = 0
        self.to_achiv = 0
        self.screen = screen
        self.globals = globals

        self.demon = [0, 0, 0]
        self.demon_standart = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [0, 0, 0]]
        self.count_demon = [0, 0, 0, 0, 0]
        self.count_demon_standart = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                                     [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]

        self.forse = [0, 0, 0, 0, 0]
        self.forse_standart = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0],
                                     [0, 0, 0, 1, 0], [0, 0, 0, 0, 1], [0, 0, 0, 0, 0]]

    def button(self, x, y, wight, height):
        '''Подстветка передаваемой кнопки'''
        surf = pygame.Surface((wight, height))
        pygame.draw.rect(surf, self.globals.B_COLOR_NEW_SURF, (0, 0, wight, height))
        surf.set_alpha(self.globals.GLOW_F)
        self.screen.blit(surf, (x, y))