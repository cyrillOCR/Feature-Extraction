
def mean_margins_bottom_top ( image) :
    number_margins = 0
    total_number = 0

    for j in range(0,len(image)) :
        flag = True
        ok = True
        i = len(image)

        while( i >= 0) :
            if image[i][j] == 255 :
                flag = True
            elif image[i][j] <= 200 and flag == True :
                number_margins += 1
                flag = False
            if image[i][j] <= 200 and ok == True:
                ok = False
                total_number +=1
            i = i - 1
    return number_margins/total_number
