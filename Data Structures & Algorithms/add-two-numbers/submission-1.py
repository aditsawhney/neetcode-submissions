# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        curr1, curr2 = head1, head2
        ans = ListNode(-1)
        curr3 = ans
        carry = 0

        while curr1 != None or curr2 != None:
            total = carry
            if curr1 != None:
                total += curr1.val
                curr1 = curr1.next
            if curr2 != None:
                total += curr2.val
                curr2 = curr2.next
            
            digit, carry = total%10, total//10
            newNode = ListNode(digit)
            curr3.next = newNode
            curr3 = curr3.next

        if carry > 0:
            newNode = ListNode(carry)
            curr3.next = newNode
        
        return ans.next