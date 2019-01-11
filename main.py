import sys

from flask import Flask, request, jsonify

from modules.dct.dct_for_each_letter import dct_means_for_each_letter_function
from modules.utils.Resize_optimizat_1 import crop
from modules.utils.json import make_json,coordSerialization
from modules.utils.base64 import decode
from modules.predicted.predict import predict
import json

app = Flask(__name__)

@app.route('/',methods=['POST'])
def requests():
    received_json = request.json
    coords_from_json=received_json["coords"]
    base64_from_json=received_json["base64"]
    coordslist=coordSerialization(coords_from_json)
    result = dct_means_for_each_letter_function(crop(decode(base64_from_json), coordslist))
    print(make_json(result))
    predictedResult = predict(make_json(result))
    #puts the predicted result in a json file
    with open('modules/predicted/predictedResult.json','w') as outfile:
        json.dump(predictedResult,outfile)
    return jsonify(make_json(result)), 200 


if __name__ == "__main__":
    app.run(port=5005,debug=True)