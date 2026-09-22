# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
            slow, fast = head, head

            # Find the half of the list
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            
            # Reverse the second half
            reversed_half = []
            curr_collect = slow.next
            slow.next = None
            while curr_collect:
                reversed_half.append(curr_collect)
                curr_collect = curr_collect.next
            
            # Now assemble the i and the n-i
            curr = head
            while reversed_half:
                last = reversed_half.pop()
                curr_next = curr.next
                last.next = curr_next
                curr.next = last 
                curr = curr_next






                
