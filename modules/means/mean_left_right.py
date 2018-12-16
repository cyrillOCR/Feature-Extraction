import cv2


def mean_left_right(image):
    newImage = image.copy()
    bw = cv2.cvtColor(newImage, cv2.COLOR_GRAY2RGB)
    left = 0
    right = 0
    up = 0
    down = 0
    for line in range(0, len(image)):
        for column in range(0, len(image[0])):
            if image[line][column] < 255:
                if column == 0 or image[line][column - 1] == 255:
                    # bw.itemset((line,column, 0), 0)
                    # #bw.itemset((line, column, 1), 0)
                    # bw.itemset((line, column, 2), 255)
                    left = left + 1
                if line == 0 or image[line - 1][column] == 255:
                    # bw.itemset((line,column, 0), 0)
                    # bw.itemset((line, column, 1), 0)
                    # #bw.itemset((line, column, 2), 122)
                    right = right + 1

                if line == len(image) - 1 or image[line + 1][column] == 255:
                    # bw.itemset((line,column, 0), 55)
                    # bw.itemset((line, column, 1), 42)
                    # bw.itemset((line, column, 2), 122)
                    up = up + 1

                if column == len(image[line]) - 1 or image[line][column + 1] == 255:
                    # bw.itemset((line,column, 0), 0)
                    # bw.itemset((line, column, 1), 41)
                    # bw.itemset((line, column, 2), 25)
                    down = down + 1
    s = up + down + left + right
    # cv2.imwrite("miruna.png", bw)

    if s == 0:
        if left == 0:
            return (0, 0, 0, 0)
        else:
            return (0, 0, 0, up / left)
    else:
        if left == 0:
            return (left / s, right / s, down / s, 0)
        else:
            return (left / s, right / s, down / s, up / left)
