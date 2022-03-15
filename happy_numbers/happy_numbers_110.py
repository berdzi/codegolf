#110
for n in range(201):
	r=n
	for i in range(9): 
		s=0
		for c in str(r): x=int(c);s+=x*x
		r=s
	if r==1: print(n)