#476
import sys;p=print;s=[128142,128196,9986,128406,129422];e=['cut','cover','crushe','poison','smashe','decapitate','eat','disprove','vaporize'];r=[[2,0,1],[1,1,0],[0,2,4],[4,3,3],[3,4,2],[2,5,4],[4,6,1],[1,7,3],[3,8,0],[0,2,2]]
for a in sys.argv:
	if len(a)<2: continue
	if a[0]==a[1]:p("Tie")
	else:
		s1=s.index(ord(a[0]))
		s2=s.index(ord(a[1]))
		for i in r:
			if i[0]==s1 and i[2]==s2:p(a[0]+' '+e[i[1]]+'s '+a[1])
			if i[0]==s2 and i[2]==s1:p(a[1]+' '+e[i[1]]+'s '+a[0])