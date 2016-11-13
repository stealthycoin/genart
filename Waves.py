import cProfile
import random
import pygame
from genart.loop import start, iterate_on_model
from genart.models import CellGrid, BaseCell

WIDTH = 750
HEIGHT = 1330
PIXEL_SIZE = 5

class WaveCell(BaseCell):
    def __init__(self, col, row):
        self.row = row
        self.col = col
        self.value = random.randint(0, 255)

        self.next_value = 0
        self.last_value = 0

    def add_cell(self, t):
        self.value[0] += t.value[0]
        self.value[1] += t.value[1]
        self.value[2] += t.value[2]
        

class WaveGrid(CellGrid):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[WaveCell(i, j) for i in range(width)] for j in range(height)]
        
    def rule(self, prev, neighbors):
        total = 0
        count = 0
        for n in neighbors:
            total += n.value
            count += 1
        avg = total / 8

        next_ = 0
        if avg == 255:
            next_ = 0
        elif avg == 0:
            next_ = 255
        else:
            next_ = prev.value + avg
            if prev.last_value > 0:
                next_ -= prev.last_value
            if next_ > 255:
                next_ = 255
            elif next_ < 0:
                next_ = 0

        prev.last_value = prev.value
        return next_
        
    def render(self, screen):
        screen.fill((0,0,0))
        x,y = 0,0
        for row in self.board:
            for col in row:
                color = col.value, col.value, col.value
                pygame.draw.circle(screen, color, (x,y), PIXEL_SIZE)
                x += PIXEL_SIZE
            x = 0
            y += PIXEL_SIZE
        pygame.display.flip()

grid = WaveGrid(WIDTH//PIXEL_SIZE, HEIGHT//PIXEL_SIZE)
cProfile.run("iterate_on_model(grid, max_iter=2000)")
start(grid, WIDTH, HEIGHT)
