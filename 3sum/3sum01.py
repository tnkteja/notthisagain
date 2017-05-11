from bisect import *
from collections import Counter
from itertools import combinations, islice

S=[-1,-2,-3,4,1,3,0,3,-2,1,-2,2,-1,1,-5,4,-3]

S.sort()
print S

for i,x in enumerate(S):
	for j,y in enumerate(islice(S,i+1,None)):
		v=bisect_left(S,0-x-y)
		if v < i+j+1 or S[v+1] < -x-y:
			break
		if v > i+j+1 and v < len(S):
			print v,S[v+1], 0-x-y, "kgk"