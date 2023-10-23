from dino_runner.utils.constants import BIRD
from dino_runner.components.obstacles.obstacle import Obstacle

import random

BIRD_HEIGHTS = [325, 250, 225]

class Bird(Obstacle):
    def __init__(self):
        super().__init__(BIRD, 0)
        self.rect.y = random.choice(BIRD_HEIGHTS)
        self.step_index = 0

    def draw(self, screen):
        screen.blit(self.image[self.step_index // 5], self.rect)
        self.step_index += 1

        if self.step_index >= 9:
            self.step_index = 0