''' This file is used to create all the initial matrixes for temperature distribution across
    the entire grid at t = 0'''

import numpy as np
import matplotlib as mp

sizeX = 10
sizeY = 10
deltaTheta = 0.01         # Dimensionless time steps

tempA = np.zeros(shape=(sizeX,sizeY))
tempB = np.zeros(shape=(sizeX,sizeY))
tempW1 = np.zeros(shape=(sizeX,sizeY))

#print tempA
