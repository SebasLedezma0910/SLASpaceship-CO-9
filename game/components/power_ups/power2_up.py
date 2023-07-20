import random
from pygame.sprite import Sprite

from game.utils.constants import SCREEN_HEIGHT, SCREEN_WIDTH

class PowerUp2(Sprite):
    def __init__(self, image, type2, spaceship_image2):
        self.type = type2
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, SCREEN_WIDTH - 100)
        self.rect.y = 0
        self.spaceship_image2 = spaceship_image2

    def update(self, game_speed, power_ups):
        self.rect.y += game_speed
        if self.rect.y >= SCREEN_HEIGHT: 
            power_ups.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)