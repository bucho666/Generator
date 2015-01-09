# -*- coding: utf-8 -*-
import sys
import os

class Map(object):
    WALL = '#'
    FLOOR = '.'

    def __init__(self, (w, h)):
        self._grid = [[self.WALL for x in range(w)] for y in range(h)]

    def render(self):
        for line in self._grid:
            for tile in line:
                sys.stdout.write(tile)
            sys.stdout.write(os.linesep)

    def size(self):
        return len(self._grid[0]), len(self._grid)

    def set_floor(self, (x, y)):
        self._grid[y][x] = self.FLOOR

    def is_wall_at(self, (x, y)):
        return self._grid[y][x] != self.FLOOR

    def is_floor_at(self, coord):
        return not self.is_wall_at(coord)

    def is_in(self, (x, y)):
        w, h = self.size()
        return x > 0 and y > 0 and \
               x < w and y < h
