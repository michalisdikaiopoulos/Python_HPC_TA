import sys
from time import perf_counter as time
import numpy as np

fname = sys.argv[1]
n = int(sys.argv[2])
matrix = np.load(fname)
result = matrix.copy()
t0 = time()
for _ in range(n):
    result @= matrix
t1 = time()
np.save('result.npy', result)
print(t1 - t0)