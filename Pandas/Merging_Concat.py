import pandas as pd 
var1=pd.DataFrame({"A":[1,2,3,4],"B":[11,12,13,14]})
var2=pd.DataFrame({"A":[1,2,3,4],"B":[21,22,23,24]})

## merging
# pd.merge(var1,var2,on="A")
# pd.merge(var1,var2,how="outer",indicator=True)
# pd.merge(var1,var2)
# pd.merge(var1,var2,left_index=True,right_index=True,suffixes=("name","python"))

## Concat
# sr1=pd.Series([1,2,3,4])
# sr2=pd.Series([11,12,13,14])
# pd.concat([sr1,sr2])
pd.concat([var1,var2],axis=1,join="outer",keys=["var1","var2"])