# -*- coding: utf-8 -*-
class Connector(object):
    def __init__(self, map):
        self._map = map
    
    def connect_regions(self):
        return self

if __name__ == '__main__':
    import generator
    generator.Main().run()
