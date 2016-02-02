''' This file is used to create all the initial matrixes for temperature distribution across
    the entire grid at t = 0'''

import numpy as np
import matplotlib as mp

infi = 999999999999

sizeX = 10
sizeY = 10
deltaTheta = 0.1         # Dimensionless time steps

tempA = np.zeros(shape=(sizeX,sizeY))
tempB = np.zeros(shape=(sizeX,sizeY))
tempC = np.zeros(shape=(sizeX,sizeY))
tempW1 = np.zeros(shape=(sizeX,sizeY))
tempW2 = np.zeros(shape=(sizeX,sizeY))

# Constants

Length = 10
deltaX = Length/sizeX
deltaY = Length/sizeY

timesteps = 10

# For fluid B
Vb = 0
phi = 0.5     # Unsure of this value
Na = 1        # Unsure of this value
Peb = infi

# For Wall 1
Si = 0.5
Rab = 1
lamdaX = 0.05
lamdaY = 0.05

# For Wall 2
Rcb = 1

# For Fluid A
Va = 0
Eab = 0.5
Pea = infi

# For Fluid C
Vc = 0
Ecb = 0.5
Pec = infi

# Getting initial input over fluid B

for j in range(sizeY):
  tempB[0,j] = 1         # For constant input
