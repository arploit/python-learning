import numpy as np

a = np.array([0, 2, 1, 5, 3, 4])
n = len(a)
b = []
for i in range(0, n):
    b.append(a[a[i]])
print(b)
