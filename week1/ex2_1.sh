#!/bin/bash
#BSUB -J sleeper
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -o outputs/sleeper_%J.out
#BSUB -e outputs/sleeper_%J.err

sleep 60

# bsub ex2_1.sh

# The bstat output does not include information about the wall time limit.
# The bjobs output includes the TIME_LEFT column, which tells us how time is left before we hit the wall time limit we set.