# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # step 1: find middle of the list, using slow and fast pointers
        slow = head
        fast = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
        
        # step 2: reverse the second half of the string
        curr = slow.next
        slow.next = None        # disconnect the first half, otherwise it would be an circular list
        prev = None
        nxt = None

        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # prev is our reversed list (second half only)

        # step 3: reorder the list
        first = head
        second = prev

        # store the original next nodes, using temporary pointers, and
        # weave the lists together

        while second != None:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2












