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

python points.py input.csv