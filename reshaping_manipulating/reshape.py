import numpy as np


##convert 1 D array to 2D array

arr = np.array([1,2,3,4,5,6])
reshaped_arr = arr.reshape(2,3)

print(reshaped_arr)