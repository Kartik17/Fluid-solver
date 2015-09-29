''' This file is used to solve for the values of temperature at different
    grid points at a given time. This is then used to calculate for the 
    next time stamp'''

from initialize import *

print tempA


#def solveTempW1():
# Currently solving for temperature of seperating sheet one

for i in range (0,sizeX):
  for j in range (0,sizeY):

  # Temperature equations for vertices
  if (i == 0 and j==0):
    tempW1[i,j] = (k2*(tempA[i,j] + tempA[i,j+1]) + k3*(tempB[i,j] + tempB[i+1,j]) + k4*(tempW1[i,j+1] + tempW1[i+1,j]))/k1
  elif (i == sizeX and j==sizeY):
    tempW1[i,j] = (k2*(tempA[i,j] + tempA[i,j-1]) + k3*(tempB[i,j] + tempB[i-1,j]) + k4*(tempW1[i,j-1] + tempW1[i-1,j]))/k1
  elif (i == 0 and j==sizeY):
    tempW1[i,j] = (k2*(tempA[i,j] + tempA[i,j-1]) + k3*(tempB[i,j] + tempB[i+1,j]) + k4*(tempW1[i,j-1] + tempW1[i+1,j]))/k1
  elif (i == sizeX and j==0):
    tempW1[i,j] = (k2*(tempA[i,j] + tempA[i,j+1]) + k3*(tempB[i,j] + tempB[i-1,j]) + k4*(tempW1[i,j+1] + tempW1[i-1,j]))/k1

  
