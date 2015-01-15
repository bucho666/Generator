# -*- coding: utf-8 -*-

class Filler(object):
    def __init__(self, map):
        self._map = map
        self._candidate = []

    def fill(self):
        self._set_candidate()
        while self._fill_deadend():
            pass

    def _set_candidate(self):
        self._candidate = [pos for pos in self._map.coordinates() \
            if not self._map.is_wall_at(pos)]

    def _fill_deadend(self):
        set_wall_num = 0
        for pos in list(self._candidate):
            set_wall_num += self._set_wall_if_dead_end(pos)
        return set_wall_num

    def _set_wall_if_dead_end(self, pos):
        if not self._map.is_deadend(pos):
            return 0
        self._map.set_wall(pos)
        self._candidate.remove(pos)
        return 1

if __name__ == '__main__':
    import generator
    generator.Main().run()
