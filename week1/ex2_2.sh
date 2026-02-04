#!/bin/bash
#BSUB -J sleeper
#BSUB -q hpc
#BSUB -W 2
#BSUB -R "rusage[mem=512MB]"
#BSUB -o outputs/sleeper_%J.out
#BSUB -e outputs/sleeper_%J.err
#BSUB -B
#BSUB -N

sleep 60

# To test, increase the period in the sleep command to be longer than the wall time limit, and submit the job again. What happens?
# Answer: The job will start as before, but after the wall time limit is reached it will be terminated. In the job summary, instead of "Successfully completed." it will say something like "TERM_RUNLIMIT: job killed after reaching LSF run time limit."
