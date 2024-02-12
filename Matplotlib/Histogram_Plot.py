## Histogram_Plot ## 

import matplotlib.pyplot as plt
import numpy as np
import random

# x=np.random.randint(10,60,(50))
# print(x)

no=[56, 10, 47, 17, 24, 10, 52, 45, 13, 20, 32, 12, 30, 56, 14, 34, 24, 48, 42, 30, 27, 35, 22, 45,
 28, 30, 14, 31, 56, 36, 36, 19, 44, 34, 22, 40, 50, 57, 46, 40, 16, 15, 19, 40, 50, 31, 51, 28,
 15, 50]
l=[10,20,30,40,50,60]
plt.hist(no,color="b",bins=1) #edgecolor="r",cumulative=-1,bottom=20,align="mid",histtype="stepfilled",orientation="horizontal",log=True

plt.title("wscube")
plt.xlabel("python")
plt.ylabel("no.")

plt.axvline(45,color="g",label="line")

plt.legend()
plt.grid()
plt.show()