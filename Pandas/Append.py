import pandas as pd
var1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var2=pd.DataFrame({"C":[10,20,30,40],"D":[11,22]})             

print(var1.append(var2,ignore_index=True))