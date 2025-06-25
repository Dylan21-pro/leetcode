class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            num = abs(x)
            minus = 1
        else:
            minus = 0
            num = x

        reverseNum = 0
        while num != 0:
            digit = num % 10
            reverseNum = reverseNum * 10 + digit
            num = num // 10

        if minus:
            reverseNum *= -1

        # Correct 32-bit signed integer range
        if -2**31 <= reverseNum <= 2**31 - 1:
            return reverseNum
        else:
            return 0


## Faster
'''
class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        s = str(abs(x))
        reversed_s = s[::-1]
        result = sign * int(reversed_s)
        
        if -2**31 <= result <= 2**31 - 1:
            return result
        else:
            return 0

'''