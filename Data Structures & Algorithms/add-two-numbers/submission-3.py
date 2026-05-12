# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return 
        
        if not l1:
            return l2
        
        if not l2:
            return l1

        
        carry = 0
        result = ListNode()
        curr = result

        while l1 and l2:
            step_sum = l1.val + l2.val + carry
            carry = 0

            if step_sum >= 10:
                carry = 1
                step_sum -= 10
            
            res_node = ListNode(step_sum)
            curr.next = res_node
            curr = res_node 

            l1, l2 = l1.next, l2.next
        
        if l1 and not l2:
            if not carry:
                curr.next = l1   
            else:
                while l1:
                    step_sum = l1.val + carry
                    carry = 0

                    if step_sum >= 10:
                        carry = 1
                        step_sum -= 10

                    res_node = ListNode(step_sum)
                    curr.next = res_node
                    curr = res_node 
                    l1 = l1.next

        if l2 and not l1:
            if not carry:
                curr.next = l2
            else:
                while l2:
                    step_sum = l2.val + carry
                    carry = 0

                    if step_sum >= 10:
                        carry = 1
                        step_sum -= 10

                    res_node = ListNode(step_sum)
                    curr.next = res_node
                    curr = res_node 
                    l2 = l2.next
        
        if carry:
            res_node = ListNode(carry)
            curr.next = res_node
            curr = res_node         
            
        return result.next
