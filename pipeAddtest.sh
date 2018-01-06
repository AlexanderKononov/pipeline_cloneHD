#!/bin/bash
set_n=$1
norm_cna=$2
tu_cna=$3
tu_baf=$4
tu_snv=$5

build/cloneHD --cna $set_n/data/$tu_cna --baf $set_n/data/$tu_baf --snv $set_n/data/$tu_snv --pre $set_n/addtestresults/$tu_cna --bias $set_n/support/$norm_cna.posterior-1.txt --seed 123 --trials 10 --nmax 5 --max-tcn 5 --cna-jumps $set_n/support/$tu_cna.bias.jumps.txt --baf-jumps $set_n/support/$tu_baf.jumps.txt --min-jump 0.1 --restarts 2 --mass-gauging 1
