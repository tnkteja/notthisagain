# Enter your code here. Read input from STDIN. Print output to STDOUT

stackOne=[]
stackTwo=[]
N=input()
for _ in xrange(N):
    inp=map(int,raw_input().split(' '))
    if inp[0] == 1:
        stackOne.append(inp[1])
    else:
        if not stackTwo:
            while stackOne:
                stackTwo.append(stackOne.pop())
        if inp[0] == 2:
            stackTwo.pop()
        else:
            top=stackTwo.pop()
            print top
            stackTwo.append(top)