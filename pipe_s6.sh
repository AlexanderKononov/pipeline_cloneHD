#!/bin/bash
set_n=$1
norm_cna=$2
tu_cna=$3
tu_baf=$4
#tu_snv=$5

build/cloneHD --cna $set_n/support6/$tu_cna.pref.txt --baf $set_n/data/$tu_baf --pre $set_n/results6/$tu_cna --bias $set_n/support6/$norm_cna.posterior-1.txt --seed 123 --trials 1 --nmax 3 --max-tcn 3 --cna-jumps $set_n/support6/$tu_cna.bias.jumps.txt --baf-jumps $set_n/support6/$tu_baf.jumps.txt --min-jump 0.1 --restarts 2 --mass-gauging 0
