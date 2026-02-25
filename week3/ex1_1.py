from time import perf_counter as time

import numpy as np

SIZE = 100

n_repeat = int(1e3)
mat = np.random.rand(SIZE, SIZE)

trow = time()
for _ in range(n_repeat):
    mat[0, :] * 1.01
trow = time() - trow

tcol = time()
for _ in range(n_repeat):
    mat[:, 0] * 1.01
tcol = time() - tcol

print('trow =', trow / n_repeat)
print('tcol =', tcol / n_repeat)