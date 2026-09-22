# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0 
    
    def heigth(self, root: Optional[TreeNode]) -> int:
        if root is None: 
            return 0
        
        right_heigth = self.heigth(root.right)
        left_heigth = self.heigth(root.left)
        d = left_heigth + right_heigth
        self.diameter = max(d, self.diameter)
        return 1 + max(right_heigth,left_heigth )

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.heigth(root)

        return self.diameter