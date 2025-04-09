class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        if digits[len(digits)-1]+1 < 10:
            digits[len(digits)-1] += 1
        else:
            whole = 0
            first_remainder = 0
            carry = 1
            count = len(digits)-1
            while carry != 0:
                if count != 0:
                    whole = (digits[count] + carry) // 10
                    first_remainder = (digits[count] + carry) % 10
                    digits[count] = first_remainder
                    carry = whole % 10
                else:
                    digits.insert(0,carry)
                    break
                count -= 1

        return digits
        
