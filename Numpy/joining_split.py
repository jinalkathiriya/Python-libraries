## join Array ##

import numpy as np

# var=np.array([1,2,3,4,5])
# var1=np.array([9,4,3,7,6])
# ar=np.concatenate((var,var1))
# print(ar)

# vr=np.array([[1,2],[3,4]])
# vr1=np.array([[9,7],[5,6]])
# ar_new=np.concatenate((vr,vr1),axis=1)
# print(vr)
# print()
# print(vr1)
# print()
# print(ar_new)

# var=np.array([1,2,3,4,5])
# var1=np.array([9,4,3,7,6])
# ar=np.stack((var,var1))
# ar1=np.hstack((var,var1))    #row
# ar2=np.vstack((var,var1))    #column
# ar3=np.dstack((var,var1))     #height
# print(ar)
# print()
# print(ar1)
# print()
# print(ar2)
# print()
# print(ar3)


## split Array ##

# var=np.array([1,2,3,4,5,6])
# print(var)
# ar=np.array_split(var,3)
# print()
# print(ar)
# print(ar[0])

var=np.array([[1,2],[3,4],[5,6]])
print(var)
ar=np.array_split(var,3)
ar1=np.array_split(var,3,axis=1)
print()
print(ar)
print()
print(ar1)


