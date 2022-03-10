#192
import math as m
for i in range(1,101):
	d=[]
	s=int(m.sqrt(i))
	for x in range(1,s+1):
		if i%x==0:    	
			d.append(x)
			if i//x!=x:
				d.append(i//x)	
	print(' '.join(map(str,sorted(d))))