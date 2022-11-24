'''
Test case for a ft_progress loading bar
'''

from time import sleep
from loading import ft_progress


def test_progress(listy):
    '''
    Function to try out ft_progress
    '''
    ret = 0
    for elem in ft_progress(listy):
        ret += (elem + 3) % 5
        sleep(0.01)
    print()
    print(ret)


test_progress(range(100))
test_progress(range(100, 200))
test_progress(range(1))
test_progress(range(4))
test_progress(range(0, -100, -1))
