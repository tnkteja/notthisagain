a=[4,3,2,7,8,2,3,1,1,8,7,5,5]
i=0
o=[]
while i<len(a):
	while a[i]!=i+1:
		v=a[i]
		if a[v-1] ==0:
			a[i]=0
			a[v-1]=v
			break
		if a[v-1]==v :
			o.append(v)
			a[i]=0
			break
		else:
			a[i]=a[v-1]
			a[v-1]=v
		print a,o
	i=i+1
	
print o