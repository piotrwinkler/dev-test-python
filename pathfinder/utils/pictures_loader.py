import numpy as np
from PIL import Image


def load_picture_as_two_dimension_numpy_array(picture_name: str) -> np.ndarray:
    image = Image.open(picture_name).convert('RGB')
    np_array_image = np.asarray(image)
    return np.mean(np_array_image, axis=2)
