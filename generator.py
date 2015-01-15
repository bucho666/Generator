# -*- coding: utf-8 -*-
import maze
import map
import room
from region import Connector
from deadend import Filler

class Main(object):
    MAP_SIZE = (81, 13)
    def __init__(self):
        self._map = map.Map(self.MAP_SIZE)

    def run(self):
        region = 0
        region = room.RoomBuilder(self._map, region)\
            .set_room_size_range((8, 16), (4, 6))\
            .build(100).current_region()
        region = maze.MazeBuilder(self._map, region).build().current_region()
        connector = Connector(self._map)
        connector.connect_regions()
        Filler(self._map).fill()
        connector.connect_random(10)
        self._map.render()
        raw_input()

if __name__ == '__main__':
    Main().run()
