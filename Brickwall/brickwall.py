inp=[[1,2,2,1], [3,1,2], [1,3,2], [2,4], [3,1,2], [1,3,1,1]]
co={}
for row in inp:
	s=0
	for c in row[:-1]:
		s+=c
		if not co.get(s,False):
			co[s]=1
		else:
			co[s]+=1
print 6-max(co.values())