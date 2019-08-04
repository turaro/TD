import pygame
import os
from .creeps import Creep


class Stain(Creep):
    def __init__(self):
        super().__init__()
        self.images = [pygame.image.load(os.path.join("assets/creeps/stain", "stain" + str(x) + ".png")) for x in range(2)]
