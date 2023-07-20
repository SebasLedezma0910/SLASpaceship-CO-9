import pygame
from game.components.bullets.bullet_manager import Bullet_Manager
from game.components.enemies.enemy_manager import Enemy_Manager
from game.components.menu import Menu
from game.components.power_ups.powerup_manager import PowerUpManager

from game.components.spaceship import Spaceship

from game.utils.constants import BG, FONT_STYLE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.running = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.player = Spaceship()
        self.enemy_manager = Enemy_Manager()
        self.bullet_manager = Bullet_Manager()
        self.power_up_manager = PowerUpManager()

        self.menu = Menu('Press any key to Enter...', ' ', ' ')
        self.score = 0
        self.death_count = 0 
        self.max_score = []


    def run(self):
        # Game loop: events - update - draw
        self.running = True
        while self.running:
            if not self.playing:
                self.show_menu()
        pygame.display.quit()
        pygame.quit()

    def play(self):
        self.playing = True
        self.enemy_manager.reset()
        self.score = 0
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
        self.max_score.append(self.score)

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.on_close()

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input, self.bullet_manager)
        self.enemy_manager.update(self)
        self.bullet_manager.update(self)
        self.power_up_manager.update(self)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.player.draw_power_up(self.screen)
        self.enemy_manager.draw(self.screen)
        self.bullet_manager.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.draw_score()
        self.draw_death_count()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def draw_score(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Score: {self.score}", True, (0, 255, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 50)
        self.screen.blit(text, text_rect)

    def draw_death_count(self):
        font = pygame.font.Font(FONT_STYLE, 22)
        text = font.render(f"Death_count: {self.death_count}", True, (255, 0, 0))
        text_rect = text.get_rect()
        text_rect.center = (1000, 80)
        self.screen.blit(text, text_rect)

    def show_menu(self):
        self.menu.draw(self.screen)
        self.menu.events(self.on_close, self.play)
        
        if self.death_count > 0:
            self.menu.summary_message1(f"Death_count: {self.death_count}")
            self.menu.summary_message2(f"Score: {self.score}")
        
        if self.max_score:
            max_score = max(self.max_score)
            self.menu.update_message(f"Max Score: {max_score}")

    def on_close(self):
        self.playing = False
        self.running = False

    def reset(self):
        self.power_up_manager.reset()