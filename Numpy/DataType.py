import numpy as np 

# var=np.array([1,2,3,4,11,2,1,1,2,2,1,1,1])
# print("Data Type: ",var.dtype)

# var=np.array([1.2,4.5,2.2])
# print("Data Type: ",var.dtype)

# var=np.array(["a","v","e","d",1,2,3,4])
# print("Data Type: ",var.dtype)


# x=np.array([1,2,3,4],dtype=np.int8)
# print("Data Type: ",x.dtype)
# print(x)

# x=np.array([1,2,3,4],dtype="f")
# print("Data Type: ",x.dtype)
# print(x)

x=np.array([1,2,3,4])

# new=np.float32(x)
# new_one=np.int_(new)
# print("Data Type: ",x.dtype)
# print("Data Type: ",new.dtype)
# print("Data Type: ",new_one.dtype)

# print(x)
# print(new)
# print(new_one)

new_1=x.astype(float)
print(x)
print(new_1)



