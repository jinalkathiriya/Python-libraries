import pandas as pd
var=pd.DataFrame({"A":[1,2,3,4],"B":[5,6,7,8]})
print(var)

# var["C"]=var["A"]-var["B"]
# print(var)

# var["C"]=var["A"]+var["B"]
# print(var)

var["python"]=var["A"]<=20
var['python_1']=var["B"]>=16
print(var)