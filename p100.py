class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Both nodes are None
        if not p and not q:
            return True
        # One is None but not the other
        if not p or not q:
            return False
        # Values differ
        if p.val != q.val:
            return False
        # Check left and right subtrees
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
