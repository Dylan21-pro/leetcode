class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        value = strs[0]
        if len(strs) == 0:
            return ""
        elif len(strs) == 1:
            return value
        else:
            for ct in range(len(strs)):
                if strs[ct] == "" or value == "":
                    return ""
                else:
                    while not strs[ct].startswith(value):
                        print(value)
                        value = value[:len(value)-1]
                
            return value







