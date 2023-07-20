from game.components.power_ups.power2_up import PowerUp2
from game.utils.constants import JET, JET_TYPE, SPACESHIP_JET


class WeaponUpgrader(PowerUp2):
    def __init__(self):
        super().__init__(JET, JET_TYPE, SPACESHIP_JET)