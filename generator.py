# -*- coding: utf-8 -*-
import maze
import map
import room
from region import Connector
from deadend import Filler

class RoomAndMazeBuilder(object):
    def __init__(self):
        self._room_width_range = (6, 8)
        self._room_height_range = (4, 6)
        self._room_create_count = 100
        self._random_doors = 10

    def set_room_width_range(self, range):
        self._room_width_range = range
        return self
        
    def set_room_height_range(self, range):
        self._room_height_range = range
        return self

    def set_room_create_count(self, count):
        self._room_create_count = count
        return self

    def set_random_doors(self, doors):
        self._random_doors = doors
        return self

    def build(self, map):
        region = 0
        region = room.RoomBuilder(map, region)\
            .set_room_size_range(self._room_width_range,
                                 self._room_height_range)\
            .build(self._room_create_count).current_region()
        maze.MazeBuilder(map, region).build()
        connector = Connector(map)
        connector.connect_regions()
        Filler(map).fill()
        connector.connect_random(self._random_doors)
        return map

class Main(object):
    MAP_SIZE = (81, 13)
    def __init__(self):
        self._map = map.Map(self.MAP_SIZE)

    def run(self):
        RoomAndMazeBuilder()\
        .set_room_width_range((12, 18))\
        .set_room_height_range((4, 6))\
        .set_room_create_count(30)\
        .set_random_doors(3)\
        .build(self._map)\
        .render()
        raw_input()

if __name__ == '__main__':
    Main().run()
