import sys
from flask import Flask, request, jsonify
from flask_cors import CORS
from modules.dct.dct_for_each_letter import dct_means_for_each_letter_function
from modules.utils.Resize_optimizat_1 import crop
from modules.utils.json import make_json, coordSerialization
from modules.utils.base64 import decode
from modules.predicted.predict import predict
from modules.text_reconstrucion.word_reconstruction import text_reconstruction
from modules.text_reconstrucion.replace_characters import replace_character, get_dictionary


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello():
    return "IT WORKS HERE AS WELL!"


dictionary_of_patterns = {}


@app.route('/feature', methods=['POST', 'OPTIONS'])
def requests():
    if request.method == 'OPTIONS':
        return ''
    # facem request modulului de front-end
    received_json = request.json
    # primim coordonatele literelor
    coords_from_json = received_json["coords"]
    # primim imaginea preprocesata
    base64_from_json = received_json["base64"]
    # facem serializarea coordonatelor din json
    coordslist = coordSerialization(coords_from_json)

    if len(coordslist) > 0:
        global dictionary_of_patterns
        # valorile in urma aplicarii dct-ului, cuantificarii si valorile mediilor
        result = dct_means_for_each_letter_function(crop(decode(base64_from_json), coordslist))
        # obtinem literele in alfabet latin
        predictedResult = predict(make_json(result))
        # aplicam reconstructia textului in urma obitnerii literelor latinesti
        reconstructed_text = text_reconstruction(coordslist, predictedResult)

        # rezultatul obtinut in urma reconstructiei textului va fi trimisa la modulul Front-End
        return jsonify(replace_character(reconstructed_text, dictionary_of_patterns)), 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
    else:
        return jsonify([]), 200, {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Headers': 'Content-Type',
        }


if __name__ == "__main__":
    dictionary_of_patterns = get_dictionary()
    app.run(host='0.0.0.0', port=5050, debug=True)
