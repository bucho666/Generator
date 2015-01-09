# -*- coding: utf-8 -*-
import maze
import map

if __name__ == '__main__':
    class Main(object):
        MAP_SIZE = (81, 21)
        def __init__(self):
            self._map = map.Map(self.MAP_SIZE)

        def run(self):
            maze.MazeBuilder(self._map).build()
            self._map.render()

    Main().run()

