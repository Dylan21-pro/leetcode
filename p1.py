class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for count in range(len(nums)):
            sub = target - nums[count]
            if sub not in dictionary:
                dictionary[nums[count]] = count
            else:
                return count, dictionary[sub]
