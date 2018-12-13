from PIL import Image
from numpy.core.multiarray import ndarray

from modules.utils.rgb_to_bw import rgb_to_bw
from modules.utils.marks_the_center_of_mass import marks_the_center_of_mass

import numpy as np
import cv2
from scipy import ndimage

def center_of_mass_coord(image:str):
    #transformarea imaginii in alb-negru
    bw_image = rgb_to_bw(image)
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