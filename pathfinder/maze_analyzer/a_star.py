import math
from operator import attrgetter

import numpy as np
from loguru import logger as log


class Node:
    def __init__(self, coordinates: tuple, parent=None):
        self.x, self.y = coordinates
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = parent

    def _compute_heuristic_distance_to_second_node(self, second_node):
        return math.sqrt(pow(self.x - second_node.x, 2) + pow(self.y - second_node.y, 2))

    def compute_g(self):
        self.g = self.parent.g + 1

    def compute_h(self, stop_node):
        self.h = self._compute_heuristic_distance_to_second_node(stop_node)

    def compute_f(self):
        self.f = self.g + self.h

    def has_same_location_as(self, second_node):
        return self.x == second_node.x and self.y == second_node.y

    @classmethod
    def generate_successor(cls, parent):
        yield cls((parent.x+1, parent.y), parent)
        yield cls((parent.x-1, parent.y), parent)
        yield cls((parent.x, parent.y+1), parent)
        yield cls((parent.x, parent.y-1), parent)
        yield cls((parent.x+1, parent.y+1), parent)
        yield cls((parent.x+1, parent.y-1), parent)
        yield cls((parent.x-1, parent.y+1), parent)
        yield cls((parent.x-1, parent.y-1), parent)


class AStar:
    def __init__(self, array: np.ndarray, start_node: tuple, stop_node: tuple, allowed_node_value: int):
        self.array = array
        self.array_height, self.array_width = array.shape
        self.start_node = Node(start_node)
        self.stop_node = Node(stop_node)
        self.allowed_node_value = allowed_node_value
        self.open_list = [self.start_node]
        self.closed_list = []

    def _is_in_boundaries(self, x: int, y: int) -> bool:
        return True if 0 <= x < self.array_height and 0 <= y < self.array_width else False

    @staticmethod
    def _find_node_in_list(node, list_):
        try:
            return next(filter(lambda list_node: list_node.has_same_location_as(node), list_))
        except StopIteration:
            return None

    def find_path(self):
        while len(self.open_list) > 0:
            q = min(self.open_list, key=attrgetter('f'))
            if q.has_same_location_as(self.stop_node):
                log.info("SUCCESS!!!")
                break
            self.open_list.remove(q)
            self.closed_list.append(q)
            for successor in q.generate_successor(parent=q):
                x = successor.x
                y = successor.y
                if not self._is_in_boundaries(x, y) or self.array[x, y] != self.allowed_node_value:
                    continue
                successor.compute_g()
                if successor_from_open_list := self._find_node_in_list(successor, self.open_list):
                    if successor.g < successor_from_open_list.g:
                        self.open_list.remove(successor_from_open_list)
                        successor.compute_h(self.stop_node)
                        successor.compute_f()
                        self.open_list.append(successor)
                elif successor_from_closed_list := self._find_node_in_list(successor, self.closed_list):
                    if successor.g < successor_from_closed_list.g:
                        self.closed_list.remove(successor_from_closed_list)
                        self.open_list.append(successor_from_closed_list)
                    else:
                        continue
                else:
                    successor.compute_h(self.stop_node)
                    successor.compute_f()
                    self.open_list.append(successor)
                    print(f"computing: {successor.x}, {successor.y}")
        for node in self.closed_list:
            log.info(f"X: {node.x}, Y: {node.y}, F,G,H {node.f}, {node.g}, {node.h}")
