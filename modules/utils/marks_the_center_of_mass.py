import cv2


def marks_the_center_of_mass(bw_image_for_show, cx, cy):
    # marcheaza centrul imaginii prin punct (latime, inaltime)
    bw_image_for_show = cv2.circle(bw_image_for_show, (int(cx), int(cy)), 3, 190, 6)
    cv2.imshow('Test black white image', bw_image_for_show)
    #Tastati 0 pentru a inchide
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return


