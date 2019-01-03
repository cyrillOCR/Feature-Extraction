import sys
import time

from modules.dct.dct_for_each_letter import dct_means_for_each_letter_function
from modules.utils.Resize import crop
from modules.utils.iterate_image import image_vector
from modules.utils.json import make_json

if __name__ == "__main__":
    try:
        t = time.time()
        vectored_image = image_vector(sys.argv[1])
        page = sys.argv[1]
        file = sys.argv[2]
        f = open("test.txt", "w")
        result = dct_means_for_each_letter_function(crop(page, file))

        for letter in result:
            test_len = 0
            # for i in letter:
            # for j in i:
            #     test_len += len(j)
            # print(letter)
            # print('\n')
            # print(test_len)
            # print('\n\n')
            f.write(str(letter))
            f.write('\n\n')
            # f.write(str(test_len))

        make_json(result)

        # for letter in dct_means_for_each_letter_function(crop(page, file)):
        #     print(letter)
        #     print('\n\n')
        #
        print(time.time() - t)
        print("Finished")

    except Exception as e:
        print(str(e))
