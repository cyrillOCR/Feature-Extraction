import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
from modules.dct.dct_for_each_letter import dct_means_for_each_letter_function
from modules.utils.Resize_optimizat_1 import crop
from modules.utils.json import make_json,coordSerialization
from modules.utils.base64 import decode
from modules.predicted.predict import predict

app = Flask(__name__)
CORS(app)
@app.route('/feature',methods=['POST','OPTIONS'])
def requests():
    received_json = request.json
    coords_from_json=received_json["coords"]
    base64_from_json=received_json["base64"]
    coordslist=coordSerialization(coords_from_json)
    
    if len(coordslist) > 0:

        result = dct_means_for_each_letter_function(crop(decode(base64_from_json), coordslist))
        predictedResult = predict(make_json(result))
        return jsonify(predictedResult), 200 , {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            }
    else:
        return jsonify({"Bad_Image":""}), 200 , {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
            }


if __name__ == "__main__":
     app.run(host='0.0.0.0', port=5050, debug=True)
