from dino_runner.utils.constants import BALLOON, BALLOON_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class Ballon(PowerUp):
    def __init__(self):
        self.image = BALLOON
        self.type = BALLOON_TYPE
        super().__init__(self.image, self.type)