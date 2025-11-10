class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # If tree is empty, no path exists
        if not root:
            return False
        
        # If we reach a leaf, check if the sum equals targetSum
        if not root.left and not root.right:
            return targetSum == root.val
        
        # Recursively check left and right subtrees
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
