# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
cnt = 1
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.result = 0

        def in_order(node: Optional[TreeNode]):
            if not node:
                return 

            # Recurse left 
            in_order(node.left)

            self.count += 1
            
            if self.count == k:
                self.result = node.val
                return 

            in_order(node.right)
        
        in_order(root)
        
        return self.result