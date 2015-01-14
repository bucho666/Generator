# -*- coding: utf-8 -*-

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

    def cardinal(self):
        return [(self + d) for d in Direction.CARDINAL]

class Direction(object):
    N = Coordinate(( 0, -1))
    S = Coordinate(( 0,  1))
    E = Coordinate(( 1,  0))
    W = Coordinate((-1,  0))
    CARDINAL = [N, S, E, W]

if __name__ == '__main__':
    print [c.xy() for c in Coordinate((1, 1)).cardinal()]
