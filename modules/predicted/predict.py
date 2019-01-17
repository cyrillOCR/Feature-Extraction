import collections
import numpy as np
import keras
import os
from keras import backend as K


# transforma o lista continand mai multe liste de numere intr-o singura doar cu numere
def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]

# creez un dictionar in care asignez fiecarui caracter posibil cate un id numeric
def create_label_mapping():
    f = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'labelsset.txt'), "r", encoding="utf-8")
    labels_set = []
    for line in f:
        line = line.replace("\n", "")
        labels_set.append(line)
    f.close()

    labels_mapping = dict()
    for index, label in enumerate(labels_set):
        labels_mapping[index] = label
    return labels_mapping


def predict(feature_dictionary):
    # creez asocierea id numeric - label
    labels_mapping = create_label_mapping()
    features = []
    # folosesc flatten pentru a obtine o lista simpla pentru fiecare caracter
    for nested_lists in feature_dictionary.values():
        flat_list = flatten(nested_lists)
        features.append(flat_list)
    # transform lista de trasaturi intr-un array numpy
    features = np.array(features)
    # normalizez trasaturile aducandu-le la intervalul [-1,1]
    features = features / 128
    x_test = features
    # incarc modelul deja antrenat
    model = keras.models.load_model(os.path.join(os.path.dirname(os.path.abspath(__file__)),'saved_model.h5'))
    # prezic cate o clasa pentru fiecare caracter
    predictions = model.predict_classes(x_test)
    # curat sesiunea pentru a evita probleme cauzate de multithreading
    K.clear_session()
    # mapez id-ul numeric al fiecarei categorii la caracterul latin careia ii corespunde
    predictions = [labels_mapping[index] for index in predictions]
    return predictions
