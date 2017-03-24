# Enter your code here. Read input from STDIN. Print output to STDOUT
from sys import maxint



class element(object):
    def __init__(self,e=[]):
        self.set=set([])
        self.isRepresentative=True
        self.representative=None
        self.n=1
    
    def getRepresentative(self):
        ref=self
        while not ref.isRepresentative:
            ref=ref.representative
        return ref
    
    def union(self, other):
        ref=element()
        ref.n=self.n+other.n
        self.isRepresentative=other.isRepresentative=False
        self.representative=other.representative=ref
        return ref
N=input()
cs={}

ma=0
mi=maxint
for _ in xrange(N):
    g,b=map(int,raw_input().split(' '))
    if not cs.get(g,False):
        cs[g]=element(g)
    if not cs.get(b,False):
        cs[b]=element(b)
        
    G=cs[g].getRepresentative()
    B=cs[b].getRepresentative()
    if G != B:
        rep=G.union(B)
        l=rep.n
        ma=max(l,ma)
        mi=min(l,mi)

print mi,ma
