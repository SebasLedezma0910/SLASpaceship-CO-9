import random
import pygame
from game.components.power_ups.shield import Shield
from game.components.power_ups.weapon_upgrader import WeaponUpgrader
from game.utils.constants import SHIELD_TYPE

class PowerUpManager:
    def __init__(self):
        self.power_ups = []
        self.when_appers = 0


    def generate_power_up(self):
        current_time = pygame.time.get_ticks()
        if not self.power_ups and current_time >= self.when_appers:
            self.when_appers += random.randint(10000, 15000)
            choose_power_up = random.choice([Shield, WeaponUpgrader])
            self.power_ups.append(choose_power_up())

    def update(self, game):
        self.generate_power_up()
        for power_up in self.power_ups:
            power_up.update(game.game_speed, self.power_ups)
            if power_up.rect.colliderect(game.player.rect):
                if power_up.type == SHIELD_TYPE:
                    start_time = pygame.time.get_ticks()
                    duration = random.randint(3, 5)
                    power_up_time_up = start_time + (duration * 1000)
                    game.player.on_pick_power_up(power_up_time_up, power_up.type, power_up.spaceship_image)
                    self.power_ups.remove(power_up)
                else:
                    start_time2 = pygame.time.get_ticks()
                    duration2 = random.randint(3, 4)
                    power_up_time_up2 = start_time2 + (duration2 * 1000)
                    game.player.on_pick_power_up2(power_up_time_up2, power_up.type, power_up.spaceship_image2)
                    self.power_ups.remove(power_up)

    def draw(self, screen):
        for power_up in self.power_ups:
            power_up.draw(screen)

    def reset(self):
        self.power_ups = []
        now = pygame.time.get_ticks()
        self.when_appers = now + random.randint(10000, 15000)