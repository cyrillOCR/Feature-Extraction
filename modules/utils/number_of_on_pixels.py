import cv2

from modules.utils.rgb_to_bw import rgb_to_bw


def count_on_pixels(image: str):
    # transformarea imaginii in alb-negru
    bw_image = rgb_to_bw(image)
    bw_image_for_show = cv2.imread(bw_image)
    bw_image_for_show = cv2.cvtColor(bw_image_for_show, cv2.COLOR_BGR2GRAY)

    # numararea efectiva a punctelor negre
    count = 0

    for line in range(0, len(bw_image_for_show)):
        for column in range(0, len(bw_image_for_show[line])):
            if bw_image_for_show[line][column] < 128:
                count += 1

    return count

# Decomentati pentru a vedea cum ruleaza pe un exemplu
# print(count_on_pixels('S_chirilic.jpg'))
