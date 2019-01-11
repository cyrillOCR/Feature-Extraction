import json
import collections
import numpy as np
import keras


def flatten(x):
    if isinstance(x, collections.Iterable):
        return [a for i in x for a in flatten(i)]
    else:
        return [x]


def create_label_mapping():
    f = open("modules/predicted/labelsset.txt", "r", encoding="utf-8")
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
    labels_mapping = create_label_mapping()
    features = []
    for nested_lists in feature_dictionary.values():
        flat_list = flatten(nested_lists)
        features.append(flat_list)
    features = np.array(features)
    features = features / 128
    x_test = features
    model = keras.models.load_model("modules/predicted/saved_model.h5")
    predictions = model.predict_classes(x_test)
    predictions = [labels_mapping[index] for index in predictions]
    return predictions
