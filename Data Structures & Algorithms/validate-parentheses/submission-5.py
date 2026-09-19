class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        bracket_map = {
            "}":"{",
            "]":"[",
            ")":"("
        }

        stack = []
        for character in s:
            # run a loop for all teh characters in the string. if the 
            # character is an open bracket, push it to stack, else,
            # if it's a closed bracket, that'd mean it's present in the
            # bracket map, in which case pop the element from stack, and 
            # check if that popped element == value associated with the 
            # closed bracket accdng to the map. if not, return false.

            if character in bracket_map:
                # pop the stack
                # if stack is empty, or popped element is not what's req
                if not stack or stack.pop() != bracket_map[character]:
                    return False
            else:
                # add to stack
                stack.append(character)

        return not stack