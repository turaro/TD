import pygame
import os
from .creeps import Creep


class Stroke(Creep):
    def __init__(self):
        super().__init__()
        self.images = [pygame.image.load(os.path.join("assets/creeps/stroke", "stroke" + str(x) + ".png")) for x in range(2)]
