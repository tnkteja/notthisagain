def ReversePrint(head):
    stack=[]
    while head:
        stack.append(head.data)
        head=head.next
    while stack:
        print stack.pop()