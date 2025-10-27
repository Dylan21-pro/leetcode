class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        left = 0
        final = []
        last = len(digits)-1
        digits[last] += 1
        for i in range(last, -1, -1):
            final.insert(0,(digits[i] + carry) % 10)
            carry = (digits[i] + carry) // 10
        if carry != 0:
            final.insert(0,carry)
        return final
        
