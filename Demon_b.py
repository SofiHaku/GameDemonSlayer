class Demon():

    def __init__(self, screen):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.name = None
        self.count_life = None

        self.image = None
        self.rect = None
        self.wight = None
        self.height = None


    def draw(self):
        self.screen.blit(self.image, self.rect)