
def give_bmi(height: list[int | float], weight: list[int | float]) \
        -> list[int | float]:
    '''
    takes in two lists: height and weight and iterates through, producing
    a new list with the corresponding BMIs
    '''
    bmi_list = []

    try:
        assert len(height) == len(weight), \
            "the arrays have to be the same size"
    except AssertionError as msg:
        print("AssertionError: " + str(msg))
        return

    for h, w in zip(height, weight):
        try:
            assert isinstance(h, (int, float)) and \
                isinstance(w, (int, float)), \
                "elements of the arrays have to either an integer or a float"
            assert h > 0 and w > 0, \
                "the heights and weights has to both be > 0"
        except AssertionError as msg:
            print("AssertionError: " + str(msg))
            return
        bmi_list.append(w / (h ** 2))

    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    '''
    iterates through the bmi (list with the BMI values). returns true
    if the BMI is higher than the limit, vice versa
    '''
    bmi_status = []

    if bmi is None:
        return

    for bmi_val in bmi:
        if bmi_val > limit:
            bmi_status.append(True)
        else:
            bmi_status.append(False)

    return bmi_status
