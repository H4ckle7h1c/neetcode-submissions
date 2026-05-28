# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap_min = []
        counter = 0
        for l in lists:
            curr = l
            while curr:
                heapq.heappush(heap_min, (curr.val, counter, curr))
                curr = curr.next
                counter += 1
            
        head = ListNode()
        curr = head

        while heap_min:
            entry = heapq.heappop(heap_min)
            node = entry[2]
            curr.next = node
            curr = node
        
        return head.next


