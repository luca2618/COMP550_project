#!/bin/sh
#BSUB -J female	
#BSUB -o %J.out
#BSUB -e %J.err
#BSUB -q hpc
#BSUB -n 8
#BSUB -R "rusage[mem=15G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 24:00

### -- send notification at start -- 
#BSUB -B 
### -- send notification at completion -- 
#BSUB -N 

# end of BSUB options


source env/bin/activate
python3 word2vec.py
#python3 clean_to_pickle_label.py
