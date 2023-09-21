
from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def zoom(path: str, scale: int):
    '''
    takes in the path of the image
        - scales it by a factor of "scale" with the middle of the image as
          reference
        - applies greyscale to the image
    '''
    try:
        assert isinstance(path, str), "The file name has to be a string"
        assert isinstance(scale, (int, float)), \
            "The scale has to be an integer or a float"
        assert scale > 0 and scale <= 1, \
            "The scale has to be in the range (0, 1]"
        image = Image.open(path)
        image_arr = np.array(image)

        x_l_offset = int((image_arr.shape[0] * (1 - scale)) / 2)
        y_l_offset = int((image_arr.shape[1] * (1 - scale)) / 2)
        x_r_offset = int(image_arr.shape[0] - x_l_offset)
        y_r_offset = int(image_arr.shape[1] - y_l_offset)
        sliced_region = image_arr[x_l_offset:x_r_offset, y_l_offset:y_r_offset]

        gs_image_arr = \
            np.dot(sliced_region[..., :3], [0.2989, 0.5870, 0.1140])
        # adding a third axis to greyscale_image_arr
        gs_image_arr_new_axis = gs_image_arr[:, :, np.newaxis]

        print("New shape after slicing: " +
              str(gs_image_arr_new_axis.shape) + " or "
              + str(gs_image_arr.shape))

        print(np.round(gs_image_arr_new_axis).astype(int))

        plt.imshow(Image.fromarray(gs_image_arr))
        plt.show()
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
    except FileNotFoundError:
        print("Error: File not found")
    except KeyboardInterrupt:
        pass


def main():
    '''
    main function
    '''
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
    zoom("animal.jpeg", 0.4)
    print()


if __name__ == "__main__":
    main()
