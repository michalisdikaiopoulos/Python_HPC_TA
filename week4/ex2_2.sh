#!/bin/sh
### General options
#BSUB -q hpc
#BSUB -J points
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=4GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -W 00:10
#BSUB -o batch_output/points_%J.out
#BSUB -e batch_output/points_%J.err

# Initialize Python environment
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

# Print CPU info
lscpu

python -m cProfile -s cumulative points.py input.csv

#Results
#1    0.000    0.000    2.339    2.339 points.py:1(<module>)
#1    2.153    2.153    2.153    2.153 points.py:7(distance_matrix)
#1    0.000    0.000    0.006    0.006 points.py:59(load_points)
#1    0.001    0.001    0.005    0.005 points.py:64(distance_stats)