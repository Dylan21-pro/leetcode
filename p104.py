# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        value = self.height(root)
        return value

    def height(self, node):
        if node == None:
            return 0
        return 1 + max(self.height(node.left), self.height(node.right))
