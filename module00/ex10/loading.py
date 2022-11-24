'''
This module defines a function that displays a progress bar
'''

import time


def ft_progress(lst):
    '''
    Displays a progress bar, and yields elements from a list
    '''
    if not lst:
        yield None
    end = lst[-1]
    start_time = time.time()
    for item in lst:
        item_to_display = item
        try:
            progress = int(100 * item_to_display/end)
        except ZeroDivisionError:
            progress = 100
        progress_bars = int(20 * progress / 100)
        elapsed_time = time.time() - start_time
        if progress != 0:
            eta = (elapsed_time * 100 / progress) - elapsed_time
        else:
            eta = 0
        print(
            f"ETA: {eta:>6.2f}s \
[ {progress:3}%][{'='*progress_bars + '>':<21}] {item_to_display}/{end} | \
elapsed time {elapsed_time:.2f}s", end='\r')
        yield item
