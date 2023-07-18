import pygame
from pygame.sprite import  Sprite

from game.utils.constants import BULLET, SCREEN_HEIGHT, SPACESHIP

class Player_Bullet(Sprite):
    SPEED = 40

    def __init__(self, spaceship):
        self.owner = spaceship.type
        self.image = pygame.transform.scale(BULLET[self.owner], (10, 30))
        self.rect = self.image.get_rect()
        self.rect.center = spaceship.rect.center

    def update(self, player_bullets):
        if self.owner == SPACESHIP:
            self.rect.y -= self.SPEED
            if self.rect.y >= SCREEN_HEIGHT:
                player_bullets.remove(self)

    def draw(self, screen):
        screen.blit(self.image, self.rect)