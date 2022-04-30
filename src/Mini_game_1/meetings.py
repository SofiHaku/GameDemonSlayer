import pygame

class meeting():
    '''События при встрече различных объектов'''
    def __init__(self):
        pass

    def eat_points(self, hero_game, points, stat_game, locations_game, globals):
        '''Встреча героя с алмазиками'''
        if pygame.sprite.spritecollide(hero_game, points, True):
            stat_game.point_in_mini_game += 1
            if stat_game.point_in_mini_game == globals.MAX_ALM:  #189
                locations_game.demon_6_moon = False
                locations_game.first_list = True
                locations_game.use_demon_6_moon = True
                with open('save_data/use_demon', 'w') as file:
                    file.write("10")

    def with_demon(self, demon_6_moon, points, hero_mini, screen, wall_mass, make_many_object_game, stat_game, globals):
        '''Встреча героя с демонами'''
        if pygame.Rect.colliderect(hero_mini.rect, demon_6_moon.rect):
            make_many_object_game.point(wall_mass, points)
            points.draw(screen)
            hero_mini.rect.x = globals.HERO_RECT[0]
            hero_mini.rect.y = globals.HERO_RECT[1]
            stat_game.point_in_mini_game = 0
            for point in points:
                point.draw()

