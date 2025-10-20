class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        new_list = list(set(nums))
        sorted_new_list = sorted(new_list)
        for i in range(len(new_list)):
            nums[i] = sorted_new_list[i]

        return len(new_list)
