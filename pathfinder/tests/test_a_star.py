import numpy as np

from pathfinder.maze_analyzer.a_star import AStar


def test_find_path():
    RGB_WHITE = 1
    maze = np.array([[0, 1, 0, 1],
                     [0, 1, 0, 1],
                     [0, 1, 0, 1],
                     [0, 1, 0, 1],
                     [0, 1, 1, 1]])
    entrance = (0, 1)
    exit_ = (0, 3)
    a_star = AStar(maze, entrance, exit_, RGB_WHITE)
    a_star.find_path()


if __name__ == "__main__":
    test_find_path()
