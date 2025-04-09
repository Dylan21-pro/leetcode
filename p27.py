class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        finalCount = 0
        for ct in range(len(nums)):
            if nums[ct] != val:
                nums[finalCount] = nums[ct]
                finalCount += 1

        return finalCount



