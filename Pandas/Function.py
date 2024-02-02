import pandas as pd
csv_1=pd.read_csv("C:\\Users\\Admin\\Desktop\\data science\\pandas\\Test_new.csv")
# print(csv_1)
# csv_1.index.array
# csv_1.columns
# csv_1.describe()
# csv_1.head(2)
# csv_1.tail(2)
# csv_1[6:11]
# csv_1.to_numpy()

# import numpy as np 
# v=np.asarray(csv_1)
# print(v)

# csv_1.sort_index(axis=0,ascending=False)
# print(csv_1)

# csv_1["SYMBOL"][0]="phthon"
# print(csv_1)

# csv_1.loc[0,"SYMBOL"]="python"
# csv_1.loc[[2,3],["SYMBOL","SECURITY"]]
# csv_1.loc[:,["SYMBOL","SECURITY"]]
# csv_1.loc[[2,3],:]
# csv_1.iloc[0,1]
# print(csv_1)

# csv_1.drop("SECURITY",axis=1)
csv_1.drop(0,axis=0)
print(csv_1)