from scipy.ndimage import imread
from scipy.misc import imshow, imsave
from warmup import clamp
import numpy as np

def mean_filter(image):
    new_image = np.array(image) # copy image
    rows, cols = new_image.shape
    for row in range(rows):
        for col in range(cols):
            suma = 0
            for n_row in range(row - 1, row + 2):
                for n_col in range(col - 1, col + 2):
                    # Be careful not to go outside the array bounds (might be
                    # useful to define helper function)
                    if n_row < rows and n_row >= 0 and \
                            n_col < cols and n_col >= 0:
                        # Be sure not to use the new image
                        suma += image[n_row, n_col]
            new_image[row, col] = suma//9 # 8-connected neighbors
    return new_image

def sobel_edge(image):
    new_image = np.array(image) # copy image
    # y-direction edge ditection
    mw = np.array([
        [1,  2,  1],
        [0,  0,  0],
       [-1, -2, -1]
    ])
    mw_rows, mw_cols = mw.shape
    rows, cols = new_image.shape
    for row in range(rows):
        for col in range(cols):
            sum_y = 0
            for n_row in range(row - 1, row + 2):
                for n_col in range(col - 1, col + 2):
                    # Be careful not to go outside the array bounds (might be
                    # useful to define helper function)
                    if n_row < rows and n_row >= 0 and \
                            n_col < cols and n_col >= 0:
                        mw_row = n_row - row + 1
                        mw_col = n_col - col + 1
                        if mw_row < 3 and mw_row >= 0 \
                                and mw_col < 3 and mw_col >= 0:
                            sum_y += image[n_row, n_col]*mw[mw_row, mw_col]
            new_image[row, col] = sum_y # 8-connected neighbors
    return clamp(new_image)

def main():
    c = imread('tulips_8bit.png')
    c2 = mean_filter(c)
    c2 = mean_filter(c2)
    c2 = mean_filter(c2)
    imsave('tulips_8bit_mean.png', c2)
    c3 = sobel_edge(c)
    imsave('tulips_8bit_sobel.png', c3)

if __name__ == '__main__':
    main()
