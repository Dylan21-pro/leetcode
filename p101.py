# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p = root.left
        q = root. right
        self.boolVal = True
        self.checked(p,q)
        return self.boolVal

    def checked(self,p,q):
        
        if not p and not q:
            return
        elif not p or not q:
            self.boolVal = False
            return
        elif p.val != q.val:
            self.boolVal = False
            return
        else:
            self.checked(p.left,q.right)
            self.checked(p.right,q.left)
