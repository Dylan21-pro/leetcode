# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        tree = self.intoBST(nums, 0, len(nums)-1)
        return tree

    def intoBST(self, arr, start, end):
        if start > end:
            return None

        mid = start + (end - start) // 2
        root = TreeNode(arr[mid])
        root.left = self.intoBST(arr, start, mid-1)
        root.right = self.intoBST(arr, mid+1, end)

        return root
