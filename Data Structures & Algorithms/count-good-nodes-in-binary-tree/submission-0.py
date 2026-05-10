# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        max_so_far = float('-inf')

        def dfs(root: TreeNode, max_so_far) -> None:
            if root is None:
                return 0

            count = 1 if root.val >= max_so_far else 0
            new_max = max(max_so_far, root.val)

            return count + dfs(root.left, new_max) + dfs(root.right, new_max)

        return dfs(root, max_so_far)