## Scatter_Plot ##

import matplotlib.pyplot as plt
day=[1,2,3,4,6,5,3]
no=[2,4,6,8,2,7,9]
no1=[3,1,4,6,7,3,2]
colors=[22,10,21,43,20,55,40]
sizes=[400,200,500,400,200,300,500]
plt.scatter(day,no,c=colors,s=sizes,cmap="BrBG") #marker="*",edgecolors="k",alpha=0.5
plt.scatter(day,no1,color="r",s=sizes)
t=plt.colorbar()
t.set_label("colabar",fontsize=15)
plt.title("scatter plot",fontsize=15)
plt.xlabel("day",fontsize=15)
plt.ylabel("no.",fontsize=15)
plt.show()