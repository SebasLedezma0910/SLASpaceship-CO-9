from game.components.enemies.enemy_2 import Enemy_2


class Enemy_2_Manager():
    def __init__(self):
        self.enemies_2 = []

    def update(self):
        if not self.enemies_2:
            self.enemies_2.append(Enemy_2())
        for enemy in self.enemies_2:
            enemy.update(self.enemies_2)

    def draw(self, screen):
        for enemy in self.enemies_2:
            enemy.draw(screen)