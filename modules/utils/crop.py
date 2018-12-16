import copy

import cv2
from numpy import array


def crop(img, file):
    
    image = cv2.imread(img, 0)
    fd = open(file, "r")
    index = fd.readlines()
    list_of_coords = []
    
    for i in range(len(index)):
        # print(index[i])
        list_of_coords.append(index[i].lstrip('(').rstrip(')\n').split(','))

    for i in range(len(list_of_coords)):
        for j in range(4):
            list_of_coords[i][j] = int(list_of_coords[i][j])
        list_of_coords[i] = tuple(list_of_coords[i])

    number_of_letters = 0
    aux = []
    cropped = []
    for i in range(len(list_of_coords)):

        for j in range(list_of_coords[i][1], list_of_coords[i][3] + 1):
            
            aux.append([])
        cropped.append(copy.deepcopy(aux))
        del aux[:]
    #print(cropped)
    
    index = 0
    for (y1, x1, y2, x2) in list_of_coords:
        row_of_letter = 0
        

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                cropped[number_of_letters][row_of_letter].append(image[i][j])
                
                # print(image[i][j])
            row_of_letter += 1
        number_of_letters += 1
        index = index +1
    
    # schimba indexul din cropped pt a obtine ce litera doresti
    return cropped

