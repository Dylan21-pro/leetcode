class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        common = strs[0]

        for next_string in strs[1:]:
            count = 0
            while count < len(common) and count < len(next_string) and common[count] == next_string[count]:
                count += 1
            common = common[:count]
            
            if not common:
                return ""

        return common
