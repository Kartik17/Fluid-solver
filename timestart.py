''' Solving at time = 1
    Hence all the terms in K(implying time = 0) are 0 hence ignored
    This code generates the temperature distributon of the mesh for 5 layers namely -
    Fluid B, Wall 1, Wall 2, Fluid A and Fluid C
    at k=0 (or time =1)'''


from initialize import *

# Constants for Fluid B
b1 = Vb/deltaTheta + 1/(2*phi) + 1/(2*(1-phi)) + 1/(deltaX) + 2*Na/(Peb*deltaX*deltaX)
ktb1 = Vb/(deltaTheta*b1)
ktb2 = 1/(phi*b1)
ktb3 = 1/((1-phi)*b1)
ktb4 = -1/(deltaX*b1)
ktb5 = Na/(Peb*deltaX*deltaX*b1)

# Constants for Wall 1
W1 = Si/deltaTheta + 1/Si + Rab + 2*lamdaX*Na/(deltaX*deltaX) + 2*lamdaY*Na/(deltaY*deltaY)
ktw11 = Si/(deltaTheta*W1)    # Ignored as of now
ktw12 = Rab/(2*W1)
ktw13 = 1/(2*phi*W1)
ktw14 = lamdaX*Na/(deltaX*deltaX*W1)
ktw15 = lamdaY*Na/(deltaY*deltaY*W1)

# Constants for Wall 2
W2 = (1-Si)/deltaTheta + 1/(1-phi) + Rcb + 2*lamdaX*Na/(deltaX*deltaX) + 2*lamdaY*Na/(deltaY*deltaY)
ktw21 = 11 # Ignored
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
ktc4 = Na/(Pec*deltaX*deltaX)/c1

import pdb;pdb.set_trace()

print 'Calculated constants'
error = 0.005
checker = []
for _ in range(sizeY):
  checker.append([False]*sizeX)

def reset():
  for i in range(1,sizeX-1):
    for j in range(1,sizeY-1):
      checker[i][j] = False

def gauss_siedel(num, arr):
  count,test = 0,0
  while count<4:
    for i in range(1,sizeX-1):
      for j in range(1,sizeY-1):
#      import pdb;pdb.set_trace()
        if not checker[i][j]:
          if num == 1:
            val = ktb2*(tempW1[i,j] + tempB[i-1,j]) + ktb3*(tempW2[i,j] + tempB[i-1,j]) + ktb4*(tempB[i-1,j]) + ktb5*(tempB[i+1,j]+tempB[i-1,j])
          elif num == 2:
            val = ktw12*(tempA[i,j] + tempA[i,j-1]) + ktw13*(tempB[i,j] + tempB[i-1,j]) + ktw14*(tempW1[i+1,j] + tempW1[i-1,j]) + ktw15*(tempW1[i,j-1] + tempW1[i,j+1])
          elif num == 3:
            val = ktw22*(tempB[i,j] + tempB[i-1,j]) + ktw23*(tempC[i,j] + tempC[i,j-1]) + ktw25*(tempW2[i+1,j] + tempW2[i-1,j]) + ktw26*(tempW2[i,j-1] + tempW2[i,j+1])
          elif num == 4:
            val = kta2*tempW1[i,j] + kta3*tempA[i,j-1] + kta4*(tempA[i,j+1] + tempA[i,j-1])
          elif num == 5:
            val = ktc2*tempW2[i,j] + ktc3*tempC[i-1,j] + ktc4*(tempC[i+1,j] + tempC[i-1,j])

          if abs(val-arr[i,j])>error:
            arr[i,j] = val
            test = 1
          else:
            checker[i][j] = True
            count+=1

  reset()
  print arr,num
  if test:
    return True
  return False


seq = [(1,tempB),(2,tempW1),(3,tempW2),(4,tempA),(5,tempC)]
counter = 0
while seq:
  pai = seq.pop(0)
  counter+=1
  print counter
  if gauss_siedel(pai[0], pai[1]):
    seq.append(pai)

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
