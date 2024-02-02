import pandas as pd
var=pd.DataFrame({"days":[1,2,3,4,5,6],"eng":[10,12,14,17,15,13],"maths":[17,18,19,20,32,52]})
print(var)

print(pd.melt(var,id_vars=["days"],var_name="python",value_name="DS"))