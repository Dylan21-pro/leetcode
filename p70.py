class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            count = 0
            prev = 2
            current = 3
            while count < n - 2:
                prev, current = current, prev
                current += prev
                count += 1
            return prev
