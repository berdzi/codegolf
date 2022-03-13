#94
for i in range(1,101):
	for x in range(1,i+1):
		if i%x==0:print("%d "%x,end="")
	print('\r')