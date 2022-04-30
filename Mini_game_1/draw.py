import pygame

class draw():
    '''Класс, отвечающий за вывод всех изображений во время 1 мини-игры'''
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load('Img/Demon_6_moon/Tangiro.png')
        self.image_rect = self.screen.get_rect()

    def all(self, lab_game, points, hero_mini, demon_6_moon, globals):
        '''Вывод всех изображений во время 1 мини-игры'''
        self.screen.fill(globals.B_COLOR_NEW_SURF)
        self.screen.blit(self.image, self.image_rect)
        lab_game.walls_draw(globals)
        for point in points:
            point.draw()
        hero_mini.draw()
        demon_6_moon.draw()
        pygame.display.flip()
