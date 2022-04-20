#436
import sys
p=print
s="💎📄✂🖖🦎"
e=['cut','cover','crushe','poison','smashe','decapitate','eat','disprove','vaporize']
r=[[2,0,1],[1,1,0],[0,2,4],[4,3,3],[3,4,2],[2,5,4],[4,6,1],[1,7,3],[3,8,0],[0,2,2]]
for a in sys.argv[1:]:
	if a[0]==a[1]:p("Tie")
	else:
		z=s.index(a[0])
		x=s.index(a[1])        
		for i in r:
			if i[0]==z and i[2]==x:p(a[0]+' '+e[i[1]]+'s '+a[1])
			if i[0]==x and i[2]==z:p(a[1]+' '+e[i[1]]+'s '+a[0])