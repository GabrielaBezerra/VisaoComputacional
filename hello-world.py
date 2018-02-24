from __future__ import print_function
import sys

import cv2 as cv

if cv is None:
  print("no cv shit")

img = cv.imread("../../opencv-3.4.0/samples/data/home.jpg",1)
if img is None :
  print("Problem reading image")
cv.imshow("img",img)
cv.waitKey(0)