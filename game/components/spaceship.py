import random
import pygame
from pygame.sprite import Sprite
from game.utils.constants import DEFAULT_TYPE, FONT_STYLE, SCREEN_WIDTH, SCREEN_HEIGHT, SPACESHIP

class Spaceship(Sprite):
    X_POS = (SCREEN_WIDTH // 2) - 30 
    Y_POS = 500
    def __init__(self):
        self.type = SPACESHIP
        self.image = pygame.transform.scale(SPACESHIP, (60, 50))
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS 
        self.power_up_type = DEFAULT_TYPE
        self.power_up_time_up = 0    

        self.shooting_time = random.randint(30, 50) 

    def update(self, user_input, bullet_manager):
        
        if user_input[pygame.K_LEFT] or user_input[pygame.K_a]:
            self.move_left()
        elif user_input[pygame.K_RIGHT] or user_input[pygame.K_d]:
            self.move_right()
        elif user_input[pygame.K_DOWN] or user_input[pygame.K_s]:
            self.move_down()
        elif user_input[pygame.K_UP] or user_input[pygame.K_w]:
            self.move_up()
        
        if user_input[pygame.K_SPACE]:
            self.shoot(bullet_manager)
        

    def move_left(self):
        if self.rect.left < 0:
            self.rect.x = SCREEN_WIDTH
        self.rect.x -= 10        
    
    def move_right(self):
        if self.rect.right > SCREEN_WIDTH:
            self.rect.x = 0
        self.rect.x += 10

    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += 10
    
    def move_up(self):
        if self.rect.top > SCREEN_HEIGHT // 2:
            self.rect.y -= 10
    
    def move_left_to_rigth(self):
        if self.rect.left > 0:
            pass

    def move_rigth_to_left(self):
        if self.rect.right < SCREEN_WIDTH:
            pass
    
    def shoot(self, bullet_manager):
        current_time = pygame.time.get_ticks()
        if self.shooting_time <= current_time:
            bullet_manager.add_player_bullet(self)
            self.shooting_time += random.randint(70, 100)

    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))        

    def on_pick_power_up(self, time_up, type, image):
        self.image = pygame.transform.scale(image, (60, 50))
        self.power_up_time_up = time_up
        self.power_up_type = type

    def draw_power_up(self, screen):
        if self.power_up_type != DEFAULT_TYPE:
            time_left = round((self.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_left >= 0:
                font = pygame.font.Font(FONT_STYLE, 22)
                text = font.render(f"{self.power_up_type.capitalize()} is enabled for {time_left}", True, (255, 0, 255))
                text_rect = text.get_rect()
                text_rect.center = (150, 50)
                screen.blit(text, text_rect)
            else:
                self.power_up_type = DEFAULT_TYPE
                self.image = pygame.transform.scale(SPACESHIP, (60, 50))