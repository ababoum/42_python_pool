'''Image processor'''

from PIL import Image
import numpy as np
from matplotlib import pyplot as plt


class ImageProcessor:
    def __init__(self) -> None:
        pass

    def load(self, path):
        im_dims = Image.open(path, 'r')
        arr = np.array(im_dims)
        print(
            f"Loading image of dimensions {im_dims.size[0]} x {im_dims.size[1]}")
        return np.divide(arr[:, :, 0:3], 255)

    def display(self, array):
        plt.imshow(array)
        plt.show()


if __name__ == "__main__":
    imp = ImageProcessor()
    arr = None
    try:
        arr = imp.load("non_existing_file.png")
    except Exception as e:
        print(e)

    print(arr)
    # Output :
    # None
    try:
        arr = imp.load("empty_file.png")
    except Exception as e:
        print(repr(e))
    # Output :
    # Exception: OSError -- strerror: None
    print(arr)
    # Output :
    # None
    arr = imp.load("42AI.png")
    # Output :
    # Loading image of dimensions 200 x 200
    print(repr(arr))
    # Long array of values...

    imp.display(arr)
    # Open a new window with the image in matplotlib
