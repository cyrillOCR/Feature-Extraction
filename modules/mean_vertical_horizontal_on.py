# mean product between vertical and horizontal distances of "on" pixels

def sum_horizontal_distance(image):
    sum=0
    for i in range(0,height):
        for j in range(0,width):
            if(image[i][j]<200):
                for k in range(j+1,width):
                    if image[i][k]==1:
                        sum=sum+k-j
                        break
    return sum

def sum_vertical_distance(image):
    sum=0
    for i in range(0,width): #coloane
        for j in range(0,height): #linii
             if(image[j][i]<200):
                for k in range(j+1,height):
                    if image[k][i]==1:
                        sum=sum+k-j
                        break
    return sum

def mean_vertical_horizontal_on(image):
    height,width=image.shape
    return (sum_vertical_distance(image,heigth,width)*sum_horizontal_distance(image,heigth,width))/2

