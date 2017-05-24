def flipverticle(A):
	i=0
	n=len(A)
	while i<(n-i-1):
		for j in xrange(n):
			tmp=A[i][j]
			A[i][j]=A[n-i-1][j]
			A[n-i-1][j]=tmp
		i+=1
	return A

A=[[1,2,3],[4,5,6],[7,8,9]]

flipverticle(A)
print A

def transpose(A):
	n=len(A)
	for i in xrange(1,n):
		for j in xrange(i):
			tmp=A[i][j]
			A[i][j]=A[j][i]
			A[j][i]=tmp

transpose(A)

print A

def rotateLeft(A):
	return transpose(flipverticle(A))