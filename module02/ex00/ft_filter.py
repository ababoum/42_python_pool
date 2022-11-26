'''
Equivalent of the filter function
'''


def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """

    if not callable(function_to_apply):
        raise TypeError(f"'{type(function_to_apply).__name__}' object is not callable")
    if not hasattr(iterable, '__iter__'):
        raise TypeError(f"'{type(iterable).__name__}' object is not iterable")

    for item in iterable:
        if function_to_apply(item):
            yield item
