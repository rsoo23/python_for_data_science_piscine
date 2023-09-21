
import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    '''
    Takes in a 2D array, prints its shape and returns a truncated version of
    the array based on the provided start and end arguments using the slicing
    method
    '''
    try:
        assert isinstance(family, list), "the family array has to be a \
2D array"
        family_arr = np.array(family)
        assert family_arr.ndim == 2, "the family array has to be a 2D array"
        assert isinstance(start, int) and isinstance(end, int), "the start \
and end has to be integers"
        print("My shape is: " + str(family_arr.shape))
        family_arr = family_arr[start:end]
        print("My new shape is: " + str(family_arr.shape))
        return family_arr.tolist()
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
    except ValueError:
        print("ValueError: the family array should only include 1D arrays \
of the same shape")
