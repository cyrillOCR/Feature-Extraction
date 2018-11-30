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
        return dis
    else:
        return 0


def mean_vertical_distance(image):
    sum_of_distances=0
    total_distances=0
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            if image[i][j]<=200 and i+1<len(image)-1:
                if image[i+1][j]>200:
                   distance_pixel=distance(i,j,image)
                   sum_of_distances+=distance_pixel
                   if distance_pixel!=0:
                       total_distances+=1
    return sum_of_distances/total_distances

#image=[[255,255,255,255,255,255,255],[255,255,0,0,0,0,255],[255,255,0,0,0,0,255],[255,0,0,255,255,255,255],[255,0,0,255,255,255,255],[255,0,0,255,255,255,255],[255,255,0,0,0,0,255],[255,255,0,0,0,0,255]]
#print(mean_vertical_distance(image))


