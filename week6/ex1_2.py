import ctypes
import multiprocessing as mp
import sys
from time import perf_counter as time

import numpy as np
from PIL import Image

def init(shared_arr_):
    global shared_arr
    shared_arr = shared_arr_

def tonumpyarray(mp_arr):
    return np.frombuffer(mp_arr, dtype='float32')

def reduce_step(args):
    b, e, s, elemshape = args
    arr = tonumpyarray(shared_arr).reshape((-1,) + elemshape)
    arr[b] = np.sum(arr[b:e:s], axis=0)

if __name__ == '__main__':
    n_processes = 1
    chunk = 64

    # Create shared array
    data = np.load(sys.argv[1])
    elemshape = data.shape[1:]
    shared_arr = mp.RawArray(ctypes.c_float, data.size)
    arr = tonumpyarray(shared_arr).reshape(data.shape)
    np.copyto(arr, data)
    del data

    t = time()
    step = 1
    # Run parallel sum
    p = mp.Pool(
        n_processes,
        initializer=init,
        initargs=(shared_arr,)
    )
    while step <= len(arr):
        p.map(
            reduce_step,
            [(i, i + step * chunk, step, elemshape)
             for i in range(0, len(arr), step*chunk)],
            chunksize=1
        )
        step *= chunk

    # Write output
    print(time() - t, end=', ')
    Image.fromarray(
        (255 * arr[0].astype(float) / len(arr)).astype('uint8')
    ).save('result.png')