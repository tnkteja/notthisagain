from operator import add

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows=[[] for _ in xrange(numRows)]
        for i,a in enumerate(s):
            r=i%4
            if r==3:
                rows[1].append(a)
            else:
                rows[r].append(a)
                
        return ''.join(reduce(add,rows))