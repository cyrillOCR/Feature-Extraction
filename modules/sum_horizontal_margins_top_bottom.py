#sum of horizontal positions of the margins met by scanning the image from top to bottom

max_black = 200

def sum_horizontal_margins_top_bottom(image):
    sum = 0

    for i in range(0, len(image[0])-1):
        ok = True
        for j in range(0, len(image)):
            if image[j][i] == 255:
                ok = True
            elif image[j][i] <= max_black and ok == True:
                sum += j
                ok = False

    return sum
