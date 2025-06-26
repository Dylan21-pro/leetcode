class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        string = ""
        while index < len(s) and s[index].isdigit():
            string += s[index]
            index += 1

        if not string:
            return 0

        final = sign * int(string)

        # Clamp to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if final < INT_MIN:
            return INT_MIN
        if final > INT_MAX:
            return INT_MAX
        return final
