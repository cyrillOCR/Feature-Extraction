import base64
import numpy as np

# decodificam imaginea primita in baza 64 de la modulul Front-end
def decode(base64_string):
    imgdata= base64.b64decode(base64_string)
    return np.fromstring(imgdata,dtype=np.uint8)

