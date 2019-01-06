import copy

import cv2
import numpy as np

ox_max = 35
oy_max = 35


def crop(img, list_of_coords):
    image = cv2.imread(img, 0)
    a = np.uint8(255)


    aux = []
    cropped = []

    number_of_letters = 0
    for (y1, x1, y2, x2) in list_of_coords:
        copy_x = x1
        aux_ox = x1 + ox_max - 1
        while (copy_x <= aux_ox):
            aux.append([])
            copy_x += 1
        cropped.append(copy.deepcopy(aux))
        del aux[:]
        aux_ox = x1 + ox_max - 1
        aux_oy = y1 + oy_max - 1
        copy_x = x1
        copy_y = y1

        row_of_letter = 0
        while (copy_x <= aux_ox):
            copy_y = y1

            while (copy_y <= aux_oy):
                if copy_x <= x2 and copy_y <= y2:
                    cropped[number_of_letters][row_of_letter].append(image[copy_x][copy_y])
                else:
                    cropped[number_of_letters][row_of_letter].append(a)

                copy_y += 1

            row_of_letter += 1
            copy_x += 1
        number_of_letters += 1
    return cropped
