import os
def get_dictionary():
    file=open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'replace.txt'))
    

    dictionary_for_pattern = {}

    for line in file:
        line=line.strip()
        car_de_inlocuit, car_corect = line.split("-")
        dictionary_for_pattern[car_de_inlocuit] = car_corect
    
    return dictionary_for_pattern


def replace_character(list_of_words,dictionary_of_patterns):
    formatted_words = []
    for word in list_of_words:
        word_copy = [word[0],word[1]]
        for key in dictionary_of_patterns:
            word_copy[1] = word_copy[1].replace(key,dictionary_of_patterns[key]) 
        formatted_words.append(word_copy)

    return formatted_words

