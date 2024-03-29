import numpy as np  

var=np.matrix([[1,2,3],[4,5,6]])
var1=np.matrix([[1,2],[4,5]])
print(var)
print()

print(np.transpose(var))    # transpose
print()
print(var.T)    
print()
print(np.swapaxes(var,0,1))     #swapaxes
print()
print(np.swapaxes(var1,0,1))     
print()
print(np.linalg.inv(var1))      #inverse
print()
print(np.linalg.matrix_power(var1,2))       #power
print()
print(np.linalg.matrix_power(var1,0))
print()
print(np.linalg.matrix_power(var1,-2))
print()
print(np.linalg.det(var1))      #determinate




