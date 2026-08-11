import numpy as np

array_1D = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9,10])

array_2D = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

num = [10, 20, 30, 40, 50]

list_to_array = np.array(num)

print(array_1D)
print(array_1D.shape)
print(array_1D.dtype)


print(array_2D)
print(array_2D.shape)
print(array_2D.dtype)


print(list_to_array)
print(list_to_array.shape)
print(list_to_array.dtype)