import pygame
import sys

class demon_3_moon_start():
    '''Заставка перед 2 мини-игрой'''
    def __init__(self, screen, globals):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.general_image = pygame.image.load("assets/Demon_6_moon/Daki.png")
        self.general_image_rect = self.general_image.get_rect()
        self.general_image_rect.x = globals.IMG_START_2_MG
        self.general_image_rect.y = globals.IMG_START_2_MG
        self.text_out_s_1 = [1, 0, 0]
        self.text_out_s_2 = False

    def draw(self, text_g, globals):
        '''Вывод текста и изображения заставки на экран'''
        self.screen.fill(globals.COLOR_BACK_TEXT)
        self.screen.blit(self.general_image, self.general_image_rect)

        if self.text_out_s_1[0] and self.text_out_s_1[1] and self.text_out_s_1[2] and self.text_out_s_2:
            text_g.draw_many_lines(globals.TEXT_LINES_T8_XY[0], globals.TEXT_LINES_T8_XY[1], text_g.mess_start_3_demon[3], globals.TEXT_SIZE, globals)
        else:
            for i in range(len(self.text_out_s_1)):
                if self.text_out_s_1[i]:
                    text_g.draw_many_lines(globals.TEXT_LINES_T8_XY[0], globals.TEXT_LINES_T6_X_DIFF[0] + i * globals.TEXT_LINES_T6_X_DIFF[1] ,
                                           text_g.mess_start_3_demon[i], globals.TEXT_SIZE, globals)
        pygame.display.flip()

    def control(self, locations_game):
        '''Контроль событий с клавиатуры во время заставки'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.text_out_s_2:
                        locations_game.demon_3_moon_start = False
                        locations_game.demon_3_moon = True
                        self.text_out_use = True
                        pygame.mixer.music.load("music/background_demon.mp3")
                        pygame.mixer.music.play(-1)
                    else:
                        self.text_out_s_2 = True
                        for i in range(len(self.text_out_s_1)):
                            if self.text_out_s_1[i] == 0:
                                self.text_out_s_1[i] = 1
                                self.text_out_s_2 = False
                                break

class demon_3_moon_end():
    '''Локация после 2 мини-игрой'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.image_cup = pygame.image.load("assets/Achievements/big_cup.png")
        self.image_cup_rect = self.image_cup.get_rect()
        self.image_cup_rect.centerx = self.screen_rect.centerx

    def draw(self, text_g, globals):
        '''Вывод текста и изображения концовки после 2 мини-игры на экран'''
        self.screen.fill(globals.COLOR_BACK_TEXT)
        self.screen.blit(self.image_cup, self.image_cup_rect)
        text_g.draw_many_lines(globals.TEXT_LINES_T7_XY[0], globals.TEXT_LINES_T7_XY[1], text_g.win, globals.TEXT_SIZE_4, globals)
        pygame.display.flip()

    def control(self, locations_game):
        '''Контроль событий с клавиатуры во время концовки'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    locations_game.demon_3_moon_end = False
                    pygame.mixer.music.load("music/background.mp3")
                    pygame.mixer.music.play(-1)
