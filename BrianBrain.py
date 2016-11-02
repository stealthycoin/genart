import pygame
from genart import WHITE, GRAY, BLACK
from genart.loop import start, iterate_on_model
from genart.models import CellGrid

class BrianBrain(CellGrid):
    def rule(self, prev, neighbors):
        if prev.value == 0:
            fire_count = 0
            for n in neighbors:
                if n.value == 1:
                    fire_count += 1
            if fire_count == 2 or fire_count == 3:
                return 1
            else:
                return prev.value
        elif prev.value == 1:
            return 2
        else:
            return 0

    def render(self, screen):
        screen.fill(GRAY)
        x,y = self.cw//2,self.cw//2
        for row in self.board:
            for col in row:
                if col.value == 1:
                    pygame.draw.circle(screen, BLACK, (x,y), self.cw//2)
                elif col.value == 2:
                    pygame.draw.circle(screen, GRAY, (x,y), self.cw//2)
                else:
                    pygame.draw.circle(screen, WHITE, (x,y), self.cw//2)                    
                x += self.cw
            y += self.ch
            x = self.cw//2
                    

        pygame.display.flip()

            

grid = BrianBrain(250, 150, 2, 2)
iterate_on_model(grid, max_iter=3)
start(grid)
