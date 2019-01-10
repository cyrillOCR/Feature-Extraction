import json
#add to main
#from modules.utils.deserialization import make_json
#from modules.utils.deserialization import serialize_json


class Letter(object):
    def __init__(self, j):
        self.dct_means = j


#this function shall be called using dct_means_for_each_letter_function(crop(page, file)) as parameter
#if data doesn't look ok in the .json file, press enter at the end of a tuple and then ctrl+Z
def make_json(list):
    data = {}
    j=0
    #add all the tuples to data
    for letter in list:
            data[j]=letter
            j=j+1
    #make .json
    return data

#this is how you print json.loads data
def print_json(python_data):
    for i in python_data.keys():
        print(i," : ", python_data[i],'\n')


def serialize_json():
    data={}
    with open('modules/utils/data.json', 'r') as outfile:
        response=outfile.read()
    data=json.loads(response)
    #print_json(data)
    list_of_letters=[]
    for key in data.keys():
        letter=Letter(data[key])
        list_of_letters.append(letter)
    #the value can be accessed as you can see below
    #for i in list_of_letters:
    #    print(i.dct_means)
    return list_of_letters

def coordSerialization(dict_coords):
    coordList=[]
    for i in dict_coords:
        coordList.append(tuple(i))
    return  coordList

