import pandas as pd
# csv_1=pd.read_csv("C:\\Users\\Admin\\Desktop\\data science\\pandas\\Test_new.csv",nrows=1,skiprows=[0],header=2,names=["col"])
csv_1=pd.read_csv("C:\\Users\\Admin\\Desktop\\data science\\pandas\\Test_new.csv",dtype={"TODAY_VOLUME":"float"})
print(type(csv_1))
print(csv_1)
