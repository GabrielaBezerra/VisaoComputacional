import numpy as np
import cv2 as cv

if cv is None:
    print("Couldn't import opencv")

img1 = cv.imread("imgs/home_icon_10x10.png", 1)
if img1 is None:
    print("Problem reading image 1")

img2 = cv.imread("imgs/home_icon2_10x10.png", 1)
if img2 is None:
    print("Problem reading image 2")


# TODO: Ver como atribui cópia em python
# passando por referencia, as alterações estão sendo feitas na img1.
newImg = img1

cont = 0

# varre todos os pixels sem indexar com ndarray
# for shape in img1:
#     for pixel in shape:
#         for value in pixel:
#             cont += 1
#             print value

cv.imshow("antes 1", img1)
cv.imshow("antes 2", img2)

# converte ndarray pra lista
data1 = np.array(img1, dtype=int)
data2 = np.array(img2, dtype=int)
list1 = data1.tolist()
list2 = data2.tolist()

# varre todos os pixels indexando com uma lista
for i, column in enumerate(list1):
    for j, row in enumerate(column):
        for p, pixel in enumerate(row):
            cont += 1
            newImg[i][j][p] = list1[i][j][p] + list2[i][j][p]

print ""
print cont

cv.imshow("depois", newImg)
cv.waitKey(0)