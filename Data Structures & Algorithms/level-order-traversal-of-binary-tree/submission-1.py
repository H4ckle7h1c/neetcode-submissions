from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = deque([root])
        res = []
        
        if root is None: 
            return []

        while level:
            level_size = len(level)
            tmp = []       
     
            for _ in range(level_size):
                node = level.popleft()
                tmp.append(node.val)

                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            
            res.append(tmp)

        return res