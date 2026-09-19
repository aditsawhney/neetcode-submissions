class MinStack:

    def __init__(self):
        # store tuples of (val, current min)
        self.items = []

    def push(self, value: int) -> None:
        if not self.items:
            self.items.append((value, value))
        else:
            current_min = min(value, self.items[-1][1])
            self.items.append((value, current_min))

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1][0]

    def getMin(self) -> int:
        return self.items[-1][1]
        
