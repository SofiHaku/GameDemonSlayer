import pygame

class draw():
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('Img/Demon_6_moon/Tangiro.png')
        self.image_rect = self.screen.get_rect()

    def all(self, lab_game, points, hero_mini, demon_6_moon):
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.image, self.image_rect)
        lab_game.walls_draw()
        for point in points:
            point.draw()
        hero_mini.draw()
        demon_6_moon.draw()
        pygame.display.flip()
