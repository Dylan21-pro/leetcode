class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        setArray = set()
        longest = 0
        count = 0


        if len(s) == "":
            return 0
        elif len(s) == 1:
            return 1
        else:
            for ct in range(len(s)):
                if not s[ct] in setArray:
                    setArray.add(s[ct])
                else:
                    if longest < len(setArray):
                        longest = len(setArray)
                    while s[ct] in setArray:
                        setArray.remove(s[count])
                        count += 1
                    setArray.add(s[ct])

        return longest if longest > len(setArray) else len(setArray)



