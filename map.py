# -*- coding: utf-8 -*-
import sys
import os
from coordinate import Coordinate

class ConnectNode(object):
    def __init__(self, coordinate, region_pair):
        self._coordinate = coordinate
        self._region_pair = tuple(sorted(region_pair))

    def coordinate(self):
        return self._coordinate

    def region_pair(self):
        return self._region_pair

class Map(object):
    WALL = '#'
    DOOR = '+'

    def __init__(self, (w, h)):
        self._grid = [[self.WALL for x in range(w)] for y in range(h)]

    def render(self):
        for line in self._grid:
            for tile in line:
                if tile == self.WALL or tile == self.DOOR:
                    sys.stdout.write(tile)
                else:
                    sys.stdout.write('.')
            sys.stdout.write(os.linesep)

    def size(self):
        return len(self._grid[0]), len(self._grid)

    def set_region(self, (x, y), region='.'):
        self._grid[y][x] = region

    def set_door(self, (x, y)):
        self._grid[y][x] = self.DOOR

    def tile(self, (x, y)):
        return self._grid[y][x]

    def is_wall_at(self, (x, y)):
        return self._grid[y][x] == self.WALL

    def is_floor_at(self, coord):
        return not self.is_wall_at(coord)

    def is_in(self, (x, y)):
        w, h = self.size()
        return x > 0 and y > 0 and \
               x < w and y < h

    def coordinates(self):
        w, h = self.size()
        for y in range(1, h - 1):
            for x in range(1, w - 1):
                yield (x, y)
 
    def odd_coordinates(self):
        w, h = self.size()
        for y in range(1, h - 1, 2):
            for x in range(1, w - 1, 2):
                yield (x, y)
         
    def connect_nodes(self):
        nodes = []
        for c in self.coordinates():
            n = self._make_connect_node(c)
            if not n: continue
            nodes.append(n)
        return nodes

    def _make_connect_node(self, coordinate):
        if not self.is_wall_at(coordinate): return None
        regions = []
        for p in [c.xy() for c in Coordinate(coordinate).cardinal()]:
            if self.is_wall_at(p): continue
            r = self.tile(p)
            if r in regions: continue
            regions.append(r)
        if len(regions) != 2: return None
        return ConnectNode(coordinate, regions)

if __name__ == '__main__':
    import generator
    generator.Main().run()
