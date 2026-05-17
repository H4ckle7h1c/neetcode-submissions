# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        

        # Mapping inorder val => index
        inorder_index = {}
        for i, v in enumerate(inorder):
            inorder_index[v] = i

        root_val = preorder[0]
        mid = inorder_index[root_val]

        left_tree = self.buildTree(preorder[1:mid+1], inorder[:mid])
        right_tree = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return TreeNode(root_val, left_tree, right_tree)

