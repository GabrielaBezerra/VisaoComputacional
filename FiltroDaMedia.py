from cv2 import *
from numpy import *

img = imread("imgs/lena.jpg")
if img is None:
    print "Error reading image from specified directory"

# convertToBlackAndWhite(img)

imshow("antes", img)

newImg = imread("imgs/lena.jpg")

# convertToBlackAndWhite(newImg)

data = array(img, dtype=int)
print data.size

cont = 0

list = data.tolist()

# for i, column in enumerate(list):
#     # print "i:", i
#     for j, row in enumerate(column):
#         # print "j:", j
#         for p, pixel in enumerate(row):
#             # print "p:", pixel
#             cont += 1
#             value = 0
#             if j < len(list)-1 and i < len(list)-1:
#                 value = (img[i][j][1] + img[i][j+1][1] + img[i+1][j][1] + img[i+1][j+1][1] + img[i-1][j][1] + img[i][j-1][1] + img[i-1][j-1][1] + img[i+1][j-1][1] + img[i-1][j+1][1])/9
#                 print value
#             print "cont", cont
#             newImg[i][j][p] = value

kernel = ones((3,3))

print kernel

def filtroDaMedia(image, kernel):
    m, n = kernel.shape
    y,x,z = image.shape

    for i in range(y):
        flag = 0
        for j in range(x):

            acc = 0

            for a in range(m):
                for b in range(n):
                    if flag == 0:
                        flag == 1
                        print a, b, i, j, 1

def convolution2d(image, kernel, bias):
    m, n = kernel.shape
    if (m == n):
        y, x, z = image.shape
        y = y - m + 1
        x = x - m + 1
        new_image = zeros((y,x,z))
        for i in range(y):
            for j in range(x):
                for p in range(z):
                    new_image[i][j][p] = sum(image[i:i+m, j:j+m, 1]/95) + bias

    return new_image

filtroDaMedia(img, kernel)
# newImg = convolution2d(img, kernel, 0)
# imshow("Filtro da Media", newImg)
waitKey(0)