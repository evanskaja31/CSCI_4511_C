from scipy.ndimage import imread
from scipy.misc import imshow, imsave
import numpy as np

from warmup import clamp

MAX_VALUE = 255
MIN_VALUE = 0

def threshold(image, value):
    new_image = np.array(image) # copy image
    rows, cols = new_image.shape
    for row in range(rows):
        for col in range(cols):
            if new_image[row, col] > value:
                new_image[row, col] = MAX_VALUE
            else:
                new_image[row, col] = MIN_VALUE
    return new_image

def threshold2(image, value):
    new_image = np.array(image) # copy image
    new_image[new_image > value] = MAX_VALUE
    new_image[new_image <= value] = MIN_VALUE
    return new_image

# value in [-255, 255]
def contrast(image, value):
    factor = (259*(value + 255))/(255*(259 - value))
    new_image = np.array(image) # copy image
    tmp = 128
    rows, cols = new_image.shape
    for row in range(rows):
        for col in range(cols):
            new_image[row, col] = factor*(new_image[row, col] - tmp) + tmp
    return clamp(new_image)

def main():
    c = imread('tulips_8bit.png')
    c2 = threshold(c, 128)
    imsave('tulips_8bit_threshold.png', c2)
    c3 = contrast(c, 128)
    imsave('tulips_8bit_contrast.png', c3)

if __name__ == '__main__':
    main()
