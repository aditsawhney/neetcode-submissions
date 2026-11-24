# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Step 1: find the middle of the list
        # Step 2: reverse the second half
        # Step 3: weave the two parts together

        if head == None or head.next == None:
            return 

        # Step 1
        slow, fast = head, head
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next    # slow is the middle
        
        # Step 2
        curr = slow.next
        slow.next = None        # break the chain, else there'd be a cycle
        prev, nxt = None, None
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # Step 3
        first, second = head, prev
        while second != None:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        












