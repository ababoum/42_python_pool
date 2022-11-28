'''
This module defines a Vector class
'''


import sys


class Error(Exception):
    """Base class for other exceptions"""
    pass


class VectorBuildError(Error):
    """Raised when the vector construction fails because of the input"""
    pass


class InvalidOperation(Error):
    """Raised when the operation cannot be done"""
    pass


class Vector:
    '''Vector object (either row or column vector)'''

    def __init__(self, values):
        # Constructor with positive integer value
        if isinstance(values, int):
            if values <= 0:
                print("Size initializer value must be a strictly positive integer")
                raise VectorBuildError
            else:
                self.values = [[float(i)] for i in range(values)]
                self.shape = (len(self.values), 1)
        # Constructor with range
        elif isinstance(values, tuple):
            if len(values) != 2 or not isinstance(values[0], int) or not isinstance(values[1], int):
                print(
                    "Wrong initializer range format. Usage: Vector((<int>, <int>))")
                raise VectorBuildError
            else:
                if values[0] >= values[1]:
                    print(
                        "Vector range initializer is invalid (start should be strictly before end)")
                    raise VectorBuildError
                self.values = [[float(i)] for i in range(values[0], values[1])]
                self.shape = (len(self.values), 1)
        # Constructor with list
        elif isinstance(values, list) and values:
            self.values = values
            if len(values) == 1:
                if any([not isinstance(item, float) for item in values[0]]):
                    print("Row vector can only contain floats")
                    raise VectorBuildError
                self.shape = (1, len(values[0]))
            else:
                if any([not isinstance(item, list) or
                        len(item) != 1 or not isinstance(item[0], float)
                        for item in values]):
                    print("Column vector can only contain lists")
                    raise VectorBuildError
                self.shape = (len(values), 1)
        else:
            print("Non-recognized constructor format")
            raise VectorBuildError

    def dot(self, other):
        '''Dot product between 2 vectors'''
        if not isinstance(other, Vector) or other.shape != self.shape:
            raise InvalidOperation
        if self.shape == (len(self.values), 1):  # Column vector
            return sum([self.values[i][0] * other.values[i][0] for i in range(len(self.values))])
        else:  # Row vector
            return sum([self.values[0][i] * other.values[0][i] for i in range(len(self.values[0]))])

    def T(self):
        '''Vector transposition'''
        if self.shape == (len(self.values), 1):  # Column vector -> Row vector
            return Vector([[item[0] for item in self.values]])
        else:  # Row vector -> Column vector
            return Vector([[item] for item in self.values[0]])

    def __add__(self, other):
        if not isinstance(other, Vector) or other.shape != self.shape:
            raise InvalidOperation
        if self.shape == (len(self.values), 1):  # Column vector
            return Vector(
                [[self.values[i][0] + other.values[i][0]]
                    for i in range(len(self.values))]
            )
        else:  # Row vector
            return Vector(
                [[self.values[0][i] + other.values[0][i]]
                    for i in range(len(self.values[0]))]
            )

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        return self.__add__(other * -1)

    def __rsub__(self, other):
        return other.__sub__(self)

    def __mul__(self, other):
        if not isinstance(other, (float, int)):
            print(
                f"Vector multiplication by {type(other).__name__} is forbidden")
            raise NotImplementedError
        if self.shape == (len(self.values), 1):  # Column vector
            return Vector([[item[0] * other] for item in self.values])
        else:
            return Vector([[item * other for item in self.values[0]]])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, (float, int)):
            raise NotImplementedError(
                "Vector can only be devided by a float or an integer")
        if (other == 0):
            raise InvalidOperation('Division by zero is forbidden')
        if self.shape == (len(self.values), 1):  # Column vector
            return Vector([[item[0] / other] for item in self.values])
        else:
            return Vector([[item / other for item in self.values[0]]])

    def __rtruediv__(self, other):
        raise NotImplementedError(
            "Division of a scalar by a Vector is not defined")

    def __str__(self) -> str:
        return f'Vector ({self.values})'

    def __repr__(self) -> str:
        return f'Vector ({self.values})'
