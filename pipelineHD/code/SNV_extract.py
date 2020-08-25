import sys
arg=sys.argv
fst=0
name_list=[]
f_w=open(arg[1],'r')
lable=f_w.readline().strip().split('\t')
sampl_list={}
curr_sampl=''
#create list of files
for col in range(len(lable)):
    if lable[col].strip('"')=='FS':
        fst=col+1
        continue
    if fst!=0:
    	if lable[col].strip('"').find('.AD')==-1 and lable[col].strip('"').find('.DP')==-1:
    		continue
    	if lable[col].strip('"').strip('.AD').strip('.DP') not in sampl_list.keys():
    		sampl_list[lable[col].strip('"').strip('.AD').strip('.DP')]=[0,0]
    	if lable[col].strip('"').find('.AD')!=-1:
    		sampl_list[lable[col].strip('"').strip('.AD')][0]=col
    	if lable[col].strip('"').find('.DP')!=-1:
    		sampl_list[lable[col].strip('"').strip('.DP')][1]=col

print(sampl_list)
#create files
file_dict={}
for i in sampl_list.keys():
	file_dict[i]=open('snv.'+i+'.txt','w')
    #file_list.append(open('snv.'+i+'.txt','w'))
for line in f_w:
    lp=line.strip().split('\t')
    chrom=lp[0].strip('"').strip('chr').replace('X','23').replace('Y','24').replace('M','25')
    if chrom=='24' or chrom=='25':
    	continue

    for i in sampl_list.keys():
    	if lp[sampl_list[i][1]]=='NA':
    		continue
    	AD=lp[sampl_list[i][0]].strip('"').split(',')
    	file_dict[i].write(chrom+'\t'+lp[1].strip('"')+'\t'+AD[1]+'\t'+lp[sampl_list[i][1]]+'\n')
#close files
for i in file_dict.keys():
    file_dict[i].close()
 
