import random
import pygame
from genart import BLACK, WHITE, GRAY

class Model():
    def __init__(self):
        pass

    def rule(self):
        pass
    
    def update(self):
        pass

    def render(self):
        pass

    def show(self):
        print("Showing")


class BaseCell():
    def __init__(self, width, height):
        self.value = random.randint(0, 1)
        self.width = width
        self.height = height

        
class CellGrid(Model):
    def __init__(self, width, height, cw, ch):
        self.width = width
        self.height = height
        self.cw = cw
        self.ch = ch
        self.board = [[BaseCell(ch, cw) for i in range(width)] for j in range(height)]

    def in_bounds(self, x, y):
        return x >= 0 and x < self.width and y > 0 and y < self.height
    
    def neighbors(self, x, y):
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if self.in_bounds(j, i) and (i != x or j != y):
                    yield self.board[i][j]

    def rule(self, prev, neighbors):
        pass
    
    def update(self):
        next_generation = [[BaseCell(self.ch, self.cw) for i in range(self.width)] for j in range(self.height)]

        for x in range(self.height):
            for y in range(self.width):
                next_generation[x][y].value = self.rule(self.board[x][y],
                                                        self.neighbors(x, y))

        self.board = next_generation

    def render(self, screen):
        screen.fill(GRAY)
        x,y = self.cw//2,self.cw//2
        for row in self.board:
            for col in row:
                if col.value == 1:
                    pygame.draw.circle(screen, WHITE, (x,y), self.cw//2)
                else:
                    pygame.draw.circle(screen, BLACK, (x,y), self.cw//2)
                x += self.cw
            y += self.ch
            x = self.cw//2
                    

        pygame.display.flip()
        
    def show(self):
        for row in self.board:
            row_data = ""
            for col in row:
                row_data += str(col.value)
            print(row_data)
                