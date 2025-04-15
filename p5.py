class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or (len(s) == 2 and s[0] != s[1]):
            return s[0]
        elif len(s) == 2 and s[0] == s[1]:
            return s
        else:
            posLongest = []
            longest = s[0]
            for ct in range(1,len(s)):
                if ct - 1 >= 0 and s[ct] == s[ct-1]:
                    posLongest.append([ct-1,ct])

                if ct - 1 >= 0 and ct + 1 < len(s) and s[ct-1] == s[ct+1]:
                    posLongest.append([ct-1,ct+1])

            for left, right in posLongest:
                while left - 1 >= 0 and right + 1 < len(s) and s[left-1] == s[right+1]:
                    left -= 1
                    right += 1 
                if len(longest) < len(s[left:right+1])+1:
                    longest = s[left:right+1]
            return longest
