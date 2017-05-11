from collections import Counter
from itertools import combinations

S=[-1,-2,-3,4,1,3,0,3,-2,1,-2,2,-1,1,-5,4,-3]

sol=set()
for comb in combinations(S, 3):
	if sum(comb) ==0:
		sol.add(tuple(sorted(Counter(comb).elements())))

print sol
print sorted([ comb for comb in sol])