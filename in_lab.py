class in_lab():
    """Определяет положенеи персонажей в лабиринте"""
    def __init__(self):
        pass

    def corner_hero(self, name, wall):
        """Определяет положенеи игрока: возможность двигаться в различные стороны"""
        name.can_move_to_left = True
        name.can_move_to_right = True
        name.can_move_to_up = True
        name.can_move_to_down = True

        if wall[(name.rect.left - 180) // 20 + 1][name.rect.centery // 19] == 1:
            name.can_move_to_right = False
        if wall[(name.rect.right - 180) // 20 - 1][name.rect.centery // 19] == 1:
            name.can_move_to_left = False
        if wall[(name.rect.centerx - 180) // 20][name.rect.top // 19 + 1] == 1:
            name.can_move_to_down = False
        if wall[(name.rect.centerx - 180) // 20][name.rect.bottom // 19 - 1] == 1:
            name.can_move_to_up = False

    def corner_demon(self, name, wall):
        """Определяет положенеи привидения: возможность двигаться в различные стороны"""
        name.type_corner = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        name.can_move = [1, 1, 1, 1]

        '''self.mass_l = [1, 0, 0, 0]
           self.mass_r = [0, 1, 0, 0]
           self.mass_u = [0, 0, 1, 0]
           self.mass_d = [0, 0, 0, 1]'''

        if wall[name.rect.left // 30 + 1][name.rect.centery // 30] == 1:
            name.can_move[1] = 0
            name.move[1] = 0
        if wall[name.rect.right // 30 - 1][name.rect.centery // 30] == 1:
            name.can_move[0] = 0
            name.move[0] = 0
        if wall[name.rect.centerx // 30][name.rect.top // 30 + 1] == 1:
            name.can_move[3] = 0
            name.move[3] = 0
        if wall[name.rect.centerx // 30][name.rect.bottom // 30 - 1] == 1:
            name.can_move[2] = 0
            name.move[2] = 0

        if name.rect.centerx // 15 == name.rect.centerx / 15 and name.rect.centerx // 30 != name.rect.centerx / 30 and name.rect.centery // 15 == name.rect.centery / 15 and name.rect.centery // 30 != name.rect.centery / 30:
            name.in_center = 1
        else:
            name.in_center = 0


