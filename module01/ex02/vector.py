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

    def __init__(self, coordinates=None, size=None, _range=None):
        if not any([coordinates, size, _range]):
            print("Vector should be initialized with some kind of parameter")
            raise VectorBuildError
        if len([x for x in [coordinates, size, _range] if x]) != 1:
            print("Vector should be initialized with only one kind of parameter")
            raise VectorBuildError
        if isinstance(coordinates, list) and coordinates:
            self.values = coordinates
            if len(coordinates) == 1:
                if any([not isinstance(item, float) for item in coordinates[0]]):
                    print("Row vector can only contain floats")
                    raise VectorBuildError
                self.shape = (1, len(coordinates[0]))
            else:
                if any([not isinstance(item, list) or
                        len(item) != 1 or not isinstance(item[0], float)
                        for item in coordinates]):
                    print("Column vector can only contain lists")
                    raise VectorBuildError
                self.shape = (len(coordinates), 1)
        elif isinstance(size, int) and size > 0:
            self.values = [[float(i) for i in range(size)]]
            self.shape = (len(self.values), 1)
        elif isinstance(_range, tuple) and len(_range) == 2 and \
                isinstance(_range[0], int) and isinstance(_range[1], int):
            if _range[0] >= _range[1]:
                print(
                    "Vector range paramater is invalid (start should be strictly before end)")
                raise VectorBuildError
            self.values = [[float(i) for i in range(_range[0], _range[1])]]
            self.shape = (len(self.values), 1)
        else:
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
            raise NotImplementedError

        if self.shape == (len(self.values), 1):  # Column vector
            return Vector([[item[0] * other] for item in self.values])
        else:
            return Vector([[item * other for item in self.values[0]]])

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if not isinstance(other, (float, int)):
            raise NotImplementedError

        if self.shape == (len(self.values), 1):  # Column vector
            return Vector([[item[0] / other] for item in self.values])
        else:
            return Vector([[item / other for item in self.values[0]]])

    def __rtruediv__(self, other):
        raise NotImplementedError(
            "Division of a scalar by a Vector is not defined.")

    def __str__(self) -> str:
        return f'{self.values}'

    def __repr__(self) -> str:
        return f'{self.values}'
