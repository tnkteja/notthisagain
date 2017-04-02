from bisect import *
from heapq import *

class lfu(object):
	def __init__(self, capacity):
		self.cache={}
		self.capacity=capacity
		self.lfukf={None:0}
		self.ranks=[None for _ in capacity]

	def get(key):
		value=self.cache.get(key,-1)
		self.lfukf[key]+=1
		return 

	def put(key,value):
		if len(self.lfukf) == self.capacity:
			_,lfuk=heappop(self.lfukf)
			del self.cache[lfuk]
		self.cache[key]=value
		heappush(self.lfukf, (0,key))
