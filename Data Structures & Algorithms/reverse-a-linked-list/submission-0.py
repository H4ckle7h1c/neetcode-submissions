# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = None
        curr = head
        
        while curr is not None:
            if new_head is None:
                new_head = ListNode(curr.val)
            else:
                new_head = ListNode(curr.val, new_head)

            curr = curr.next


        return new_head 
