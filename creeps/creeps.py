import pygame
import math


class Creep:
    images = []

    def __init__(self):
        self.width = 32
        self.height = 32
        self.frames = 0
        self.health = 1
        self.velocity = 3
        self.path = [(14, 148), (683, 151), (873, 309), (873, 566), (3, 568), (-20, 568)]
        self.x = self.path[0][0]
        self.y = self.path[0][1]
        self.path_position = 0
        self.distance = 0
        self.image = []
        self.move_vector = 0

    def draw(self, win):

        self.image = self.images[self.frames//3]
        self.frames += 1

        if self.frames >= len(self.images)*3:
            self.frames = 0

        win.blit(self.image, (self.x, self.y))
        self.move()

    def collide(self, a, b):
        if self.x + self.width >= a >= self.x:
            if self.y + self.height >= b >= self.y:
                return True
        return False

    def move(self):
        x1, y1 = self.path[self.path_position]
        if self.path_position + 1 >= len(self.path):
            x2, y2 = (-10, 570)
        else:
            x2, y2 = self.path[self.path_position + 1]

        move_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        dx = x2 - x1
        dy = y2 - y1
        self.move_vector += 1
        direction = (dx, dy)
        move_x, move_y = (self.x + direction[0] * self.move_vector, self.y + direction[1] * self.move_vector)

        #Go to next point
        self.distance += math.sqrt((move_x - x1)**2 + (move_y - y1)**2)
        if self.distance >= move_distance:
            self.distance = 0
            self.move_vector = 0
            self.path_position += 1
            if self.path_position >= len(self.path):
                return False

        self.x = move_x
        self.y = move_y
        return True

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True
