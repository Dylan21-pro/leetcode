class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for ct in range(len(nums)):
            if nums[ct] == target:
                return ct

        if target < nums[0]:
            return 0
        if target > nums[len(nums)-1]:
            return len(nums)
        else:
            for ct in range(1,len(nums)):
                if target > nums[ct-1] and target <= nums[ct]:
                    return ct
