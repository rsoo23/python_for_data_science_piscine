
import numpy as np


def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    '''
    takes in two lists: height and weight and iterates through, producing
    a new list with the corresponding BMIs
    '''
    if height is None or weight is None:
        print("the height and weight arrays cannot be None")
        return

    height_arr = np.array(height)
    weight_arr = np.array(weight)

    if height_arr.ndim != 1 or weight_arr.ndim != 1:
        print("the height and weight arrays both have to be one dimensional lists")
        return

    if height_arr.size != weight_arr.size:
        print("the height and weight arrays need to have the same number of elements")
        return

    if not np.isin(height_arr.dtype, [int, float]):
        print("the height arrays can only include integers and floats")
        return

    if not np.isin(weight_arr.dtype, [int, float]):
        print("the weight arrays can only include integers and floats")
        return

    if not (np.all(height_arr > 0) and np.all(weight_arr > 0)):
        print("the height and weight arrays can only include non-negative values")
        return

    return list(weight_arr / (height_arr * height_arr))


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    iterates through the bmi (list with the BMI values). returns true
    if the BMI is higher than the limit, vice versa
    '''
    bmi_status = []

    if bmi is None:
        print("the bmi list cannot be None")
        return
    
    if limit < 0:
        print("the bmi limit has to be >= 0")
        return

    for bmi_val in bmi:
        if bmi_val > limit:
            bmi_status.append(True)
        else:
            bmi_status.append(False)

    return bmi_status
