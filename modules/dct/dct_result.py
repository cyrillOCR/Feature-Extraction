from modules.dct.dct import dct_function
from modules.dct.quantize_transformation_coeff import quantize_function
from modules.dct.resize_image import resize
from modules.dct.zig_zag_traversal import zig_zag


def dct_result_function(matrix_of_letter):
    resize_letter = resize(matrix_of_letter)
    dct_result = dct_function(resize_letter)
    # quantize_result = quantize_function(dct_result)

    return zig_zag(dct_result)
