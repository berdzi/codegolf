#75
a=[0,1]
for i in range(2,31): a.append(a[i-1]+a[i-2])
for q in a: print (q)