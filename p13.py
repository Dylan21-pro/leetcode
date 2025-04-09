class Solution:
    def romanToInt(self, s: str) -> int:
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        special = {
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        t = 0
        c = 0

        while c < len(s):
            if s[c:c+2] in special:
                t += special[s[c:c+2]]
                c += 2
            else:
                t += map[s[c]] 
                c += 1

        return t
        
