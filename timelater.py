''' Fluid equation for time>0 '''


from timestart import *
#import pdb;pdb.set_trace()
finalB,finalA,finalC = [],[],[]
reset()

def gauss_siedel_2(num, arr):
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
          res = image_point(i,j,countX-1,countY-1)
          incX,incY,decX,decY = res[0],res[1],res[2],res[3]
          if num == 1:
            val = ktb1*tempB[i,j] + ktb2*(tempW12[i,j] + tempB2[decX,j]) + ktb3*(tempW22[i,j] + tempB2[decX,j]) + ktb4*(tempB2[decX,j]) + ktb5*(tempB2[incX,j]+tempB2[decX,j])
          elif num == 2:
            val = ktw11*tempW1[i,j] + ktw12*(tempA2[i,j] + tempA2[i,decY]) + ktw13*(tempB2[i,j] + tempB2[decX,j]) + ktw14*(tempW12[incX,j] + tempW12[decX,j]) + ktw15*(tempW12[i,decY] + tempW12[i,incY])
          elif num == 3:
            val = ktw21*tempW2[i,j] + ktw22*(tempB2[i,j] + tempB2[decX,j]) + ktw23*(tempC2[i,j] + tempC2[i,decY]) + ktw25*(tempW22[incX,j] + tempW22[decX,j]) + ktw26*(tempW22[i,decY] + tempW22[i,incY])
          elif num == 4:
            val = kta1*tempA[i,j] + kta2*tempW12[i,j] + kta3*tempA2[i,decY] + kta4*(tempA2[i,incY] + tempA2[i,decY])
          elif num == 5:
            val = ktc1*tempC[i,j] + ktc2*tempW22[i,j] + ktc3*tempC2[decX,j] + ktc4*(tempC2[incX,j] + tempC2[decX,j])

          if abs(val-arr[i,j])>error:
            arr[i,j] = val
            test = 1
          else:
            checker[i][j] = True
            count+=1

  reset()
  if test:
    return True
  return False


for i in range(timesteps):
  print 'Calculating for time :'+str(i)
  tempA2 = np.zeros(shape=(sizeX,sizeY))
  tempB2 = np.zeros(shape=(sizeX,sizeY))
  tempC2 = np.zeros(shape=(sizeX,sizeY))
  tempW12 = np.zeros(shape=(sizeX,sizeY))
  tempW22 = np.zeros(shape=(sizeX,sizeY))

# Getting initial input over fluid B

  for j in range(countY):
    tempB2[0,j] = 1         # For constant input

  for j in range(countY):
    tempC2[0,j] = 1         # For constant input


  seq = [(1,tempB2),(2,tempW12),(3,tempW22),(4,tempA2),(5,tempC2)]
  counter = 0
  while seq:
    pai = seq.pop(0)
    counter+=1
    print counter
    if gauss_siedel_2(pai[0], pai[1]):
      seq.append(pai)
    #import pdb;pdb.set_trace()  

# Calculate result
  tem1,tem2,tem3 = 0,0,0
  for j in range(countY):
    tem1 += tempB2[sizeX-1,j]
    tem2 += tempA2[sizeX-1,j]
    tem3 += tempC2[sizeX-1,j]
  finalB.append(tem1/sizeY)
  finalA.append(tem2/sizeY)
  finalC.append(tem3/sizeY)  

  tempA = np.copy(tempA2)
  tempB = np.copy(tempB2)
  tempC = np.copy(tempC2)
  tempW1 = np.copy(tempW12)
  tempW2 = np.copy(tempW22)  

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
