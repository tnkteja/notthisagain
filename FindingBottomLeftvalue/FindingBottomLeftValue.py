class Node:
	def __init__(self,data, left, right):
		self.data=data
		self.left=left
		self.right=right


stack=[root]

d,v=0,root.data

while stack:
	node=stack[-1]
	if node.left:
		stack.append(node.left)
		continue
	if node.right:
		stack.append(node.right)
		continue

	if len(stack)>d:
		d,v=len(stack),node.data

print d,v