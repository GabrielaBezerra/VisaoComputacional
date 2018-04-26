from numpy import *
from cv2 import *

img = imread('imgs/coins.png')
gray = cvtColor(img,COLOR_BGR2GRAY)
ret, thresh = threshold(gray,0,255,THRESH_BINARY_INV+THRESH_OTSU)

imshow('coins.png',img)

# noise removal
kernel = ones((3,3),uint8)
opening = morphologyEx(thresh,MORPH_OPEN,kernel, iterations = 2)

# sure background area
sure_bg = dilate(opening,kernel,iterations=3)

# Finding sure foreground area
dist_transform = distanceTransform(opening,DIST_L2,5)
ret, sure_fg = threshold(dist_transform,0.7*dist_transform.max(),255,0)

# Finding unknown region
sure_fg = uint8(sure_fg)
unknown = subtract(sure_bg,sure_fg)

# Marker labelling
ret, markers = connectedComponents(sure_fg)

# Add one to all labels so that sure background is not 0, but 1
markers = markers+1

# Now, mark the region of unknown with zero
markers[unknown==255] = 0

markers = watershed(img,markers)
img[markers == -1] = [255,0,0]

imshow("Deteccao de bordas com o Watershed",img)
waitKey(0)
