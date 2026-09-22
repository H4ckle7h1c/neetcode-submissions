# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root is None or subRoot is None:
            return False
        if root is None and subRoot is None:
            return True

        def check(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if root is None and subRoot is None:
                return True

            if root is None or subRoot is None:
                return False

            if root.val is not subRoot.val: 
                return 
            return check(root.left, subRoot.left) and check(root.right, subRoot.right)

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)

        if root.val == subRoot.val:
            if check(root, subRoot):
                return True
        
        return left or right
