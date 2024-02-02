import pandas as pd
var=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})

## insert 
# var.insert(1,"python",var["A"])
# var.insert(1,"python_1",[11,12,13,14])
# var["python_12"]=var["A"][:3]
# print(var)

## delete
del var["A"]
print(var)
# var1=var.pop("B")
# print(var1)
