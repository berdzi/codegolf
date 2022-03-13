#90
for i in range(1,101):
	o=""
	for x in range(1,i+1):
		if i%x==0:o+=str(x)+' '		
	print(o)