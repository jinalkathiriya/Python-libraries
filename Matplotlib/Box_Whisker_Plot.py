## Box or whisker Plot ## 

# import matplotlib.pyplot as plt
# x=[10,20,30,40,50,60,70,120,300]
# plt.boxplot(x,labels=["python"],showmeans=True,sym="g+",boxprops=dict(color="r"),capprops=dict(color="r"),whiskerprops=dict(color="r"),
#             flierprops=dict(markeredgecolor="y")) # notch=True,widths=10,patch_artist=True,whis=2
# plt.show()

import matplotlib.pyplot as plt

x=[10,20,30,40,50,60,70,120,300]
x1=[12,22,33,46,51,64,73]
y=[x,x1]

plt.boxplot(y,labels=["python","c++"],showmeans=True,sym="g+",boxprops=dict(color="r"),capprops=dict(color="r"),whiskerprops=dict(color="r"),
            flierprops=dict(markeredgecolor="y")) # notch=True,widths=10,patch_artist=True,whis=2
plt.show()


