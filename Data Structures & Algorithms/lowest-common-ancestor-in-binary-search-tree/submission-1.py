# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        right = max(p.val, q.val)
        left = min(p.val, q.val)
        while root.val < left or root.val > right:
            print(root.val)
            if root.val < left:
                root = root.right
            elif root.val > right:
                root = root.left
            
        return root