import math

import numpy as np

def dct_function(tiles):
    PI = 3.1415926535897
    matrix_result = np.zeros((8, 8))
    new_tiles = {}
    eight = 8

    try:
        for tile in tiles:
            for u in range(0, 8):
                for v in range(0, 8):
                    sum = 0

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

                    matrix_result[u][v] = 1 / 4.0 * cu * cv * sum

                for i in range(0, 8):
                    for j in range(0, 8):
                        if not tile in new_tiles:
                            new_tiles[tile] = np.zeros((eight, eight))
                        else:
                            new_tiles[tile][(i)][j] = '{:8.1f}'.format(matrix_result[i][j])

    except Exception as e:
        print(str(e))

    return new_tiles
