#py 170
def h(n):
    try:
        n=str(n);s=0
        for c in n: x=int(c);s=s+x*x
        return s==1 or h(s) or False
    except: pass
for n in range(201):
	if h(n): print(n)