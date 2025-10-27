class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        final = s.strip().split(" ")
        return len(final.pop())
