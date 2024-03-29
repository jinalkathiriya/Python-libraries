import numpy as np

## insert ##

# var=np.array([1,2,3,4])
# print(var)
# v=np.insert(var,2,40)
# v1=np.insert(var,(2,4),4.5)
# x=np.append(var,6.5)
# print(x)
# print(v)
# print(v1)

# var=np.array([[1,2,3],[1,2,3]])
# v=np.insert(var,2,6,axis=1)
# v1=np.insert(var,2,[22,23,24],axis=0)
# v2=np.append(var,[[45,44,23]],axis=0)
# print(v)
# print(v1)
# print(v2)

## Delete ##

var=np.array([1,2,3,4])
print(var)
d=np.delete(var,2)
print(d)