import pygame

class meeting():
    def __init__(self):
        pass

    def eat_points(self, hero_game, points, stat_game, locations_game):
        if pygame.sprite.spritecollide(hero_game, points, True):
            stat_game.point_in_mini_game += 1
            if stat_game.point_in_mini_game == 6:  #189
                locations_game.demon_6_moon = False
                locations_game.first_list = True
                locations_game.use_demon_6_moon = True
                with open('Save_data/use_demon', 'w') as file:
                    file.write("10")

    def with_demon(self, demon_6_moon, points, hero_mini, screen, wall_mass, make_many_object_game, stat_game):

        if pygame.Rect.colliderect(hero_mini.rect, demon_6_moon.rect):
            make_many_object_game.point(wall_mass, points)
            points.draw(screen)
            hero_mini.rect.x = 180 + 21 * 18 + 2
            hero_mini.rect.y = 21 * 17 + 4
            stat_game.point_in_mini_game = 0
            for point in points:
                point.draw()

