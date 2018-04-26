





[1][1][1]
[1][1][1]
[1][1][1] 3x3 -> 1  
		center    = image[i][j][p]
len - len - 1   down      = image[i][j + 1][p]      if j < len(list)-1                       else 0
                right     = image[i + 1][j][p]      if i < len(list)-1                       else 0
                left      = image[i - 1][j][p]      if i > 0                                 else 0
                up        = image[i][j - 1][p]      if j > 0                                 else 0
                upleft    = image[i - 1][j - 1][p]  if (i > 0 and j > 0)                     else 0
                upright   = image[i + 1][j - 1][p]  if (i < len(list)-1 and j > 0)           else 0
                downleft  = image[i - 1][j + 1][p]  if (i > 0 and j < len(list)-1)           else 0
                downright = image[i + 1][j + 1][p]  if (i < len(list)-1 and j < len(list)-1) else 0



                       [][][][][][][]
                       [][][][][][][]
[][][][][]             [][][][][][][]
[][][][][]             [][][][][][][]
[][][][][]             [][][][][][][]
[][][][][]             [][][][][][][]
[][][][][] 5x5 -> 2    [][][][][][][] 7x7 -> 3    
		center    = image[i][j][p]
len - len - 1   down      = image[i][j + 1][p]      if j < len(list)-1                       else 0
 5     4        right     = image[i + 1][j][p]      if i < len(list)-1                       else 0
 wrong btch X   left      = image[i - 1][j][p]      if i > 0                                 else 0
                up        = image[i][j - 1][p]      if j > 0                                 else 0
                upleft    = image[i - 1][j - 1][p]  if (i > 0 and j > 0)                     else 0
                upright   = image[i + 1][j - 1][p]  if (i < len(list)-1 and j > 0)           else 0
                downleft  = image[i - 1][j + 1][p]  if (i > 0 and j < len(list)-1)           else 0
                downright = image[i + 1][j + 1][p]  if (i < len(list)-1 and j < len(list)-1) else 0

# SOLUÇÃO BTCH
index_centro = len(linha)/2 		-> arredonda pra baixo
mask[index_centro][index_centro] 	-> centro da mask que será alinhado com cada pixel da imagem.
mask[index_centro + 1][index_centro]
mask[index_centro + 2][index_centro]    -? Talvez dê pra usar um count pra linhas cl, e um count pra colunas cc.

# center_index_mask
cim = int(len(mask.shape[0])/2) arrendondada pra baixo
ac = 0

# for w in range(len(mask.shape[0])):

#  for h in range(len(mask.shape[1])):  -? Will i really need those 2 first loops? Maybe no because of the sum loops.

    for x in range(len(img.shape[0])): 

      for y in range (len(img.shape[1])):

        for p in range (3):
          
          # pixel access

          for v1 in range(-cim, cim):  

            for v2 in range(-cim, cim):

              if x+v1 < 0 || y+v2 < 0 || x+v1 > len(img.shape[0])-1 || y+v2 > len(img.shape[1])-1 : 
                ac += 1
              else:
                ac += (mask[cim+v1][cim+v2][p] * img[x+v1][y+v2][p]) / len(mask.shape[0]) 

#27 vezes - mascara 3x3
nbounds,   173.0  [x: 9 , y: 9 ]  * ( 0 , 0 ) 
inbounds,   428.0  [x: 9 , y: 9 ]  * ( 0 , 1 ) 
outbounds,  429.0  [x: 9 , y: 9 ]  * ( 0 , 2 ) 
inbounds,   602.0  [x: 9 , y: 9 ]  * ( 1 , 0 ) 
inbounds,   857.0  [x: 9 , y: 9 ]  * ( 1 , 1 ) 
outbounds,  858.0  [x: 9 , y: 9 ]  * ( 1 , 2 ) 
outbounds,  859.0  [x: 9 , y: 9 ]  * ( 2 , 0 ) 
outbounds,  860.0  [x: 9 , y: 9 ]  * ( 2 , 1 ) 
outbounds,  861.0  [x: 9 , y: 9 ]  * ( 2 , 2 ) 
inbounds,   173.0  [x: 9 , y: 9 ]  * ( 0 , 0 ) 
inbounds,   428.0  [x: 9 , y: 9 ]  * ( 0 , 1 ) 
outbounds,  429.0  [x: 9 , y: 9 ]  * ( 0 , 2 ) 
inbounds,   602.0  [x: 9 , y: 9 ]  * ( 1 , 0 ) 
inbounds,   857.0  [x: 9 , y: 9 ]  * ( 1 , 1 ) 
outbounds,  858.0  [x: 9 , y: 9 ]  * ( 1 , 2 ) 
outbounds,  859.0  [x: 9 , y: 9 ]  * ( 2 , 0 ) 
outbounds,  860.0  [x: 9 , y: 9 ]  * ( 2 , 1 ) 
outbounds,  861.0  [x: 9 , y: 9 ]  * ( 2 , 2 ) 
inbounds,   173.0  [x: 9 , y: 9 ]  * ( 0 , 0 ) 
inbounds,   428.0  [x: 9 , y: 9 ]  * ( 0 , 1 ) 
outbounds,  429.0  [x: 9 , y: 9 ]  * ( 0 , 2 ) 
inbounds,   602.0  [x: 9 , y: 9 ]  * ( 1 , 0 ) 
inbounds,   857.0  [x: 9 , y: 9 ]  * ( 1 , 1 ) 
outbounds,  858.0  [x: 9 , y: 9 ]  * ( 1 , 2 ) 
outbounds,  859.0  [x: 9 , y: 9 ]  * ( 2 , 0 ) 
outbounds,  860.0  [x: 9 , y: 9 ]  * ( 2 , 1 ) 
outbounds,  861.0  [x: 9 , y: 9 ]  * ( 2 , 2 








