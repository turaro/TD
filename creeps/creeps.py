import pygame


class Creep:
    images = []

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.frames = 0
        self.health = 1
        self.path = []
        self.image = []

    def draw(self, win):
        self.frames += 1
        self.image = self.images[self.frames]
        if self.frames >= len(self.images):
            self.frames = 0
        win.blit(self.image, (self.x, self.y))
        self.move

    def collide(self, a, b):
        if self.x + self.width >= a >= self.x:
            if self.y + self.height >= b >= self.y:
                return True
        return False

    def move(self):
        pass

    def hit(self):
        self.health -= 1
        if self.health <= 0:
            return True
