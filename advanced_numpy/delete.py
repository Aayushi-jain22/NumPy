import numpy as np


arr = np.array([10,20,30,40])

new_arr = np.delete(arr,2)
print(new_arr)


##For 2d

arr_2d = np.array([[1,2,3],[4,5,6]])
#axis = 0 for row and axis = 1 for column

new_2d_arr = np.delete(arr_2d, 1, axis=1)
print(new_2d_arr)




# Agar sirf 4 delete karna hai

# NumPy me np.delete() se ek single element ko 2D array se directly delete nahi kar sakte.

# Lekin flatten karke kar sakte ho:

# import numpy as np

# arr_2d = np.array([[1,2,3],
#                    [4,5,6]])

# new_arr = np.delete(arr_2d.flatten(), 3)
# print(new_arr)