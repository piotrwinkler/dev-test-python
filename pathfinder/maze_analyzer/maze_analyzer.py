import numpy as np
from loguru import logger as log

from pathfinder.utils.pictures_loader import display_numpy_array_as_pillow_image, \
    load_picture_as_two_dimension_numpy_array
from pathfinder.maze_analyzer.a_star import AStar


class MazeAnalyzer:
    EXPECTED_NUMBER_OF_ENTRIES = 2
    RGB_BLACK = 0
    RGB_WHITE = 255

    def __init__(self, file_path: str):
        self._mazes_to_analyze = self.load_mazes_from_file(file_path)

    @staticmethod
    def load_mazes_from_file(file_path: str):
        # TODO read all mazes from single file (glob)
        mazes = load_picture_as_two_dimension_numpy_array(file_path)
        return [mazes]

    @classmethod
    def localize_entrance_and_exit(cls, maze: np.ndarray):
        # TODO what if boundaries are white
        maze_height, maze_width = maze.shape
        holes = []
        for index in range(maze_height):
            if maze[index, 0] == cls.RGB_WHITE:
                holes.append((index, 0))
                break
        for index in range(maze_height):
            if maze[index, maze_width-1] == cls.RGB_WHITE:
                holes.append((index, maze_width))
                break
        for index in range(maze_width):
            if maze[0, index] == cls.RGB_WHITE:
                holes.append((0, index))
                break
        for index in range(maze_width):
            if maze[maze_height-1, index] == cls.RGB_WHITE:
                holes.append((maze_height, index))
                break
        if len(holes) == cls.EXPECTED_NUMBER_OF_ENTRIES:
            entrance = holes[0]
            exit_ = holes[1]
            log.info(f"Entrance found: {entrance}, Exit found: {exit_}")
            return entrance, exit_
        else:
            log.warning(f"Wrong number ({len(holes)}) of maze entries found!")
            return None

    def analyze_mazes(self):
        for maze in self._mazes_to_analyze:
            entries = self.localize_entrance_and_exit(maze)
            if entries:
                entrance, exit_ = entries
                a_star = AStar(maze, entrance, exit_, self.RGB_WHITE)
                a_star.find_path()
                log.info("OK")
            else:
                continue
