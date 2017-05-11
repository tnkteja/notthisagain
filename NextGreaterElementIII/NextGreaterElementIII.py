s="0125330"
print s
i=len(s)-1
while i>0 and s[i]<s[i-1]:
	i-=1

s=list(s)
tmp=s[-1]
s[-1]=s[i-1]
s[i-1]=tmp

s=s[:i] + sorted(s[i:])

print ''.join(s)