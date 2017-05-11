a=[0,1]
n=7
while len(a) <= n:
	l=len(a)
	for i in xrange(l):
		a.append(a[i]+1)
		if len(a)==n+1:
			break
print a