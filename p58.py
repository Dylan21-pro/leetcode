class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        string = s.rstrip()
        arr = string.split(' ')
        return len(arr[len(arr)-1])
