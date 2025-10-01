class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index in range(len(nums)):
            sub = target - nums[index]
            if sub in dictionary:
                return [index, dictionary[sub]]
            else:
                dictionary[nums[index]] = index

        
