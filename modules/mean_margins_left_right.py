
max_black = 200

def mean_margins_left_right(image):

    number_margins = 0
    total_number = 0
    for i in range(0,len(image)):
        flag = True
        ok = True
        for j in range (0,len(image[i])-1):
            if image[i][j] == 255:
                flag = True
            elif image[i][j] <=max_black and flag == True:
                number_margins = number_margins +1
                flag = False
            if image[i][j] <=max_black and ok == True:
                ok = False
                total_number = total_number+1

    return number_margins/total_number