class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # This stack holds the minimum value at each level.

    def push(self, val: int) -> None:
        self.stack.append(val)
        # If min_stack is empty or val is less than or equal to the current min, push it onto min_stack.
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)
        else:
            # Otherwise, repeat the current minimum.
            self.min_stack.append(self.min_stack[-1])

    def pop(self) -> None:
        if self.stack:
            self.min_stack.pop()
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        else:
            raise IndexError("top from empty stack")

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]
        else:
            raise IndexError("getMin from empty stack")
