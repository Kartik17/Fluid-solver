''' Solving at time = 1
    Hence all the terms in K(implying time = 0) are 0 hence ignored
    This code generates the temperature distributon of the mesh for 5 layers namely -
    Fluid B, Wall 1, Wall 2, Fluid A and Fluid C
    at k=0 (or time =1)'''

def image_point(i,j,sizeX, sizeY):
  incX,incY,decX,decY = j+1,i+1,j-1,i-1

  if j == 1:
    decX = j+1
  elif j == sizeX:
    incX = j-1

  if i == 1:
    decY = i+1
  elif i == sizeY:
    incY = i-1

  return [incX,incY,decX,decY]

def boundary(i,j,arr):
	if i == countY:
		return i-1
	else:
		return i+1

def boundaryB(i,j,arr):
	if j == countX:
		return j-1
	else:
		return j+1

from initialize import *

# Constants for Fluid B
b1 = Vb/deltaTheta + 1/(2*phi) + 1/(2*(1-phi)) + 1/(deltaX) + 2*Na/(Peb*deltaX*deltaX)
ktb1 = Vb/(deltaTheta*b1)
ktb2 = 1/(phi*b1)
ktb3 = 1/((1-phi)*b1)
ktb4 = -1/(deltaX*b1)
ktb5 = Na/(Peb*deltaX*deltaX*b1)

# Constants for Wall 1
W1 = Si/deltaTheta + 1/phi + Rab + 2*lamdaX*Na/(deltaX*deltaX) + 2*lamdaY*Na/(deltaY*deltaY)
ktw11 = Si/(deltaTheta*W1)    # Ignored as of now
ktw12 = Rab/(2*W1)
ktw13 = 1/(2*phi*W1)
ktw14 = lamdaX*Na/(deltaX*deltaX*W1)
ktw15 = lamdaY*Na/(deltaY*deltaY*W1)

# Constants for Wall 2
W2 = (1-Si)/deltaTheta + 1/(1-phi) + Rcb + (2*lamdaX*Na)/(deltaX*deltaX) + (2*lamdaY*Na)/(deltaY*deltaY)
ktw21 = (1-Si)/(deltaTheta*W2) # Ignored
ktw22 = 1/(2*(1-phi)*W2)
ktw23 = Rcb/2*W2
ktw24 = (1/(1-phi) + Rcb)/W2
ktw25 = 2*lamdaX*Na/(deltaX*deltaX*W2)
ktw26 = 2*lamdaY*Na/(deltaY*deltaY*W2)

# Costants for Fluid A
a1 = Va/(Rab*deltaTheta) + 0.5 + Eab/(Rab*deltaY) + (2*Na*Eab)/(Pea*deltaY*deltaY*Rab)
kta1 = Va/(Rab*deltaTheta*a1)    # Ignored at time zero (k=0)
kta2 = 1/a1
kta3 = (Eab/(Rab*deltaY) - 0.5)/a1
kta4 = Na*Eab/(Pea*deltaY*deltaY*Rab*a1)

# Consants for Fluid C    (Moving in Y-direction in a rightward direction)
c1 = Vc/(Rcb*deltaTheta) + 0.5 + Ecb/(Rcb*deltaX) + 2*Na/(Pec*deltaX*deltaX)
ktc1 = Vc/(Rcb*deltaTheta*c1)       # Ignored at time zero (k=0)
ktc2 = 1/c1
ktc3 = (Ecb/(Rcb*deltaX) - 0.5)/a1
ktc4 = Na/(Pec*deltaX*deltaX)/c1
#import pdb;pdb.set_trace()

print 'Calculated constants'
error = 0.01
checkerA = []
checkerB = []
checkerC = []
checkerW1 = []
checkerW2 = []  
 
for _ in range(countY+1):
	checkerA.append([False]*(countX+1))
	checkerB.append([False]*(countX+1))
	checkerC.append([False]*(countX+1))
	checkerW1.append([False]*(countX+1))
	checkerW2.append([False]*(countX+1))

def reset(num):
	if num == 4 :
		for i in range(0,countY+1):
			for j in range(0,countX+1):
				checkerA[i][j] = False
	elif num == 2:
		for i in range(0,countY+1):
			for j in range(0,countX+1):
				checkerW1[i][j] = False
	elif num == 1:
		for i in range(0,countY+1):
			for j in range(0,countX+1):
				checkerB[i][j] = False
	elif num == 3:
		for i in range(0,countY+1):
			for j in range(0,countX+1):
				checkerW2[i][j] = False	
	elif num == 5:
		for i in range(0,countY+1):
			for j in range(0,countX+1):
				checkerC[i][j] = False

def gauss_siedel(num, arr):
	count,test = 0,0
	if num == 4 :
		#while count < count_checkerAC:
			for i in range(1,countY+1):   #Rows
				for j in range(1,countX+1): #columns
					res = boundary(i,j,arr)
					incY = res
					if not checkerA[i][j]:
						val = kta2*tempW1[i,j] + kta3*tempA[i-1,j] + kta4*(tempA[incY,j] + tempA[i-1,j])

						if abs(val-arr[i,j]) > error:
							arr[i,j] = val
							test = 1
						else:
							checkerA[i][j] = True
							count+=1
	elif num == 1:
		#while count < count_checkerB:
			for i in range(1,countY+1):
				for j in range(1,countX+1):
					res=boundaryB(i,j,arr)
					incX=res
					if not checkerB[i][j]:
						val = ktb2*(tempW1[i,j] + tempB[i,j-1]) + ktb3*(tempW2[i,j] + tempB[i,j-1]) + ktb4*(tempB[i,j-1]) + ktb5*(tempB[i,incX]+tempB[i,j-1])

						if abs(val-arr[i,j])>error:
							arr[i,j] = val
							test = 1
						else:
							checkerB[i][j] = True
							count+=1
	elif num == 2 :
		#while count < count_checkerWalls:
			for i in range(1,countY+1):
				for j in range(1,countX+1):
					res = image_point(i,j,countX,countY)
					incX,incY,decX,decY = res[0],res[1],res[2],res[3]
					if not checkerW1[i][j]:
						val = ktw12*(tempA[i,j] + tempA[i-1,j]) + ktw13*(tempB[i,j] + tempB[i,j-1]) + ktw14*(tempW1[i,incX] + tempW1[i,decX]) + ktw15*(tempW1[decY,j] + tempW1[incY,j])

						if abs(val-arr[i,j])>error:
							arr[i,j] = val
							test = 1
						else:
							checkerW1[i][j] = True
							count+=1

	elif num == 3:
		#while count < count_checkerWalls:
			for i in range(1,countY+1):
				for j in range(1,countX+1):
					res = image_point(i,j,countX,countY)
					incX,incY,decX,decY = res[0],res[1],res[2],res[3]
					if not checkerW2[i][j]:
						val = ktw22*(tempB[i,j] + tempB[i,j-1]) + ktw23*(tempC[i,j] + tempC[i-1,j]) + ktw25*(tempW2[i,incX] + tempW2[i,decX]) + ktw26*(tempW2[decY,j] + tempW2[incY,j])

						if abs(val-arr[i,j])>error:
							arr[i,j] = val
							test = 1
						else:
							checkerW2[i][j] = True
							count+=1

	elif num == 5 :
		#while count < count_checkerAC:
			for i in range(1,countY+1):
				for j in range(1,countX+1):
					res = boundary(i,j,arr)
					incY = res
					if not checkerC[i][j]:
						val = ktc2*tempW2[i,j] + ktc3*tempC[i-1,j] + ktc4*(tempC[incY,j] + tempC[i-1,j])

						if abs(val-arr[i,j]) > error:
							arr[i,j] = val
							test = 1
						else:
							checkerC[i][j] = True
							count+=1

	#reset(num)
	print arr,num,count
	if test :
		return True
	else:
		return False


seq = [(2,tempW1),(3,tempW2),(1,tempB),(4,tempA),(5,tempC)]
counter = 0


while seq:
#  import pdb;pdb.set_trace()
  pai = seq.pop(0)
  counter+=1
  print counter
  if gauss_siedel(pai[0], pai[1]):
    seq.append(pai)

print 'FINAL VALUE\n'
print 'Temperature of Fluid B'
print tempB
print checkerB
print 'Temperature of Wall 1'
print tempW1
print 'Temperature of Wall 2'
print tempW2
print 'Temperature of Fluid A'
print tempA
print 'Temperature of Fluid C'
print tempC