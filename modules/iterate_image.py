from PIL import Image
import cv2
from skimage.color import rgb2gray

def image_vector(path):
    img = cv2.imread(path,cv2.IMREAD_GRAYSCALE )
    # to remove this 
    imggray = rgb2gray(img)
    return imggray
    