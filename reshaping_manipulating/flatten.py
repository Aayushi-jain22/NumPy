import numpy as np

#ravel()
#falttern() and ravel() are used to convert a multi-dimensional array into a 1D array.

arr = np.array([[1,2,3],[4,5,6]])

print(arr.ravel()) #ravel() returns a flattened array
print(arr.flatten()) #flatten() returns a flattened array