#!/bin/sh
#BSUB -q hpc
#BSUB -J blosc
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=4GB]"
#BSUB -W 00:10
#BSUB -o batch_output/blosc_%J.out
#BSUB -e batch_output/blosc_%J.err

# Initialize Python environment
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

# Print CPU info
lscpu

# Run Python script
for n in 256 512 1024; do
    echo n = $n
    #python -u bloscbench.py $n zeros
    #python -u bloscbench.py $n tile
    python -u bloscbench.py $n random
done

# List files for later reference
ls -lh numpy*.npy blosc*.bl