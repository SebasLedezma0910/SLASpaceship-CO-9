import random
from game.components.enemies.enemy import Enemy
from game.components.enemies.enemy_2 import Enemy_2

class Enemy_Manager():
    def __init__(self):
        self.enemies = []

    def update(self, game):
        if not self.enemies:
            choose_enemy = random.choice([Enemy, Enemy_2])
            self.enemies.append(choose_enemy())
            
        for enemy in self.enemies:
            enemy.update(self.enemies, game.bullet_manager)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)
    
    def reset(self):
        self.enemies = []