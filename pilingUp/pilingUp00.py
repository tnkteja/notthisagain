# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque

T=input()
for _ in xrange(T):
    N=input()
    cubes=deque(map(int,raw_input().split(' ')))
    stack=[]
    ans="Yes"
    while cubes:
        index=0 if cubes[0] > cubes[-1] else -1
        if stack and cubes[index] > stack[-1]:
            ans="No"
            break
        stack.append(cubes[index])
        del cubes[index]
    print ans
    