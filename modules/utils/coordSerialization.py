import json
def coordSerialization(jsonPath):
    coordList=[]
    with open(jsonPath) as f:
        data = json.load(f)
    for i in data['coords']:
        coordList.append(tuple(i))
    return  coordList
#coordSerialization("coord3.json")

