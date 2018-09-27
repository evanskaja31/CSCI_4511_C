import imageio
import numpy
import scipy
from matplotlib import pyplot


def clamp(image):
    newim = numpy.array(image)
    rows, cols = image.shape
    for row in range(rows):
        for col in range(cols):
            newim[row,col] = max(0, min(255, image[row,col]))
    return newim
