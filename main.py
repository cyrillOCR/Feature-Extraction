import sys

from flask import Flask, request, jsonify

from modules.dct.dct_for_each_letter import dct_means_for_each_letter_function
from modules.utils.Resize_optimizat_1 import crop
from modules.utils.json import make_json,coordSerialization
from modules.utils.base64 import decode

app = Flask(__name__)

@app.route('/feature',methods = ['POST','OPTIONS'])
def requests():
   
    received_json = request.json
    coords_from_json=received_json["coords"]
    base64_from_json=received_json["base64"]
    coordsList=coordSerialization(coords_from_json)
    result = dct_means_for_each_letter_function(crop(decode(base64_from_json), coordsList))
    return jsonify(make_json(result)), 200 , {
        'Acces-Control-Allow-Origin': '*',
        'Acces-Control-Allow-Headers': 'Content-Type',
        }


if __name__ == "__main__":
    app.run(host='0.0.0.0')