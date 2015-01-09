# -*- coding: utf-8 -*-
import maze
import map
import room

if __name__ == '__main__':
    class Main(object):
        MAP_SIZE = (81, 21)
        def __init__(self):
            self._map = map.Map(self.MAP_SIZE)

        def run(self):
            room.RoomBuilder(self._map).build(100)
            maze.MazeBuilder(self._map).build()
            self._map.render()

    Main().run()

