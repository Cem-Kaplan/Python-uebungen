import numpy as np
from numpy import random  

#0D array
arr_0d = np.array(234)

#1D array
arr_1d = np.array([1, 2, 3, 4])

#2D array
arr_2d = np.array([[1,2,3], [3,2,1]])

#typ erkennen
#print(arr_0d.dtype)

#kopieren
x = arr_0d.copy()

#zufällige zahl
zahl = random.randint(0, 10)
print(zahl)