class in_lab():
    """Определяет положенеи персонажей в лабиринте"""
    def __init__(self):
        pass

    def corner_hero(self, name, wall, globals):
        """Определяет положенеи игрока: возможность двигаться в различные стороны"""
        name.can_move_to_left = True
        name.can_move_to_right = True
        name.can_move_to_up = True
        name.can_move_to_down = True

        if wall[(name.rect.left - globals.WALL_X_LEFT) // globals.MAX_WALL + 1][name.rect.centery // globals.MAX_WALL_H] == 1:
            name.can_move_to_right = False
        if wall[(name.rect.right - globals.WALL_X_LEFT) // globals.MAX_WALL - 1][name.rect.centery // globals.MAX_WALL_H] == 1:
            name.can_move_to_left = False
        if wall[(name.rect.centerx - globals.WALL_X_LEFT) // globals.MAX_WALL][name.rect.top // globals.MAX_WALL_H + 1] == 1:
            name.can_move_to_down = False
        if wall[(name.rect.centerx - globals.WALL_X_LEFT) // globals.MAX_WALL][name.rect.bottom // globals.MAX_WALL_H - 1] == 1:
            name.can_move_to_up = False

    def corner_demon(self, name, wall, globals):
        """Определяет положение демона: возможность двигаться в различные стороны"""
        name.type_corner = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        name.can_move = [1, 1, 1, 1]
        if wall[(name.rect.left - globals.WALL_X_LEFT) // globals.MAX_WALL + 1][name.rect.centery // globals.MAX_WALL_H] == 1:
            name.can_move[1] = 0
            name.move[1] = 0
        if wall[(name.rect.right - globals.WALL_X_LEFT) // globals.MAX_WALL - 1][name.rect.centery // globals.MAX_WALL_H] == 1:
            name.can_move[0] = 0
            name.move[0] = 0
        if wall[(name.rect.centerx - globals.WALL_X_LEFT) // globals.MAX_WALL][name.rect.top // globals.MAX_WALL_H + 1] == 1:
            name.can_move[3] = 0
            name.move[3] = 0
        if wall[(name.rect.centerx - globals.WALL_X_LEFT) // globals.MAX_WALL][name.rect.bottom // globals.MAX_WALL_H - 1] == 1:
            name.can_move[2] = 0
            name.move[2] = 0
        if name.rect.centerx // globals.WALL_CENTER_DEL == name.rect.centerx / globals.WALL_CENTER_DEL and \
                name.rect.centerx // (globals.WALL_CENTER_DEL*2) != name.rect.centerx / (globals.WALL_CENTER_DEL*2) and \
                name.rect.centery // globals.WALL_CENTER_DEL == name.rect.centery / globals.WALL_CENTER_DEL \
                and name.rect.centery // (globals.WALL_CENTER_DEL*2) != name.rect.centery / (globals.WALL_CENTER_DEL*2):
            name.in_center = 1
        else:
            name.in_center = 0


