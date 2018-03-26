from cv2 import *
from numpy import *

img = imread("imgs/lena.jpg")
if img is None:
    print "Error reading image from specified directory"

# convertToBlackAndWhite(img)

imshow("antes", img)

newImg = imread("imgs/lena.jpg")

# convertToBlackAndWhite(newImg)

data = array(img, dtype=uint8)
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
    x,y,z = image.shape

# Percurring every pixel on Picture
    for i in range(x):
        for j in range(y):
            for p in range(z):
                center    = image[i][j][p]
                down      = image[i][j + 1][p]      if j < len(list)-1                       else 0
                right     = image[i + 1][j][p]      if i < len(list)-1                       else 0
                left      = image[i - 1][j][p]      if i > 0                                 else 0
                up        = image[i][j - 1][p]      if j > 0                                 else 0
                upleft    = image[i - 1][j - 1][p]  if (i > 0 and j > 0)                     else 0
                upright   = image[i + 1][j - 1][p]  if (i < len(list)-1 and j > 0)           else 0
                downleft  = image[i - 1][j + 1][p]  if (i > 0 and j < len(list)-1)           else 0
                downright = image[i + 1][j + 1][p]  if (i < len(list)-1 and j < len(list)-1) else 0

                value = (int(center) + int(down) + int(right) + int(left) + int(up) + int(upleft) + int(upright) + int(downleft) + int(downright))/9
                newImg[i][j][p] = value


        # Percurring every pixel on Masknt(
            # for a in range(m):0
            #     for b in range(n):
            #

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
for i in range(25):
    print "Filtro #", i
    filtroDaMedia(newImg, kernel)
# newImg = convolution2d(img, kernel, 0)
imshow("Filtro da Media", newImg)
waitKey(0)