import numpy as np


# facem un resize pentru fiecare litera inainte de a aplica dct
# avem nevoie de blocuri de 8x8 si in cazul in care nu avem un
# numar fix de blocuri, vom aduga matricii valori de 0 pana vom ajunge la dimensiunea dorita
def resize(image):
    height, width = image.shape
    eight = 8
    tiles = {}

    try:
        for y in range(height):
            for x in range(width):
                current_tile = (x // eight, y // eight)
                if not current_tile in tiles:
                    tiles[current_tile] = np.zeros((eight, eight))
                tiles[current_tile][(y % eight)][x % eight] = image[y][x]

    except Exception as e:
        print(str(e))

    return tiles
