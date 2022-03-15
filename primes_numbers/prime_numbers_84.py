#84
import re
for i in range(100): 
	if not re.match(r'^1?$|^(11+?)\1+$','1'*i):print(i)