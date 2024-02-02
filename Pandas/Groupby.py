import pandas as pd
var=pd.DataFrame({ "Name": ["a","b","c","d","a","b","a","b","a","c","c"],
                  "s_1":[12,13,14,12,13,14,15,23,25,16,10],
                  "s_2":[23,24,25,26,27,28,29,30,25,34,35]})
# print(var)

var_New=var.groupby("Name")
# print(var_New) 

# for x,y in var_New:
#     print(x)
#     print(y) 

# var_New.get_group("a")
# var_New.min()
# var_New.max()
# var_New.mean()

li=list(var_New)
print(li)
