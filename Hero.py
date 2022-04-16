import pygame

class Hero():

    def __init__(self, screen, name_img):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load(name_img)
        self.rect = self.image.get_rect()
        self.rect.y = 185
        self.rect.right = 550

        self.image_m = pygame.image.load("Img/Hero/Mini_t.png")
        self.rect_m = self.image_m.get_rect()
        self.rect_m.x = 180 + 21 * 18 + 1
        self.rect_m.y = 21 * 17 + 1


        self.speed = 1

        self.can_move_to_left = True
        self.can_move_to_right = True
        self.can_move_to_up = True
        self.can_move_to_down = True

        self.move_to_left = False
        self.move_to_right = False
        self.move_to_up = False
        self.move_to_down = False

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def draw_mini(self):
        self.screen.blit(self.image_m, self.rect_m)

    def update(self):
        if self.move_to_up and self.can_move_to_up:
            self.rect_m.centery -= self.speed
        elif self.move_to_down and self.can_move_to_down:
            self.rect_m.centery += self.speed
        elif self.move_to_left and self.can_move_to_left:
            self.rect_m.centerx -= self.speed
        elif self.move_to_right and self.can_move_to_right:
            self.rect_m.centerx += self.speed

