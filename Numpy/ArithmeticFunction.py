import numpy as np

var=np.array([4,4,5,4,1,3,2])

# print("min: ",np.min(var),np.argmin(var)) #argmin is show index of that number.
# print("max: ",np.max(var),np.argmax(var))
# print("sqrt: ",np.sqrt(var))
# print(np.sin(var))
# print(np.cos(var))
# print(np.cumsum(var)) 

# var=np.array([[3,2,5],[1,0,8]])
# print(np.min(var,axis=0)) ## column min

# np.random.shuffle(var)
# print(var)

# x=np.unique(var,return_index=True,return_counts=True)
# print(x)

y=np.resize(var,(2,3))
y=np.resize(var,(3,2))
print(y)
print()
print("Flatten: ",y.flatten(order="F"))
print("Ravel: ",np.ravel(y,order="A"))


    
