#mean product between the square of vertical and horizonftal distances between all "on" pixels; (Andrada)


#from mean_vertical_horizontal_on import sum_horizontal_distance
#from mean_vertical_horizontal_on import sum_vertical_distance

def sum_horizontal_distance(image):
    sum=0
    height=len(image)
    width=len(image[0])
    for i in range(0,height):
        for j in range(0,width):
            if(image[i][j]>200):
                for k in range(j+1,width):
                    if image[i][k]>200:
                        sum=sum+k-j
                        break
    return sum

def sum_vertical_distance(image):
    sum=0
    height=len(image)
    width=len(image[0])
    for i in range(0,width): #coloane
        for j in range(0,height): #linii
             if(image[j][i]>200):
                for k in range(j+1,height):
                    if image[k][i]>200:
                        sum=sum+k-j
                        break
    return sum

def mean_vertical_horizontal_on(image):
    return (sum_vertical_distance(image)*sum_horizontal_distance(image))/2

def mean_square_vertical_horizontal_on(image):
    vertical=sum_vertical_distance(image)
    horizontal=sum_horizontal_distance(image)
    return (vertical*vertical*horizontal*horizontal)/2