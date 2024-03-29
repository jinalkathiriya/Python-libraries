import numpy as np

## shape ##

# var=np.array([[1,2],[1,2]])
# print(var)
# print()
# print(var.shape)

# var1=np.array([1,2,3,4],ndmin=4)
# print(var1)
# print(var1.ndim)
# print(var1.shape)

## reshape ##

# var2=np.array([1,2,3,4,5,6,1,2,3])
# print(var2)
# print(var2.ndim)
# print()
# x=var2.reshape(3,3)
# print(x)
# print(x.ndim)

var3=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
print(var3)
print(var3.ndim)
print()
x=var3.reshape(2,3,2)
print(x)
print(x.ndim)
print()

one=x.reshape(-1)
print(one)
print(one.ndim)



