
from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage


def zoom(image_arr: list, scale: float):
    x_offset_left = int((image_arr.shape[0] * (1 - scale)) / 2)
    y_offset_left = int((image_arr.shape[1] * (1 - scale)) / 2)
    x_offset_right = int(image_arr.shape[0] - x_offset_left)
    y_offset_right = int(image_arr.shape[1] - y_offset_left)
    sliced_region = image_arr[x_offset_left:x_offset_right, \
        			y_offset_left:y_offset_right]

    greyscale_image_arr = np.dot(sliced_region[...,:3], [0.2989, 0.5870, 0.1140])

    temp_list = list(sliced_region.shape)
    temp_list[2] = 1

    print("The shape of the image is: " + str(tuple(temp_list)) + \
        " or " + str(sliced_region.shape[0:2]))

    greyscale_val_arr = \
        np.round(greyscale_image_arr[:, :, np.newaxis]).astype(int)
    print(greyscale_val_arr)

    return greyscale_image_arr, greyscale_val_arr, sliced_region.shape[0:2]


def rotate(path: str, rotation: int):
    try:
        assert isinstance(path, str), "The file name has to be a string"
        assert isinstance(rotation, int), "The rotation has to be an integer"
        image = Image.open(path)
        image_arr = np.array(image)

        greyscale_image_arr, greyscale_val_arr, image_shape = zoom(image_arr, 0.5)

        print("New shape after Transpose: " + str(image_shape[::-1]))
        print(np.squeeze(greyscale_val_arr));

        rotated_image = ndimage.rotate(greyscale_image_arr, rotation)

        plt.imshow(Image.fromarray(rotated_image))
        plt.show()

    except AssertionError as msg:
        print("AssertionError: " + str(msg))
    except FileNotFoundError:
        print("Error: File not found")
    except KeyboardInterrupt:
        pass


def main():
    print("Invalid file test:")
    rotate("ani.jpeg", 90)
    print()
    rotate(None, 90)
    print()

    print("Invalid rotation test:")
    rotate("animal.jpeg", "dd")
    print()

    print("Valid file test:")
    ft_load("animal.jpeg")
    # rotate("animal.jpeg", 30)
    # rotate("animal.jpeg", 60)
    rotate("animal.jpeg", 90)
    print()


if __name__ == "__main__":
    main()

# [[146 168 177 ...  88  89 104]
#  [142 148 145 ... 102  98 101]
#  [141 131 122 ... 100 109 117]
#  ...
#  [  8  15   2 ... 119 113 109]
#  [ 11  17   2 ... 114 111 109]
#  [ 14  18   2 ... 109 116 121]]