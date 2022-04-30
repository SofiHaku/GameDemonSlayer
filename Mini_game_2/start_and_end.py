import pygame
import sys

class demon_3_moon_start():
    '''Заставка перед 2 мини-игрой'''
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.general_image = pygame.image.load("Img/Demon_6_moon/Daki.png")
        self.general_image_rect = self.general_image.get_rect()
        self.general_image_rect.x = 50
        self.general_image_rect.y = 50
        self.text_out_s_1 = [1, 0, 0]
        self.text_out_s_2 = False

    def draw(self, text_g):
        '''Вывод текста и изображения заставки на экран'''
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.general_image,self.general_image_rect)

        if self.text_out_s_1[0] and self.text_out_s_1[1] and self.text_out_s_1[2] and self.text_out_s_2:
            text_g.draw_many_lines(280, 150, text_g.mess_start_3_demon[3], 20)
        else:
            for i in range(len(self.text_out_s_1)):
                if self.text_out_s_1[i]:
                    text_g.draw_many_lines(280, 30 + i * 90, text_g.mess_start_3_demon[i], 20)
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
                        pygame.mixer.music.load("Music/фон_битва_с_демонами.mp3")
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
        self.image_cup = pygame.image.load("Img/Achievements/big_cup.png")
        self.image_cup_rect = self.image_cup.get_rect()
        self.image_cup_rect.centerx = self.screen_rect.centerx

    def draw(self, text_g):
        '''Вывод текста и изображения концовки после 2 мини-игры на экран'''
        self.screen.fill((255, 255, 255))
        self.screen.blit(self.image_cup, self.image_cup_rect)
        text_g.draw_many_lines(150, 280, text_g.win, 40)
        pygame.display.flip()

    def control(self, locations_game):
        '''Контроль событий с клавиатуры во время концовки'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    locations_game.demon_3_moon_end = False
                    pygame.mixer.music.load("Music/фон.mp3")
                    pygame.mixer.music.play(-1)
