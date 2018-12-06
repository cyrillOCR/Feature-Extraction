import copy
image = [[16, 11, 10, 16, 24, 40, 51, 61],
                           [12, 12, 14, 19, 26, 58, 60, 55],
                           [14, 13, 16, 24, 40, 57, 69, 56],
                           [14, 17, 22, 29, 51, 87, 80, 62],
                           [18, 22, 37, 56, 68, 109, 103, 77],
                           [24, 35, 55, 64, 81, 104, 113, 92],
                           [49, 64, 78, 87, 103, 121, 120, 101],
                           [72, 92, 95, 98, 112, 100, 103, 99]
                           ]
def crop(image,list_of_coords):
    #image is a list o list(matrix)
    #list_of_coord is a list with the coords of all letters
    row_of_letter=0
    number_of_letters=0
    aux=[]
    cropped=[]
    for i in range(len(list_of_coords)):

        for j in range(list_of_coords[i][0][0],list_of_coords[i][1][0]+1):
            aux.append([])
        cropped.append(copy.deepcopy(aux))
        del aux[:]
    print(cropped)
    for (upper_left,lower_right) in list_of_coords:
        row_of_letter=0;
        for i in range(upper_left[0],lower_right[0]+1):
            for j in range (upper_left[1],lower_right[1]+1):
                cropped[number_of_letters][row_of_letter].append(image[i][j])
            row_of_letter+=1
        number_of_letters+=1
    return cropped
a=[([0,0],[2,2]),([1,3],[5,7]),([1,1],[6,3])]
print(crop(image,a))
#print(a[0][1][1])

