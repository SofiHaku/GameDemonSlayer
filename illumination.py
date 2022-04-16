import pygame

class illumination():
    def __init__(self, screen):
        self.hero = [0, 0, 0]
        self.hero_standart = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.skills = [0, 0, 0, 0, 0, 0, 0, 0]
        self.skills_standart = [[1, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 0, 0, 1]]
        self.exc = 0
        self.to_shop = 0
        self.screen = screen

    def button(self, x, y, wight, height):
        surf = pygame.Surface((wight, height))
        pygame.draw.rect(surf, (255, 255, 0), (0, 0, wight, height))
        surf.set_alpha(50)
        self.screen.blit(surf, (x, y))