# mean product between the square of horizontal and vertical distances between all "on" pixels;
from modules.mean_vertical_horizontal_on import sum_horizontal_distance
from modules.mean_vertical_horizontal_on import sum_vertical_distance


def mean_square_vertical_horizontal_on(image):
    height,width=image.shape
    vertical=sum_vertical_distance(image,heigth,width)
    horizontal=sum_horizontal_distance(image,heigth,width)
    return (vertical*vertical*horizontal*horizontal)/2
