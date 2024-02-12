## Step Plot ## 

import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[4,1,2,5,3]

plt.step(x,y,color="r",marker="o",label="python")

plt.title("python")
plt.xlabel("x_ax")
plt.ylabel("y_ax")
plt.legend(loc=1)
plt.grid()
plt.show()


