import pathfinder.utils.pictures_loader as pictures_loader
from pathfinder.maze_analyzer.maze_analyzer import MazeAnalyzer


def test_localize_entrance_and_exit():
    print("Enter picture path: ")
    picture_path = input()
    numpy_array = pictures_loader.load_picture_as_two_dimension_numpy_array(picture_path)
    MazeAnalyzer.localize_entrance_and_exit(numpy_array)


def test_analyze_mazes():
    print("Enter picture path: ")
    picture_path = input()
    analyzer = MazeAnalyzer(picture_path)
    analyzer.analyze_mazes()


if __name__ == "__main__":
    # test_localize_entrance_and_exit()
    test_analyze_mazes()
