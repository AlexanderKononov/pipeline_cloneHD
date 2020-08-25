# Toolbox for work with CloneHD application
General pipeline from bam file to clonHD results.
ClonHD application is a tool to reconstruct the subclonal structure of tumour by WGS data.
http://dx.doi.org/10.1016/j.celrep.2014.04.055
The pipeline also includes the steps utilising GATK tools
https://gatk.broadinstitute.org/hc/en-us

This project has scripts for preprocessing data from BAM file to input format of CloneHD, scripts to run CloneHD as the pipeline for a set of samples, and scripts to extract and visualize results from CloneHD output files

Process in general consist of 3 part:  call of polymorphisms, filtering and clastering.
Call part contined the steps for HaplotypeCeller from GATK
Filtering part contined from filtration by GATK and script which make additional filtration.
And clasterization part cottined instruction for cloneHD.
