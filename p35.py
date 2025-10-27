class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        final = nums.copy()
        length = len(final)
        a = 0
        for i in range(length):
            if final[i] != val:
                nums[a] = final[i]
                a += 1
        return a
            
