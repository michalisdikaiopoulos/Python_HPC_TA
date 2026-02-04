#!/bin/bash
#BSUB -J sleeper
#BSUB -q hpc
#BSUB -W 2
#BSUB -n 64
#BSUB -R "rusage[mem=512MB] span[hosts=1]"
#BSUB -o outputs/sleeper_%J.out
#BSUB -e outputs/sleeper_%J.err

sleep 60