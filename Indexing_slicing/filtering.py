##Boolean Masking

import numpy as np
arr = np.array([10,20,30,40,50])

print(arr[arr>30]) #filtering values greater than 30

##2D array
arr2d = np.array([[1,2,3],[4,5,6]])
print(arr2d[arr2d>3]) #filtering values greater than 3