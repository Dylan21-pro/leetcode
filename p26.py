class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        finalCount = 1
        for ct in range(1,len(nums)):
            if nums[ct] != nums[ct-1]:
                nums[finalCount] = nums[ct]
                finalCount += 1

        return finalCount
