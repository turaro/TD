import pygame
import os


class Game:
    def __init__(self):
        self.width = 1024
        self.height = 768
        self.window = pygame.display.set_mode((self.width, self.height))
        self.towers = []
        self.creeps = []
        self.lives = 10
        self.money = 100
        self.background = pygame.image.load(os.path.join("assets", "background.png"))
        self.background = pygame.transform.scale(self.background, (self.width, self.height))
        self.click = []  # temporary

    def run(self):
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run: False

                position = pygame.mouse.get_pos()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.click.append(position)
                    print(position)

                self.draw()
        pygame.quit()

    def draw(self):
        self.window.blit(self.background, (0, 0))
        for i in self.click:
            pygame.draw.circle(self.window, (255, 0, 0), (i[0], i[1]), 5, 0)
        pygame.display.update()


g = Game()
g.run()
