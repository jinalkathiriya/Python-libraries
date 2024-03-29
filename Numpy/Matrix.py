import numpy as np  

## matrix ##

var=np.matrix([[1,2],[1,2]])
var2=np.matrix([[1,2],[1,2]])

print(var)
print(type(var))    
print()
print(var.dot(var2))
print()

## Array ##

var1=np.array([[1,2,3],[1,2,3]])
print(var1)
print(type(var1))
print()
print(var1*var1)


