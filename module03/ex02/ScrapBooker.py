'''Scrapbooker: Manipulation and initiation to slicing method on numpy arrays'''

import numpy as np


class ScrapBooker:
    def __init__(self) -> None:
        pass

    def crop(self, array, dim, position=(0, 0)):
        """
        Crops the image as a rectangle via dim arguments (being the new height
        and width of the image) from the coordinates given by position arguments.
        Args:
        -----
        array: numpy.ndarray
        dim: tuple of 2 integers.
        position: tuple of 2 integers.
        Return:
        -------
        new_arr: the cropped numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) \
                or not isinstance(dim, tuple) or len(dim) != 2 \
                or not isinstance(dim[0], int) or not isinstance(dim[1], int) \
                or dim[0] < 0 or dim[1] < 0 \
                or not isinstance(position, tuple) or len(position) != 2 \
                or not isinstance(position[0], int) or not isinstance(position[1], int) \
                or position[0] < 0 or position[1] < 0:
            return None
        new_array = np.array(0)

        # split following the position
        if position[0] != 0:
            new_array = np.split(array, [position[0], len(array)])[1]
        if position[1] != 0:
            new_array = np.hsplit(
                new_array, [position[1], new_array.shape[1]])[1]

        # split following the shape
        new_array = np.split(new_array, [0, dim[0]])[1]
        new_array = np.hsplit(new_array, [0, dim[1]])[1]

        return new_array

    def thin(self, array, n, axis):
        """
        Deletes every n-th line pixels along the specified axis (0: Horizontal, 1: Vertical)
        Args:
        -----
        array: numpy.ndarray.
        n: non null positive integer lower than the number of row/column of the array
        (depending of axis value).
        axis: positive non null integer.
        Return:
        -------
        new_arr: thined numpy.ndarray.
        None (if combinaison of parameters not compatible).
        Raise:
        ------
        This function should not raise any Exception.
        """
        if not isinstance(axis, int) or (axis != 0 and axis != 1):
            return None
        if not isinstance(array, np.ndarray) \
                or not isinstance(n, int) \
                or n <= 0 or n >= array.shape[axis]:
            return None
        
        axis = (axis + 1) % 2

        new_array = np.array(0)
        to_del = list(range(n - 1, array.shape[axis], n))
        new_array = np.delete(array, to_del, axis=axis)
        return new_array

    def juxtapose(self, array, n, axis):
        """
        Juxtaposes n copies of the image along the specified axis.
        Args:
        -----
        array: numpy.ndarray.
        n: positive non null integer.
        axis: integer of value 0 or 1.
        Return:
        -------
        new_arr: juxtaposed numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(axis, int) or (axis != 0 and axis != 1):
            return None
        if not isinstance(array, np.ndarray) \
                or not isinstance(n, int) \
                or n <= 0:
            return None

        new_array = array
        for _ in range(1, n):
            new_array = np.concatenate((new_array, array), axis=axis)
        return new_array

    def mosaic(self, array, dim):
        """
        Makes a grid with multiple copies of the array. The dim argument specifies
        the number of repetition along each dimensions.
        Args:
        -----
        array: numpy.ndarray.
        dim: tuple of 2 integers.
        Return:
        -------
        new_arr: mosaic numpy.ndarray.
        None (combinaison of parameters not compatible).
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray) \
                or not isinstance(dim, tuple) or len(dim) != 2 \
                or not isinstance(dim[0], int) or not isinstance(dim[1], int) \
                or dim[0] < 0 or dim[1] < 0:
            return None
        
        new_array = self.juxtapose(array, dim[0], axis=0)
        new_array = self.juxtapose(new_array, dim[1], axis=1)

        return new_array


if __name__ == "__main__":
    spb = ScrapBooker()
    arr1 = np.arange(0, 25).reshape(5, 5)
    print(spb.crop(arr1, (3, 1), (1, 0)))
    # Output :
    # array([[ 5],
    # [10],
    # [15]])
    print('*' * 25)
    arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
    print(f"Before:\n{arr2}")
    print(f"After:\n{spb.thin(arr2,3,0)}")
    # Output :
    # array([[’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
    # [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
    # [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
    # [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
    # [’A’, ’B’, ’D’, ’E’, ’G’, ’H’],
    # [’A’, ’B’, ’D’, ’E’, ’G’, ’H’]], dtype=’<U1’)
    print('*' * 25)
    arr3 = np.array([[var] * 10 for var in "ABCDEFG"])
    print(spb.thin(arr3,3,1))
    # See scale for result
    print('*' * 25)
    arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
    print(spb.juxtapose(arr3, 3, 1))
    print('*' * 25)
    # Output :
    # array([[1, 2, 3, 1, 2, 3, 1, 2, 3],
    # [1, 2, 3, 1, 2, 3, 1, 2, 3],
    # [1, 2, 3, 1, 2, 3, 1, 2, 3]])
    print(spb.juxtapose(arr3, 3, 0))
    print('*' * 25)
    print(spb.juxtapose(arr3, 1, 0))
    print('*' * 25)

    arr4 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
    print(spb.juxtapose(arr4, 2, 0))

    print('*' * 25)

    arr4 = np.array([[1, 2, 3],['*', '-', '*'],[4, 5, 6]])
    print(spb.mosaic(arr4, (1,1)))
    print('*' * 25)
    print(spb.mosaic(arr4, (3,3)))
    print('*' * 25)
    print(spb.mosaic(arr4, (3,1)))

    print('=' * 21 + "ERROR MANAGEMENT" + '=' * 21)

    not_numpy_arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
    print(spb.crop(not_numpy_arr, (1,2)))
    print(spb.juxtapose(arr4, -2, 0))
    print(spb.mosaic(arr4, (1, 2, 3)))


