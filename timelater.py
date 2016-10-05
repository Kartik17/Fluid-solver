''' Fluid equation for time>0 '''


from timestart import *
#import pdb;pdb.set_trace()
finalB,finalA,finalC = [],[],[]
for i in range(1,6):
	reset(i)

'''def gauss_siedel_2(num, arr):
  count,test = 0,0
  start = 0
  if num == 1:
    start = 1
  while count<count_checker:
    for i in range(start,countX-1):
      for j in range(0,countY-1):
        if not checker[i][j]:
          if num == 1:
            val = ktb1*tempB[i,j] + ktb2*(tempW12[i,j] + tempB2[i-1,j]) + ktb3*(tempW22[i,j] + tempB2[i-1,j]) + ktb4*(tempB2[i-1,j]) + ktb5*(tempB2[i+1,j]+tempB2[i-1,j])
          elif num == 2:
            val = ktw11*tempW1[i,j] + ktw12*(tempA2[i,j] + tempA2[i,j-1]) + ktw13*(tempB2[i,j] + tempB2[i-1,j]) + ktw14*(tempW12[i+1,j] + tempW12[i-1,j]) + ktw15*(tempW12[i,j-1] + tempW12[i,j+1])
          elif num == 3:
            val = ktw21*tempW2[i,j] + ktw22*(tempB2[i,j] + tempB2[i-1,j]) + ktw23*(tempC2[i,j] + tempC2[i,j-1]) + ktw25*(tempW22[i+1,j] + tempW22[i-1,j]) + ktw26*(tempW22[i,j-1] + tempW22[i,j+1])
          elif num == 4:
            val = kta1*tempA[i,j] + kta2*tempW12[i,j] + kta3*tempA2[i,j-1] + kta4*(tempA2[i,j+1] + tempA2[i,j-1])
          elif num == 5:
            val = ktc1*tempC[i,j] + ktc2*tempW22[i,j] + ktc3*tempC2[i-1,j] + ktc4*(tempC2[i+1,j] + tempC2[i-1,j])

          if abs(val-arr[i,j])>error:
            arr[i,j] = val
            test = 1
          else:
            checker[i][j] = True
            count+=1

  reset()
  if test:
    return True
  return False'''

def gauss_siedel_2(num, arr):
	count,test = 0,0
	if num == 4 :
		while count < count_checkerAC:
			for i in range(1,countY+1):   #Rows
				for j in range(1,countX+1): #columns
					res = boundary(i,j,arr)
					incY = res
					if not checkerA[i][j]:
						val = kta1*tempA[i,j] + kta2*tempW12[i,j] + kta3*tempA2[i-1,j] + kta4*(tempA2[incY,j] + tempA2[i-1,j])

						if abs(val-arr[i,j]) > error:
							arr[i,j] = val
							test = 1
						else:
							checkerA[i][j] = True
							count+=1
	elif num == 1:
		while count < count_checkerB:
			for i in range(1,countY+1):
				for j in range(1,countX+1):
					res=boundaryB(i,j,arr)
					incX=res
					if not checkerB[i][j]:
						val = ktb1*tempB[i,j] + ktb2*(tempW12[i,j] + tempB2[i,j-1]) + ktb3*(tempW22[i,j] + tempB2[i,j-1]) + ktb4*(tempB2[i,j-1]) + ktb5*(tempB2[i,incX]+tempB2[i,j-1])

						if abs(val-arr[i,j])>error:
							arr[i,j] = val
							test = 1
						else:
							checkerB[i][j] = True
							count+=1
	elif num == 2 :
		while count < count_checkerWalls:
			for i in range(1,countY+1):
				for j in range(1,countX+1):
					res = image_point(i,j,countX,countY)
					incX,incY,decX,decY = res[0],res[1],res[2],res[3]
					if not checkerW1[i][j]:
						val = ktw11*tempW1[i,j] + ktw12*(tempA2[i,j] + tempA2[i-1,j]) + ktw13*(tempB2[i,j] + tempB2[i,j-1]) + ktw14*(tempW12[i,incX] + tempW12[i,decX]) + ktw15*(tempW12[decY,j] + tempW12[incY,j])

						if abs(val-arr[i,j])>error:
							arr[i,j] = val
							test = 1
						else:
							checkerW1[i][j] = True
							count+=1

	elif num == 3:
		while count < count_checkerWalls:
			for i in range(1,countY+1):
				for j in range(1,countX+1):
					res = image_point(i,j,countX,countY)
					incX,incY,decX,decY = res[0],res[1],res[2],res[3]
					if not checkerW2[i][j]:
						val = ktw21*tempW2[i,j] + ktw22*(tempB2[i,j] + tempB2[i,j-1]) + ktw23*(tempC2[i,j] + tempC2[i-1,j]) + ktw25*(tempW22[i,incX] + tempW22[i,decX]) + ktw26*(tempW22[decY,j] + tempW22[incY,j])

						if abs(val-arr[i,j])>error:
							arr[i,j] = val
							test = 1
						else:
							checkerW2[i][j] = True
							count+=1

	elif num == 5 :
		while count < count_checkerAC:
			for i in range(1,countY+1):
				for j in range(1,countX+1):
					res = boundary(i,j,arr)
					incY = res
					if not checkerC[i][j]:
						val = ktc1*tempC[i,j] + ktc2*tempW22[i,j] + ktc3*tempC2[i-1,j] + ktc4*(tempC2[incY,j] + tempC2[i-1,j])

						if abs(val-arr[i,j]) > error:
							arr[i,j] = val
							test = 1
						else:
							checkerC[i][j] = True
							count+=1

	reset(num)
	print arr,num,count
	if test :
		return True
	else:
		return False

for i in range(timesteps):
  print 'Calculating for time :'+str(i)
  tempA2 = np.zeros(shape=(countY+1,countX+1))
  tempB2 = np.zeros(shape=(countY+1,countX+1))
  tempC2 = np.zeros(shape=(countY+1,countX+1))
  tempW12 = np.zeros(shape=(countY+1,countX+1))
  tempW22 = np.zeros(shape=(countY+1,countX+1))

# Getting initial input over fluid B

  for j in range(countY+1):
	tempB2[j,0] = 1.0         # For constant input
	tempB2[j,1] = 1.0 
  for j in range(countX+1):
	tempC2[0,j] = 01.0 
	tempC2[1,j] = 01.0 
  for i in range(0,countX+1):
	tempA2[0,i] = 0.0
	tempA2[1,i] = 0.0	# For constant input


  seq = [(1,tempB2),(2,tempW12),(3,tempW22),(4,tempA2),(5,tempC2)]
  counter = 0
  while seq:
    pai = seq.pop(0)
    counter+=1
    print counter
    if gauss_siedel_2(pai[0], pai[1]):
      seq.append(pai)

# Calculate result
  tem1,tem2,tem3 = 0,0,0
  for j in range(1,countY+1):
    tem1 += tempB2[j,countX]
    tem2 += tempA2[j,countX]
    tem3 += tempC2[j,countX]
  finalB.append(tem1/countY)
  finalA.append(tem2/countY)
  finalC.append(tem3/countY)

  tempA = np.copy(tempA2)
  tempB = np.copy(tempB2)
  tempC = np.copy(tempC2)
  tempW1 = np.copy(tempW12)
  tempW2 = np.copy(tempW22)  

  for i in range(1,6):
	reset(i)

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

print finalB
print finalA
print finalC
xran = [i for i in range(timesteps)]
plt.plot(xran, finalB)
plt.plot(xran, finalA, color='r')
plt.plot(xran, finalC, color='g')
plt.show()
