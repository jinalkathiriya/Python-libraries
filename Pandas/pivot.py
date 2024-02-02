import pandas as pd
var=pd.DataFrame ({"days":[1,2,3,4,5,6],
                  "st_Name":["a","b","c","a","b","c"],"eng":[10,11,12,13,14,15],"maths":[17,18,19,10,20,29]})

# print(var.pivot(index="days",columns="st_Name",values="eng"))

print(var.pivot_table(index="st_Name",columns="days",aggfunc="sum",margins="True"))
