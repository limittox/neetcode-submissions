class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = sys.maxsize

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minimum = min(val, self.minimum)

    def pop(self) -> None:
        poppedNum = self.stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)
