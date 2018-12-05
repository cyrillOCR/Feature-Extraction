# mean product between the square of horizontal and vertical distances between all "on" pixels;
from mean_vertical_horizontal_on import sum_horizontal_distance
from mean_vertical_horizontal_on import sum_vertical_distance


def mean_square_vertical_horizontal_on(image):
    vertical=sum_vertical_distance(image)
    horizontal=sum_horizontal_distance(image)
    return (vertical*vertical*horizontal*horizontal)/2


mage=[[   0, 255, 255, 255, 255, 255, 255],
       [255, 255,   0,   0,   0,   0, 255],
       [255, 255,   0,   0,   0,   0, 255],
       [255,   0,   0, 255, 255, 255, 255]]
print(mean_square_vertical_horizontal_on(mage))