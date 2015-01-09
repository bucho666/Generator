# -*- coding: utf-8 -*-

import random

class MazeBuilder(object):
    def __init__(self, map):
        self._map = map

    def build(self):
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
    STEP = 2
    def __init__(self, map, start_coordinate):
        self._map =  map
        self._joints = []
        self._tip = Coordinate(start_coordinate)

    def dig(self):
        self._grow_branch()
        while self._joints:
            self._grow_branch()

    def _grow_branch(self):
        for dir in self._random_dir_list():
            if not self._growable(dir): continue
            self._grow_branch_to(dir)
            return
        self._tip_back()

    def _random_dir_list(self):
        dirs = list(Direction.ALL)
        random.shuffle(dirs)
        return dirs

    def _tip_back(self):
        self._tip = self._joints.pop()

    def _grow_branch_to(self, direction):
        for s in range(self.STEP):
            self._tip += direction
            self._dig_tip_coordinate()
        self._joints.append(self._tip.copy())

    def _growable(self, direction):
        check_point = self._tip.copy()
        for s in range(self.STEP):
            check_point += direction
            if not self._growable_coordinate(check_point): return False
        return True

    def _growable_coordinate(self, coordinate):
        if not self._map.is_in(coordinate.xy()): return False
        if self._map.is_floor_at(coordinate.xy()): return False
        return True

    def _dig_tip_coordinate(self):
        self._map.set_floor(self._tip.xy())

if __name__ == '__main__':
    import map
    class Main(object):
        MAP_SIZE = (81, 21)
        def __init__(self):
            self._map = map.Map(self.MAP_SIZE)

        def run(self):
            MazeBuilder(self._map).build()
            self._map.render()

    Main().run()
