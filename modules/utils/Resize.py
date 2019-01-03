import copy

import cv2
import numpy as np

ox_max = 65
oy_max = 65


def crop(img, file):
    image = cv2.imread(img, 0)
    a = np.uint8(255)
    fd = open(file, "r")
    index = fd.readlines()
    list_of_coords = []
    # print(list_of_coords)

    for i in range(len(index)):
        # print(index[i])
        list_of_coords.append(index[i].lstrip('(').rstrip(')\n').split(','))

    # print(list_of_coords)

    for i in range(len(list_of_coords)):
        for j in range(4):
            list_of_coords[i][j] = int(list_of_coords[i][j])
        list_of_coords[i] = tuple(list_of_coords[i])
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

    # imagine = array(cropped[6])
    # cv2.imshow('image', imagine)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    return cropped
