# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.arr = []
        self._inorder(root)
        return self.arr

    def _inorder(self,node):
        if node:
            self._inorder(node.left)
            self.arr.append(node.val)
            self._inorder(node.right)
