#!/bin/sh
#BSUB -q hpc
#BSUB -J ppandas
#BSUB -n 1
#BSUB -R "span[hosts=1]"
#BSUB -R "rusage[mem=16GB]"
#BSUB -R "select[model == XeonGold6226R]"
#BSUB -W 00:10
#BSUB -o batch_output/precip_pandas_%J.out
#BSUB -e batch_output/precip_pandas_%J.err

# Initialize Python environment
source /dtu/projects/02613_2025/conda/conda_init.sh
conda activate 02613

echo $CPUTYPE

set -e  # Stop on first error (because that would mean our script is wrong)

# Loop over chunk sizes
for c in 1000 10000 100000 1000000; do
echo $c
/usr/bin/time -f"mem=%M KB runtime=%e s" \
python precip_pandas.py \
    /dtu/projects/02613_2025/data/dmi/2023_01.csv.zip $c \
2>&1  # Magic to redirect stderr to stdour (since time prints to stderr)
done


#XeonGold6226R
#1000
#12548.630000000054
#mem=131712 KB runtime=27.61 s
#10000
#12548.629999999994
#mem=137628 KB runtime=16.70 s
#100000
#12548.629999999997
#mem=197120 KB runtime=15.92 s
#1000000
#12548.630000000001
#mem=559220 KB runtime=16.50 s