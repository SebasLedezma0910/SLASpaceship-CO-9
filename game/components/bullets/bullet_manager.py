import pygame
from game.components.bullets.bullet import Bullet
from game.components.bullets.player_bullet import Player_Bullet
from game.utils.constants import ENEMY_TYPE, SPACESHIP


class Bullet_Manager():
    def __init__(self):
        self.enemy_bullets = []
        self.player_bullets = []

    def update(self, game):
        for bullet in self.enemy_bullets:
            bullet.update(self.enemy_bullets)
            if bullet.rect.colliderect(game.player.rect):
                self.enemy_bullets.remove(bullet)
                game.playing = False
                game.death_count += 1
                print(game.death_count)
                pygame.time.delay(1000)
                break

        for bullet in self.player_bullets:
            bullet.update(self.player_bullets)
            for enemy in game.enemy_manager.enemies:
                if bullet.rect.colliderect(enemy.rect):
                    game.enemy_manager.enemies.remove(enemy)
                    self.player_bullets.remove(bullet)
                    game.score += 1

    def draw(self, screen):
        for bullet in self.enemy_bullets + self.player_bullets:
            bullet.draw(screen)

    def add_bullet(self, spaceship):
        if spaceship.type == ENEMY_TYPE and not self.enemy_bullets:
            self.enemy_bullets.append(Bullet(spaceship))
        
    def add_player_bullet(self, spaceship):
        if spaceship.type == SPACESHIP and not self.player_bullets:
            self.player_bullets.append(Player_Bullet(spaceship))