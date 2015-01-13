# -*- coding: utf-8 -*-
import maze
import map
import room

class Main(object):
    MAP_SIZE = (49, 9)
    def __init__(self):
        self._map = map.Map(self.MAP_SIZE)

    def run(self):
        region = 0
        region = room.RoomBuilder(self._map, region).build(100).current_region()
        region = maze.MazeBuilder(self._map, region).build().current_region()
        self._map.render()
        print region
        raw_input()

if __name__ == '__main__':
    Main().run()
