# -*- coding: utf-8 -*-

import random
import math

class Room(object):
    def __init__(self, coordinate, size):
        self._coordinate = coordinate
        self._size = size

    def dig(self, map):
        cx, cy = self._coordinate
        cx += 1
        cy += 1
        w, h = self._size
        for y in range(h-1):
            for x in range(w-1):
                map.set_floor((x+cx, y+cy))

    def is_over_lapped(self, other):
        (x, y), (w, h) = self._coordinate, self._size
        (ox, oy), (ow, oh) = other._coordinate, other._size
        x_hit = (x <= ox+ow and x+w >= ox)
        y_hit = (y <= oy+oh and y+h >= oy)
        return x_hit and y_hit

    def is_inside(self, (x, y)):
        cx, cy = self._coordinate
        w, h = self._size
        return cx <= x and x <= cx+w and cy <= y and y <= cy+h

class Range(object):
    def __init__(self, min, max):
        self._min = min
        self._max = max

    def random_value(self, step=1):
        return random.choice(range(self._min, self._max+1, step))
        
class TupleRange(object):
    def __init__(self, a, b):
        self._a = a
        self._b = b

    def random_value(self, step=1):
        return (self._a.random_value(step), self._b.random_value(step))

class RoomBuilder(object):
    def __init__(self, map):
        self._map = map
        self._room_size_range = TupleRange(Range(6, 12), Range(4, 6))
        self._rooms = []

    def build(self, room_build_num):
        for count in range(room_build_num):
            self._build_room()

    def _build_room(self):
        room_size = self._room_size_range.random_value(step=2)
        room_position = self._random_room_position(room_size)
        room = Room(room_position, room_size)
        if self._is_over_lapped(room): return
        room.dig(self._map)
        self._rooms.append(room)

    def _is_over_lapped(self, target_room):
        for room in self._rooms:
            if target_room.is_over_lapped(room): return True
        return False

    def _random_room_position(self, (room_width, room_height)):
        map_width, map_height = self._map.size()
        room_position_range = TupleRange(Range(0, map_width - room_width), Range(0, map_height - room_height))
        return room_position_range.random_value(step=2)

if __name__ == '__main__':
    import map
    class Main(object):
        MAP_SIZE = (21, 9)
        def __init__(self):
            self._map = map.Map(self.MAP_SIZE)

        def run(self):
            RoomBuilder(self._map).build(10)
            self._map.render()

    Main().run()

