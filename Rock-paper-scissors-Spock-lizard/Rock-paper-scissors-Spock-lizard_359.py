#359
import sys
p=print
s={"✂📄":"cut","📄💎":"cover","💎🦎":"crushe","🦎🖖":"poison","🖖✂":"smashe","✂🦎":"decapitate","🦎📄":"eat","📄🖖":"disprove","🖖💎":"vaporize","💎✂":"crushe"}
for a in sys.argv[1:]:
	if a[0]==a[1]:p("Tie")
	else:
		if a in s.keys():p(a[0]+' '+s[a]+'s '+a[1])
		else:p(a[1]+' '+s[a[::-1]]+'s '+a[0])