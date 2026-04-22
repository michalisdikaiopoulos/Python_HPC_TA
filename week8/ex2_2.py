import multiprocessing
import sys
from time import perf_counter as time
import numpy as np

def index_to_point(i, imsize, limits):
    c = np.unravel_index(i, imsize)
    stepw = (limits[1] - limits[0]) / imsize[0]
    steph = (limits[3] - limits[2]) / imsize[1]
    c = limits[0] + c[0] * stepw + 1j * (limits[2] + c[1] * steph)
    return c

def mandelbrot_escape_time(i, imsize, limits):
    c = index_to_point(i, imsize, limits)
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2:
            return i
    return 100

def mandelbrot_escape_time_multiple(imsize, limits, fname, begin, end):
    chunk = np.array([mandelbrot_escape_time(i, imsize, limits)
                    for i in range(begin, end)])
    file = np.memmap(fname, dtype='int32', mode='r+')
    file[begin:end] = chunk
    file.flush()

def generate_mandelbrot_set_chunks(imsize, limits, fname, num_processes):
    pool = multiprocessing.Pool(num_processes)
    chunk_size = 100*100
    n_pixels = imsize[0] * imsize[1]
    tasks = []
    for b in range(0, n_pixels, chunk_size):
        tasks.append(pool.apply_async(
            mandelbrot_escape_time_multiple,
            (imsize, limits, fname, b, min(b + chunk_size, n_pixels)),
        ))
    for t in tasks:
        t.get()
    pool.close()
    pool.join()

if __name__ == "__main__":
    width = int(sys.argv[1])
    height = width
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    num_proc = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    fname = sys.argv[3] if len(sys.argv) > 3 else 'mandelbrot.raw'

    # Make sure the file is created and has the correct size
    np.memmap(fname, dtype='int32', mode='w+', shape=(width * height,))

    t = time()
    generate_mandelbrot_set_chunks(
        (width, height),
        (xmin, xmax, ymin, ymax),
        fname,
        num_proc
    )
    print(time() - t)
