from numpy import *
from cv2 import *



# AQUISICAO DA IMAGEM

img = imread("imgs/lena.jpg")
newImg = imread("imgs/lena.jpg")





# PRE-PROCESSAMENTO

SIZE_OF_MASK = 3
mask = ones((SIZE_OF_MASK, SIZE_OF_MASK, 3))
center_index_mask = int(mask.shape[0] / 2)

for x in range(img.shape[0]):

    for y in range(img.shape[1]):

        for p in range(3):

            # pixel access
            ac = 0

            for v1 in range(-center_index_mask, center_index_mask + 1, 1):

                for v2 in range(-center_index_mask, center_index_mask + 1, 1):

                    # cont += 1
                    # print cont
                    # print v1+cim, v2+cim

                    if x + v1 < 0 or y + v2 < 0 or x + v1 > img.shape[0] - 1 or y + v2 > img.shape[1] - 1:
                        ac += 1
                        # print "outbounds ", "p:", p," [x:",x,", y:",y,"]","* (",v1+cim,",",v2+cim,")   ", ac
                    else:
                        ac += (mask[center_index_mask + v1][center_index_mask + v2][p] * img[x + v1][y + v2][p])
                        # print "inbounds  ", "p:", p," [x:",x,", y:",y,"]","* (",v1+cim,",",v2+cim,")   ", ac


            newImg[x][y][p] = int(ac / (mask.shape[0] * mask.shape[1]))




# MOSTRA RESULTADO

imshow("result", newImg)
waitKey(0)