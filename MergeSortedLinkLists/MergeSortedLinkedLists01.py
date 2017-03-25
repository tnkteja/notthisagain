 """
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    if not headA:
        return headB
    if not headB:
        return headA
    
    newHead=Node()
    newTail=newHead
    nextA=headA.next
    nextB=headB.next
    
    while True:
        one,after= (headA,headB) if headA.data < headB.data else (headB,headA)
        
        # Making a new tail
        newTail.next=one
        one.next=after
        newTail=after
        
        if not nextA:
            newTail.next=nextB
            break
        if not nextB:
            newTail.next=nextA
            break
        
        headA=nextA
        nextA=headA.next
        headB=nextB
        nextB=headB.next
        
    return newHead.next

  