from random import randint

A=[ randint(0,2) for _ in xrange(10000)]

print A

def Solution(A):
	def swap(A,i,j):
		tmp=A[i]
		A[i]=A[j]
		A[j]=tmp

	i=0
	k=len(A)-1
	j=0
	while j<k:
		if A[j]==0:
			swap(A,i,j)
			i+=1
		if A[j]==2:
			swap(A,j,k)
			k-=1
		j+=1
	return A

Solution(A)

print A