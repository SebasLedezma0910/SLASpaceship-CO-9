import pygame
from pygame.sprite import  Sprite

from game.utils.constants import BULLET, SPACESHIP

class Player_Bullet(Sprite):
    SPEED = 100

    def __init__(self, spaceship):
        self.owner = spaceship.type
        self.image = pygame.transform.scale(BULLET, (10, 30))
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center

    def update(self, player_bullets):
        if self.owner == SPACESHIP:
            self.rect.y -= self.SPEED
            if self.rect.y <= 0:
                player_bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)