import numpy as np

%timeit [j**4 for j in range(1,9)]

%timeit np.arange(1,9)**4
