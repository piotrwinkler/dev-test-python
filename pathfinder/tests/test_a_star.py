import numpy as np

from pathfinder.maze_analyzer.a_star import AStar


def test_find_path():
    maze = np.array([[0, 1, 0, 0],
                     [0, 1, 0, 0],
                     [0, 1, 1, 0],
                     [0, 0, 1, 0],
                     [0, 0, 1, 0]])
    entrance = (0, 1)
    exit_ = (4, 2)
    a_star = AStar(maze, entrance, exit_)
    a_star.find_path()


if __name__ == "__main__":
    test_find_path()
