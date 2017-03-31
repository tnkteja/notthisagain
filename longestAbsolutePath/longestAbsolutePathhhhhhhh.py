s="dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
print  s.split('\n')
soFarMaxLength=0
soFarMaxPath=[]
path=[]
curdepth=0

def depth(s):
	for i,a in enumerate(s):
		if a != '\t':
			break
	return i,s[i:]

for token in s.split('\n'):
	d,pt=depth(token)
	print d,pt
	if len(path) <= d:
		path.append(pt)
	else:
		curpath='/'.join(path)
		if len(curpath) == soFarMaxLength:
			soFarMaxPath.append(curpath)
		elif len(curpath) > soFarMaxLength:
			soFarMaxPath=[path]
			soFarMaxLength=len(curpath)
			path.pop()


print soFarMaxPath