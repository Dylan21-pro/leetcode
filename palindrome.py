class Solution:
    def isPalindrome(self, x: int) -> bool:
        value = x
        self = 0

        while x > 0:
            last_digit = x % 10
            self = self*10 + last_digit
            x //= 10

        if self == value:
            return True
        else:
            return False
