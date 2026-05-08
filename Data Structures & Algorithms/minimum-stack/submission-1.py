class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0)
            self.minimum = val
        else:
            self.stack.append(val - self.minimum)
            if val < self.minimum:
                self.minimum = val

    def pop(self) -> None:
        if not self.stack:
            return
        
        pop_val = self.stack.pop()
        if pop_val < 0:
            self.minimum = self.minimum - pop_val

    def top(self) -> int:
        top_val = self.stack[-1]
        
        if top_val < 0:
            return self.minimum
        else:
            return top_val + self.minimum

    def getMin(self) -> int:
        return self.minimum