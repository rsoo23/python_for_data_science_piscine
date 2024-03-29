
# *args is a tuple
# **kwargs is a dictionary

from typing import Any


def ft_mean(args: [float | int]):
    '''calculates the mean'''
    length = len(args)

    if length == 0:
        return

    return sum(args) / length


def ft_median(args: [float | int]):
    '''calculates the median'''
    sorted_list = sorted(args)
    length = len(args)

    if length == 0:
        return

    if length % 2 == 0:
        return \
            (sorted_list[int(length * 0.5 - 1)] +
             sorted_list[int(length * 0.5)]) * 0.5
    return sorted_list[int((length + 1) * 0.5 - 1)]


# def ft_quartile(args: [float | int]):
#     '''calculates the quartile (25% and 75%)'''
#     sorted_list = sorted(args)
#     length = len(args)

#     if length == 0:
#         return
#     if length >= 1 and length <= 3:
#         return [float(sorted_list[0]),
#                 float(sorted_list[length - 1])]
#     return [float(ft_median(sorted_list[:(length // 2)])),
#             float(ft_median(sorted_list[(length // 2):]))]

def ft_quartile(args: [float | int]):
    '''calculates the quartile (25% and 75%)'''
    sorted_list = sorted(args)
    length = len(args)

    if length == 0:
        return
    return [float(sorted_list[int(length * 0.25)]),
            float(sorted_list[int(length * 3 * 0.25)])]


def ft_var(args: [float | int]):
    '''calculates the variance'''
    length = len(args)

    if length == 0:
        return

    mean = ft_mean(args)
    sum_of_squares = sum([(num - mean) ** 2 for num in args])

    return sum_of_squares / length


def ft_std(args: [float | int]):
    '''calculates the standard deviation'''
    return ft_var(args) ** 0.5


def ft_statistics(*args: [float | int], **kwargs: Any) -> None:
    '''calculates common useful statistical values'''
    for value in kwargs.items():
        if value[1] == "mean":
            res = ft_mean(args)
        elif value[1] == "median":
            res = ft_median(args)
        elif value[1] == "quartile":
            res = ft_quartile(args)
        elif value[1] == "std":
            res = ft_std(args)
        elif value[1] == "var":
            res = ft_var(args)
        else:
            return

        if res is None:
            print("ERROR")
        else:
            print(str(value[1]) + " : " + str(res))

# 1: 0 0
# 2: 0 1
# 3: 0 2
# 4: 0+1 2+3
# 5: 0+1 3+4
# 6: 1 4
