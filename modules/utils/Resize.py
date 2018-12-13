import copy
import cv2
from numpy import array
import numpy as np

def crop(img,file):
    image = cv2.imread(img, 0)
    a=np.uint8(255)
    print(a,type(a))
    fd=open(file,"r")
    index=fd.readlines()
    list_of_coords=[]
    #print(list_of_coords)
    for i in range(len(index)):
        #print(index[i])
        list_of_coords.append(index[i].lstrip('(').rstrip(')\n').split(','))

    for i in range(len(list_of_coords)):
        for j in range(4):
            list_of_coords[i][j]=int(list_of_coords[i][j])
        list_of_coords[i]=tuple(list_of_coords[i])
    print(list_of_coords)
    number_of_letters=0
    aux=[]
    cropped=[]
    ox_max=0
    oy_max=0
    #print(cropped)
    for (y1, x2, y2, x1) in list_of_coords:
        if(x2-x1+1)>ox_max:
            ox_max=x2-x1+1
        if(y2-y1+1)>oy_max:
            oy_max=y2-y1+1
    print(ox_max,oy_max)
    for (y1, x2, y2, x1) in list_of_coords:
        row_of_letter = 0;
        # for i in range(x1,x2+1):
        #     for j in range (y1,y2+1):
        aux_ox=x1+ox_max-1;
        aux_oy=y1+oy_max-1;
        #print(aux_ox,aux_oy)
        copy_x=x1
        copy_y=y1
        while (copy_x <= aux_ox):
            aux.append([])
            copy_x+=1
        cropped.append(copy.deepcopy(aux))
        del aux[:]
    print(cropped)
    number_of_letters=0
    for (y1, x2, y2, x1) in list_of_coords:
        aux_ox = x1 + ox_max - 1;
        aux_oy = y1 + oy_max - 1;
        copy_x = x1
        copy_y = y1

        row_of_letter = 0
        while(copy_x<=aux_ox):
            copy_y=y1
            while(copy_y<=aux_oy):
                if copy_x<=x2 and copy_y<=y2:
                    cropped[number_of_letters][row_of_letter].append(image[copy_x][copy_y])
                else:
                    cropped[number_of_letters][row_of_letter].append(a)


                copy_y+=1

            row_of_letter+=1
            copy_x+=1
        number_of_letters+=1
    imagine=array(cropped[1])
    #schimba indexul din cropped pt a obtine ce litera doresti
    cv2.imshow('image',imagine)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return cropped
print(crop("black-white.png","output4.txt"))

