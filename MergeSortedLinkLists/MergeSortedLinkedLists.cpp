/*
  Merge two sorted lists A and B as one linked list
  Node is defined as 
  struct Node
  {
     int data;
     struct Node *next;
  }
*/
Node* MergeLists(Node *headA, Node* headB)
{
  // This is a "method-only" submission. 
  // You only need to complete this method 
  if(!headA)
      return headB;
  if(!headB)
      return headA;
  
  Node* newHead=NULL;
      Node* newTail=NULL;
    
  if(headA->data < headB->data){
      newHead=newTail=headA;
      headA=headA->next;
  }
      
      else{
          newHead=newTail=headB;
      headB=headB->next;
      }
      
      while(1){
          if(!headA){
              newTail->next=headB;
              break;
          }
          if(!headB){
              newTail->next=headA;
              break;
          }
          if (headA->data < headB->data){
              newTail->next=headA;
              newTail=headA;
              headA=headA->next;
          }else{
              newTail->next=headB;
              newTail=headB;
              headB=headB->next;
          }
      }
      return newHead;
}


