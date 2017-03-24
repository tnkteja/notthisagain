from sys import maxint

N=input()
components={}
for _ in xrange(N):
    g,b=map(int,raw_input().split(' '))
    s=set([g,b])
    if components.get(g, False):
        components[g].add(b)
        s=components[g]
    if components.get(b,False):
        if len(s) > len(components[b]):
            s.update(components[b])
        else:
            components[b].update(s)
            s=components[b]
    for i in s:
        components[i]=s
    
ma=2
mi=maxint
for c in components.values():
    l=len(c)
    ma=max(l,ma)
    mi=min(l,mi)

print mi,ma
        
