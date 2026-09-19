class Solution:
    def isValid(self, s: str) -> bool:

        if len(s)%2 != 0:
            return False
        
        stack = []
        bracket_map = {']':'[', ')':'(', '}':'{'}

        for ch in s:
            if ch not in bracket_map:
                stack.append(ch)
            elif ch in bracket_map:
                if len(stack) == 0 or stack.pop() != bracket_map[ch]:
                    return False
        
        return len(stack) == 0
        