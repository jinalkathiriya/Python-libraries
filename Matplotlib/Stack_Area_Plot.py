## Stack or Area Plot ## 

import matplotlib.pyplot as plt

x=[1,2,3,4,5]
area=[4,1,7,4,5]
area1=[2,4,1,7,0]
area2=[4,3,7,2,1]

l=["area","area1","area2"]
plt.stackplot(x,area,area1,area2,labels=l,colors=["r","g","y"],baseline="sym")

plt.title("python")
plt.xlabel("x_ax")
plt.ylabel("y_ax")
# plt.grid()
plt.legend(loc=2)
plt.show()

