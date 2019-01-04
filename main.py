import sys
import time

from flask import Flask, request, jsonify

from modules.dct.dct_for_each_letter import dct_means_for_each_letter_function
from modules.utils.Resize import crop
from modules.utils.iterate_image import image_vector
from modules.utils.json import make_json
from modules.utils.coordSerialization import coordSerialization

app = Flask(__name__)

@app.route('/',methods = ['POST'])
def requests():
   
    coordsList = []
    # functie care transforma din base64 in imagine normala
    page = 'images/i5bw.jpg'
    coords_json = request.json
    
    # de schimbat aici cu scriptul de serializarea a coordonatelor care trebuie modificat
    for i in coords_json['coords']:
        coordsList.append(tuple(i))
    # am folosit scriptul 'Resize' trebuie copiat in alt script
    result = dct_means_for_each_letter_function(crop(page, coordsList))
    return jsonify(make_json(result)), 200


if __name__ == "__main__":
    app.run(port = 5005,debug=True)