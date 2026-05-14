#!/bin/bash

END=29
for i in $(seq 0 $END); do 
    
    python workload_bkp.py 0.1 | shuf > ./0.1/$i.csv
    #python workload.py 0.05 | shuf > ./queries1/0.05/q$i.csv
    #python workload.py 0.15 | shuf > ./queries1/0.15/q$i.csv


done
