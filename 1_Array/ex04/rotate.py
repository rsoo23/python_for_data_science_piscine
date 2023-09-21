
from load_image import ft_load
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def square_slice(image_arr: list):
    '''
    takes in the path of the image
        - scales it by a factor of "scale" with the middle of the image as
          reference
        - applies greyscale to the image
    '''
    x_l_offset = int((image_arr.shape[0] * 0.5) / 2)
    x_r_offset = int(image_arr.shape[0] - x_l_offset)
    sliced_region = image_arr[x_l_offset:x_r_offset, x_l_offset:x_r_offset]

    gs_image_arr = \
        np.dot(sliced_region[..., :3], [0.2989, 0.5870, 0.1140])
    # adding a third axis to greyscale_image_arr
    gs_image_arr_new_axis = gs_image_arr[:, :, np.newaxis]

    print("The shape of the image is: " +
          str(gs_image_arr_new_axis.shape) + " or "
          + str(gs_image_arr.shape))

    print(np.round(gs_image_arr_new_axis).astype(int))

    return gs_image_arr


def rotate(path: str, rotation: int):
    try:
        assert isinstance(path, str), "The file name has to be a string"
        assert isinstance(rotation, int), "The rotation has to be an integer"
        assert rotation == 90, "The rotation only can be 90 degrees"
        image = Image.open(path)
        image_arr = np.array(image)

        gs_sq_image_arr = square_slice(image_arr)

        gs_sq_image_arr = np.squeeze(gs_sq_image_arr)
        print(gs_sq_image_arr.shape)

        rotated_image_arr = \
            np.zeros((len(gs_sq_image_arr), len(gs_sq_image_arr)))
        for i in range(len(gs_sq_image_arr)):
            for j in range(len(gs_sq_image_arr[0])):
                rotated_image_arr[j][i] = gs_sq_image_arr[i][j]

        print("New shape after Transpose: " + str(rotated_image_arr.shape))
        print(np.round(rotated_image_arr).astype(int))

        plt.imshow(Image.fromarray(rotated_image_arr))
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
    rotate("animal.jpeg", 30)
    rotate("animal.jpeg", 60)
    print()

    print("Valid file test:")
    ft_load("animal.jpeg")
    rotate("animal.jpeg", 90)
    # rotate("animal.jpeg", 180)
    # rotate("animal.jpeg", 270)
    print()


if __name__ == "__main__":
    main()
