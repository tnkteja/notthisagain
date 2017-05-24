def InsertNth(head, data, position):
    if position==0:
        return Node(data=data, next_node=head)
    prevref=None
    curref=head
    while curref and position>0:
        prevref=curref
        curref=curref.next
        position-=1
    
    if position>0:
        return head
    
    prevref.next=Node(data=data,next_node=curref)
    
    return head
        