a=[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

a.sort(key=lambda x: (x[0],-x[1]))

from collections import deque
from bisect import insort
o=[]
while a:
	p=a.pop()
	o.insert(p[1],p)

print o