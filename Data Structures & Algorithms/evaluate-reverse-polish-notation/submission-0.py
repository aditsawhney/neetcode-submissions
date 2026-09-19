class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # make a stack, as we encounter integers, push them to the stack, whenever an operand is encountered, pop the top two elements, calculate the result, and push that result to top of stack, and continue

        stack = []
        for token in tokens:
            if token in "+/*-":
                b = stack.pop()
                a = stack.pop()

                if token == "+":
                    result = (a + b)
                elif token == "-":
                    result = (a-b)
                elif token == "*":
                    result = (a * b)
                else:
                    result = int(a/b)
                
                stack.append(result)

            else:
                stack.append(int(token))        

        return stack[0]