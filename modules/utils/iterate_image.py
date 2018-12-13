import cv2

def image_vector(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)

    return img
