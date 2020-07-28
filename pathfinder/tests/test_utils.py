from pathfinder.utils.pictures_loader import load_picture_as_two_dimension_numpy_array


def test_load_picture_as_two_dimension_numpy_array():
    print("Enter picture path: ")
    picture_path = input()
    numpy_array = load_picture_as_two_dimension_numpy_array(picture_path)
    print(numpy_array)
    print(numpy_array.shape)


if __name__ == "__main__":
    test_load_picture_as_two_dimension_numpy_array()
