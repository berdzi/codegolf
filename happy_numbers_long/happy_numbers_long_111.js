//111
for(n=0;n<1001;n++){r=n;for(i=0;i<6;i++){s=[...r+''].map(n=>+n).reduce((a,b)=>a+b*b,0);r=s;};if (r==1)print(n)}