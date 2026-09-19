# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use a two pointer approach, a slow and a fast pointer
        # simple logic, if there's a straight line, 2 pointers
        # moving through different speeds would never meet, however
        # if there's a cycle, they would

        slow = head
        fast = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        
        return False