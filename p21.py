# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        if not list1 and list2:
            return list2
        elif not list2 and list1:
            return list1
        elif not list1 and not list2:
            return None
        else: 
            tmp = None
            final = None

            if list1.val <= list2.val:
                tmp = list1
                list1 = list1.next
            else:
                tmp = list2
                list2 = list2.next

            final = tmp
            
            while list1 and list2:
                if list1.val <= list2.val:
                    tmp.next = list1
                    list1 = list1.next
                else:
                    tmp.next = list2
                    list2 = list2.next

                tmp = tmp.next

            while list1:
                tmp.next = list1
                list1 = list1.next
                tmp = tmp.next

            while list2:
                tmp.next = list2
                list2 = list2.next
                tmp = tmp.next

            return final

            



        
