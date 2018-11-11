def quadrans_sum(vector_image):
    quadrans_dictionary={}
    height,width = vector_image.shape
    quadran1,quadran2,quadran3,quadran4 = 0,0,0,0
    for i in range(0,height):
        for j in range(0,width):
            if i<=height/2 and j<=width/2:
                quadran1 += vector_image[i][j]
            if i<=height/2 and j>=width/2:
                quadran2 += vector_image[i][j]
            if i>=height/2 and j<=width/2:
                quadran3 += vector_image[i][j]
            if i>=height/2 and j>=width/2:
                quadran4 += vector_image[i][j]
    quadrans_dictionary['pixel_sum_quadran1'] = quadran1
    quadrans_dictionary['pixel_sum_quadran2'] = quadran2
    quadrans_dictionary['pixel_sum_quadran3'] = quadran3
    quadrans_dictionary['pixel_sum_quadran4'] = quadran4
    return quadrans_dictionary
