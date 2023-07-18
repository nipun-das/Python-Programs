import numpy as np

a = np.array([(1,2),(3,4)])
b = np.array([(1,2),(3,4)])

print(np.add(a,b))

print(np.subtract(a,b))

print(np.multiply(a,b))

print(np.divide(a,b))

print(a.transpose())

print(np.linalg.inv(a))

print(np.linalg.det(a))


"""
[[2 4]
 [6 8]]
 
[[0 0]
 [0 0]]
 
[[ 1  4]
 [ 9 16]]
 
[[1. 1.]
 [1. 1.]]
 
[[1 3]
 [2 4]]
 
[[-2.   1. ]
 [ 1.5 -0.5]]
 
-2.0000000000000004

"""