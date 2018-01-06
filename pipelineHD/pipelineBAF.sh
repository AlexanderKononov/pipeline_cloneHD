#!/bin/bash/
wey=$1
bam_file=$(echo  $wey | rev | cut -d'/' -f 1 | rev)

mkdir tmp.$bam_file

/apps/general/bcftools-1.5/bin/samtools mpileup -q 15 -Q20 -f /fs/projects/hercules/akononov/GRCh38.d1.vd1/GRCh38.d1.vd1.fa -l /fs/projects/hercules/akononov/SNP/snp137.bed $wey > tmp.$bam_file/mpu.$bam_file

perl code/strangescript2.pl tmp.$bam_file/mpu.$bam_file  > tmp.$bam_file/mpu2.$bam_file.bed

python code/bafFromBed.py tmp.$bam_file/mpu2.$bam_file.bed 

if [ $# -gt 1 ]
then

python code/getNormPosition.py $2 tmp.$bam_file/mpu2.$bam_file.bed.baf.txt

mv tmp.$bam_file/$bam_file.bed.baf.txt.except.txt ./baf.$bam_file.txt

else

python code/filter5.py tmp.$bam_file/mpu2.$bam_file.bed.baf.txt

mv tmp.$bam_file/$bam_file.baf.txt ./baf.$bam_file.txt

fi

#rm -r tmp.$bam_file

