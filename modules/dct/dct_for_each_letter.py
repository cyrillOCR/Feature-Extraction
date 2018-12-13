import numpy as np

from modules.dct.dct_result import dct_result_function
from modules.means.means_supervisor import means_supervisor_function


def dct_means_for_each_letter_function(cropped_letters):
    means_and_dct_for_all_letters_list = list()
    means = tuple()

    for letter in cropped_letters:
        means_and_dct_for_one_letter = list()
        means_and_dct_for_one_letter.append(dct_result_function(np.array(letter)))
        means_and_dct_for_one_letter.append(means_supervisor_function(np.array(letter)))

        means_and_dct_for_all_letters_list.append(tuple(means_and_dct_for_one_letter))

    return means_and_dct_for_all_letters_list
