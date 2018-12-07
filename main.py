import sys

from cv2.cv2 import dct
from modules.iterate_image import image_vector
from modules.quadrans import quadrans_sum
from modules.resize_image import resize
from modules.dct import dct_function
from modules.quantize_transformation_coeff import quantize_function
from modules.zig_zag_traversal import zig_zag
from modules.mean_margins_left_right import mean_margins_left_right
from modules.mean_vertical_horizontal_on import mean_vertical_horizontal_on,mean_square_vertical_horizontal_on
from modules.mean_square_horizontal_vertical import mean_square_horizontal_vertical
#from modules.mean_margins_bottom_top import mean_margins_bottom_top
if __name__ == "__main__":
    try:
        print ("Main function")

        img = image_vector(sys.argv[1])
        dictionary = {}
        dictionary['quadrans_sum'] = quadrans_sum(img)
        dictionary['mean-margins-left-right'] = mean_margins_left_right(img)
        dictionary['mean_square_vertical_horizontal_on'] = mean_square_vertical_horizontal_on(img)
        dictionary['mean_vertical_horizontal_on'] = mean_vertical_horizontal_on(img)
        dictionary['mean_square_horizontal_vertical'] = mean_square_horizontal_vertical(img)
       # dictionary['mean_margins_bottom_top'] = mean.mean_margins_bottom_top
       # resize_result = resize(img)
        #dct_result = dct_function(resize_result)
        #quantize_result = quantize_function(dct_result)
        #vectorize_coeff_result = zig_zag(quantize_result)
        print (dictionary)

    except:
        pass


