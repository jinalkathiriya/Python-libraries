import numpy as np

# var=np.array([9,7,6,5,4])
# print(var)
# print()
# print()
# for i in var:
#     print(i)

# var=np.array([[9,7,6,5,4],[1,2,3,4,5]])
# print(var)
# print()
# for j in var:
#     print(j)
# print()
# for k in var:
#     for l in k:
#         print(l)

# var=np.array([[[9,7,6,5,4],[1,2,3,4,5]]])
# print(var)
# print(var.ndim)
# print()
# for i in var:
#     for j in i:
#         for k in j:
#             print(k)

var=np.array([[[9,7,6,5,4],[1,2,3,4,5]]])
print(var)
print(var.ndim)
print()
# for i in np.nditer(var):
#     print(i)
for i,d in np.ndenumerate(var):
    print(i,d)



