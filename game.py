import pygame
import os
from creeps.stroke import Stroke


class Game:
    def __init__(self):
        self.width = 1024
        self.height = 768
        self.window = pygame.display.set_mode((self.width, self.height))
        self.towers = []
        self.creeps = [Stroke()]
        self.lives = 10
        self.money = 100
        self.background = pygame.image.load(os.path.join("assets", "bg/background2.png"))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run: False

                position = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

            #Removing passed creeps
            removal = []
            for creep in self.creeps:
                if creep.x < -1:
                    removal.append(creep)
            for r in removal:
                self.creeps.remove(r)

            self.draw()

        pygame.quit()

    def draw(self):
        self.window.blit(self.background, (0, 0))

        for creep in self.creeps:
            creep.draw(self.window)
        pygame.display.update()


g = Game()
g.run()
