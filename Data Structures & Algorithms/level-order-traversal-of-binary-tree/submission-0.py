from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = [root]
        stack = deque()
        res = []
        
        if root is None: 
            return []

        while level:
            tmp = []       
            for entry in level:
                if entry is None: 
                    continue 

                if entry.left:
                    stack.append(entry.left)
                if entry.right:
                    stack.append(entry.right)
                
                tmp.append(entry.val)
                
            level = []
            while stack: 
                level.append(stack.popleft())
            res.append(tmp)
        return res