#!/bin/sh
#BSUB -q hpc
#BSUB -J zarr
#BSUB -n 24
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=1GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -W 00:10
#BSUB -o batch_output/zarr_%J.out
#BSUB -e batch_output/zarr_%J.err

# Initialize Python environment
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

set -e
ns="10 25 50 100 200"
echo $ns
for n in $ns; do
    echo $n
    python mandelbrot_zarr.py 1000 <math xmlns="http://www.w3.org/1998/Math/MathML" display="inline"><mrow><mi>n</mi></mrow></math>(cpucount) mandelbrot_${LSB_JOBID}.zarr
    du -sh mandelbrot_${LSB_JOBID}.zarr
done
