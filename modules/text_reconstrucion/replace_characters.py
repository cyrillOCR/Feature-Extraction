import os

# Din fisierul replace.txt vom lua caracterele ce trebuie inlocuite si, respectiv, caracterele inlocuitoare
# si vom salva datele din fisierul replace.txt intr-un dictionar care va fi de forma dct[caracter_de_inlocuit] = caracter_corect
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
            word_copy[1] = word_copy[1].replace("\u02191\u02192","\u0219")
            word_copy[1] = word_copy[1].replace("\u02191","\u0219")
            word_copy[1] = word_copy[1].replace("\u02192","\u0219")
            word_copy[1] = word_copy[1].replace("\u0219t1\u0219t2","\u0219t")
            word_copy[1] = word_copy[1].replace("\u0219t1","\u0219t")
            word_copy[1] = word_copy[1].replace("\u0219t2","\u0219t")
            word_copy[1] = word_copy[1].replace("\u021B1\u021B2","\u021B")
            word_copy[1] = word_copy[1].replace("\u021B1","\u021B")
            word_copy[1] = word_copy[1].replace("\u021B2","\u021B")
            word_copy[1] = word_copy[1].replace("\u0219.","\u0219")
            word_copy[1] = word_copy[1].replace("\u021b.","\u021b")
            word_copy[1] = word_copy[1].replace("\u00e2.","\u00e2")
            word_copy[1] = word_copy[1].replace("\u0103.","\u0103")
            word_copy[1] = word_copy[1].replace("\u00ee.","\u00ee")


        formatted_words.append(word_copy)

    return formatted_words

