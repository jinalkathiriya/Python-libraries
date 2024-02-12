## bar_PLot ## 

import matplotlib.pyplot as plt 
import numpy as np

x=["python","c","c++","java"]
y=[55,65,44,77]
z=[20,22,77,55]

width=0.2
p=np.arange(len(x))
p1=[j+width for j in p]

plt.xlabel("language",fontsize=15)
plt.ylabel("No.",fontsize=15)
plt.title("wscube",fontsize=15)

plt.barh (p,y,width,color="r",label="popularity")
plt.bar(p1,z,width,color="y",label="popularity1") 

plt.xticks(p+width/2,x,rotation=20)
plt.legend()
plt.show()