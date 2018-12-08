import sys

from modules.iterate_image import image_vector
from modules.means.mean_margins_bottom_top import mean_margins_bottom_top
from modules.means.mean_margins_left_right import mean_margins_left_right
from modules.means.mean_square_horizontal_vertical import mean_square_horizontal_vertical
from modules.means.mean_vertical_horizontal_on import mean_square_vertical_horizontal_on
from modules.dct.resize_image import resize
from modules.dct.dct import dct_function
from modules.dct.quantize_transformation_coeff import quantize_function
from modules.dct.zig_zag_traversal import zig_zag
if __name__ == "__main__":
    try:
        vectored_image = image_vector(sys.argv[1])

        print(mean_margins_bottom_top(vectored_image))
        print(mean_margins_left_right(vectored_image))
        print(mean_square_horizontal_vertical(vectored_image))
        print(mean_square_vertical_horizontal_on(vectored_image))

        resize = resize(vectored_image)
        dct_result = dct_function(resize)
        qr = quantize_function(dct_result)
        vect_q = zig_zag(qr)

        print(vect_q)

        

        print("Finished")
    except Exception as e:
        print (str(e))


