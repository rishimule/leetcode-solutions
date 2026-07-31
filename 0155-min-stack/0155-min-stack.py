class MinStack:

    def __init__(self):
        self.stack  = []
        self.minIdx = -1
        self.prevMinIdx = {}
        

    def push(self, value: int) -> None:
        if self.minIdx < 0 or value <= self.stack[self.minIdx]:
                self.prevMinIdx[len(self.stack)] = self.minIdx
                self.minIdx = len(self.stack)
        
        self.stack.append(value)
        

    def pop(self) -> None:
        if self.stack:
            if self.minIdx == len(self.stack)-1:
                self.minIdx = self.prevMinIdx[self.minIdx]
                del self.prevMinIdx[len(self.stack)-1]
            self.stack.pop()
            
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return None
        

    def getMin(self) -> int:
        if self.stack:
            return self.stack[self.minIdx]
        return None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()