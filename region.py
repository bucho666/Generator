# -*- coding: utf-8 -*-
import random
class Connector(object):
    def __init__(self, map):
        self._map = map
        self._conection_nodes = []
        self._remain = set()
        self._connected = set()
        self._candidate = []

    def connect_regions(self):
        self._candidate = self._map.connect_nodes()
        self._make_remain_nodes()
        while(self._remain):
            self._try_connect()
        self._set_doors()
        return self

    def connect_random(self, num):
        self._candidate = self._map.connect_nodes()
        self._conection_nodes = []
        for c in range(num):
            self._connect_random()
        self._set_doors()

    def _connect_random(self):
        n = random.choice(self._candidate)
        self._add_connection_nodes(n)

    def _try_connect(self):
        n = random.choice(self._candidate)
        if self._new_connection(n):
            self._add_connection_nodes(n)
        else:
            self._candidate.remove(n)

    def _make_remain_nodes(self):
        for n in self._candidate:
            self._remain.update(n.region_pair())

    def _add_connection_nodes(self, node):
        regions = node.region_pair()
        self._connected.update(regions)
        self._remain.difference_update(regions)
        self._conection_nodes.append(node)

    def _set_doors(self):
        for c in [n.coordinate() for n in self._conection_nodes]:
            self._map.set_door(c)
        return self

    def _new_connection(self, node):
        if not self._connected: return True
        low, upper = set(node.region_pair())
        connected_upper = upper in self._connected
        connected_low = low in self._connected
        return connected_upper != connected_low

if __name__ == '__main__':
    import generator
    generator.Main().run()
