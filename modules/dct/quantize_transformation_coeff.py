import numpy as np


def quantize_function(dct_tiles):
    quantize_tiles = {}

    jpeg_quantizer = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                               [12, 12, 14, 19, 26, 58, 60, 55],
                               [14, 13, 16, 24, 40, 57, 69, 56],
                               [14, 17, 22, 29, 51, 87, 80, 62],
                               [18, 22, 37, 56, 68, 109, 103, 77],
                               [24, 35, 55, 64, 81, 104, 113, 92],
                               [49, 64, 78, 87, 103, 121, 120, 101],
                               [72, 92, 95, 98, 112, 100, 103, 99]
                               ])
    matrix_result_quantize = np.zeros((8, 8))

    for tile in dct_tiles:
        for u in range(0, 8):
            for v in range(0, 8):
                result = round(dct_tiles[tile][u][v] / jpeg_quantizer[u][v])
                matrix_result_quantize[u][v] = result

        for i in range(0, 8):
            for j in range(0, 8):
                if not tile in quantize_tiles:
                    quantize_tiles[tile] = np.zeros((8, 8))
                    quantize_tiles[tile][i][j] = matrix_result_quantize[i][j]
                else:
                    quantize_tiles[tile][i][j] = matrix_result_quantize[i][j]

    return quantize_tiles
