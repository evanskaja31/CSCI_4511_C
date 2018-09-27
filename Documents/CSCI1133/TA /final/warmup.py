# 1133 Extra Lab
# Warm Up
import numpy as np

if __name__ == '__main__':
    numbers = np.array([1, 2, 3, 4])

    for n in numbers:
        print(n)

    # A 2-dimensional matrix:
    matrix = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])

    matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

    print(matrix[2, 2])

    matrix_copy = np.array(matrix)

    from scipy.misc import imread, imshow, imsave

    tiny = imread('tiny.png')

    print(tiny)

    print(tiny[3, 14])

    pixels = imread('cat_8bit.png')
    imshow(pixels)

    imsave('cat_copy.png', pixels)

    pixels = imread('cat_rgb.png', flatten=True)

def clamp(im):
    rows, cols = im.shape
    new_im = np.array(im)
    for row in range(rows):
        for col in range(cols):
            if new_im[row, col] > 255:
                new_im[row, col] = 255
            elif new_im[row, col] < 0:
                new_im[row, col] = 0
    return new_im

def clamp2(image):
    new_image = np.array(image)
    new_image[new_image > 255] = 255
    new_image[new_image < 0] = 0
    return new_image

