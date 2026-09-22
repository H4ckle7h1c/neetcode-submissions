"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        nodes = {}

        if not head:
            return 
            
        while curr:
            node = Node(curr.val)
            nodes[curr] = node
            curr = curr.next

        curr = head

        while curr: 
            if curr.random:
                nodes[curr].random = nodes[curr.random]
            nodes[curr].next = nodes.get(curr.next, None)
            curr = curr.next
        
        deep_copy = nodes[head]
        return deep_copy




        
