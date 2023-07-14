import pygame
from pygame.sprite import Sprite
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 30 
    Y_POS = 500
    def __init__(self):
        self.image = pygame.transform.scale(SPACESHIP, (60, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS    

    def update(self, user_input):
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        elif user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()
        elif user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()
        elif user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()

    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 10
    
    def move_right(self):
        if self.rect.right < SCREEN_WIDTH:
            self.rect.x += 10

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10
    
    def move_up(self):
        if self.rect.top > SCREEN_HEIGHT // 2:
            self.rect.y -= 10

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))        

