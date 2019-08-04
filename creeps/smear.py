import pygame
import os
from .creeps import Creep


class Smear(Creep):
    def __init__(self):
        super().__init__()
        self.images = [pygame.image.load(os.path.join("assets/creeps/smear", "smear" + str(x) + ".png")) for x in range(2)]
