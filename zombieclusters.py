class cluster(object):
    def __init__(self,members=[]):
        self.s=set(members)
    
    def merge(self, other):
        self.s.union(other.s)
        return self
        
class clusterManager(object):
    def __init__(self,clusters={}):
        self.c=clusters
    
    def merge(self, i, j):
        self.c[i]=self.c[j]=self.c[i].merge(self.c[j])
        
    def count(self):
        return len(set(self.c.values()))
    
def  zombieCluster(zombies):
    cm=clusterManager(clusters={i:cluster(members=[i]) for i in xrange(len(zombies))})
    for i,row in enumerate(zombies):
        for j,column in enumerate(row):
            if column == '1':
                cm.merge(i,j)
    return cm.count()
