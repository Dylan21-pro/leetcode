# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        if not  l1:
            return l2
        elif not l2:
            return l1
        else:
            sub = ListNode(0)
            final = sub

            first = 0
            second = 0
            whole = 0
            first_remainder = 0
            second_remainder = 0

            while l1 or l2 or second_remainder:
                if l1:
                    first = l1.val
                    l1 = l1.next
                else:
                    first = 0

                if l2:
                    second = l2.val
                    l2 = l2.next
                else:
                    second = 0

                whole = (first + second + second_remainder) // 10
                first_remainder = (first + second + second_remainder) % 10
                second_remainder = whole % 10
                sub.next = ListNode(first_remainder)
                sub = sub.next

        return final.next

