# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.symChecked(root.left, root.right)
    

    def symChecked(self, left, right):
        if not right and not left:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.symChecked(left.left, right.right) and self.symChecked(left.right, right.left)
