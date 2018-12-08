def suma_horizontal(image):
    suma=0
    height=len(image)
    width=len(image[0])
    for i in range(0,height):
        for j in range(0,width):
            if(image[i][j]>200):
                for k in range(j+1,width):
                    if image[i][k]>200:
                        suma=suma+k-j
                        break

    return suma

def suma_vertical(image):
    suma=0
    height=len(image)
    width=len(image[0])
    for i in range(0,width): #coloane
        for j in range(0,height): #linii
             if(image[j][i]>200):
                for k in range(j+1,height):
                    if image[k][i]>200:
                        suma=suma+k-j
                        break
    return suma

def mean_horizontal_vertical(image):
    return (suma_vertical(image)* suma_horizontal(image))/2

def mean_square_horizontal_vertical(image):
    vertical=suma_vertical(image)
    horizontal=suma_horizontal(image)
    return (vertical*vertical*horizontal*horizontal)/2

