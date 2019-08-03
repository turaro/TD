import pygame
import os
from .creeps import Creep


class Stroke(Creep):
    images = [pygame.image.load(os.path.join("assets/creeps/stroke", "stroke" + str(x) + ".png")) for x in range(2)]

    def __init__(self):
        super().__init__()

#
