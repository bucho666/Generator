# -*- coding: utf-8 -*-
import random
class Connector(object):
    def __init__(self, map):
        self._map = map
        self._conection_nodes = []
        self._remain = set()
        self._connected = set()

    def connect_regions(self):
        candidate = self._map.connect_nodes()
        self._make_remain_nodes(candidate)
        while(self._remain):
            n = random.choice(candidate)
            if self._is_connected_node(n):
                candidate.remove(n)
                continue
            self._add_connection_nodes(n)
        self._set_doors()
        return self

    def _make_remain_nodes(self, candidate):
        for n in candidate:
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

    def _is_connected_node(self, node):
        low, upper = set(node.region_pair())
        return self._connected and low in self._connected == upper in self._connected

if __name__ == '__main__':
    import generator
    generator.Main().run()
