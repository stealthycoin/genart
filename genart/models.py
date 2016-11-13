import random
import pygame
from genart import BLACK, WHITE, GRAY
from genart.decorators import cached

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
        self.next_value = 0
        self.width = width
        self.height = height

        
class CellGrid(Model):
    def __init__(self, width, height, cw, ch):
        self.width = width
        self.height = height
        self.cw = cw
        self.ch = ch
        self.board = [[self.create_cell(ch, cw) for i in range(width)] for j in range(height)]

    def create_cell(self, *args, **kwargs):
        return BaseCell(*args, **kwargs)
        
    def in_bounds(self, x, y):
        return x >= 0 and x < self.width and y >= 0 and y < self.height

    @cached
    def neighbors(self, x, y):
        results = []
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                if self.in_bounds(j, i) and (i != x or j != y):
                    results.append(self.board[i][j])
        return results

    def rule(self, prev, neighbors):
        pass
    
    def update(self):
        for x in range(self.height):
            for y in range(self.width):
                self.board[x][y].next_value = self.rule(self.board[x][y],
                                                        self.neighbors(x, y))

        for x in range(self.height):
            for y in range(self.width):
                self.board[x][y].value = self.board[x][y].next_value

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
                
