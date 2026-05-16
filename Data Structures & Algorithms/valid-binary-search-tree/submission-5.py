# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def checkTree(node, left_border, right_border):
            if not node:
                return True
            if node.val <= left_border or node.val >= right_border:
                return False
            return checkTree(node.left, left_border, node.val) and checkTree(node.right, node.val, right_border)
        return checkTree(root, -float("inf"), float("inf"))