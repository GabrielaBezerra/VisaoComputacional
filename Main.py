from __future__ import print_function
from Convolucao2D import *

print("Running...")


# CONSTANTES
image_path = "imgs/blox.jpg"
size_of_mask = 3


# AQUISICAO
img = imread(image_path)
mask = ones((size_of_mask, size_of_mask, 3))

# FILTRO DA MEDIA
# A mascara eh a mesma

# FITRO PREWIT
# Mascara pra analise das bordas Horizontais
for p in range(3):
  mask[0][0][p] = -1
  mask[0][1][p] = -1
  mask[0][2][p] = -1

  mask[1][0][p] = 0
  mask[1][1][p] = 0
  mask[1][2][p] = 0

  mask[2][0][p] = 1
  mask[2][1][p] = 1
  mask[2][2][p] = 1

# Mascara pra analise das bordas Verticais
for p in range(3):
  mask[0][0][p] = -1
  mask[0][1][p] =  0
  mask[0][2][p] =  1

  mask[1][0][p] = -1
  mask[1][1][p] =  0
  mask[1][2][p] =  1

  mask[2][0][p] = -1
  mask[2][1][p] =  0
  mask[2][2][p] =  1



# PREPROCESSAMENTO
result = convolucao2D(mask, image_path)


# EXIBIR RESULTADOS
if result is not None:
  imshow("result", result)
  waitKey(0)

