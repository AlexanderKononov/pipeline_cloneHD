#!/bin/bash
wey=$1
file=$(echo $wey | rev | cut -d'/' -f 1 | rev)

echo $file

mkdir $file.tmp

/apps/general/bcftools-1.5/bin/samtools view -H $wey > $file.tmp/$file.heder.txt

python code/extractBedSeg.py $file.tmp/$file.heder.txt

/apps/general/bcftools-1.5/bin/samtools bedcov $file.tmp/$file.segmented.bed $wey > $file.tmp/$file.rd.txt

awk -v OFS='\t' '{gsub(/chr/,"");gsub(/X/,"23");print $1,$3,int(0.5+$4/10000.0),10}' $file.tmp/$file.rd.txt > $file.tmp/$file.rd2.txt

if [ $# -gt 1 ]
then

python code/getNormPosition.py $2 $file.tmp/$file.rd2.txt

cp $file.tmp/$file.except.txt cna.$file.txt

else

~/cloneHD-v1.17.8/build/pre-filter --data $file.tmp/$file.rd2.txt  --pre $file.tmp/$file.rd2.txt

cp $file.tmp/$file.rd2.txt.pref.txt cna.$file.txt

fi

#rm -r $file.tmp
