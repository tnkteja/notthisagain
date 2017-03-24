# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import maxint

N=input()
components={}
for _ in xrange(N):
    g,b=map(int,raw_input().split(' '))
    s=set([g,b])
    if components.get(g, False):
        s.update(components[g])
    if components.get(b,False):
        s.update(components[b])
    for i in s:
        components[i]=s
    
ma=2
mi=maxint
for c in components.values():
    l=len(c)
    ma=max(l,ma)
    mi=min(l,mi)

print mi,ma
        
