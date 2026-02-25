import os
import sys
import timeit
from time import perf_counter as time

import numpy as np
from ex2_utils import *

np.random.seed(2800)

n = int(sys.argv[1])
gen = 'zeros'  # sys.argv[2]

if gen == 'zeros':
    arr = np.zeros((n,) * 3, dtype='uint8')
elif gen == 'tile':
    arr = np.tile(
        np.arange(256, dtype='uint8'),
        (n // 256) * n * n,
    ).reshape(n, n, n)
elif gen == 'random':
    arr = np.random.randint(0, 256, size=(n,) * 3, dtype='uint8')
else:
    raise ValueError("Unknown gen method")

# NumPy
t_write_numpy = time()
write_numpy(arr, f"numpy_{n}")
t_write_numpy = time() - t_write_numpy

t_read_numpy = time()
read_numpy(f"numpy_{n}")
t_read_numpy = time() - t_read_numpy

# Blosc
t_write_blosc = time()
write_blosc(arr, f"blosc_{n}", cname="zstd")
t_write_blosc = time() - t_write_blosc

t_read_blosc = time()
read_blosc(f"blosc_{n}")
t_read_blosc = time() - t_read_blosc

print(f"numpy write: {t_write_numpy}")
print(f" numpy read: {t_read_numpy}")
print(f"blosc write: {t_write_blosc}")
print(f" blosc read: {t_read_blosc}")