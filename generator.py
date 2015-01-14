# -*- coding: utf-8 -*-
import maze
import map
import room
from region import Connector

class Main(object):
    MAP_SIZE = (81, 13)
    def __init__(self):
        self._map = map.Map(self.MAP_SIZE)

    def run(self):
        region = 0
        region = room.RoomBuilder(self._map, region).build(100).current_region()
        region = maze.MazeBuilder(self._map, region).build().current_region()
        Connector(self._map).connect_regions(10)
        self._map.render()
        raw_input()

if __name__ == '__main__':
    Main().run()
