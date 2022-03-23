#100
import re
for x in range(51):
	if not re.match(r'^1?$|^(11+?)\1+$','1'*f"{x:b}".count('1')):print(x)