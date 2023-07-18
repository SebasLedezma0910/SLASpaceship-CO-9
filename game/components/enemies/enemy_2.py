import random
import pygame
from pygame.sprite import Sprite

from game.utils.constants import ENEMY_2, ENEMY_TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

DOWN = "down"
UP = "up"

class Enemy_2(Sprite):
    X_POS = 20
    Y_POS_LIST = [y_pos for y_pos in range(70, SCREEN_HEIGHT, 70)]
    SPEED_X = 2
    SPEED_Y = 6

    def __init__(self):
        self.type = ENEMY_TYPE
        self.image = pygame.transform.scale(ENEMY_2, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = random.choice(self.Y_POS_LIST)

        self.speed_x = self.SPEED_X
        self.speed_y = self.SPEED_Y
        self.movement = random.choice([DOWN, UP])
        self.move_y = random.randint(50, 100)
        self.moving_index = 0

        self.shooting_time = random.randint(10, 30)

    def update(self, enemies_2, bullet_manager):
        self.shoot2(bullet_manager)
        self.rect.x += self.SPEED_X
        if self.movement == UP:
            self.rect.y += self.speed_y
        else:
            self.rect.y -= self.speed_y

        self.update_movement()
        if self.rect.x >= SCREEN_WIDTH:
            enemies_2.remove(self)
    
    def update_movement(self):
        self.moving_index += 1
        if self.rect.top >= SCREEN_HEIGHT // 2:
            self.movement = DOWN
        elif self.rect.y <= 0:
            self.movement = UP
        
        if self.moving_index >= self.move_y:
            self.moving_index = 0
            self.movement = DOWN if self.movement == UP else UP

    def shoot2(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet_manager.add_bullet(self)
            self.shooting_time += random.randint(30, 70)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))