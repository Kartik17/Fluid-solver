''' Solving at time = 0'''


from initialize import *

# Constants for Fluid B
b1 = Vb/deltaTheta + 1/(2*phi) + 1/(2*(1-phi)) + 1/(deltaX) + 2*Na/(Peb*deltaX*deltaX)
ktb1 = 1/(phi*b1)
ktb2 = 1/((1-phi)*b1)
ktb3 = -1/(deltaX*b1)
ktb4 = Na/(Peb*deltaX*deltaX*b1)

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
            val = ktb1*(tempW1[i,j] + tempB[i-1,j]) + ktb2*(tempW2[i,j] + tempB[i-1,j]) + ktb3*(tempB[i-1,j]) + ktb4*(tempB[i+1,j]+tempB[i-1,j])
          elif num == 2:
            val = ktw12*(tempA[i,j] + tempA[i,j-1]) + ktw13*(tempB[i,j] + tempB[i-1,j]) + ktw14*(tempW1[i+1,j] + tempW1[i-1,j]) + ktw15*(tempW1[i,j-1] + tempW1[i,j+1])
          elif num == 3:
            val = ktw22*(tempB[i,j] + tempB[i-1,j]) + ktw23*(tempC[i,j] + tempC[i,j-1]) + ktw25*(tempW2[i+1,j] + tempW2[i-1,j]) + ktw26*(tempW2[i,j-1] + tempW2[i,j+1])
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


#eqnB = ktb1*(tempW1[i,j] + tempB[i-1,j]) + ktb2*(tempW2[i,j] + tempB[i-1,j]) + ktb3*(tempB[i-1,j]) + ktb4*(tempB[i+1,j]+tempB[i-1,j])
#eqnW1 = ktw2*(tempA[i,j] + tempA[i,j-1]) + ktw3*(tempB[i,j] + tempB[i-1,j]) + ktw4*(tempW1[i+1,j] + tempW1[i-1,j]) + ktw5*(tempW1[i,j-1] + tempW1[i,j+1])

seq = [(1, tempB),(2, tempW1),(3,tempW2)]
counter = 0
while seq:
  pai = seq.pop(0)
  counter+=1
  print counter
  if gauss_siedel(pai[0], pai[1]):
    seq.append(pai)

print 'FINAL VALUE\n'
print tempB
print 'Temperature of Wall 1'
print tempW1
print 'Temperature of Wall 2'
print tempW2
