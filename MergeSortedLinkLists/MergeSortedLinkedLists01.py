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

        if not headA:
            newTail.next=headB
        if not headB:
            newTail.next=headA

        if headA.data < headB.data:
            newTail=headA
            newTail.next=headA
            headA=headA.next
        else:
            newTail=headB
            newTail.next=headB
            headB=headB.next
        
    return newHead.next

  