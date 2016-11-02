from genart.loop import start, iterate_on_model
from genart.models import CellGrid

class ViachniacGrid(CellGrid):
    def rule(self, prev, neighbors):
        livecount = 0
        if prev.value == 1:
            livecount += 1
        for n in neighbors:
            if n.value == 1:
                livecount += 1

        next_ = 1 if livecount > 4 else 0
        if livecount == 4 or livecount == 5:
            next_ = 1 - next_

        return next_

grid = ViachniacGrid(100, 60, 5, 5)
iterate_on_model(grid, max_iter=10)
start(grid)
