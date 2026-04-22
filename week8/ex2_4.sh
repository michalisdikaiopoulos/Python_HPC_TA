#!/bin/sh
### General options
#BSUB -q hpc
#BSUB -J mandelpic
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=2GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -W 00:10
#BSUB -o batch_output/mandelbrot_pic_%J.out
#BSUB -e batch_output/mandelbrot_pic_%J.err

# Initialize Python environment
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

for n in 1 2 4 8 16; do
    echo $n
    /usr/bin/time -f"mem=%M KB runtime=%e s" \
    python mandelbrot_memmap_pic.py \
    /dtu/projects/02613_2025/data/mandelbrot/mandelbrot.raw $n \
    2>&1
done