def distance(i,j,image):
    dis=0
    find=0
    for k in range(j+1,len(image[i])):
        if image[i][k] <= 200:
            find=1
            break
        else:
            dis+=1
    if find==1 :
        return dis,k
    else:
        return 0,k


def mean_vertical_distance(image):
    sum_of_distances=0
    total_distances=0
    i=0
    while(i<len(image)):
        j=0
        while( j<len(image[i])):
            if image[i][j]<=200 and j+1<len(image)-1:
                if image[i][j+1]>200:
                   distance_pixel,k=distance(i,j,image)
                   sum_of_distances+=distance_pixel
                   j=k
                   if distance_pixel!=0:
                       total_distances+=1
            j+=1
        i+=1;

    return sum_of_distances/total_distances
