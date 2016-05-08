''' Solving at time = 1
    Hence all the terms in K(implying time = 0) are 0 hence ignored
    This code generates the temperature distributon of the mesh for 5 layers namely -
    Fluid B, Wall 1, Wall 2, Fluid A and Fluid C
    at k=0 (or time =1)'''

def image_point(i,j,sizeX, sizeY):
  incX,incY,decX,decY = i+1,j+1,i-1,j-1

  if i == 0:
    decX = i+1
  elif i == sizeX:
    incX = i-1

  if j == 0:
    decY = j+1
  elif j == sizeY:
    incY = j-1

  return [incX,incY,decX,decY]

from initialize import *

# Constants for Fluid B
b1 = Vb/deltaTheta + 1/(2*phi) + 1/(2*(1-phi)) + 1/(deltaX) + (2*Na)/(Peb*deltaX*deltaX) 
ktb1 = Vb/(deltaTheta*b1)
ktb2 = 1/(phi*b1)
ktb3 = 1/((1-phi)*b1)
ktb4 = -1/(deltaX*b1)
ktb5 = Na/(Peb*deltaX*deltaX*b1)

# Constants for Wall 1
W1 = Si/deltaTheta + 1/phi + Rab + (2*lamdaX*Na)/(deltaX*deltaX) + (2*lamdaY*Na)/(deltaY*deltaY) 
ktw11 = Si/(deltaTheta*W1)    # Ignored as of now
ktw12 = Rab/(2*W1)
ktw13 = 1/(2*phi*W1)
ktw14 = lamdaX*Na/(deltaX*deltaX*W1)
ktw15 = lamdaY*Na/(deltaY*deltaY*W1)

# Constants for Wall 2
W2 = (1-Si)/deltaTheta + 1/(1-phi) + Rcb + 2*lamdaX*Na/(deltaX*deltaX) + 2*lamdaY*Na/(deltaY*deltaY) 
ktw21 = (1-Si)/(deltaTheta*W2) # Ignored
ktw22 = 1/(2*(1-phi)*W2)
ktw23 = Rcb/2*W2
ktw24 = (1/(1-phi) + Rcb)/W2
ktw25 = 2*lamdaX*Na/(deltaX*deltaX*W2)
ktw26 = 2*lamdaY*Na/(deltaY*deltaY*W2)

# Costants for Fluid A
a1 = Va/(Rab*deltaTheta) + 0.5 + Eab/(Rab*deltaY) + 2*Na*Eab/(Pea*deltaY*deltaY*Rab) 
kta1 = Va/(Rab*deltaTheta*a1)    # Ignored at time zero (k=0)
kta2 = 1/a1
kta3 = (Eab/(Rab*deltaY) - 0.5)/a1
kta4 = Na*Eab/(Pea*deltaY*deltaY*Rab*a1)

# Consants for Fluid C    (Moving in X-direction in a rightward direction)
c1 = Vc/(Rcb*deltaTheta) + 0.5 + Ecb/(Rcb*deltaX) + 2*Na/(Pec*deltaX*deltaX) 
ktc1 = Vc/(Rcb*deltaTheta*c1)       # Ignored at time zero (k=0)
ktc2 = 1/c1
ktc3 = (Ecb/(Rcb*deltaX) - 0.5)/a1
ktc4 = (Na/(Pec*deltaX*deltaX))/c1

print 'Calculated constants'
error = 0.005
checker = []
for _ in range(countY):
  checker.append([False]*countX)
#import pdb;pdb.set_trace()

def reset():
  for i in range(0,countX):
    for j in range(0,countY):
      checker[i][j] = False

def gauss_siedel(num, arr):
  count,test = 0,0
  startX, startY, endX, endY = 0,0,countX,countY
  count_checker = count_checker_all
  if num == 1 or num == 5:
    startX, startY, endY = 1,1, countY-1
    count_checker = count_checker_B

  if num == 4:
    startX,startY,endX = 1,1,countX-1
    count_checker = count_checker_A


  while count<count_checker:
    for i in range(startX,endX):
      for j in range(startY,endY):
        if not checker[i][j]:
          print count
          print i,j
#          if i == 8 and j == 8:
#            import pdb;pdb.set_trace()
          res = image_point(i,j,countX-1,countY-1)
          incX,incY,decX,decY = res[0],res[1],res[2],res[3]
          if num == 1:
            val = ktb2*(tempW1[i,j] + tempB[decX,j]) + ktb3*(tempW2[i,j] + tempB[decX,j]) + ktb4*(tempB[decX,j]) + ktb5*(tempB[incX,j]+tempB[decX,j])
          elif num == 2:
            val = ktw12*(tempA[i,j] + tempA[i,decY]) + ktw13*(tempB[i,j] + tempB[decX,j]) + ktw14*(tempW1[incX,j] + tempW1[decX,j]) + ktw15*(tempW1[i,decY] + tempW1[i,incY])
          elif num == 3:
            val = ktw22*(tempB[i,j] + tempB[decX,j]) + ktw23*(tempC[i,j] + tempC[i,decY]) + ktw25*(tempW2[incX,j] + tempW2[decX,j]) + ktw26*(tempW2[i,decY] + tempW2[i,incY])
          elif num == 4:
            val = kta2*tempW1[i,j] + kta3*tempA[i,decY] + kta4*(tempA[i,incY] + tempA[i,decY])
          elif num == 5:
            val = ktc2*tempW2[i,j] + ktc3*tempC[decX,j] + ktc4*(tempC[incX,j] + tempC[decX,j])

          if abs(val-arr[i,j])>error:
            arr[i,j] = val
            test = 1
          else:
            checker[i][j] = True
            count+=1

  print arr,num
#  import pdb;pdb.set_trace()
  reset() 
  if test:
    return True
  return False


seq = [(2,tempW1),(3,tempW2),(1,tempB),(4,tempA),(5,tempC)]
counter = 0
while seq:
#  import pdb;pdb.set_trace()
  pai = seq.pop(0)
  counter+=1
  if gauss_siedel(pai[0], pai[1]):
    seq.append(pai)

import pdb;pdb.set_trace()
print 'FINAL VALUE\n'
print 'Temperature of Fluid B'
print tempB
print 'Temperature of Wall 1'
print tempW1
print 'Temperature of Wall 2'
print tempW2
print 'Temperature of Fluid A'
print tempA
print 'Temperature of Fluid C'
print tempC
