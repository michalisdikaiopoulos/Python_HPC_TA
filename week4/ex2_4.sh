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
#1    0.000    0.000    0.196    0.196 points.py:1(<module>)
#1    0.026    0.026    0.026    0.026 points.py:21(distance_matrix)
#1    0.000    0.000    0.008    0.008 points.py:66(load_points)
#1    0.001    0.001    0.003    0.003 points.py:71(distance_stats)