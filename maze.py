# -*- coding: utf-8 -*-

import random

class MazeBuilder(object):
    def __init__(self, map):
        self._map = map

    def build(self):
        self._map.fill('#')
        self._dig_maze()

    def _dig_maze(self):
        w, h = self._map.size()
        for y in range(1, h - 1, 2):
            for x in range(1, w - 1, 2):
                self._dig_tree((x, y))

    def _dig_tree(self, (x, y)):
        if self._map.is_floor_at((x, y)): return
        TreeDigger(self._map, (x, y)).dig()

class Coordinate(object):
    def __init__(self, coordinate):
        self._coordinate = coordinate

    def xy(self):
        return self._coordinate

    def __add__(self, other):
        x, y = self._coordinate
        ox, oy = other.xy()
        return Coordinate((x + ox, y + oy))

    def copy(self):
        return Coordinate(self._coordinate)

class Direction(object):
    N = Coordinate(( 0, -1))
    S = Coordinate(( 0,  1))
    E = Coordinate(( 1,  0))
    W = Coordinate((-1,  0))
    ALL = [N, S, E, W]

class TreeDigger(object):
    def __init__(self, map, start_coordinate):
        self._map =  map
        self.joints = []
        self._current = Coordinate(start_coordinate)

    def dig(self):
        self._grow_branch()
        while self.joints:
            self._grow_branch()

    def _grow_branch(self):
        dirs = list(Direction.ALL)
        random.shuffle(dirs)
        for dir in dirs:
            if not self._can_dig(dir): continue
            self._graw_branch_to(dir)
            return
        self._current_back()

    def _current_back(self):
        self._current = self.joints.pop()

    def _graw_branch_to(self, direction):
        for s in range(2):
            self._current += direction
            self._dig_current_coordinate()
        self.joints.append(self._current.copy())

    def _can_dig(self, direction):
        check = self._current.copy()
        for s in range(2):
            check += direction
            if not self._map.is_in(check.xy()): return False
            if self._map.is_floor_at(check.xy()): return False
        return True

    def _dig_current_coordinate(self):
        xy = self._current.xy()
        self._map.set_tile('.', xy)

if __name__ == '__main__':
    class Main(object):
        MAP_SIZE = (81, 21)
        def __init__(self):
            self._map = Map(self.MAP_SIZE)

        def run(self):
            MazeBuilder(self._map).build()
            self._map.render()

    Main().run()
