//110
for(n=0;n<201;n++){r=n;for(i=0;i<5;i++){s=[...r+''].map(n=>+n).reduce((a,b)=>a+b*b,0);r=s;};if (r==1)print(n)}