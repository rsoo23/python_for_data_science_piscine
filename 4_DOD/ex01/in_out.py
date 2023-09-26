
def square(x: int | float) -> int | float:
    '''calculates the square'''
    return float(x ** 2)


def pow(x: int | float) -> int | float:
    '''calculates the value of the number raised to itself'''
    return float(x ** x)


# nonlocal: allows you to modify a variable that belongs
#           to an outer function but is not a global var
def outer(x: int | float, function) -> object:
    '''outer function'''
    count = 0

    def inner() -> float:
        '''inner function'''
        if count == 0:
            nonlocal x
            temp = x
            x = function(x)
        return function(temp)

    return inner
