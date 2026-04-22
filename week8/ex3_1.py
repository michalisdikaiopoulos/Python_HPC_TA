import sys
from time import perf_counter as time
import numpy as np
import zarr

def index_to_point(i, j, imsize, limits):
    # Subtract 1 from imsize[*] to match linspace
    stepw = (limits[1] - limits[0]) / (imsize[1] - 1)
    steph = (limits[3] - limits[2]) / (imsize[0] - 1)
    c = 1j * (limits[0] + i * stepw) + 1 * (limits[2] + j * steph)
    return c

def mandelbrot_escape_time(c):
    z = 0
    for i in range(100):
        z = z**2 + c
        if np.abs(z) > 2:
            return i
    return 100

def mandelbrot_escape_time_chunk(array, limits, i):
    chunks = np.array(array.chunks)
    chunk_shape = np.ceil(np.array(array.shape) / chunks).astype(int)
    chunk_pos = np.array(np.unravel_index(i, chunk_shape))
    p0 = chunk_pos * chunks
    chunk = np.array([
        mandelbrot_escape_time(index_to_point(p0[0] + i, p0[1] + j,
                                            array.shape, limits))
        for j in range(chunks[1]) for i in range(chunks[0])
    ]).reshape(chunks)

    b0 = chunk_pos[1] * chunks[0]
    b1 = chunk_pos[0] * chunks[1]
    e0 = min((chunk_pos[1] + 1) * chunks[0], array.shape[0])
    e1 = min((chunk_pos[0] + 1) * chunks[1], array.shape[1])
    array[b0:e0, b1:e1] = chunk[:e0 - b0, :e1 - b1]

def generate_mandelbrot_set_chunks(array, limits):
    for i in range(array.nchunks):
        mandelbrot_escape_time_chunk(array, limits, i)

if __name__ == "__main__":
    width = int(sys.argv[1])
    height = width
    xmin, xmax = -2, 2
    ymin, ymax = -2, 2
    chunks = sys.argv[2] if len(sys.argv) > 2 else 200
    fname = sys.argv[3] if len(sys.argv) > 3 else 'mandelbrot.zarr'
    # Make sure the file is created and has the correct size
    array = zarr.open(
    fname,
    mode='w',
    shape=(width, height,),
    dtype='int32',
    chunks=(chunks,) * 2,
    )
    t = time()
    generate_mandelbrot_set_chunks(
    array,
    (xmin, xmax, ymin, ymax),
    )
    print(time() - t)