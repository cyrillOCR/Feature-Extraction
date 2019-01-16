import numpy as np

from modules.dct.dct_result import dct_result_function
from modules.means.means_supervisor import means_supervisor_function


# cream o tupla, ce va cotine pentru fiecare litera cate o lista cu valorile dupa aplicarea algoritmului dct si valorile
# mediilor aplicate pe litera respectiva
def dct_means_for_each_letter_function(cropped_letters):
    # lista ce va contine valorile pixelilor dupa aplicarea dct. si mediile corespunzatoare pentru toate literele
    means_and_dct_for_all_letters_list = list()

    # parcurgem toate literele
    for letter in cropped_letters:
        means_and_dct_for_one_letter = list()
        # adaugam in lista valorile pixelilor literei dupa dct
        means_and_dct_for_one_letter.append(dct_result_function(np.array(letter)))
        # adaugam in lista valorile mediilor corespunzatoare literei
        means_and_dct_for_one_letter.append(means_supervisor_function(np.array(letter)))

        # cream o tupla ce va contine pentru fiecare litera informatiile de mai sus
        means_and_dct_for_all_letters_list.append(tuple(means_and_dct_for_one_letter))

    return means_and_dct_for_all_letters_list
