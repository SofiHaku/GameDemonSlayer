from Mini_game_1.points import Point
class make_many():
    def __init__(self, screen):
        self.screen = screen

    def point(self, wall_mass, points):
        for i in range(len(wall_mass)):
            for j in range(len( wall_mass[i])):
                if   wall_mass[i][j] != 1 and not (
                        (i == 5 or i == 15) and (j == 3 or j == 13) or (i == 7 or i == 13) and (j == 7 or j == 11)):
                    point_game = Point(self.screen)
                    point_game.rect.x = 180 + i * 20
                    point_game.rect.y = j * 19
                    points.add(point_game)
