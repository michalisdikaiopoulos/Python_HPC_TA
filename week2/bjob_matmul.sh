#!/bin/bash
#BSUB -J matmul
#BSUB -q hpc
#BSUB -W 2
#BSUB -n 1
#BSUB -R "rusage[mem=512MB] span[hosts=1]"
#BSUB -o matmul_%J.out
#BSUB -e matmul_%J.err

source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

python matmul.py input.npy 10