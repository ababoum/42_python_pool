'''
Equivalent of the reduce function
'''


def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """

    if not callable(function_to_apply):
        raise TypeError(f"'{type(function_to_apply).__name__}' object is not callable")
    if not hasattr(iterable, '__iter__'):
        raise TypeError(f'ft_reduce() arg 2 must support iteration')

    res = iterable[0]
    count = -1
    for item in iterable:
        count += 1
        if count == 0:
            continue
        res = function_to_apply(res, item)
    return res
