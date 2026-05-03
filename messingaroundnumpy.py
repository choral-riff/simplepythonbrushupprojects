# create multiple dimension arrays using numpy 

import numpy as np 

#0D ndarray using numpy 
zerodim = np.array(5)
onedim = np.array([1,2,3,4])
# a list of lists -- 2D array 
two = np.array ([[1,2,3], [4,5,6]])
#a list of lists that contain lists -- 3D array 
three = np.array([[[1,2,3], [2,3,4], [3,4,5]], [[2,3,4], [3,4,5], [4,5,6]]])

five = np.array([1,2,3,4], ndmin=5)

print(zerodim)
print(zerodim.ndim)
print("\n")
print(onedim)
print(onedim.ndim)
print("\n")
print(two)
print(two.ndim)
print("\n")
print(three)
print(three.ndim)
print("\n")
print(five)
print(five.ndim)
