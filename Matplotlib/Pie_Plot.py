## Pie_Plot ## 

import matplotlib.pyplot as plt

# x=[10,20,30,40]
# y=["c","c++","java","python"]
# ex=[0.3,0.0,0.0,0.0]
# c=["r","b","g","y"]

# plt.pie(x,labels=y,explode=ex,colors=c,autopct="%0.1f%%",shadow=True,radius=1.5,
#         labeldistance=1.1,startangle=180,textprops={"fontsize":15},counterclock=False,
#         wedgeprops={"linewidth":5},rotatelabels=False)

# plt.title("tech")
# plt.legend(loc=3)
# plt.show()

x=[10,20,30,40]
x1=[40,30,20,10]
y=["c","c++","java","python"]

c=["r","b","g","y"]

plt.pie(x,labels=y,radius=1.5)
cr=plt.Circle(xy=(0,0),radius=1,facecolor="w")
plt.gca().add_artist(cr)

plt.show()
