import math

class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        elif x == 1 or x == 2 :
            return 1
       
        left = 0
        right = x
        while left < right:
            mid = math.ceil((right-left)/2 + left)
            double = mid * mid
            if double == x or (double < x and (mid+1)**2 > x):
                return mid
            elif double < x:
                left = mid
            elif double > x:
                right = mid
        return mid
