class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # make a stack, and an output array. stack should contain
        # the element, and it's index

        result = [0] * len(temperatures)
        stack = []  # store [temp, index]

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = (index - stackIndex)
            stack.append([temperature, index])
        return result



