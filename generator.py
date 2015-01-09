# -*- coding: utf-8 -*-
import maze
import sys
import os

class Map(object):
    def __init__(self, (w, h)):
        self._grid = [[' ' for x in range(w)] for y in range(h)]

    def render(self):
        for line in self._grid:
            for tile in line:
                sys.stdout.write(tile)
            sys.stdout.write(os.linesep)

    def fill(self, tile):
        for y, line in enumerate(self._grid):
            for x in range(len(line)):
                self._grid[y][x] = tile

    def size(self):
        return len(self._grid[0]), len(self._grid)

    def set_tile(self, tile, (x, y)):
        self._grid[y][x] = tile

    def is_wall_at(self, (x, y)):
        return self._grid[y][x] != '.'

    def is_floor_at(self, coord):
        return not self.is_wall_at(coord)

    def is_in(self, (x, y)):
        w, h = self.size()
        return x > 0 and y > 0 and \
               x < w and y < h

if __name__ == '__main__':
    class Main(object):
        MAP_SIZE = (81, 21)
        def __init__(self):
            self._map = Map(self.MAP_SIZE)

        def run(self):
            maze.MazeBuilder(self._map).build()
            self._map.render()

    Main().run()

