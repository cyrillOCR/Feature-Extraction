from modules.dct.dct import dct_function
from modules.dct.resize_image import resize
from modules.dct.zig_zag_traversal import zig_zag


def dct_result_function(matrix_of_letter):
    # aplicam resize-ul pentru a obtine un numar fix de blocuri de 8x8
    resize_letter = resize(matrix_of_letter)
    # aplicam algoritmul dct + cuantificarea jpeg
    dct_result = dct_function(resize_letter)

    # vom returna valorile semnificative (cele care se afla deasupra diagonalei secundare)
    return zig_zag(dct_result)
