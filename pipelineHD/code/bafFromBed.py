import sys

arg=sys.argv
data=[]
#lable=True
f_cvf=open(arg[1], 'r')
f_baf=open(arg[1]+'.baf.txt', 'w')
cr_list=[]
for i in range(23):
	cr_list.append(str(i+1))
print(cr_list)

line=f_cvf.readline()
while line!= '':
	if line[0]=='#':
		line=f_cvf.readline()
		continue
	#if line=='':
	#	break
	colm=line.strip().split('\t')
	if float(colm[5])<10 or float(colm[5])>90:
		line=f_cvf.readline()
		continue
	colm[0]=colm[0].replace('chr','').replace('X', '23').replace('Y', '24').replace('M', '25')
	if colm[0] not in cr_list:
		line=f_cvf.readline()
                continue
	if int(colm[3])<4:
                line=f_cvf.readline()
                continue
	if int(colm[4])<10:
		line=f_cvf.readline()
		continue
	if colm[0]=='24':
                line=f_cvf.readline()
                continue
	f_baf.write(str(colm[0])+'\t'+str(colm[2])+'\t'+str(colm[3])+'\t'+str(colm[4])+'\n')
	line=f_cvf.readline()
f_cvf.close()
f_baf.close()
