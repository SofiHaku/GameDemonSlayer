import pygame
import sys

class demon_6_moon_start():
    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = self.screen.get_rect()

        self.general_image = pygame.image.load("Img/Demon_6_moon/Tangiro.png")
        self.general_image_rect = self.general_image.get_rect()
        self.general_image_rect.x = 360
        self.text_out_s_1 = [1, 0, 0]
        self.text_out_s_2 = False
        with open('Save_data/use_start_6_demon.txt', 'r') as file:
            self.text_out_use = int(file.read())

    def draw(self, text_g):

        self.screen.fill((255, 255, 255))
        self.screen.blit(self.general_image,self.general_image_rect)

        if self.text_out_s_1[0] and self.text_out_s_1[1] and self.text_out_s_1[2] and self.text_out_s_2:
            text_g.draw_many_lines(30, 150, text_g.mess_start_6_demon[3], 20)
        else:
            for i in range(len(self.text_out_s_1)):
                if self.text_out_s_1[i]:
                    text_g.draw_many_lines(30, 30 + i * 90, text_g.mess_start_6_demon[i], 20)

    def control(self, locations_game):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.text_out_s_2:
                        locations_game.demon_6_moon_start = False
                        locations_game.demon_6_moon = True
                        self.text_out_use = True
                        with open('Save_data/use_start_6_demon.txt', 'w') as file:
                            file.write("".join("1"))
                    else:
                        self.text_out_s_2 = True
                        for i in range(len(self.text_out_s_1)):
                            if self.text_out_s_1[i] == 0:
                                self.text_out_s_1[i] = 1
                                self.text_out_s_2 = False
                                break
    def use(self):
        return self.text_out_use


