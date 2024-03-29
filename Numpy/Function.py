import numpy as np

### functions ###

## zeros ##

# ar_zero=np.zeros(4)
# ar_zero1=np.zeros((3,4))
# print(ar_zero)
# print()
# print(ar_zero1)

## ones ##

# ar_one=np.ones(4)
# print(ar_one)

## Empty ##

# ar_em=np.empty(4)
# print(ar_em)

## range ##

# ar_rn=np.arange(4)
# print(ar_rn)

## diagonal ##

# ar_dia=np.eye(3)
# print(ar_dia)

# ar_dia=np.eye(3,5)
# print(ar_dia)

## linspace ##

# ar_lin=np.linspace(0,20,num=5)
# print(ar_lin)

## search ##

# var=np.array([1,2,3,4,5,2,6,7])
# # x=np.where(var==2)
# x=np.where((var%2)==0)
# print(x)

## search sorted ##

# var=np.array([1,2,3,4,5,2,6,7])
# x=np.searchsorted(var,[2,3,4],side="right")
# print(x)

## sort ##

# var=np.array([1,2,3,4,5,2,6,7])
# print(np.sort(var))
# var1=np.array(["a","b","n","h"])
# print(np.sort(var1))
# var2=np.array([[1,2],[3,4],[5,2],[6,7]])
# print(np.sort(var2))

## filter Array ##

var=np.array(["a","b","n","h"])
f=[True,False,False,True]
new=var[f]
print(new)
print(type(new))




