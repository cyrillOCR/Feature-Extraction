from PIL import Image
from numpy.core.multiarray import ndarray

import rgb_to_bw as bw_transformation
import marks_the_center_of_mass as marks_the_center
import numpy as np
import cv2
from scipy import ndimage

def center_of_mass_coord(image:str):
    #transformarea imaginii in alb-negru
    bw_image = bw_transformation.rgb_to_bw(image)
    bw_image_for_show = cv2.imread(bw_image)
    bw_image_for_show = cv2.cvtColor(bw_image_for_show, cv2.COLOR_BGR2GRAY)
    #calculul centrului de masa inaltimea(cy) si latimea(cx)
    cy, cx = ndimage.measurements.center_of_mass(np.array((bw_image_for_show)))
    #marcheaza centrul de masa (decomentati pentru verificare):
    #marks_the_center.marks_the_center_of_mass(bw_image_for_show, cy, cx)
    #returneaza coordonatele centrului inaltimea si latimea
    return (cy, cx)

#Decomentati pentru a vedea cum ruleaza pe un exemplu
#print(center_of_mass_coord('S_chirilic.jpg'))