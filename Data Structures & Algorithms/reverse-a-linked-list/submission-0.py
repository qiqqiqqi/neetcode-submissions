# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        while head!=None:
            stack.append(head.val)
            head=head.next
        
        dummy = ListNode()
        current = dummy

        while stack:
            new_node = ListNode(stack.pop())
            current.next=new_node
            current=current.next
            
        return dummy.next




