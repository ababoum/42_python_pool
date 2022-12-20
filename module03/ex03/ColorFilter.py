'''Color filter: Manipulation of loaded image via numpy arrays, broadcasting'''

from ImageProcessor import ImageProcessor
import numpy as np


class ColorFilter:
    def __init__(self) -> None:
        pass

    def invert(self, array):
        """
        Inverts the color of the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None
        return 1 - array

    def to_blue(self, array):
        """
        Applies a blue filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None

        new_array = np.copy(array)
        for line in new_array:
            for pixel in line:
                pixel[0] = 0
                pixel[1] = 0
        return new_array

    def to_green(self, array):
        """
        Applies a green filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None

        new_array = np.copy(array)
        for line in new_array:
            for pixel in line:
                pixel[0] = 0
                pixel[2] = 0
        return new_array

    def to_red(self, array):
        """
        Applies a red filter to the image received as a numpy array.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None

        new_array = np.copy(array)
        for line in new_array:
            for pixel in line:
                pixel[1] = 0
                pixel[2] = 0
        return new_array

    def to_celluloid(self, array):
        """
        Applies a celluloid filter to the image received as a numpy array.
        Celluloid filter must display at least four thresholds of shades.
        Be careful! You are not asked to apply black contour on the object,
        you only have to work on the shades of your images.
        Remarks:
        celluloid filter is also known as cel-shading or toon-shading.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None

        new_array = np.copy(array)
        thresholds = np.linspace(0.0, 1.0, num=4, endpoint=False)
        for threshold in thresholds:
            new_array[array > threshold] = threshold
        return new_array

    def to_grayscale(self, array, filter, **kwargs):
        """
        Applies a grayscale filter to the image received as a numpy array.
        For filter = 'mean'/'m': performs the mean of RBG channels.
        For filter = 'weight'/'w': performs a weighted mean of RBG channels.
        Args:
        -----
        array: numpy.ndarray corresponding to the image.
        filter: string with accepted values in ['m','mean','w','weight']
        weights: [kwargs] list of 3 floats where the sum equals to 1,
        corresponding to the weights of each RBG channels.
        Return:
        -------
        array: numpy.ndarray corresponding to the transformed image.
        None: otherwise.
        Raises:
        -------
        This function should not raise any Exception.
        """
        if not isinstance(array, np.ndarray):
            return None

        if filter in ['mean', 'm']:
            new_array = np.array(array)
            for line in new_array:
                for pixel in line:
                    mean_color = pixel.sum() / 3
                    pixel[0] = mean_color
                    pixel[1] = mean_color
                    pixel[2] = mean_color
            return new_array

        if filter in ['weight', 'w']:
            if not kwargs['weights']:
                return None
            if not isinstance(kwargs['weights'], list) or len(kwargs['weights']) != 3 \
                or any(not isinstance(x, (float, int)) for x in kwargs['weights']):
                return None
            weight = np.array(kwargs['weights'])
            new_array = np.array(array)
            if weight.sum() != 1:
                return None
            for line in new_array:
                for pixel in line:
                    mean_color = (pixel * weight).sum()
                    pixel[0] = mean_color
                    pixel[1] = mean_color
                    pixel[2] = mean_color
            return new_array

        return None


if __name__ == "__main__":
    imp = ImageProcessor()
    arr = imp.load("42AI.png")
    # arr = imp.load("elon_canaGAN.png")
    # Output :
    # Loading image of dimensions 200 x 200
    cf = ColorFilter()
    imp.display(arr)
    imp.display(cf.invert(arr))
    imp.display(cf.to_green(arr))
    imp.display(cf.to_red(arr))
    imp.display(cf.to_blue(arr))
    imp.display(cf.to_celluloid(arr))
    imp.display(cf.to_grayscale(arr, 'm'))
    imp.display(cf.to_grayscale(arr, 'weight', weights=[0.1, 0.3, 0.6]))
