import pandas as pd 
var=pd.read_csv("C:\\Users\\Admin\\Desktop\\data science\\pandas\\Test_new.csv")
# print(var)

## Replace
# var.replace(to_replace=1,value=22)
# var.replace(to_replace="ELECTHERM",value="python")
# var.replace([1,2,3,4,5,6,7,8,9],22)
# var.replace("[A-Za-z]","python",regex=True)
# var.replace({"SYMBOL":'[A-Z]'},22,regex=True)
# var.replace(1,method="ffill",limit=2,inplace=True)
# print(var)

# Interpolate
# var.interpolate(method="linear",axis=0)
# var.interpolate(limit_direction="forward",limit=2,inplace=True)
var.interpolate(limit_area="inside")
print(var)