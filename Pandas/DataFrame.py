import pandas as pd
# l=[1,2,3,4,5,6]
# var=pd.DataFrame(l)
# print(type(var))

# d={"a":[1,2,3,4,5],"s":[1,2,3,4,5],"d":[1,2,3,4,5],1:[1,2,3,4,5]}
# var1=pd.DataFrame(d,columns=["a"])
# print(type(var1))
# print(var1)
# print(var1["a"][3])

# list_1=[[1,2,3,4,5],[11,12,13,14,15]]
# var2=pd.DataFrame(list_1)
# print(type(var2))
# print(var2)

sr={"s":pd.Series([1,2,3,4]),"r":pd.Series([1,2,3,4])}
var3=pd.DataFrame(sr)
print(type(var3))
print(var3)