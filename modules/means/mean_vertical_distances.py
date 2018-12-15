
def distance(i,j,image):
    dis=0
    find=0
    for k in range(i+1,len(image)):
        if image[k][j] <= 200:
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
    j=0
    while j<len(image[0]):
        i=0
        while i<len(image):
            if image[i][j]<=200 and i+1<len(image)-1:
                if image[i+1][j]>200:
                   distance_pixel,k=distance(i,j,image)
                   sum_of_distances+=distance_pixel
                   i=k
                   if distance_pixel!=0:
                       total_distances+=1
            i+=1
        j+=1
    
    if total_distances != 0:
        return sum_of_distances/total_distances

    return 0
