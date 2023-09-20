
from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def zoom(path: str, scale: int):
    try:
        assert isinstance(path, str), "The file name has to be a string"
        assert isinstance(scale, (int, float)), \
            "The scale has to be an integer or a float"
        assert scale > 0 and scale <= 1, "The scale has to be in the range (0, 1]"
        image = Image.open(path)
        image_arr = np.array(image)

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

        print(np.round(greyscale_image_arr[:, :, np.newaxis]).astype(int))

        plt.imshow(Image.fromarray(greyscale_image_arr));
        plt.show();
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
    except FileNotFoundError:
        print("Error: File not found")
    except KeyboardInterrupt:
        pass

def main():
    print("Invalid file test:")
    print(ft_load("anima.jpeg"))
    print()

    print("Invalid scale test:")
    zoom("animal.jpeg", 1.8)
    zoom("animal.jpeg", -0.8)
    zoom("animal.jpeg", 0)
    zoom("animal.jpeg", "dd")
    print()

    print("Valid file test:")
    print(ft_load("animal.jpeg"))
    zoom("animal.jpeg", 0.8)
    print()


if __name__ == "__main__":
    main()

