class Solution:
    def climbStairs(self, n: int) -> int:
        count = 0
        this_number = 0
        prev_number = 0
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        elif n == 3:
            return 3
        else:
            this_number = 3
            prev_number = 2
            count = 3
            while count < n:
                num = this_number
                this_number += prev_number
                prev_number = num
                count += 1
            return this_number


    def fibonacci(a, b):

        return 0
