import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])  # one Dimensition Array
# print(a)
arr = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]
b = np.array(arr)  # two Dimensition Array
print(b.ndim) # no. of Dimi
print(b.shape) # shape : (x,y) x: no of all arrays/ y : Elementof array
print(b.size) # size : Total no. of element
print(b.dtype) # size : Total no. of element
