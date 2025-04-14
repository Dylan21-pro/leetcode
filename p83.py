# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = ListNode(101)
        second = ListNode(-101)
        first.next = second

        if head == None or head.next == None:
            return head
        else:
            while head != None:

                if second.val != head.val :
                    second.next = head
                    second = second.next
                
                head = head.next
            second.next = None

            return first.next.next
                

                

        print(first.next)
        return first.next.next
'''

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        realHead = ListNode(101)
        secondHead = ListNode(101)
        realHead.next = secondHead
        newSet = set()
        count = 0 
        
        if head == None or head.next == None:
            return head
        else:
            while head != None:
                newSet.add(head.val)
                if len(newSet) > count:
                    count += 1
                    secondHead.next = ListNode(head.val)
                    secondHead = secondHead.next

                head = head.next
                
        return realHead.next.next







                
