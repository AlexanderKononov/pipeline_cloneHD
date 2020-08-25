import sys
import numpy as np
import math

arg=sys.argv
data=[]
#lable=True
f_cvf=open(arg[1], 'r')
f_baf=open(arg[1].replace('mpu2.','').replace('.bed.baf.txt', '')+'.baf.txt', 'w')
step=1000
delcoin=0
line=f_cvf.readline()
while line!= '':
	if line[0]=='#':
		line=f_cvf.readline()
		continue
	data=[]
	lable_data=np.array([(0,0,0)], dtype=[('pos', int),('baf', float),('lvl', int)])
	for i in range(step):
		if line=='':
			break
		colm=line.strip().split('\t')
		colm[0]=colm[0].replace('chr','').replace('X', '23').replace('Y', '24').replace('M', '25')
		baf=float(colm[2])/float(colm[3])
		if baf<0.1 or baf>0.9:
			line=f_cvf.readline()
                        continue
		if int(colm[2])<3:
                        line=f_cvf.readline()
                        continue
		if int(colm[3])<10:
                        line=f_cvf.readline()
                        continue
		#if int(rg[2])<10:
                #        line=f_cvf.readline()
                #        continue

		data.append(str(colm[0])+'\t'+str(colm[1])+'\t'+str(colm[2])+'\t'+str(colm[3])+'\n')
		
		#mdl=math.fabs((float(rb[1])/float(rg[2]))-0.5)
		#baf=float(rb[1])/float(rg[2])
		lvl=baf//0.01

		lable_data=np.insert(lable_data,-1,(len(data)-1,float(baf), lvl), axis=0)
		line=f_cvf.readline()
	#print(lable_data[:,0])
	lable_data=np.sort(lable_data, order='lvl')
	#print(lable_data)
	memb_lvl=0
	curr_lvl=0
	del_list_lvl=[]
	for i in lable_data:
		if i[2]!=curr_lvl:
			if memb_lvl<=10:
				del_list_lvl.append(curr_lvl)
			curr_lvl=i[2]
			memb_lvl=0
			continue
		memb_lvl+=1
		
	lable_data=np.sort(lable_data, order='pos')
	
	'''	
	while i <=len(lable_data):
		if lable_data[i][2] in del_list_lvl:
			lable_data=np.delete(lable_data, i, 0)
			continue
		i+=1
	'''	
	if len(lable_data)<2:
		break	
	for i in lable_data:
			if i[2] in del_list_lvl:
				continue
			f_baf.write(data[int(i[0])])
f_cvf.close()
f_baf.close()
