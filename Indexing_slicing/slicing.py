import numpy as np

arr= np.array([10,20,30,40,50])

print(arr[1:4]) #slicing from index 1 to 3
print(arr[0:5:2]) #slicing from index 0 to 4 with step size of 2
print(arr[::2]) #slicing from start to end with step size of 2
print(arr[::-1]) #slicing from end to start with step size of -1
print(arr[:2]) #slicing from index 1 to 3 with step size of 2


arr2d = np.array([[1,2,3],[4,5,6]])
print(arr2d[0:2,1:3]) #slicing rows 0
print(arr2d[0:2,::2]) #slicing rows 0 and 1 with step size of 2