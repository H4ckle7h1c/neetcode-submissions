from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []    

        level = deque([root])
        res = []

        while level:
            node = None
            level_size = len(level)

            for i in range(level_size):
                node = level.popleft()

                if i == level_size - 1  :
                    res.append(node.val)
                
                if node.left:
                    level.append(node.left)
                if node.right:
                    level.append(node.right)
            
        return res