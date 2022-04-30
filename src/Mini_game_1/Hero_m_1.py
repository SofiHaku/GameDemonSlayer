import pygame

class Hero():
    '''Главный герой во время 1 мини-игры'''
    def __init__(self, screen, globals):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load("assets/Demon_6_moon/Mini_t.png")
        self.rect = self.image.get_rect()
        self.rect.x = globals.HERO_RECT[0]
        self.rect.y = globals.HERO_RECT[1]

        self.speed = 2

        self.can_move_to_left = True
        self.can_move_to_right = True
        self.can_move_to_up = True
        self.can_move_to_down = True

        self.move_to_left = False
        self.move_to_right = False
        self.move_to_up = False
        self.move_to_down = False

    def draw(self):
        '''Вывод игрока на экран'''
        self.screen.blit(self.image, self.rect)

    def update(self):
        '''Обновление положения игрока'''
        if self.move_to_up and self.can_move_to_up:
            self.rect.centery -= self.speed
        elif self.move_to_down and self.can_move_to_down:
            self.rect.centery += self.speed
        elif self.move_to_left and self.can_move_to_left:
            self.rect.centerx -= self.speed
        elif self.move_to_right and self.can_move_to_right:
            self.rect.centerx += self.speed

