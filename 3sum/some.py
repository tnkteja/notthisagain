#
# a2[]
#
#
#
#

from collections import deque

exp=deque("2[a[3[ef]]]")
stack=[]
while exp:
	while exp[0]!=']':
		stack.append(exp.popleft())
		print stack
	exp.popleft()
	out=''
	while stack[-1] != '[':
		out+=stack.pop()
	stack.pop()
	f=stack.pop()
	stack.append(int(f)*out)
	print stack, exp
	break
