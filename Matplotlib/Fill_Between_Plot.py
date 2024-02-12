## Fill_Between_Plot ##

import matplotlib.pyplot as plt
import numpy as np

x=np.array[1,2,3,4,5]
y=np.array[4,1,2,5,3]

plt.plot(x,y,color="r")

plt.fill_between(x=[3,5],y1=2,y2=4,color="g",where=(x>=2)&(x<=4),alpha=0.3)

plt.title("python")
plt.xlabel("x_ax")
plt.ylabel("y_ax")
plt.show()