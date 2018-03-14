import numpy as np
import cv2 as cv

img = cv.imread("imgs/lena.jpg")
if img is None:
    print "Error reading image from specified directory"

cv.imshow("antes", img)

data = np.array(img, dtype=int)

print data.size

list = data.tolist()

newImg = []

for i, column in enumerate(list):
    print "i:", i
    for j, row in enumerate(column):
        print "j:", j
        pb = 0
        for p, pixel in enumerate(row):
            print "p:", pixel
            pb += pixel

        pb = pb/3
        if pb > 255 :
            print "overpixeled"
        newImg.append(pb)

imgPB = np.zeros([data.shape[0],data.shape[1],1], dtype=int)

for p,  in imgPB :
        p = e

cv.imshow("depois",imgPB)

cv.waitKey(0)