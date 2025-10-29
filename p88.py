class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums2.extend(nums1[0:m])
        nums1.clear()
        nums1.extend(sorted(nums2))
        
