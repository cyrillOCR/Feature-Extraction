import sys
from modules.iterate_image import image_vector
from modules.quadrans import quadrans_sum

if __name__ == "__main__":
    try:
        print ("Main function")

        img = image_vector(sys.argv[1])
        dictionary = {}
        dictionary['quadrans_sum'] = quadrans_sum(img)
        print (dictionary)

    except:
        pass


