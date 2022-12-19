'''Statistics functions'''

import numpy

class TinyStatistician:

    def __init__(self) -> None:
        pass

    def mean(self, x):
        '''Computes the mean value of a list of numbers'''
        if not isinstance(x, (list, numpy.ndarray)) or any(not isinstance(item, (float, int)) for item in x ):
            print("Function 'mean' takes only a list or an array of numbers as parameter")
            return None
        if not x:
            return None
        total = 0.0
        for item in x:
            total += item
        return total / len(x)

    def median(self, x):
        '''Computes the median value of a list of numbers'''
        if not isinstance(x, (list, numpy.ndarray)) or any(not isinstance(item, (float, int)) for item in x ):
            print("Function 'median' takes only a list or an array of numbers as parameter")
            return None
        if not x:
            return None
        y = x
        y.sort()
        if len(y) % 2 == 1:
            return y[len(y) // 2]
        return (y[len(y) // 2] + y[-1 + len(y) // 2]) / 2

    def quartiles(self, x):
        '''Computes the first and third quartiles of a list of numbers'''
        if not isinstance(x, (list, numpy.ndarray)) or any(not isinstance(item, (float, int)) for item in x ):
            print("Function 'quartiles' takes only a list or an array of numbers as parameter")
            return None
        if not x:
            return None
        y = x
        y.sort()
        return [float(y[len(y) // 4]), float(y[3 * len(y) // 4])]

    def var(self, x):
        '''Computes the variance of a list of numbers'''
        if not isinstance(x, (list, numpy.ndarray)) or any(not isinstance(item, (float, int)) for item in x ):
            print("Function 'var' takes only a list or an array of numbers as parameter")
            return None
        if not x:
            return None
        total = 0.0
        for item in x:
            total += (item - self.mean(x)) ** 2
        return total / len(x)

    def std(self, x):
        '''Computes the standard deviation of a list of numbers'''
        if not isinstance(x, (list, numpy.ndarray)) or any(not isinstance(item, (float, int)) for item in x ):
            print("Function 'var' takes only a list or an array of numbers as parameter")
            return None
        var = self.var(x)
        if not var:
            return None
        else:
            return var ** 0.5


if __name__ == "__main__":
    tstat = TinyStatistician()
    a = [1, 42, 300, 10, 59]
    b = [1, 5, 7, 89]
    print(tstat.mean(a))
    # Expected result: 82.4
    print(tstat.mean(b))
    # Expected result: 25.5
    print(tstat.median(a))
    # Expected result: 42.0
    print(tstat.median(b))
    # Expected result: 6.0
    print(tstat.quartiles(a))
    # Expected result: [10.0, 59.0]
    print(tstat.quartiles(b))
    # Expected result: [5.0, 89.0]
    print(tstat.var(a))
    # Expected result: 12279.439999999999
    print(tstat.var(b))
    # Expected result: 1348.75
    print(tstat.std(a))
    # Expected result: 110.81263465868862
    print(tstat.std(b))
    # Expected result: 36.72533185690771