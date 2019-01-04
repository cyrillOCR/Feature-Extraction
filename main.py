import sys
import time

from flask import Flask

from modules.dct.dct_for_each_letter import dct_means_for_each_letter_function
from modules.utils.Resize import crop
from modules.utils.iterate_image import image_vector
from modules.utils.json import make_json

app = Flask(__name__)

@app.route('/',methods = ['POST'])
def requests():
    try:
        t = time.time()
        vectored_image = image_vector(sys.argv[1])
        page = sys.argv[1]
        file = sys.argv[2]
        f = open("test.txt", "w")
        result = dct_means_for_each_letter_function(crop(page, file))
        make_json(result)

        print(time.time() - t)
        print("Finished")

    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    app.run('0.0.0.0',port = 80,debug=True)