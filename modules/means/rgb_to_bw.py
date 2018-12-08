import re
from PIL import Image

def rgb_to_bw(image: str):
    color_img = Image.open(image)   #deschide imaginea
    gray_img = color_img.convert('L') #converteste in gray_scale
    bw_img = gray_img.point(lambda x: 0 if x < 128 else 255, '1') #transforma imaginea in alb_negru
    name_of_file = re.sub(image, image[0:len(image)-4]+'_bw.jpg', image) #memoreaza denumirea fisierului
    bw_img.save(name_of_file)
    return name_of_file     #returneza denumirea fisierului

