"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # have 2 passes, and store inside a hash map
        # first pass for the values, and second one for the linking

        if head == None:
            return None

        # First Pass
        oldToCopy = {None:None}
        curr = head
        while curr != None:
            oldToCopy[curr] = Node(curr.val)
            curr = curr.next
        
        # Second Pass
        curr = head
        while curr != None:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next

        return oldToCopy[head]
        