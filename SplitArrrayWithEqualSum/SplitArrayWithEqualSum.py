a=[10, 20 , 30 , 5 , 3, 40 , 50 , 40 , 15]
i=0
j=len(a)-1

lsum=a[i]
rsum=a[j]

while i<j and lsum != rsum:

	while i<j and lsum < rsum:
		i=i+1
		lsum+=a[i]
	while i<j and rsum < lsum:
		j=j-1
		rsum+=a[j]

	print i,j

print i,j