#!/bin/bash
set_n=$1
norm_cna=$2
tu_cna=$3
tu_baf=$4

build/pre-filter --data $set_n/data/$norm_cna --pre $set_n/support/$norm_cna 

build/pre-filter --data $set_n/data/$tu_cna --pre $set_n/support/$tu_cna

build/filterHD --data $set_n/support/$norm_cna.pref.txt --mode 3 --pre $set_n/support/$norm_cna --rnd 0

build/filterHD --data $set_n/support/$tu_cna.pref.txt --mode 3 --pre $set_n/support/$tu_cna.bias --bias $set_n/support/$norm_cna.posterior-1.txt --sigma 0 --rnd 0 --jumps 1

build/filterHD --data $set_n/data/$tu_baf --mode 1 --pre $set_n/support/$tu_baf --sigma 0 --jumps 1 --reflect 1 --dist 1 --rnd 0

build/cloneHD --cna $set_n/data/$norm_cna --baf $set_n/data/$tu_baf --pre $set_n/results/$tu_cna --bias $set_n/support/$norm_cna.posterior-1.txt --seed 123 --trials 4 --nmax 30 --max-tcn 12 --cna-jumps $set_n/support/$tu_cna.bias.jumps.txt --baf-jumps $set_n/support/$tu_baf.jumps.txt --min-jump 0.01 --restarts 10 --mass-gauging 1
