import pygame

class lab():
    """Создание стен лабиринта"""
    def __init__(self, screen):
        self.bool = False
        self.screen = screen
        self.all_lab = []
        self.image_drum = pygame.image.load("Img/Demon_6_moon/drum.png")
        self.rect_drum = self.image_drum.get_rect()
        #Основной массив
        #Элемент массива '1' - стены
        #Остались последствия старой реализации (будет убрано). Описано ниже
        #'2' - возможно движение влево-вправо, '0' - вверх-вниз, '3','4','5' - тип угла
        self.wall =    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
               [1, 3, 0, 4, 0, 3, 1, 1, 1, 2, 1, 1, 1, 2, 0, 3, 1, 3, 0, 3, 1],
               [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 3, 0, 4, 1, 2, 1],
               [1, 3, 0, 4, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1],
               [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 3, 4, 4, 1, 2, 1],
               [1, 3, 0, 5, 0, 4, 0, 0, 0, 5, 0, 0, 0, 5, 0, 5, 4, 3, 1, 2, 1],
               [1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1],
               [1, 2, 1, 4, 0, 3, 1, 3, 0, 4, 0, 4, 0, 4, 1, 4, 0, 3, 1, 2, 1],
               [1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
               [1, 3, 0, 4, 1, 3, 0, 4, 1, 1, 1, 2, 1, 3, 0, 4, 1, 0, 0, 4, 1],
               [1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1],
               [1, 3, 0, 4, 1, 3, 0, 4, 1, 1, 1, 2, 1, 3, 0, 4, 1, 3, 0, 4, 1],
               [1, 2, 1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1],
               [1, 2, 1, 4, 0, 3, 1, 3, 0, 4, 0, 4, 0, 4, 1, 4, 0, 3, 1, 2, 1],
               [1, 2, 1, 2, 1, 1, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1],
               [1, 4, 0, 5, 0, 4, 0, 0, 0, 5, 0, 0, 0, 5, 0, 5, 4, 3, 1, 2, 1],
               [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 3, 4, 2, 1, 2, 1],
               [1, 4, 0, 4, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 2, 1],
               [1, 2, 1, 2, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2, 1, 3, 0, 4, 1, 2, 1],
               [1, 3, 0, 4, 0, 3, 1, 1, 1, 2, 1, 1, 1, 3, 0, 0, 1, 3, 0, 3, 1],
               [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]


    def return_wall(self):
        """Передаем массив для использования в других функциях"""
        return self.wall

    def walls_draw(self, globals):
        """Рисуем стены"""
        for i in range(len(self.wall)):
            for j in range(len(self.wall[i])):
                if self.wall[i][j] == 1:
                    one_path_of_lab = pygame.Rect((globals.WALL_X_LEFT + i * globals.MAX_WALL, j * globals.MAX_WALL_H, globals.MAX_WALL, globals.MAX_WALL_H))
                    pygame.draw.rect(self.screen, globals.BACK_C, one_path_of_lab)

                elif (i == globals.IDEX_SPEC[0][0] or i == globals.IDEX_SPEC[0][1]) and (j == globals.IDEX_SPEC[1][0] or j == globals.IDEX_SPEC[1][1]) \
                        or (i == globals.IDEX_SPEC[2][0] or i == globals.IDEX_SPEC[2][1]) and (j == globals.IDEX_SPEC[3][0] or j == globals.IDEX_SPEC[3][1]):
                    self.rect_drum.x = globals.WALL_X_LEFT + i * globals.MAX_WALL
                    self.rect_drum.y = j * globals.MAX_WALL_H
                    self.screen.blit(self.image_drum, self.rect_drum)


