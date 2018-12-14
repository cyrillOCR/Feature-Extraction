from PIL import Image
import cv2
from skimage.color import rgb2gray


def image_vector(path):
    img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    # to remove this
    imggray = rgb2gray(img)
    return imggray


def horizontal_distance(i,j,image):
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

def vertical_distance(i,j,image):
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



def mean_vertical_horizontal_distance(image):
    sum_of_horizontal_distances=0
    sum_of_vertical_distances=0
    total_horizontal_distances=0
    total_vertical_distances=0
    i=0
    while(i<len(image)):
        j=0
        while( j<len(image[i])):
            if image[i][j]<=200:
                if i + 1 < len(image) - 1 and image[i + 1][j] > 200:
                        distance_pixel=vertical_distance(i,j,image)
                        #print(image[i][j], distance_pixel, image[x][j])
                        sum_of_vertical_distances+=distance_pixel
                        if distance_pixel != 0:
                            total_vertical_distances += 1

                if j+1<len(image)-1 and image[i][j+1]>200:
                       distance_pixel,k= horizontal_distance(i,j,image)
                       #print(image[i][j],distance_pixel,image[i][k])
                       sum_of_horizontal_distances+=distance_pixel
                       j = k-1
                       #print(distance_pixel , i , j)
                       if distance_pixel!=0:
                           total_horizontal_distances+=1
            j+=1
        i+=1

    if total_horizontal_distances!=0:
        mean_horizontal=sum_of_horizontal_distances/total_horizontal_distances
    else:
        mean_horizontal=0
    if total_vertical_distances!=0:
        mean_vertical=sum_of_vertical_distances/total_vertical_distances
    else:
        mean_vertical=0
    return mean_horizontal,mean_vertical




#image=image_vector("C:\\Users\\sfirn\\Desktop\\Feature-Extraction\\images\\letter.png")
#image=[[255,255,255,255,255,255,255],[255,255,0,0,0,0,255],[255,255,0,0,0,0,255],[255,0,0,255,255,255,255],[255,0,0,255,255,255,255],[255,0,0,255,255,255,255],[255,255,0,0,0,0,255],[255,255,0,0,0,0,255]]
#print(mean_vertical_horizontal_distance(image))