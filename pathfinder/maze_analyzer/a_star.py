from operator import attrgetter

import numpy as np
from loguru import logger as log


class Node:
    def __init__(self, coordinates: tuple):
        self.x, self.y = coordinates
        self.f = 0
        self.g = 0
        self.g = 0
        self.parent = None


class AStar:
    def __init__(self, array: np.ndarray, start_node: tuple, stop_node: tuple):
        self.array = array
        self.array_height, self.array_width = array.shape
        self.start_node = Node(start_node)
        self.stop_node = Node(stop_node)
        self.open_list = [self.start_node]
        self.closed_list = []

    def _check_boundaries(self, x: int, y: int) -> bool:
        return True if 0 < x < self.array_height and 0 < y < self.array_width else False

    def _generate_successor(self):
        pass

    def find_path(self):
        while len(self.open_list) > 0:
            log.debug(len(self.open_list))
            q = min(self.open_list, key=attrgetter('f'))
            self.open_list.remove(q)
            log.debug(f'X: {q.x}, Y: {q.y}')
            log.debug(len(self.open_list))
