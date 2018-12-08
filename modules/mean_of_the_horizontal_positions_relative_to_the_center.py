
import math
import center_of_mass as center
import number_of_on_pixels
import cv2

def compute_mean_of_horizontal_positions(image:str):
    height, width = center.center_of_mass_coord(image)
    image_mat = cv2.imread(image)
    image_mat = cv2.cvtColor(image_mat, cv2.COLOR_BGR2GRAY)

    sum = 0
    for line in range(0, len(image_mat)):
        for column in range(0, len(image_mat[line])):
            if(image_mat[line][column])<128:
                sum += abs(width - column)

    mean = sum/(number_of_on_pixels.count_on_pixels(image))
    return mean


#Decomentati pentru a vedea cum ruleaza pe un exemplu
#print(compute_mean_of_horizontal_positions('S_chirilic.jpg'))