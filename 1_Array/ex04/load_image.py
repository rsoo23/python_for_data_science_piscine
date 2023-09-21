
import numpy as np
from PIL import Image


def ft_load(path: str) -> list:
    '''
    Takes in a path for a .jpg or .jpeg image. Prints its format and its
    pixel content in RGB format
    '''
    try:
        assert isinstance(path, str), "The file name has to be a string"
        image = Image.open(path)
        image_arr = np.array(image)
        return image_arr
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
    except FileNotFoundError:
        print("Error: File not found")
