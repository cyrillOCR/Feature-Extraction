import sys

from modules.dct.dct_result import dct_result_function
from modules.utils.iterate_image import image_vector
from modules.means.means_supervisor import means_supervisor_function
from modules.utils.crop import crop
from modules.dct.dct_for_each_letter import dct_means_for_each_letter_function


if __name__ == "__main__":
    try:
        vectored_image = image_vector(sys.argv[1])
        page = sys.argv[1]
        file = sys.argv[2]
        for letter in dct_means_for_each_letter_function(crop(page, file)):
            print(letter)

        print("Finished")

    except Exception as e:
        print(str(e))
