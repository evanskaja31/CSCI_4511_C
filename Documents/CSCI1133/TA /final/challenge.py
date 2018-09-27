from scipy.ndimage import imread
from scipy.misc import imshow
import numpy as np

from stretch import threshold

MAX_VALUE = 255
MIN_VALUE = 0

def match_char(image, row, col):
    rows, cols = image.shape
    patterns = {
            '....':' ',
            '.X..':'\'',
            'X...':'.',
            '..X.':',',
            '...X':'"',
            'XX..':'-',
            '..XX':'(',
            'X.X.':')',
            '.X.X':'J',
            '.XXX':'L',
            'XX.X':'7',
            'XXX.':'P',
            'XXXX':'8'
    }
    for pat in patterns:
        pat_index = 0
        count = 0
        for n_row in range(row - 1, row + 1):
            for n_col in range(col - 1, col + 1):
                if n_row < rows and n_row >= 0 and \
                        n_col < cols and n_col >= 0:
                    if (image[n_row, n_col] > MIN_VALUE and \
                            pat[pat_index] == 'X') or (
                            image[n_row, n_col] == MIN_VALUE and\
                            pat[pat_index] == '.'):
                        count += 1
                pat_index += 1
        if count >= 4:
            return patterns[pat]
    return ' '

#  http://www.jave.de/image2ascii/algorithms.html
def img_to_ascii(image):
    rows, cols = image.shape
    ascii_img = [['']*cols for _ in range(rows)]
    for row in range(rows):
        for col in range(cols):
            ascii_img[row][col] = match_char(image, row, col)
    return ascii_img

def print_ascii_img(img):
    for row in img:
        print(''.join(row))

if __name__ == '__main__':
    im = imread('./tiny2.png')
    asc = img_to_ascii(im)
    print_ascii_img(asc)
