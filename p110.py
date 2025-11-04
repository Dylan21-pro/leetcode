# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def findHeight(node):
            if not node: return 0
            lTree = findHeight(node.left)
            if lTree == -1: return -1
            rTree = findHeight(node.right)
            if rTree == -1: return -1
            if abs(lTree - rTree) > 1: return -1
            return 1 + max(lTree,rTree)
        return findHeight(root) != -1
        

