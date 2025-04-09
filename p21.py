class Solution:
    def isValid(self, s: str) -> bool:
        arr = []

        map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        for char in s:
            if len(arr) == 0:
                arr.append(char)
            else:
                if arr[len(arr)-1] in map and map[arr[len(arr)-1]] == char:
                    arr.pop()
                else:
                    arr.append(char)

        return True if len(arr) == 0 else False 
            
