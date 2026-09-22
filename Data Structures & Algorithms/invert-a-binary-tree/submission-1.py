# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        root.right, root.left  = self.invertTree(root.left), self.invertTree(root.right)
        return root 