#!/bin/sh
#BSUB -q hpc
#BSUB -J cache
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=12GB]"
#BSUB -R "select[model == XeonGold6126]"
#BSUB -W 00:10
#BSUB -o batch_output/cache_%J.out
#BSUB -e batch_output/cache_%J.err

# Initialize Python environment
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

# Print CPU info
lscpu

# Run Python script
python ex1_1.py