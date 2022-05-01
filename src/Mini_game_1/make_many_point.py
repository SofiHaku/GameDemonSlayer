from src.Mini_game_1.points import Point
class make_many():
    '''Класс создания многих объектов'''
    def __init__(self, screen):
        self.screen = screen

    def point(self, wall_mass, points, globals):
        '''Создание алмазиков во всех пустых ячейках лабиринта'''
        for i in range(len(wall_mass)):
            for j in range(len( wall_mass[i])):
                if  wall_mass[i][j] != 1 and not (
                        (i == globals.IDEX_SPEC[0][0] or i == globals.IDEX_SPEC[0][1]) and
                        (j == globals.IDEX_SPEC[1][0] or j == globals.IDEX_SPEC[1][1]) or
                        (i == globals.IDEX_SPEC[2][0] or i == globals.IDEX_SPEC[2][1]) and
                        (j == globals.IDEX_SPEC[3][0] or j == globals.IDEX_SPEC[3][1])):
                    point_game = Point(self.screen)
                    point_game.rect.x = globals.WALL_X_LEFT + i * globals.MAX_WALL
                    point_game.rect.y = j * globals.MAX_WALL_H
                    points.add(point_game)
