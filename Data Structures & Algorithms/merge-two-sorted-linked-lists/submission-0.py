# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # since the two lists are sorted, compare values
        # whosever value is used, move it ahead

        curr1 = list1
        curr2 = list2
        
        ans = ListNode(-1)      # dummy node for answer list
        curr3 = ans

        # step 1: compare lists when both have nodes
        while curr1 != None and curr2 != None:
            if curr1.val <= curr2.val:
                curr3.next = curr1
                curr1 = curr1.next
            else:
                curr3.next = curr2
                curr2 = curr2.next
            
            curr3 = curr3.next
        
        # if one list runs out, attach the remaining node sof other one
        if curr1 != None:
            curr3.next = curr1
        else:
            curr3.next = curr2

        return ans.next
