
import numpy as np
import matplotlib.pyplot as plt


def ft_invert(array) -> list:
    '''
    Takes in a 3D array of an image.
        - inverts the colors using this formula: 255 - rgb_val
    '''
    try:
        assert isinstance(array, np.ndarray), \
            "the array has to be a numpy array"
        assert array.ndim == 3, "the array has to be 3D"
        inverted_arr = 255 - array
        plt.imshow(inverted_arr)
        plt.show()
        return inverted_arr
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
    except KeyboardInterrupt:
        pass


def ft_red(array) -> list:
    '''
    Takes in a 3D array of an image.
        - retains the R value
        - set both the G and B to 0
    '''
    try:
        assert isinstance(array, np.ndarray), \
            \
            "the array has to be a numpy array"
        assert array.ndim == 3, "the array has to be 3D"
        red_arr = np.copy(array)
        red_arr[:, :, 1] = 0
        red_arr[:, :, 2] = 0
        plt.imshow(red_arr)
        plt.show()
        return red_arr
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
    except KeyboardInterrupt:
        pass


def ft_green(array) -> list:
    '''
    Takes in a 3D array of an image.
        - retains the G value
        - set both the R and B to 0
    '''
    try:
        assert isinstance(array, np.ndarray), \
            "the array has to be a numpy array"
        assert array.ndim == 3, "the array has to be 3D"
        green_arr = np.copy(array)
        green_arr[:, :, 0] = 0
        green_arr[:, :, 2] = 0
        plt.imshow(green_arr)
        plt.show()
        return green_arr
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
    except KeyboardInterrupt:
        pass


def ft_blue(array) -> list:
    '''
    Takes in a 3D array of an image.
        - retains the B value
        - set both the R and G to 0
    '''
    try:
        assert isinstance(array, np.ndarray), \
            "the array has to be a numpy array"
        assert array.ndim == 3, "the array has to be 3D"
        blue_arr = np.copy(array)
        blue_arr[:, :, 0] = 0
        blue_arr[:, :, 1] = 0
        plt.imshow(blue_arr)
        plt.show()
        return blue_arr
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
    except KeyboardInterrupt:
        pass


def ft_grey(array) -> list:
    '''
    Takes in a 3D array of an image.
        - applies the greyscale dot product
    '''
    try:
        assert isinstance(array, np.ndarray), \
            "the array has to be a numpy array"
        assert array.ndim == 3, "the array has to be 3D"
        gs_arr = np.copy(array)
        gs_arr[:, :, 0] = 0
        gs_arr[:, :, 2] = 0
        gs_arr = gs_arr[:, :, 1]

        # gs_arr = np.dot(array[..., :3], [0.2989, 0.5870, 0.1140])
        plt.imshow(gs_arr, cmap='gray')
        plt.show()
        return gs_arr
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
    except KeyboardInterrupt:
        pass
