import pandas as pd 
var=pd.read_csv("C:\\Users\\Admin\\Desktop\\data science\\pandas\\Test_new.csv")
# print(var)

##dropna
# var.dropna(axis=1)
# var.dropna(how="all")
# var.dropna(subset=["CHANGE"])
# var.dropna(inplace=True)
# var.dropna(thresh=2)

##fillna
# var.fillna("python")
# var.fillna({"SYMBOL":"python","SECURITY":"C"})
# var.fillna(method="bfill",axis=1)
# var.fillna(12,inplace=True)
var.fillna("python",limit=2)
print(var)
