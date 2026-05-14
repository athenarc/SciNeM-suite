#!/bin/bash

END=9
for i in $(seq 0 $END); do 


python neo4j_workload.py 0.1 | shuf > queries100/q$i.csv


done
