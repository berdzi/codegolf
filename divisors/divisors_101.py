#101
for i in range(1,101):
	d=[]
	for x in range(1,i+1):
		if i%x==0:d.append(str(x))
	print(' '.join(d))