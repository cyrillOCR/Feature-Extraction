import numpy as np


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
