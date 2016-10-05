''' This file is used to create all the initial matrixes for temperature distribution across
    the entire grid at t = 0'''

import numpy as np
import matplotlib.pyplot as plt

infi = float("inf")

sizeX = 50.0			#means a 11x11 matrix
sizeY = 50.0
deltaTheta = 0.2       # Dimensionless time steps

countX = int(sizeX)+1	#11 points on X
countY = int(sizeY)+1	#11 points on Y
count_checkerAC = (countX-1)*(countY)  #For A and C we have, 10R*11C
count_checkerWalls = (countX)*(countY)	#For W1 and W2 we have, 11R*11C
count_checkerB = (countX-1)*(countY)   #For B we have, 11R*10C

tempA = np.zeros(shape=(countY+1,countX+1))			#Taking all as 13X13 matrix
tempB = np.zeros(shape=(countY+1,countX+1))
tempC = np.zeros(shape=(countY+1,countX+1))
tempW1 = np.zeros(shape=(countY+1,countX+1))
tempW2 = np.zeros(shape=(countY+1,countX+1))

'''tempA = np.zeros(shape=(sizeX,sizeY))
tempB = np.zeros(shape=(sizeX,sizeY))
tempC = np.zeros(shape=(sizeX,sizeY))
tempW1 = np.zeros(shape=(sizeX,sizeY))
tempW2 = np.zeros(shape=(sizeX,sizeY))
'''
# Constants

Na = 0.5
deltaX = Na/sizeX
deltaY = Na/sizeY

timesteps = 50

# For fluid B
Vb = 0.0
phi = 0.5     # Unsure of this value
Peb = infi

# For Wall 1
Si = 0.5
Rab = 2.0
lamdaX = 0.0
lamdaY = 0.0

# For Wall 2
Rcb = 2.0

# For Fluid A
Va = 0.0
Eab = 0.5
Pea = infi

# For Fluid C
Vc = 0.0
Ecb = 0.5
Pec = infi

# Getting initial input over fluid B

for j in range(0,countY+1):
  tempB[j,0] = 1.0   # For constant input
  tempB[j,1] = 1.0

'''for j in range(countY):
  tempC[0,j] = 1.0         # For constant input'''

for i in range(0,countX+1):
 # For constant input #change
  tempC[0,i] = 01.0
  tempC[1,i] = 01.0
for i in range(0,countX+1):
	tempA[0,i] = 0.0
	tempA[1,i] = 0.0

print tempB
print '***********-----------------************---------'
print tempA
print '***********-----------------************---------'
print tempC
print '***********-----------------************---------'
print tempW1
print '***********-----------------************---------'
print tempW2