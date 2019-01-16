import math

import numpy as np


def dct_function(tiles):  # metoda primeste ca input matricile ce contin pixelii
    # fiecarei litere
    PI = 3.1415926535897
    matrix_result = np.zeros((8, 8))
    new_tiles = {}
    eight = 8

    # Matricea standard de cuantificare folosita pentru compresia imaginii (cuantificator jpeg)
    jpeg_quantizer = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                               [12, 12, 14, 19, 26, 58, 60, 55],
                               [14, 13, 16, 24, 40, 57, 69, 56],
                               [14, 17, 22, 29, 51, 87, 80, 62],
                               [18, 22, 37, 56, 68, 109, 103, 77],
                               [24, 35, 55, 64, 81, 104, 113, 92],
                               [49, 64, 78, 87, 103, 121, 120, 101],
                               [72, 92, 95, 98, 112, 100, 103, 99]
                               ])

    try:
        for tile in tiles:  # parcurgem fiecare matrice corespunzatoare unei litere
            for u in range(0, 8):  # aplicam dct pentru blocuri de pixeli de 8x8
                for v in range(0, 8):
                    sum = 0

                    # aplicam formula algoritmului dct pentru matricea de pixeli de 8x8
                    for x in range(0, 8):
                        for y in range(0, 8):
                            sum = sum + tiles[tile][x][y] * math.cos(((2.0 * x + 1) * u * PI) / 16.0) * \
                                  math.cos(((2.0 * y + 1) * v * PI) / 16.0)

                    if u == 0:
                        cu = 1 / math.sqrt(2)
                    else:
                        cu = 1

                    if v == 0:
                        cv = 1 / math.sqrt(2)
                    else:
                        cv = 1

                    # rezultatul in urma aplicarii algoritmului dct
                    matrix_result[u][v] = '{:8.1f}'.format(1 / 4.0 * cu * cv * sum)

                    # aplicam cuantifactorul jpeg pe matricea rezultata dupa aplicarea alg. dct
                    matrix_result[u][v] = round(matrix_result[u][v] / jpeg_quantizer[u][v])

                # toate valorile blocurilor matricilor de 8x8 dupa aplicarea alg. dct a unei litere
                # vor fi puse intr-o lista
                for i in range(0, 8):
                    for j in range(0, 8):
                        if not tile in new_tiles:
                            new_tiles[tile] = np.zeros((eight, eight))
                        else:
                            # vom pune lista finala intr-un dictionar
                            new_tiles[tile][(i)][j] = matrix_result[i][j]

    except Exception as e:
        print(str(e))

    return new_tiles
