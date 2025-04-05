# O(n) time

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for index, value in enumerate(nums):
            complement = target - value
            if complement in dictionary:
                return [index,dictionary[complement]]
            
            dictionary[value] = index


