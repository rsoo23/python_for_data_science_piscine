

def isEven(num):
    '''
    checks if a number is even
    '''
    return num % 2 == 0


def isOdd(num):
    '''
    checks if a number is odd
    '''
    return num % 2 != 0


def ft_filter(func, iterable):
    '''filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.'''
    new = [x for x in iterable if func(x)]
    return new


def main():
    '''
    replicate the standard the Python filter function
    '''
    iterable = [1, 2, 3, 4, 5, 6, 7]

    result = filter(isEven, iterable)
    print(filter.__doc__)
    for x in result:
        print(x)

    result = ft_filter(isEven, iterable)
    print(ft_filter.__doc__)
    for x in result:
        print(x)


if __name__ == "__main__":
    main()

# filter(function, iterable)
