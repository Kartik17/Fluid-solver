''' Solving at time = 0'''


from initialize import *

c1 = Vb/deltaTheta + 1/(2*phi) + 1/(2*(1-phi)) + 1/(deltaX) + 2*Na/(Peb*deltaX*deltaX)
ktb1 = 1/(phi*c1)
ktb2 = 1/((1-phi)*c1)
ktb3 = -1/(deltaX*c1)
ktb4 = Na/(Peb*deltaX*deltaX*c1)


count = 0
error = 0.05
checker = []
for _ in range(sizeY):
  checker.append([False]*sizeX)

print tempB

while count<4:
  for i in range(1,sizeX-1):
    for j in range(1,sizeY-1):
#      import pdb;pdb.set_trace()
      if not checker[i][j]:
        val = ktb1*(tempW1[i,j] + tempB[i-1,j]) + ktb2*(tempW2[i,j] + tempB[i-1,j]) + ktb3*(tempB[i-1,j]) + ktb4*(tempB[i+1,j]+tempB[i-1,j])
        if abs(val-tempB[i,j])>error:
          tempB[i,j] = val
        else:
          checker[i][j] = True
          count+=1

print tempB
