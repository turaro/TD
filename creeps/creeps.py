import pygame
import math
import numpy


class Creep:

    def __init__(self):
        self.width = 32
        self.height = 32
        self.frames = 0
        self.health = 1
        self.velocity = 3
        self.path = [(-32, 148), (14, 148), (683, 151), (873, 309), (873, 566), (3, 568), (-20, 568)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.path_position = 0
        self.distance = 0
        self.image = []
        self.images = []
        self.flip = False

    def draw(self, window):

        self.image = self.images[self.frames]
        self.frames += 1

        if self.frames >= len(self.images):
            self.frames = 0

        window.blit(self.image, (self.x - self.image.get_width()/2, self.y - self.image.get_height()/2))
        self.move()

        for dot in self.path:
            pygame.draw.circle(window, (255,0,0), dot, 10, 0)

    def collide(self, a, b):
        if self.x + self.width >= a >= self.x:
            if self.y + self.height >= b >= self.y:
                return True
        return False

    def move(self):
        x1, y1 = self.path[self.path_position]
        if self.path_position + 1 >= len(self.path):
            x2, y2 = (-33, 570)
        else:
            x2, y2 = self.path[self.path_position + 1]

        direction = (x2 - x1, y2 - y1)
        move_distance = numpy.linalg.norm(direction)
        direction = direction/move_distance


        if direction[0] < 0 and not self.flip:
            self.flip = True
            for x,  image in enumerate(self.images):
                self.images[x] = pygame.transform.flip(image, True, False)

        move_x, move_y = (self.x + direction[0], self.y + direction[1])

        self.x = move_x
        self.y = move_y
        # Go to next point
        self.distance += math.sqrt((move_x - x1)**2 + (move_y - y1)**2)
        if direction[0] >= 0:
            if direction[1] >= 0:
                if self.x >= x2 and self.y >= y2:
                    self.path_position += 1
            else:
                if self.x >= x2 and self.y <= y2:
                    self.path_position += 1
        else:
            if direction[1] >= 0:
                if self.x <= x2 and self.y >= y2:
                    self.path_position += 1
            else:
                if self.x <= x2 and self.y <= y2:
                    self.path_position += 1

        return True

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True
