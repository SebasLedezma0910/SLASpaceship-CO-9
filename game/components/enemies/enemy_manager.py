from game.components.enemies.enemy import Enemy

class Enemy_Manager():
    def __init__(self):
        self.enemies = []

    def update(self):
        if not self.enemies:
            self.enemies.append(Enemy())
        for enemy in self.enemies:
            enemy.update(self.enemies)

    def draw(self, screen):
        for enemy in self.enemies:
            enemy.draw(screen)