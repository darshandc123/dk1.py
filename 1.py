import numpy as np
arr=np.array([[2,3,4],[1,6,5]])
print("sum of the array:",arr.sum())
print("maximum of the array:",arr.max())
print("minimum of the array:",arr.min())
print("minimum in row:",arr.min(axis=1))
print("maximum in row:",arr.max(axis=1))
print(arr.cumsum(axis=1))
print(np.average(arr))


