from numpy import *
from cv2 import *


def convolucao2D(mask, imgPath, img=None):

  if img is None:
    img = imread(imgPath)

  newimg = imread(imgPath)

  if mask.shape[0]%2 == 0:
    print "\n# ERROR: MASK SHAPE IS EVEN! \n  SIZE OF MASK:", mask.shape[0], "\n  SIZE OF IMAGE:", img.shape[0]
    return

  if mask.shape[0] > img.shape[0]:
    print "\n# ERROR: MASK IS TOO BIG! \n  SIZE OF MASK:", mask.shape[0], "\n  SIZE OF IMAGE:", img.shape[0]
    return

  center_index_mask = int(mask.shape[0] / 2)

  for x in range(img.shape[0]):

    for y in range(img.shape[1]):

      for p in range(3):

        # pixel access
        ac = 0

        for v1 in range(-center_index_mask, center_index_mask + 1, 1):

          for v2 in range(-center_index_mask, center_index_mask + 1, 1):

            if x + v1 < 0 or y + v2 < 0 or x + v1 > img.shape[0] - 1 or y + v2 > img.shape[1] - 1:
              ac += int(mask[v1][v2][p])
              # print "outbounds ", "p:", p," [x:",x,", y:",y,"]","* (",v1+center_index_mask,",",v2+center_index_mask,")   ", ac
            else:
              ac += (mask[center_index_mask + v1][center_index_mask + v2][p] * img[x + v1][y + v2][p])
              # print "inbounds  ", "p:", p," [x:",x,", y:",y,"]","* (",v1+center_index_mask,",",v2+center_index_mask,")   ", ac

          newimg[x][y][p] = int(ac / (mask.shape[0]*mask.shape[1]))

  return newimg






# Main

image_path = "imgs/blox.jpg"
size_of_mask = 3

img = imread(image_path)
mask = ones((size_of_mask, size_of_mask, 3))

result = convolucao2D(mask, image_path)

if result is not None:
  imshow("result", result)
  waitKey(0)