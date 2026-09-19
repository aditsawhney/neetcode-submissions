class MinStack:

    def __init__(self):
        # store tuples of (val, current_min)
        self.items = []
        
    def push(self, val: int) -> None:
        if not self.items:
            self.items.append((val, val))
        else:
            current_min = min(val, self.items[-1][1])
            self.items.append((val, current_min))

    def pop(self) -> None:
        self.items.pop()

    def top(self) -> int:
        return self.items[-1][0]
        
    def getMin(self) -> int:
        return self.items[-1][1]
