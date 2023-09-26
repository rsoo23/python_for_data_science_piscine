
from functools import wraps
from typing import Any

# wrappers (aka decorators)
# - extends the behavior of the wrapped function, without permanently
#   modifying it


def callLimit(limit: int):
    '''call Limit'''
    count = 0

    def callLimiter(function):
        '''call Limiter'''
        @wraps(function)
        def limit_function(*args: Any, **kwds: Any):
            '''limit_function'''
            nonlocal count
            if count < limit:
                res = function(*args, **kwds)
                count += 1
                return res
            else:
                print("Error: " + str(function) + " call too many times")
                return None
        return limit_function
    return callLimiter
