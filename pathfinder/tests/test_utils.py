import pathfinder.utils.pictures_loader as pictures_loader


def test_load_picture_as_two_dimension_numpy_array():
    print("Enter picture path: ")
    picture_path = input()
    numpy_array = pictures_loader.load_picture_as_two_dimension_numpy_array(picture_path)
    print(numpy_array)
    print(numpy_array.shape)


def test_display_numpy_array_as_pillow_image():
    print("Enter picture path: ")
    picture_path = input()
    numpy_array = pictures_loader.load_picture_as_two_dimension_numpy_array(picture_path)
    pictures_loader.display_numpy_array_as_pillow_image(numpy_array)


if __name__ == "__main__":
    test_load_picture_as_two_dimension_numpy_array()
    # test_display_numpy_array_as_pillow_image()
