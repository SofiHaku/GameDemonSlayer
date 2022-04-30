import pygame
from Globals import Globals

class draw():
    '''Класс, отвечающий за вывод всех изображений во время 2 мини-игры'''
    def __init__(self, screen):
        self.globals = Globals()
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image_back = pygame.image.load("Img/Mini_game_2/back2.png")
        self.image_back_rect = self.image_back.get_rect()
        self.image_back_rect.x = self.globals.START_X

        self.image_road1 = pygame.image.load("Img/Mini_game_2/road.png")
        self.image_road1_rect = self.image_road1.get_rect()
        self.image_road1_rect.y = self.globals.HEIGHT - self.globals.FRAME_S_M2
        self.image_road1_rect.x = self.globals.START_X

        self.image_road2 = pygame.image.load("Img/Mini_game_2/road.png")
        self.image_road2_rect = self.image_road2.get_rect()
        self.image_road2_rect.y = self.globals.HEIGHT - self.globals.FRAME_S_M2
        self.image_road2_rect.right = self.image_road1_rect.left

        self.image_tap = pygame.image.load("Img/Mini_game_2/tap_to_play.png")
        self.image_tap_rect = self.image_road1.get_rect()
        self.image_tap_rect.y = self.globals.TAP_TO_PLAY_XY[1]
        self.image_tap_rect.x = self.globals.TAP_TO_PLAY_XY[0]

    def anim(self):
        '''Анимация дороги'''
        self.image_road1_rect.left += 1
        self.image_road2_rect.left += 1
        if self.image_road1_rect.left >= self.screen_rect.right - self.globals.START_X:
            self.image_road1_rect.right = self.image_road2_rect.left
        elif self.image_road2_rect.left >= self.screen_rect.right - self.globals.START_X:
            self.image_road2_rect.right = self.image_road1_rect.left

    def all(self, hero, many_belts):
        '''Вывод всех изображений во время 2 мини-игры'''
        self.screen.blit(self.image_back, self.image_back_rect)
        many_belts.draw_belts()
        self.screen.blit(self.image_road1, self.image_road1_rect)
        self.screen.blit(self.image_road2, self.image_road2_rect)

        pygame.draw.rect(self.screen, self.globals.COLOR_BACK_TEXT, (self.screen_rect.x, self.screen_rect.y,
                                                        self.globals.START_X, self.globals.HEIGHT))
        pygame.draw.rect(self.screen, self.globals.COLOR_BACK_TEXT, (self.screen_rect.right - self.globals.START_X,
                                                        self.screen_rect.y,  self.globals.START_X, self.globals.HEIGHT))
        hero.draw()

    def draw(self):
        '''Вывод надписи "нажмите, чтобы играть"'''
        self.screen.blit(self.image_tap, self.image_tap_rect)

    def flip(self):
        '''Переворачивает экран:техническая часть pygame
        Необходима, чтобы не писать дополнительные условия'''
        pygame.display.flip()

