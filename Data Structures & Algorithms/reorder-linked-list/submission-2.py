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
            curr_collect = slow.next
            slow.next = None
            prev = None
            while curr_collect:
                next_node = curr_collect.next
                curr_collect.next = prev
                prev = curr_collect
                curr_collect = next_node
            second = prev 

            # Now assemble the i and the n-i
            curr = head
            while second:
                next_node = curr.next
                curr.next = second 
                second = second.next
                curr.next.next = next_node
                curr = next_node