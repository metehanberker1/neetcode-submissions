# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = None
        def helper(node):
            nonlocal k, res
            if not node or k == 0:
                return
            helper(node.left)
            k -= 1
            if k == 0:
                res = node.val
                return
            helper(node.right)
        helper(root)
        return res
