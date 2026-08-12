# Last updated: 8/12/2026, 12:22:33 PM
class MinStack:
    def __init__(self):
        # Initialize two stacks: one for values, one for minimums
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # Only push to min_stack if it's empty or val <= current min
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            val = self.stack.pop()
            # If popped value is the current min, remove from min_stack too
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
