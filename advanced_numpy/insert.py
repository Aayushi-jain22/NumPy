import numpy as np

arr = np.array([10,20,30,40,50])

new_arr = np.insert(arr,2,24)

print(new_arr)

##For 2d

arr_2d = np.array([[1,2,3],[4,5,6]])

#axis = 0 for row and axis = 1 for column

new_2d_arr = np.insert(arr_2d, 1,[7,8,8], axis=0)

# for column 
# new_2d_arr = np.insert(arr_2d, 1,[7,8], axis=1)
print(new_2d_arr)