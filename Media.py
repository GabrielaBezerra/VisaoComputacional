import numpy as np
import cv2 as cv

img = cv.imread("imgs/lena.jpg")
if img is None:
    print "Error reading image from specified directory"

cv.imshow("antes", img)


def convertToBlackAndWhite(img):
    data = np.array(img, dtype=int)
    print data.size

    list = data.tolist()
    for i, column in enumerate(list):
        # print "i:", i
        for j, row in enumerate(column):
            # print "j:", j
            for p, pixel in enumerate(row):
                # print "p:", pixel
                img[i][j][p] = img[i][j][1]


convertToBlackAndWhite(img)

cv.imshow("depois", img)
cv.waitKey(0)
