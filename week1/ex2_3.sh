#!/bin/bash
#BSUB -J sleeper
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "select[model==XeonGold6226R]"
#BSUB -R "rusage[mem=512MB]"
#BSUB -o outputs/sleeper_%J.out
#BSUB -e outputs/sleeper_%J.err
#BSUB -B
#BSUB -N

lscpu
sleep 60